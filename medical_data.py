"""
medical_data.py - permanent structured medical study library.

This module is intentionally local and deterministic. It powers the Static
Resource Vault without making network calls, so core study content remains
available even when AI services are unavailable.
"""

from __future__ import annotations


MEDICAL_LIBRARY = {
    "Cardiology": {
        "Acute Coronary Syndrome": {
            "overview": (
                "Acute coronary syndrome is myocardial ischemia caused by an abrupt "
                "drop in coronary blood flow. The key clinical task is to separate "
                "STEMI, NSTEMI, and unstable angina quickly."
            ),
            "detailed_notes": [
                "Typical symptoms include central crushing chest pain, radiation to the left arm or jaw, diaphoresis, nausea, and dyspnea.",
                "Immediate assessment includes ABCDE, 12-lead ECG within 10 minutes, troponin trend, vitals, contraindications to antithrombotics, and reperfusion eligibility.",
                "STEMI needs urgent reperfusion. NSTEMI risk stratification guides invasive timing and antithrombotic intensity.",
            ],
            "high_yield": [
                "ST elevation in contiguous leads is a reperfusion emergency.",
                "A normal first troponin does not exclude ACS if symptoms are early.",
                "Inferior MI can involve the right ventricle, so avoid nitrates if hypotensive or RV infarct is suspected.",
            ],
            "mcqs": [
                {
                    "question": "A 58-year-old man has crushing chest pain and ST elevation in II, III, and aVF. What is the most likely infarct territory?",
                    "options": ["Anterior", "Inferior", "Lateral", "Posterior"],
                    "answer": "Inferior",
                    "explanation": "Leads II, III, and aVF look at the inferior wall, commonly supplied by the RCA.",
                }
            ],
            "flashcards": [
                {"front": "Which ECG leads suggest inferior MI?", "back": "II, III, and aVF."},
                {"front": "What is the first test in suspected ACS?", "back": "Immediate 12-lead ECG, ideally within 10 minutes."},
            ],
        }
    },
    "Endocrinology": {
        "Diabetic Ketoacidosis": {
            "overview": (
                "DKA is an acute metabolic emergency caused by insulin deficiency "
                "with counter-regulatory hormone excess, producing hyperglycemia, "
                "ketosis, and metabolic acidosis."
            ),
            "detailed_notes": [
                "Common triggers include infection, missed insulin, myocardial infarction, stroke, pancreatitis, and new diagnosis of type 1 diabetes.",
                "Core management is fluids first, fixed-rate IV insulin, potassium monitoring/replacement, trigger treatment, and frequent reassessment.",
                "Do not start insulin if potassium is dangerously low; correct potassium first to avoid arrhythmia.",
            ],
            "high_yield": [
                "DKA diagnosis: hyperglycemia, ketones, and high anion gap metabolic acidosis.",
                "Total body potassium is depleted even if serum potassium is normal or high at presentation.",
                "Cerebral edema is a feared complication, especially with rapid osmolar shifts.",
            ],
            "mcqs": [
                {
                    "question": "A patient with DKA has K+ 2.9 mmol/L before insulin. What should happen first?",
                    "options": ["Start insulin immediately", "Give bicarbonate routinely", "Replace potassium before insulin", "Stop IV fluids"],
                    "answer": "Replace potassium before insulin",
                    "explanation": "Insulin shifts potassium intracellularly and can worsen hypokalemia, causing dangerous arrhythmias.",
                }
            ],
            "flashcards": [
                {"front": "What three features define DKA?", "back": "Hyperglycemia, ketonemia/ketonuria, and metabolic acidosis."},
                {"front": "Why can DKA serum potassium be high?", "back": "Acidosis and insulin deficiency shift potassium out of cells despite total body depletion."},
            ],
        }
    },
    "Neurology": {
        "Stroke Localization": {
            "overview": (
                "Stroke localization links neurologic deficits to vascular territories "
                "so urgent imaging, reperfusion decisions, and secondary prevention can be targeted."
            ),
            "detailed_notes": [
                "MCA stroke commonly causes contralateral face/arm weakness and sensory loss, aphasia if dominant hemisphere, or neglect if non-dominant.",
                "ACA stroke affects contralateral leg more than arm and may cause abulia or urinary incontinence.",
                "Posterior circulation stroke can cause diplopia, dysarthria, dysphagia, ataxia, vertigo, and crossed signs.",
            ],
            "high_yield": [
                "FAST catches many anterior circulation strokes but can miss posterior circulation signs.",
                "Dominant MCA lesions may cause aphasia; non-dominant MCA lesions may cause neglect.",
                "Time last known well determines thrombolysis/thrombectomy pathways.",
            ],
            "mcqs": [
                {
                    "question": "Right arm weakness, expressive aphasia, and right facial droop most strongly suggest which territory?",
                    "options": ["Left MCA", "Right MCA", "Left ACA", "Basilar artery"],
                    "answer": "Left MCA",
                    "explanation": "Dominant left MCA affects language cortex and contralateral face/arm motor function.",
                }
            ],
            "flashcards": [
                {"front": "Which artery is linked to aphasia?", "back": "Dominant hemisphere MCA."},
                {"front": "Which stroke territory affects leg more than arm?", "back": "ACA territory."},
            ],
        }
    },
}


def get_subjects() -> list[str]:
    return sorted(MEDICAL_LIBRARY)


def get_topics(subject: str) -> list[str]:
    return sorted(MEDICAL_LIBRARY.get(subject, {}))


def get_topic(subject: str, topic: str) -> dict:
    return MEDICAL_LIBRARY.get(subject, {}).get(topic, {})
