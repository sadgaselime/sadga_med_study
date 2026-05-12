"""
ai_service.py - small resilient AI API wrapper for MedStudy Oman.

Supports Gemini and OpenAI-style chat completions through st.secrets. All
public functions return safe dictionaries/strings instead of raising into the
Streamlit app.
"""

from __future__ import annotations

import json
import re
from typing import Any

import requests
import streamlit as st


DEFAULT_ERROR = "The AI service is unavailable right now. Please check your API key or network connection and try again."


def _secret(*names: str) -> str | None:
    for name in names:
        try:
            value = st.secrets.get(name)
        except Exception:
            value = None
        if value:
            return str(value)
    for provider in ("gemini", "openai"):
        for name in names:
            try:
                value = st.secrets.get(provider, {}).get(name)
            except Exception:
                value = None
            if value:
                return str(value)
    return None


def get_ai_status() -> dict[str, str | bool]:
    if _secret("GEMINI_API_KEY", "gemini_api_key"):
        return {"ready": True, "provider": "gemini"}
    if _secret("OPENAI_API_KEY", "openai_api_key"):
        return {"ready": True, "provider": "openai"}
    return {"ready": False, "provider": "none"}


def call_ai(prompt: str, system_prompt: str = "", *, temperature: float = 0.4, max_tokens: int = 2200) -> str:
    status = get_ai_status()
    if not status["ready"]:
        return DEFAULT_ERROR
    try:
        if status["provider"] == "openai":
            return _call_openai(prompt, system_prompt, temperature, max_tokens)
        return _call_gemini(prompt, system_prompt, temperature, max_tokens)
    except requests.exceptions.Timeout:
        return "The AI request timed out. Please try again with a shorter prompt."
    except requests.exceptions.RequestException:
        return DEFAULT_ERROR
    except Exception:
        return DEFAULT_ERROR


def _call_gemini(prompt: str, system_prompt: str, temperature: float, max_tokens: int) -> str:
    api_key = _secret("GEMINI_API_KEY", "gemini_api_key")
    model = _secret("GEMINI_MODEL", "gemini_model") or "gemini-1.5-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    payload: dict[str, Any] = {
        "contents": [{"role": "user", "parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": temperature, "maxOutputTokens": max_tokens},
    }
    if system_prompt:
        payload["systemInstruction"] = {"parts": [{"text": system_prompt}]}
    response = requests.post(url, json=payload, timeout=45)
    response.raise_for_status()
    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]


def _call_openai(prompt: str, system_prompt: str, temperature: float, max_tokens: int) -> str:
    api_key = _secret("OPENAI_API_KEY", "openai_api_key")
    model = _secret("OPENAI_MODEL", "openai_model") or "gpt-4o-mini"
    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": prompt})
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
        json={"model": model, "messages": messages, "temperature": temperature, "max_tokens": max_tokens},
        timeout=45,
    )
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]


def parse_json_object(raw_text: str) -> tuple[dict | None, str | None]:
    if not raw_text or raw_text == DEFAULT_ERROR:
        return None, raw_text or DEFAULT_ERROR
    cleaned = re.sub(r"```(?:json)?|```", "", raw_text).strip()
    candidates = [cleaned]
    match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
    if match:
        candidates.append(match.group(0))
    for candidate in candidates:
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed, None
    return None, "The AI response was not valid JSON. Please try again."


def _as_list(value: Any) -> list:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [str(value)]


def _normalize_topic_module(data: dict) -> dict:
    normalized = {
        "overview": str(data.get("overview") or ""),
        "detailed_notes": [str(item) for item in _as_list(data.get("detailed_notes"))],
        "high_yield": [str(item) for item in _as_list(data.get("high_yield"))],
        "mcqs": [],
        "flashcards": [],
    }
    for mcq in _as_list(data.get("mcqs")):
        if not isinstance(mcq, dict):
            continue
        options = [str(option) for option in _as_list(mcq.get("options"))]
        answer = str(mcq.get("answer") or mcq.get("correct") or mcq.get("correct_answer") or "")
        if not answer and isinstance(mcq.get("correct_index"), int) and 0 <= mcq["correct_index"] < len(options):
            answer = options[mcq["correct_index"]]
        if len(options) < 4 or answer not in options:
            continue
        normalized["mcqs"].append(
            {
                "question": str(mcq.get("question") or mcq.get("stem") or ""),
                "options": options[:4],
                "answer": answer,
                "explanation": str(mcq.get("explanation") or ""),
            }
        )
    for card in _as_list(data.get("flashcards")):
        if not isinstance(card, dict):
            continue
        front = str(card.get("front") or card.get("question") or "")
        back = str(card.get("back") or card.get("answer") or "")
        if front and back:
            normalized["flashcards"].append({"front": front, "back": back})
    return normalized


def generate_topic_module(topic: str) -> tuple[dict | None, str | None]:
    system_prompt = (
        "You are a senior medical curriculum architect. Return only strict JSON. "
        "Do not include markdown fences, commentary, citations, or text outside JSON."
    )
    prompt = f"""
Create a premium medical study module for the topic: {topic}

Return exactly one JSON object with these keys:
- overview: string
- detailed_notes: array of concise strings
- high_yield: array of exam-focused strings
- mcqs: array of objects with question, options, answer, explanation
- flashcards: array of objects with front, back

Rules:
- Write for medical students.
- Make the content clinically accurate and high-yield.
- Include 3 MCQs and 5 flashcards.
- Every MCQ must have 4 options and an answer that exactly matches one option.
"""
    raw = call_ai(prompt, system_prompt, temperature=0.25, max_tokens=3000)
    data, error = parse_json_object(raw)
    if error:
        return None, error
    required = {"overview", "detailed_notes", "high_yield", "mcqs", "flashcards"}
    missing = required.difference(data or {})
    if missing:
        return None, f"The AI response was missing: {', '.join(sorted(missing))}."
    normalized = _normalize_topic_module(data)
    if not normalized["overview"] or not normalized["detailed_notes"]:
        return None, "The AI response did not include enough usable study notes. Please try again."
    return normalized, None


def generate_mnemonic(facts: str, style: str) -> str:
    system_prompt = (
        "You are an elite medical memory coach. Create acronym-based mnemonics "
        "that are accurate, memorable, and perfectly mapped to the supplied facts."
    )
    prompt = f"""
Facts or symptoms to remember:
{facts}

Mnemonic style: {style}

Return a polished response with:
1. A bold acronym mnemonic.
2. A letter-by-letter mapping where every letter maps to a specific supplied fact.
3. One short story or mental image matching the selected style.
4. A high-yield clinical caution if any item is dangerous, commonly missed, or exam-critical.

Do not invent extra medical facts that are not needed for the mapping.
"""
    return call_ai(prompt, system_prompt, temperature=0.85, max_tokens=1400)


def tutor_reply(history: list[dict[str, str]], user_message: str) -> str:
    system_prompt = (
        "You are an elite, encouraging Clinical Medicine Professor. Use clear "
        "formatting, appropriate emojis, and step-by-step diagnostic breakdown "
        "logic. Teach mechanisms first, then clinical features, investigations, "
        "management, and high-yield exam pearls. Be concise but complete."
    )
    history_text = "\n".join(f"{m['role'].title()}: {m['content']}" for m in history[-8:])
    prompt = f"""
Conversation so far:
{history_text}

Student question:
{user_message}

Answer as the professor. Use headings, bullets, diagnostic reasoning steps, and a brief encouraging close.
"""
    return call_ai(prompt, system_prompt, temperature=0.55, max_tokens=1800)
