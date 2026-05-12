"""
pulse_backend.py - Supabase data layer for PULSE.md.

This module keeps backend concerns out of the Streamlit UI. It uses Supabase
REST/Auth endpoints directly so the app remains deployable with only secure
Streamlit secrets:

SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_ANON_KEY = "..."
SUPABASE_SERVICE_ROLE_KEY = "..."  # optional, only for admin writes
ADMIN_EMAILS = "you@example.com,admin@example.com"
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Any

import requests
import streamlit as st


def secret(*names: str) -> str | None:
    for name in names:
        try:
            value = st.secrets.get(name)
        except Exception:
            value = None
        if value:
            return str(value)
    for group in ("supabase", "ai", "openai", "gemini"):
        for name in names:
            try:
                value = st.secrets.get(group, {}).get(name)
            except Exception:
                value = None
            if value:
                return str(value)
    return None


@dataclass
class SupabaseConfig:
    url: str
    anon_key: str
    service_key: str | None = None


def get_config() -> SupabaseConfig | None:
    url = secret("SUPABASE_URL", "supabase_url")
    anon = secret("SUPABASE_ANON_KEY", "supabase_anon_key")
    if not url or not anon:
        return None
    return SupabaseConfig(url=url.rstrip("/"), anon_key=anon, service_key=secret("SUPABASE_SERVICE_ROLE_KEY", "supabase_service_role_key"))


def is_configured() -> bool:
    return get_config() is not None


def admin_emails() -> set[str]:
    raw = secret("ADMIN_EMAILS", "admin_emails") or ""
    return {email.strip().lower() for email in raw.split(",") if email.strip()}


class PulseStore:
    def __init__(self, access_token: str | None = None, admin: bool = False):
        self.config = get_config()
        self.access_token = access_token
        self.admin = admin

    @property
    def ready(self) -> bool:
        return self.config is not None

    def _headers(self, prefer: str | None = None) -> dict[str, str]:
        if not self.config:
            return {}
        api_key = self.config.service_key if self.admin and self.config.service_key else self.config.anon_key
        bearer = self.access_token or api_key
        headers = {
            "apikey": api_key,
            "Authorization": f"Bearer {bearer}",
            "Content-Type": "application/json",
        }
        if prefer:
            headers["Prefer"] = prefer
        return headers

    def _rest(self, table: str) -> str:
        if not self.config:
            raise RuntimeError("Supabase is not configured")
        return f"{self.config.url}/rest/v1/{table}"

    def select(self, table: str, params: dict[str, str] | None = None, order: str | None = None) -> list[dict[str, Any]]:
        if not self.ready:
            return []
        query = dict(params or {})
        if order:
            query["order"] = order
        try:
            resp = requests.get(self._rest(table), headers=self._headers(), params=query, timeout=25)
            resp.raise_for_status()
            data = resp.json()
            return data if isinstance(data, list) else []
        except Exception as exc:
            st.session_state.backend_error = str(exc)
            return []

    def insert(self, table: str, payload: dict[str, Any] | list[dict[str, Any]]) -> list[dict[str, Any]]:
        if not self.ready:
            return []
        try:
            resp = requests.post(self._rest(table), headers=self._headers("return=representation"), json=payload, timeout=25)
            resp.raise_for_status()
            data = resp.json()
            return data if isinstance(data, list) else []
        except Exception as exc:
            st.session_state.backend_error = str(exc)
            return []

    def update(self, table: str, payload: dict[str, Any], filters: dict[str, str]) -> list[dict[str, Any]]:
        if not self.ready:
            return []
        try:
            resp = requests.patch(self._rest(table), headers=self._headers("return=representation"), params=filters, json=payload, timeout=25)
            resp.raise_for_status()
            data = resp.json()
            return data if isinstance(data, list) else []
        except Exception as exc:
            st.session_state.backend_error = str(exc)
            return []

    def delete(self, table: str, filters: dict[str, str]) -> bool:
        if not self.ready:
            return False
        try:
            resp = requests.delete(self._rest(table), headers=self._headers(), params=filters, timeout=25)
            resp.raise_for_status()
            return True
        except Exception as exc:
            st.session_state.backend_error = str(exc)
            return False

    def upsert(self, table: str, payload: dict[str, Any], conflict: str) -> list[dict[str, Any]]:
        if not self.ready:
            return []
        try:
            resp = requests.post(
                self._rest(table),
                headers=self._headers("resolution=merge-duplicates,return=representation"),
                params={"on_conflict": conflict},
                json=payload,
                timeout=25,
            )
            resp.raise_for_status()
            data = resp.json()
            return data if isinstance(data, list) else []
        except Exception as exc:
            st.session_state.backend_error = str(exc)
            return []


def auth_sign_up(email: str, password: str, full_name: str = "") -> tuple[bool, str, dict[str, Any] | None]:
    config = get_config()
    if not config:
        return False, "Supabase is not configured.", None
    try:
        resp = requests.post(
            f"{config.url}/auth/v1/signup",
            headers={"apikey": config.anon_key, "Content-Type": "application/json"},
            json={"email": email, "password": password, "data": {"full_name": full_name}},
            timeout=25,
        )
        resp.raise_for_status()
        data = resp.json()
        return True, "Account created. Check email confirmation if enabled.", data
    except Exception as exc:
        return False, str(exc), None


def auth_sign_in(email: str, password: str) -> tuple[bool, str, dict[str, Any] | None]:
    config = get_config()
    if not config:
        return False, "Supabase is not configured.", None
    try:
        resp = requests.post(
            f"{config.url}/auth/v1/token?grant_type=password",
            headers={"apikey": config.anon_key, "Content-Type": "application/json"},
            json={"email": email, "password": password},
            timeout=25,
        )
        resp.raise_for_status()
        data = resp.json()
        return True, "Signed in.", data
    except Exception as exc:
        return False, str(exc), None


def current_user() -> dict[str, Any] | None:
    auth = st.session_state.get("auth")
    if not auth:
        return None
    user = auth.get("user") or {}
    email = (user.get("email") or "").lower()
    return {
        "id": user.get("id"),
        "email": email,
        "full_name": (user.get("user_metadata") or {}).get("full_name") or email.split("@")[0],
        "is_admin": email in admin_emails(),
        "access_token": auth.get("access_token"),
    }


def active_store(admin: bool = False) -> PulseStore:
    user = current_user()
    return PulseStore(access_token=(user or {}).get("access_token"), admin=admin)


def ensure_profile() -> None:
    user = current_user()
    if not user:
        return
    store = active_store()
    rows = store.select("profiles", {"id": f"eq.{user['id']}", "select": "*"})
    if rows:
        return
    store.insert(
        "profiles",
        {
            "id": user["id"],
            "email": user["email"],
            "full_name": user["full_name"],
            "role": "admin" if user["is_admin"] else "student",
        },
    )


def fetch_content_tree(fallback_tree: dict[str, Any]) -> dict[str, Any]:
    store = active_store()
    if not store.ready:
        return fallback_tree
    subjects = store.select("subjects", {"select": "*", "is_published": "eq.true"}, "sort_order.asc,name.asc")
    chapters = store.select("chapters", {"select": "*", "is_published": "eq.true"}, "sort_order.asc,title.asc")
    topics = store.select("topics", {"select": "*", "is_published": "eq.true"}, "sort_order.asc,title.asc")
    notes = store.select("notes", {"select": "*"}, "created_at.desc")
    resources = store.select("resources", {"select": "*"}, "created_at.desc")
    quizzes = store.select("quizzes", {"select": "*"}, "created_at.desc")
    questions = store.select("quiz_questions", {"select": "*"}, "sort_order.asc")
    flashcards = store.select("flashcards", {"select": "*"}, "sort_order.asc")
    if not subjects:
        return fallback_tree

    by_chapter: dict[str, list[dict[str, Any]]] = {}
    for chapter in chapters:
        by_chapter.setdefault(chapter["subject_id"], []).append(chapter)
    by_topic_notes: dict[str, list[dict[str, Any]]] = {}
    for note in notes:
        by_topic_notes.setdefault(note["topic_id"], []).append(note)
    by_topic_resources: dict[str, list[dict[str, Any]]] = {}
    for res in resources:
        by_topic_resources.setdefault(res["topic_id"], []).append(res)
    by_topic_quizzes: dict[str, list[dict[str, Any]]] = {}
    for quiz in quizzes:
        by_topic_quizzes.setdefault(quiz["topic_id"], []).append(quiz)
    by_quiz_questions: dict[str, list[dict[str, Any]]] = {}
    for question in questions:
        by_quiz_questions.setdefault(question["quiz_id"], []).append(question)
    by_topic_cards: dict[str, list[dict[str, Any]]] = {}
    for card in flashcards:
        by_topic_cards.setdefault(card["topic_id"], []).append(card)

    tree: dict[str, Any] = {}
    for subject in subjects:
        subject_name = subject["name"]
        tree[subject_name] = {}
        for chapter in by_chapter.get(subject["id"], []):
            tree[subject_name][chapter["title"]] = {}
            for topic in [row for row in topics if row["chapter_id"] == chapter["id"]]:
                topic_notes = by_topic_notes.get(topic["id"], [])
                long_note = next((n for n in topic_notes if n.get("note_type") == "full"), None) or (topic_notes[0] if topic_notes else {})
                short_note = next((n for n in topic_notes if n.get("note_type") == "short"), None) or {}
                pearls = topic.get("high_yield_points") or []
                if isinstance(pearls, str):
                    pearls = [pearls]
                cards = [{"id": c["id"], "front": c["front"], "back": c["back"]} for c in by_topic_cards.get(topic["id"], [])]
                topic_mcqs = []
                for quiz in by_topic_quizzes.get(topic["id"], []):
                    for question in by_quiz_questions.get(quiz["id"], []):
                        topic_mcqs.append(
                            {
                                "id": question["id"],
                                "quiz_id": quiz["id"],
                                "question": question["question"],
                                "options": question.get("options") or [],
                                "correct": question.get("correct_answer"),
                                "explanation": question.get("explanation") or "",
                            }
                        )
                tree[subject_name][chapter["title"]][topic["title"]] = {
                    "id": topic["id"],
                    "subject_id": subject["id"],
                    "chapter_id": chapter["id"],
                    "overview": topic.get("overview") or "",
                    "notes": long_note.get("content") or topic.get("full_notes") or "",
                    "short_notes": short_note.get("content") or topic.get("short_notes") or "",
                    "pearls": pearls,
                    "mnemonics": topic.get("mnemonics") or [],
                    "diagrams": [r for r in by_topic_resources.get(topic["id"], []) if r.get("resource_type") in {"diagram", "image"}],
                    "resources": by_topic_resources.get(topic["id"], []),
                    "flashcards": cards,
                    "mcqs": topic_mcqs,
                    "osce_viva": topic.get("osce_viva") or [],
                }
    return tree or fallback_tree


def fetch_assessment_bank(tree: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        q
        for subject in tree.values()
        for chapter in subject.values()
        for topic in chapter.values()
        for q in topic.get("mcqs", [])
    ]


def dashboard_metrics() -> dict[str, Any]:
    user = current_user()
    if not user:
        return {"streak": 0, "due_cards": 0, "completion": 0, "recent": []}
    store = active_store()
    progress = store.select("user_progress", {"user_id": f"eq.{user['id']}", "select": "*"}, "last_opened_at.desc")
    attempts = store.select("quiz_attempts", {"user_id": f"eq.{user['id']}", "select": "*"}, "created_at.desc")
    completed = len([p for p in progress if p.get("status") == "completed"])
    recent = progress[:6]
    dates = {str(p.get("last_opened_at", ""))[:10] for p in progress if p.get("last_opened_at")}
    streak = 0
    today = date.today()
    for offset in range(365):
        if (today - timedelta(days=offset)).isoformat() in dates:
            streak += 1
        else:
            break
    return {
        "streak": streak,
        "due_cards": max(0, 30 - completed),
        "completion": min(100, completed * 12),
        "recent": recent,
        "attempts": attempts[:5],
    }


def mark_topic_opened(topic_id: str | None) -> None:
    user = current_user()
    if not user or not topic_id:
        return
    active_store().upsert(
        "user_progress",
        {
            "user_id": user["id"],
            "topic_id": topic_id,
            "status": "in_progress",
            "last_opened_at": datetime.utcnow().isoformat(),
        },
        "user_id,topic_id",
    )


def mark_topic_completed(topic_id: str | None) -> None:
    user = current_user()
    if not user or not topic_id:
        return
    active_store().upsert(
        "user_progress",
        {
            "user_id": user["id"],
            "topic_id": topic_id,
            "status": "completed",
            "completion_percent": 100,
            "completed_at": datetime.utcnow().isoformat(),
            "last_opened_at": datetime.utcnow().isoformat(),
        },
        "user_id,topic_id",
    )


def save_bookmark(topic_id: str | None, resource_id: str | None = None) -> None:
    user = current_user()
    if not user or not topic_id:
        return
    active_store().upsert(
        "bookmarks",
        {"user_id": user["id"], "topic_id": topic_id, "resource_id": resource_id},
        "user_id,topic_id,resource_id",
    )


def save_last_opened_subject(subject_id: str | None) -> None:
    user = current_user()
    if not user or not subject_id:
        return
    active_store().update(
        "profiles",
        {"last_opened_subject_id": subject_id, "updated_at": datetime.utcnow().isoformat()},
        {"id": f"eq.{user['id']}"},
    )


def save_flashcard_progress(flashcard_id: str | None, rating: str) -> None:
    user = current_user()
    if not user or not flashcard_id:
        return
    active_store().upsert(
        "flashcard_progress",
        {"user_id": user["id"], "flashcard_id": flashcard_id, "rating": rating, "reviewed_at": datetime.utcnow().isoformat()},
        "user_id,flashcard_id",
    )


def save_quiz_attempt(quiz_id: str | None, topic_id: str | None, score: int, total: int, answers: dict[str, Any]) -> None:
    user = current_user()
    if not user:
        return
    active_store().insert(
        "quiz_attempts",
        {
            "user_id": user["id"],
            "quiz_id": quiz_id,
            "topic_id": topic_id,
            "score": score,
            "total_questions": total,
            "answers": answers,
        },
    )


def admin_delete(table: str, row_id: str) -> bool:
    return active_store(admin=True).delete(table, {"id": f"eq.{row_id}"})


def admin_insert(table: str, payload: dict[str, Any]) -> list[dict[str, Any]]:
    return active_store(admin=True).insert(table, payload)
