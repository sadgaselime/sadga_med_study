"""
subjects_page.py — MedStudy Oman 🏥
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Comprehensive Medical Subject Library: Years 1–6
· All subjects, all years, curated resources
· AI-powered real-time content generation
· Save-to-Vault for logged-in users
· Search, filter, topic explorer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import streamlit as st
import time
from datetime import datetime

try:
    import anthropic as _anthropic_lib
    _ANTHROPIC_OK = True
except ImportError:
    _ANTHROPIC_OK = False

# ══════════════════════════════════════════════════════════════════════════════
#  MASTER SUBJECTS LIBRARY
# ══════════════════════════════════════════════════════════════════════════════

SUBJECTS_LIBRARY = {

    # ─────────────────────────────── YEAR 1 ──────────────────────────────────
    1: {
        "Gross Anatomy": {
            "icon": "🦴", "color": "#e53e3e",
            "description": "Systematic study of the human body — limbs, thorax, abdomen, pelvis, head & neck, neuroanatomy.",
            "key_topics": [
                "Upper Limb", "Lower Limb", "Thorax & Mediastinum",
                "Abdomen & Pelvis", "Head & Neck", "Neuroanatomy",
                "Back & Vertebral Column", "Surface Anatomy"
            ],
            "resources": [
                {"type": "book", "title": "Gray's Anatomy for Students (4th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/grays-anatomy-for-students/drake/978-0-323-39304-1", "description": "The gold standard anatomy textbook used worldwide — comprehensive with stunning illustrations.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Clinically Oriented Anatomy — Moore (8th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781975155117", "description": "Clinically focused, great for connecting anatomy to medicine. Blue boxes = high yield.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Snell's Clinical Anatomy (10th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781496345660", "description": "Excellent clinical correlation, widely used in Gulf medical schools.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Netter's Atlas of Human Anatomy (7th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/netters-atlas-of-human-anatomy/netter/978-0-323-39304-1", "description": "The most beautiful anatomical atlas. Use alongside any textbook.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Anatomy | Ninja Nerd Science (Full Playlist)", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Whiteboard-style lectures covering all regions. Extremely clear and well-structured.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Anatomy Lectures — Armando Hasudungan", "source": "YouTube", "url": "https://www.youtube.com/@armandohasudungan", "description": "Artist-style anatomical drawings with narration. Perfect for visual learners.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Acland's Video Atlas of Human Anatomy", "source": "Acland Anatomy", "url": "https://aclandanatomy.com/", "description": "Dissection videos of real cadavers organized by region. Unmatched for 3D understanding.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Complete Human Anatomy — Dr. Najeeb", "source": "Dr. Najeeb Lectures", "url": "https://www.drnajeeblectures.com/", "description": "5000+ hours of medical lectures. Anatomy section is exhaustive and highly rated.", "free": False, "difficulty": "intermediate"},
                {"type": "notes", "title": "High-Yield Anatomy Notes — Medscape", "source": "Medscape", "url": "https://emedicine.medscape.com/anatomy", "description": "Concise clinical anatomy reference organized by system and region.", "free": True, "difficulty": "intermediate"},
                {"type": "mcq", "title": "Anatomy MCQs — Amboss Qbank", "source": "Amboss", "url": "https://www.amboss.com/us/qbank", "description": "High-quality anatomy questions with detailed explanations and learning cards.", "free": False, "difficulty": "advanced"},
                {"type": "app", "title": "Complete Anatomy — 3D4Medical", "source": "App Store / Play Store", "url": "https://3d4medical.com/apps/complete-anatomy", "description": "Best 3D anatomy app — rotate, dissect, and label. Essential for lab preparation.", "free": False, "difficulty": "beginner"},
                {"type": "app", "title": "Visible Body — Human Anatomy Atlas", "source": "Visible Body", "url": "https://www.visiblebody.com/", "description": "Interactive 3D models of all body systems. Great for studying spatial relationships.", "free": False, "difficulty": "beginner"},
                {"type": "guideline", "title": "Terminologia Anatomica (International Standard)", "source": "FCAT / FICAT", "url": "https://fipat.library.dal.ca/ta2/", "description": "Official anatomical terminology reference. Essential for precise medical communication.", "free": True, "difficulty": "advanced"},
            ],
        },

        "Histology & Embryology": {
            "icon": "🔬", "color": "#6b46c1",
            "description": "Microscopic anatomy of tissues and organs, plus development from fertilisation to birth.",
            "key_topics": [
                "Epithelial Tissue", "Connective Tissue", "Muscle Tissue",
                "Nervous Tissue", "Cardiovascular System Histo", "Gametogenesis",
                "Early Embryology", "Organogenesis", "Teratology", "Placenta"
            ],
            "resources": [
                {"type": "book", "title": "Junqueira's Basic Histology (16th Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=2850", "description": "Most comprehensive histology text with clear microscopy images and clinical notes.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Langman's Medical Embryology (14th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781975138561", "description": "The embryology classic — clear diagrams, clinical correlations, and mnemonics.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "The Developing Human (Moore & Persaud, 11th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/the-developing-human/moore/978-0-323-61154-0", "description": "Richly illustrated embryology with superb clinical correlation boxes.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Histology Lectures — Dr. Najeeb", "source": "Dr. Najeeb Lectures", "url": "https://www.drnajeeblectures.com/", "description": "Drawing-based histology explanations with clinical integration. Highly rated.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Embryology — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Whiteboard embryology series — gametogenesis through organogenesis.", "free": True, "difficulty": "beginner"},
                {"type": "notes", "title": "HistoGuide — Online Histology Atlas", "source": "University of Michigan", "url": "http://www.histologyguide.com/", "description": "Free virtual slides from U of Michigan. Pan and zoom high-resolution tissue sections.", "free": True, "difficulty": "intermediate"},
                {"type": "notes", "title": "BluHistology — Free Slide Atlas", "source": "Blue Histology", "url": "https://www.lab.anhb.uwa.edu.au/mb140/", "description": "Free annotated histology slides from University of Western Australia.", "free": True, "difficulty": "beginner"},
                {"type": "mcq", "title": "Histology & Cell Biology: BRS (6th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781975107291", "description": "Board-style review with questions per chapter. Excellent for exam prep.", "free": False, "difficulty": "advanced"},
            ],
        },

        "Physiology": {
            "icon": "💓", "color": "#e53e3e",
            "description": "How the body works — cardiovascular, respiratory, renal, GI, endocrine, neurophysiology.",
            "key_topics": [
                "Cell Physiology", "Cardiovascular Physiology", "Respiratory Physiology",
                "Renal & Acid-Base", "Gastrointestinal Physiology", "Endocrine Physiology",
                "Neurophysiology", "Muscle Physiology", "Reproductive Physiology"
            ],
            "resources": [
                {"type": "book", "title": "Guyton & Hall Medical Physiology (14th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/guyton-and-hall-textbook-of-medical-physiology/hall/978-0-323-59712-8", "description": "The definitive physiology textbook. Every medical student needs this reference.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Ganong's Review of Medical Physiology (26th Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=2525", "description": "More concise than Guyton; great review format with clinical vignettes.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "BRS Physiology (7th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781975106392", "description": "Perfect for exam review — concise summaries and board-style questions.", "free": False, "difficulty": "advanced"},
                {"type": "video", "title": "Physiology — Ninja Nerd Science (Complete)", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Best free physiology series on YouTube. Covers all organ systems comprehensively.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Cardiovascular Physiology — Khan Academy Medicine", "source": "YouTube / Khan Academy", "url": "https://www.khanacademy.org/science/health-and-medicine", "description": "Animated explanations of heart function, blood pressure regulation, ECG.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Physiology lectures — Professor Fink", "source": "YouTube", "url": "https://www.youtube.com/@ProfessorFink", "description": "Detailed physiology lectures — especially excellent for renal and respiratory.", "free": True, "difficulty": "intermediate"},
                {"type": "notes", "title": "Physiology Notes — Lecturio", "source": "Lecturio", "url": "https://www.lecturio.com/courses/physiology/", "description": "Concise physiology notes with embedded quiz questions.", "free": False, "difficulty": "intermediate"},
                {"type": "mcq", "title": "Physiology Viva & MCQ — Sembulingam", "source": "Jaypee", "url": "https://www.jaypeedigital.com/", "description": "Popular in Gulf medical schools — viva questions with model answers.", "free": False, "difficulty": "intermediate"},
                {"type": "app", "title": "Physiology Animations — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/", "description": "Beautifully animated physiology videos — great for visual understanding.", "free": False, "difficulty": "beginner"},
            ],
        },

        "Biochemistry": {
            "icon": "⚗️", "color": "#f6ad55",
            "description": "Metabolism, enzymology, molecular biology, and clinical correlations of biochemical disorders.",
            "key_topics": [
                "Carbohydrate Metabolism", "Lipid Metabolism", "Protein Metabolism",
                "Enzymes & Kinetics", "DNA/RNA & Molecular Biology", "Vitamins & Minerals",
                "Acid-Base Chemistry", "Haemoglobin & Porphyrins", "Nucleotide Metabolism"
            ],
            "resources": [
                {"type": "book", "title": "Harper's Illustrated Biochemistry (31st Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=3073", "description": "Comprehensive and clinically connected. Standard text in most medical schools.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Lippincott's Illustrated Reviews: Biochemistry (8th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781975155241", "description": "Most popular review book — clear illustrations, summaries, and Q&A.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "Lehninger Principles of Biochemistry (8th Ed)", "source": "W.H. Freeman", "url": "https://www.macmillanlearning.com/", "description": "In-depth biochemistry for thorough understanding of mechanisms.", "free": False, "difficulty": "advanced"},
                {"type": "video", "title": "Biochemistry — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Detailed whiteboard biochemistry covering all metabolic pathways.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Metabolism Lectures — Dr. Najeeb", "source": "Dr. Najeeb Lectures", "url": "https://www.drnajeeblectures.com/", "description": "Extremely detailed metabolic pathway lectures. Best for deep understanding.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Biochemistry — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Biochemistry", "description": "Animated biochemistry covering clinical correlations of metabolic disorders.", "free": False, "difficulty": "beginner"},
                {"type": "notes", "title": "Biochemistry Review — AMBOSS Library", "source": "AMBOSS", "url": "https://www.amboss.com/", "description": "High-yield biochemistry cards covering clinically relevant pathways.", "free": False, "difficulty": "advanced"},
                {"type": "mcq", "title": "Biochemistry MCQs — Champe Review", "source": "Wolters Kluwer", "url": "https://www.lww.com/", "description": "350 board-style questions with detailed explanations.", "free": False, "difficulty": "advanced"},
            ],
        },

        "Medical Ethics & Communication": {
            "icon": "⚖️", "color": "#38a169",
            "description": "Principles of biomedical ethics, patient communication, professionalism, and Omani medical law.",
            "key_topics": [
                "The 4 Principles (Beauchamp & Childress)", "Informed Consent",
                "Patient Confidentiality", "End-of-Life Decisions", "Research Ethics",
                "Islamic Medical Ethics", "Omani Medical Law", "Communication Skills"
            ],
            "resources": [
                {"type": "book", "title": "Principles of Biomedical Ethics (Beauchamp & Childress, 8th Ed)", "source": "Oxford University Press", "url": "https://global.oup.com/academic/product/principles-of-biomedical-ethics-9780190640873", "description": "The foundational text in biomedical ethics. Required reading for all medical students.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Medical Ethics Today — BMA (3rd Ed)", "source": "BMJ Books", "url": "https://www.bmj.com/", "description": "Practical guide to ethical decision-making in clinical practice.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Medical Ethics — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Medical_ethics", "description": "Concise animated videos on consent, confidentiality, and autonomy.", "free": False, "difficulty": "beginner"},
                {"type": "notes", "title": "Islamic Medical Ethics — IMANA Resources", "source": "IMANA", "url": "https://www.imana.org/", "description": "Islamic perspectives on biomedical ethics — particularly relevant for Oman.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "Oman Medical Speciality Board — Ethics Guidelines", "source": "OMSB", "url": "https://www.omsb.org/", "description": "Official OMSB professional conduct and ethics guidelines for Omani practitioners.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "Introduction to Clinical Medicine": {
            "icon": "🩺", "color": "#3182ce",
            "description": "History taking, physical examination skills, clinical reasoning, and patient interaction.",
            "key_topics": [
                "History Taking Framework", "General Examination", "Cardiovascular Exam",
                "Respiratory Exam", "Abdominal Exam", "Neurological Exam",
                "Clinical Reasoning", "Medical Documentation"
            ],
            "resources": [
                {"type": "book", "title": "Clinical Examination — Talley & O'Connor (9th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/clinical-examination/talley/978-0-7295-4259-9", "description": "The best clinical examination guide. Beautiful photos and systematic approach.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "Macleod's Clinical Examination (14th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/macleods-clinical-examination/douglas/978-0-7020-7467-0", "description": "Classic UK clinical examination text. Comprehensive with clinical tips.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Clinical Skills Videos — Geeky Medics", "source": "YouTube / Geeky Medics", "url": "https://www.youtube.com/@Geekymedics", "description": "OSCE-style examination videos for every system. Checklists included.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Stanford Medicine 25 — Clinical Exam Skills", "source": "Stanford Medicine", "url": "https://stanfordmedicine25.stanford.edu/", "description": "Expert clinical examination technique videos from Stanford faculty.", "free": True, "difficulty": "intermediate"},
                {"type": "app", "title": "Geeky Medics OSCE App", "source": "Geeky Medics", "url": "https://geekymedics.com/", "description": "OSCE checklists, clinical cases, and examination guides.", "free": False, "difficulty": "beginner"},
            ],
        },
    },

    # ─────────────────────────────── YEAR 2 ──────────────────────────────────
    2: {
        "General Pathology": {
            "icon": "🧫", "color": "#e53e3e",
            "description": "Mechanisms of disease — cell injury, inflammation, neoplasia, haemodynamics, immunopathology.",
            "key_topics": [
                "Cell Injury & Death", "Inflammation (Acute & Chronic)", "Tissue Repair",
                "Haemodynamic Disorders", "Neoplasia", "Immunopathology",
                "Environmental Pathology", "Nutritional Pathology"
            ],
            "resources": [
                {"type": "book", "title": "Robbins & Cotran Pathologic Basis of Disease (10th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/robbins-and-cotran-pathologic-basis-of-disease/kumar/978-0-323-53113-9", "description": "The bible of pathology. Comprehensive with excellent clinical correlation.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Robbins Basic Pathology (10th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/robbins-basic-pathology/kumar/978-0-323-35317-5", "description": "The condensed version of Robbins — ideal for medical students.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Pathoma — Fundamentals of Pathology (Hussain Sattar)", "source": "Pathoma", "url": "https://www.pathoma.com/", "description": "The most popular pathology review. Concise, high-yield, comes with video lectures.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Pathology — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Comprehensive pathology lectures organized by organ system.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Pathoma Video Lectures", "source": "Pathoma", "url": "https://www.pathoma.com/", "description": "Dr. Sattar's video lectures accompanying Pathoma text. Highest-rated pathology videos.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "General Pathology — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Pathology", "description": "Animated pathology with clinical cases and Q&A.", "free": False, "difficulty": "beginner"},
                {"type": "notes", "title": "PathologyOutlines.com — Free Reference", "source": "PathologyOutlines", "url": "https://www.pathologyoutlines.com/", "description": "Free comprehensive online pathology reference used by pathologists worldwide.", "free": True, "difficulty": "advanced"},
                {"type": "mcq", "title": "Goljan Rapid Review Pathology (5th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/rapid-review-pathology/goljan/978-0-323-47883-4", "description": "High-yield MCQ review. Dr. Goljan's audio lectures are legendary.", "free": False, "difficulty": "advanced"},
            ],
        },

        "Microbiology & Parasitology": {
            "icon": "🦠", "color": "#38a169",
            "description": "Bacteriology, virology, mycology, parasitology, and antimicrobial pharmacology.",
            "key_topics": [
                "Bacteriology (Gram +/−)", "Virology (DNA & RNA viruses)", "Mycology",
                "Parasitology (Protozoa, Helminths)", "Hospital-Acquired Infections",
                "Antimicrobial Mechanisms & Resistance", "Tropical Diseases (Oman-relevant)"
            ],
            "resources": [
                {"type": "book", "title": "Murray's Medical Microbiology (9th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/medical-microbiology/murray/978-0-323-67322-7", "description": "The most comprehensive microbiology text. Covers all organisms with pathogenesis.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Jawetz Melnick & Adelberg's Medical Microbiology (28th Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=2629", "description": "Classic microbiology text with excellent clinical vignettes.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Clinical Microbiology Made Ridiculously Simple (8th Ed)", "source": "MedMaster", "url": "https://medmaster.net/", "description": "Hilariously mnemonics-heavy — makes memorisation fun. Perfect complement.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Microbiology — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Complete microbiology coverage with detailed organism-by-organism breakdown.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Sketchy Micro (Mnemonics Videos)", "source": "Sketchy Medical", "url": "https://www.sketchy.com/", "description": "Story-based mnemonics for every microbe. Students consistently score higher after using this.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Bacteriology — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Bacteriology", "description": "Animated microbiology with clinical cases.", "free": False, "difficulty": "beginner"},
                {"type": "notes", "title": "WHO Tropical Disease Resources (Oman-relevant)", "source": "WHO EMRO", "url": "https://www.emro.who.int/topics/tropical-diseases/", "description": "WHO Eastern Mediterranean resources on tropical diseases prevalent in Oman.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "Oman National Antimicrobial Guidelines", "source": "Ministry of Health Oman", "url": "https://www.moh.gov.om/", "description": "Official MOH Oman antibiotic stewardship guidelines — clinically essential.", "free": True, "difficulty": "advanced"},
            ],
        },

        "Pharmacology": {
            "icon": "💊", "color": "#6b46c1",
            "description": "Drug mechanisms, pharmacokinetics, pharmacodynamics, and adverse effects by system.",
            "key_topics": [
                "Pharmacokinetics (ADME)", "CNS Pharmacology", "Cardiovascular Drugs",
                "Respiratory Drugs", "Antimicrobials", "GI Pharmacology",
                "Endocrine Pharmacology", "Cancer Chemotherapy", "Drug Interactions"
            ],
            "resources": [
                {"type": "book", "title": "Katzung's Basic & Clinical Pharmacology (15th Ed)", "source": "McGraw-Hill", "url": "https://accesspharmacy.mhmedical.com/book.aspx?bookID=2988", "description": "The definitive pharmacology textbook. Comprehensive with clinical focus.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Lippincott's Illustrated Reviews: Pharmacology (8th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781975170554", "description": "Most popular pharmacology review — colour diagrams and chapter summaries.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Pharmacology Made Easy — Pocket Guide", "source": "Various", "url": "https://www.sketchy.com/", "description": "Quick-reference drug card sets — ideal for clinical rotations.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Pharmacology — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Detailed mechanism-focused pharmacology lectures.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Sketchy Pharmacology (Mnemonics)", "source": "Sketchy Medical", "url": "https://www.sketchy.com/", "description": "Story-based drug mnemonics. One of the most effective learning tools for pharmacology.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Pharmacology — Dr. Najeeb", "source": "Dr. Najeeb Lectures", "url": "https://www.drnajeeblectures.com/", "description": "In-depth pharmacology with mechanisms drawn out step by step.", "free": False, "difficulty": "intermediate"},
                {"type": "notes", "title": "BNF Online (British National Formulary)", "source": "NICE / BNF", "url": "https://bnf.nice.org.uk/", "description": "Free online drug reference — doses, interactions, contraindications. Essential clinical tool.", "free": True, "difficulty": "intermediate"},
                {"type": "app", "title": "Epocrates Drug Reference App", "source": "Epocrates", "url": "https://www.epocrates.com/", "description": "Free drug interaction checker and reference app for clinical use.", "free": True, "difficulty": "beginner"},
                {"type": "mcq", "title": "Pharmacology Flashcards — Anki Deck (Zanki)", "source": "Anki / Zanki", "url": "https://ankiweb.net/", "description": "Community pharmacology Anki decks — spaced repetition for drug facts.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "Immunology": {
            "icon": "🛡️", "color": "#3182ce",
            "description": "Innate and adaptive immunity, hypersensitivity, immunodeficiency, autoimmunity, transplantation.",
            "key_topics": [
                "Innate Immunity", "Adaptive Immunity (B & T cells)", "Complement System",
                "MHC & Antigen Presentation", "Hypersensitivity (Type I–IV)",
                "Autoimmune Diseases", "Immunodeficiencies", "Transplant Immunology"
            ],
            "resources": [
                {"type": "book", "title": "Janeway's Immunobiology (10th Ed)", "source": "Garland Science", "url": "https://www.garlandscience.com/product/isbn/9780815345237", "description": "The definitive immunology text. Available free online via NCBI Bookshelf.", "free": True, "difficulty": "advanced"},
                {"type": "book", "title": "Clinical Immunology and Serology (Stevens, 4th Ed)", "source": "F.A. Davis", "url": "https://www.fadavis.com/", "description": "Clinical focus with laboratory immunology — excellent for practical applications.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Immunology — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Complete immunology series — one of the best free resources.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Immunology — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Immunology", "description": "Animated immunology with clear clinical correlations.", "free": False, "difficulty": "beginner"},
                {"type": "notes", "title": "Immunology Flashcards — Anki", "source": "Anki", "url": "https://ankiweb.net/", "description": "Shared Anki decks for immunology — use Zanki or Bros decks.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "Allergy & Immunology Guidelines — WAO", "source": "World Allergy Organization", "url": "https://www.worldallergy.org/", "description": "Clinical guidelines for allergic and immunological diseases.", "free": True, "difficulty": "advanced"},
            ],
        },

        "Genetics & Molecular Medicine": {
            "icon": "🧬", "color": "#e67e22",
            "description": "Mendelian genetics, chromosomal disorders, genetic testing, cancer genetics, and pharmacogenomics.",
            "key_topics": [
                "Mendelian Inheritance Patterns", "Chromosomal Disorders", "DNA Repair Disorders",
                "Mitochondrial Genetics", "Cancer Genetics", "Genetic Testing & Counselling",
                "Pharmacogenomics", "Gene Therapy"
            ],
            "resources": [
                {"type": "book", "title": "Thompson & Thompson Genetics in Medicine (8th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/genetics-in-medicine/nussbaum/978-1-4377-0696-3", "description": "The standard medical genetics textbook. Clear pedigree analysis and clinical cases.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Medical Genetics — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Medical_genetics", "description": "Animated genetics covering inheritance patterns and chromosomal disorders.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Genetics Explained — NHGRI YouTube", "source": "YouTube / NHGRI", "url": "https://www.youtube.com/@Genomedotgov", "description": "NIH National Human Genome Research Institute educational videos.", "free": True, "difficulty": "beginner"},
                {"type": "notes", "title": "OMIM — Online Mendelian Inheritance in Man", "source": "OMIM", "url": "https://www.omim.org/", "description": "Free comprehensive genetic disease database — essential reference.", "free": True, "difficulty": "advanced"},
            ],
        },

        "Biostatistics & Epidemiology": {
            "icon": "📊", "color": "#2c7873",
            "description": "Study design, statistical analysis, epidemiological measures, and evidence-based medicine fundamentals.",
            "key_topics": [
                "Types of Studies", "Bias & Confounding", "Sensitivity & Specificity",
                "Statistical Tests (t-test, chi-square)", "Relative Risk & Odds Ratio",
                "NNT & NNH", "Confidence Intervals", "Evidence-Based Medicine"
            ],
            "resources": [
                {"type": "book", "title": "Biostatistics for the Biological and Health Sciences (Triola, 3rd Ed)", "source": "Pearson", "url": "https://www.pearson.com/", "description": "Accessible stats for health sciences students with medical examples.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Essential Epidemiology (Webb et al., 4th Ed)", "source": "Cambridge University Press", "url": "https://www.cambridge.org/", "description": "Clear introduction to epidemiological principles with public health applications.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Biostatistics & Epidemiology — Ninja Nerd", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "High-yield stats series — covers every concept tested on boards.", "free": True, "difficulty": "beginner"},
                {"type": "notes", "title": "Cochrane Training Resources — Free", "source": "Cochrane", "url": "https://training.cochrane.org/", "description": "Free evidence-based medicine and systematic review methodology training.", "free": True, "difficulty": "intermediate"},
                {"type": "app", "title": "StatsCrunch — Online Statistics Calculator", "source": "StatsCrunch", "url": "https://www.statcrunch.com/", "description": "Web-based statistical analysis tool for practice problems.", "free": False, "difficulty": "intermediate"},
            ],
        },
    },

    # ─────────────────────────────── YEAR 3 ──────────────────────────────────
    3: {
        "Clinical Medicine I": {
            "icon": "🏥", "color": "#e53e3e",
            "description": "Systematic approach to common medical diseases — CVS, respiratory, GI, renal presentations.",
            "key_topics": [
                "Chest Pain & ACS", "Heart Failure", "Pneumonia & COPD",
                "Peptic Ulcer Disease", "Liver Disease", "Renal Failure (AKI vs CKD)",
                "Anaemia", "Diabetes Mellitus", "Hypertension"
            ],
            "resources": [
                {"type": "book", "title": "Kumar & Clark's Clinical Medicine (10th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/kumar-and-clarks-clinical-medicine/feather/978-0-7020-7870-8", "description": "The most comprehensive clinical medicine textbook — used in clinics worldwide.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Oxford Handbook of Clinical Medicine (10th Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-clinical-medicine-9780198745495", "description": "The pocket-sized clinical bible. Every doctor carries one.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "Harrison's Principles of Internal Medicine (21st Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=3095", "description": "The definitive internal medicine reference for complex presentations.", "free": False, "difficulty": "advanced"},
                {"type": "video", "title": "Internal Medicine — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Disease-by-disease walkthrough with pathophysiology to treatment.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Osmosis Clinical Medicine Videos", "source": "Osmosis", "url": "https://www.osmosis.org/", "description": "Animated disease explanations with clinical cases and MCQs.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "MedCram — Medical Topics Explained Clearly", "source": "YouTube / MedCram", "url": "https://www.youtube.com/@MedCram", "description": "Focused whiteboard explanations of clinical conditions — great for ward prep.", "free": True, "difficulty": "intermediate"},
                {"type": "notes", "title": "UpToDate Clinical Decision Support", "source": "UpToDate", "url": "https://www.uptodate.com/", "description": "The gold standard clinical reference used by practising physicians.", "free": False, "difficulty": "advanced"},
                {"type": "clinical", "title": "NICE Clinical Guidelines (UK)", "source": "NICE", "url": "https://www.nice.org.uk/guidance", "description": "Evidence-based clinical management guidelines.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "General Surgery": {
            "icon": "🔪", "color": "#2d3748",
            "description": "Surgical principles, trauma, pre/post-operative care, and common surgical conditions.",
            "key_topics": [
                "Surgical Principles & Consent", "Wound Healing", "Fluid & Electrolytes",
                "Acute Abdomen", "Appendicitis", "Hernia", "Bowel Obstruction",
                "Trauma Assessment (ATLS)", "Surgical Oncology Principles"
            ],
            "resources": [
                {"type": "book", "title": "Bailey & Love's Short Practice of Surgery (28th Ed)", "source": "CRC Press", "url": "https://www.crcpress.com/Bailey-and-Loves-Short-Practice-of-Surgery/Williams-OConnell-McCaskie/p/book/9781138292741", "description": "The definitive surgery textbook. Comprehensive coverage of all surgical conditions.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Oxford Handbook of Clinical Surgery (4th Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-clinical-surgery-9780198749301", "description": "Essential pocket guide for surgical wards and theatres.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "Schwartz's Principles of Surgery (11th Ed)", "source": "McGraw-Hill", "url": "https://accesssurgery.mhmedical.com/book.aspx?bookID=2576", "description": "American surgical standard text — comprehensive with excellent illustrations.", "free": False, "difficulty": "advanced"},
                {"type": "video", "title": "Surgery — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Surgical condition lectures from a clinical perspective.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "WebSurg — Surgical Video Library", "source": "WebSurg", "url": "https://www.websurg.com/", "description": "Free surgical procedure videos. Excellent for understanding operative techniques.", "free": True, "difficulty": "intermediate"},
                {"type": "clinical", "title": "ATLS — Advanced Trauma Life Support Guidelines", "source": "ACS", "url": "https://www.facs.org/quality-programs/atls/", "description": "Standard trauma management protocol. Essential for surgical clerks.", "free": False, "difficulty": "intermediate"},
            ],
        },

        "Community Medicine & Public Health": {
            "icon": "🌍", "color": "#38a169",
            "description": "Epidemiology, health promotion, preventive medicine, and Oman's health system.",
            "key_topics": [
                "Oman Health System", "National Vaccination Programme",
                "Non-Communicable Disease Prevention", "Maternal & Child Health",
                "Occupational Health", "Environmental Health",
                "Health Promotion Strategies", "Healthcare Economics"
            ],
            "resources": [
                {"type": "book", "title": "Park's Textbook of Preventive & Social Medicine (26th Ed)", "source": "Jaypee", "url": "https://www.jaypeedigital.com/", "description": "The go-to community medicine text used widely in Gulf medical schools.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Oxford Handbook of Public Health Practice (3rd Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-public-health-practice-9780199586097", "description": "Practical public health guide with global and regional perspectives.", "free": False, "difficulty": "intermediate"},
                {"type": "notes", "title": "Ministry of Health Oman — Annual Health Reports", "source": "MOH Oman", "url": "https://www.moh.gov.om/en/-/--27", "description": "Oman's official health statistics and public health reports — essential for exams.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "WHO EMRO — Eastern Mediterranean Health Reports", "source": "WHO EMRO", "url": "https://www.emro.who.int/", "description": "Regional health data and disease burden specific to the Middle East.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "Clinical Skills & OSCE Preparation": {
            "icon": "📋", "color": "#d69e2e",
            "description": "Clinical examination, procedural skills, communication, and OSCE technique.",
            "key_topics": [
                "Systemic Clinical Examination", "History Taking Frameworks",
                "Clinical Procedures (Cannula, Catheter, etc.)", "Interpretation Skills",
                "Breaking Bad News", "OSCE Station Technique", "Clinical Reasoning"
            ],
            "resources": [
                {"type": "video", "title": "Geeky Medics — All OSCE Stations", "source": "YouTube / Geeky Medics", "url": "https://www.youtube.com/@Geekymedics", "description": "The best free OSCE preparation resource — every station with checklists.", "free": True, "difficulty": "beginner"},
                {"type": "book", "title": "OSCE & Clinical Skills Handbook (Kate Tattersall)", "source": "Elsevier", "url": "https://www.elsevier.com/", "description": "Systematic guide to every OSCE station type.", "free": False, "difficulty": "beginner"},
                {"type": "app", "title": "Geeky Medics OSCE App", "source": "Geeky Medics", "url": "https://geekymedics.com/", "description": "OSCE checklists and clinical cases in app form.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Clinical Examination Videos — Stanford Medicine 25", "source": "Stanford", "url": "https://stanfordmedicine25.stanford.edu/", "description": "Technique-focused clinical examination videos from expert clinicians.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "Dermatology": {
            "icon": "🧴", "color": "#c05621",
            "description": "Skin diseases common in Oman — sun-related, infectious, inflammatory, and neoplastic.",
            "key_topics": [
                "Rash Morphology & Terminology", "Acne & Rosacea", "Eczema & Psoriasis",
                "Skin Infections (Fungal, Bacterial, Viral)", "Skin Cancer",
                "Vitiligo & Pigmentation Disorders", "Drug Reactions", "Tropical Skin Diseases"
            ],
            "resources": [
                {"type": "book", "title": "Rook's Textbook of Dermatology (9th Ed)", "source": "Wiley-Blackwell", "url": "https://www.wiley.com/en-gb/Rook%27s+Textbook+of+Dermatology%2C+4+Volume+Set%2C+9th+Edition-p-9781118441176", "description": "Comprehensive dermatology reference.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Oxford Handbook of Dermatology (4th Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-dermatology-9780198793342", "description": "Pocket guide ideal for clinical rotation.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "DermNet NZ Educational Videos", "source": "DermNet NZ", "url": "https://dermnetnz.org/", "description": "Free world-class dermatology image library and educational resources.", "free": True, "difficulty": "intermediate"},
                {"type": "notes", "title": "DermNet NZ — Free Image & Topic Library", "source": "DermNet NZ", "url": "https://dermnetnz.org/", "description": "The most comprehensive free online dermatology reference with clinical photos.", "free": True, "difficulty": "intermediate"},
            ],
        },
    },

    # ─────────────────────────────── YEAR 4 ──────────────────────────────────
    4: {
        "Internal Medicine": {
            "icon": "💉", "color": "#e53e3e",
            "description": "Advanced clinical management of medical conditions across all subspecialties.",
            "key_topics": [
                "Cardiology (ACS, Heart Failure, Arrhythmias)", "Respiratory (Asthma, COPD, TB)",
                "Gastroenterology", "Nephrology", "Endocrinology (DM, Thyroid)",
                "Rheumatology", "Haematology", "Neurology", "Infectious Diseases"
            ],
            "resources": [
                {"type": "book", "title": "Harrison's Principles of Internal Medicine (21st Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=3095", "description": "The gold standard internal medicine reference.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Washington Manual of Medical Therapeutics (36th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/", "description": "Essential ward manual — drug doses, management algorithms, practical guides.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Current Medical Diagnosis & Treatment (CMDT, 2024)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=3248", "description": "Annual update of clinical management guidelines. Highly practical.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Strong Medicine — YouTube", "source": "YouTube", "url": "https://www.youtube.com/@StrongMedicineYT", "description": "Excellent internal medicine case-based teaching videos.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Cardiovascular Medicine — Blaufuss", "source": "Blaufuss", "url": "http://www.blaufuss.org/", "description": "Free interactive heart sounds and murmur identification tool.", "free": True, "difficulty": "beginner"},
                {"type": "clinical", "title": "UpToDate — Clinical Decision Support", "source": "UpToDate", "url": "https://www.uptodate.com/", "description": "Used by practising physicians daily. The standard of care reference.", "free": False, "difficulty": "advanced"},
                {"type": "app", "title": "MDCalc — Medical Calculator App", "source": "MDCalc", "url": "https://www.mdcalc.com/", "description": "Free clinical scoring calculators — Wells, CHADS₂, Glasgow Coma Scale, etc.", "free": True, "difficulty": "intermediate"},
                {"type": "mcq", "title": "AMBOSS Qbank — Internal Medicine", "source": "AMBOSS", "url": "https://www.amboss.com/", "description": "Highest quality clinical question bank with detailed explanations.", "free": False, "difficulty": "advanced"},
            ],
        },

        "Obstetrics & Gynaecology": {
            "icon": "🤰", "color": "#e91e8c",
            "description": "Antenatal care, labour & delivery, postnatal care, gynaecological conditions and surgery.",
            "key_topics": [
                "Antenatal Care & Screening", "Labour & Delivery", "Obstetric Emergencies",
                "Postnatal Care", "Gynaecological Cancers", "Contraception",
                "Infertility", "Menstrual Disorders", "Ectopic Pregnancy"
            ],
            "resources": [
                {"type": "book", "title": "Williams Obstetrics (26th Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=3032", "description": "The definitive obstetrics reference. Comprehensive and evidence-based.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Oxford Handbook of O&G (3rd Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-obstetrics-and-gynaecology-9780198752738", "description": "Essential ward companion for O&G rotation.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "Ten Teachers Obstetrics (20th Ed)", "source": "CRC Press", "url": "https://www.crcpress.com/", "description": "Classic O&G undergraduate text — clear and well-illustrated.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "O&G — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Obstetrics_and_Gynecology", "description": "Animated O&G videos covering common conditions and emergencies.", "free": False, "difficulty": "beginner"},
                {"type": "guideline", "title": "RCOG Green-top Guidelines (Free)", "source": "RCOG", "url": "https://www.rcog.org.uk/guidance/browse-all-guidance/green-top-guidelines/", "description": "Free evidence-based obstetric and gynaecological management guidelines.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "WHO Obstetric Care Recommendations", "source": "WHO", "url": "https://www.who.int/publications/i/item/9789241550215", "description": "WHO antenatal, intrapartum, and postnatal care guidelines.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "Paediatrics & Child Health": {
            "icon": "👶", "color": "#ff9a3c",
            "description": "Child development, paediatric diseases, neonatology, and paediatric emergencies.",
            "key_topics": [
                "Normal Child Development & Growth", "Neonatology", "Paediatric Emergencies",
                "Respiratory Infections in Children", "Diarrhoeal Disease",
                "Malnutrition", "Congenital Heart Disease", "Febrile Seizures",
                "Vaccination Schedule (Oman)"
            ],
            "resources": [
                {"type": "book", "title": "Nelson Textbook of Paediatrics (21st Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/nelson-textbook-of-pediatrics/kliegman/978-0-323-52950-1", "description": "The bible of paediatrics. Comprehensive coverage of every childhood condition.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Oxford Handbook of Paediatrics (3rd Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-paediatrics-9780198789031", "description": "Essential pocket paediatrics guide for clinical rotations.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "Illustrated Textbook of Paediatrics (Lissauer, 5th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/illustrated-textbook-of-paediatrics/lissauer/978-0-7234-3874-0", "description": "Best undergraduate paediatrics text — highly visual with case presentations.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Paediatrics — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Pediatrics", "description": "Animated paediatric disease videos.", "free": False, "difficulty": "beginner"},
                {"type": "guideline", "title": "Oman Expanded Programme of Immunisation (EPI)", "source": "MOH Oman", "url": "https://www.moh.gov.om/", "description": "Official Oman vaccination schedule for children — essential for paediatrics.", "free": True, "difficulty": "beginner"},
                {"type": "guideline", "title": "PALS Guidelines — Paediatric Advanced Life Support", "source": "AHA / Resuscitation Council", "url": "https://www.heart.org/en/cpr/pals-for-healthcare-providers", "description": "Paediatric emergency management protocols.", "free": False, "difficulty": "intermediate"},
            ],
        },

        "Psychiatry & Behavioural Medicine": {
            "icon": "🧠", "color": "#6b46c1",
            "description": "Mental health disorders, psychopharmacology, psychotherapy, and consultation liaison psychiatry.",
            "key_topics": [
                "History Taking in Psychiatry", "Depression & Bipolar Disorder", "Schizophrenia",
                "Anxiety Disorders", "Substance Use Disorders", "Personality Disorders",
                "Child Psychiatry", "Dementia & Delirium", "Psychopharmacology",
                "Mental Health in Oman"
            ],
            "resources": [
                {"type": "book", "title": "Kaplan & Sadock's Synopsis of Psychiatry (12th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/product/9781975145569", "description": "The definitive psychiatry reference. Comprehensive and clinically oriented.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Oxford Handbook of Psychiatry (4th Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-psychiatry-9780198826200", "description": "Essential clinical psychiatry guide for rotation.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "DSM-5-TR — Diagnostic Manual", "source": "APA", "url": "https://www.psychiatry.org/psychiatrists/practice/dsm", "description": "Diagnostic criteria for all psychiatric disorders.", "free": False, "difficulty": "intermediate"},
                {"type": "video", "title": "Psychiatry — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Psychiatry", "description": "Clear animated psychiatry videos covering all major disorders.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Psychiatry — Ninja Nerd Science", "source": "YouTube", "url": "https://www.youtube.com/@NinjaNerdScience/playlists", "description": "Comprehensive psychiatry lecture series.", "free": True, "difficulty": "intermediate"},
                {"type": "notes", "title": "Mental Health Atlas — Oman WHO Report", "source": "WHO", "url": "https://www.who.int/teams/mental-health-and-substance-use/data-research/mental-health-atlas", "description": "WHO mental health data for Oman and the region.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "Radiology & Medical Imaging": {
            "icon": "🩻", "color": "#718096",
            "description": "Interpretation of X-rays, CT, MRI, ultrasound, and interventional radiology basics.",
            "key_topics": [
                "Chest X-Ray Interpretation", "Abdominal X-Ray", "CT Brain",
                "CT Chest & Abdomen", "Ultrasound Basics", "MRI Principles",
                "Contrast Studies", "Radiation Safety", "Interventional Radiology"
            ],
            "resources": [
                {"type": "book", "title": "Clinical Radiology: The Essentials (4th Ed)", "source": "Wolters Kluwer", "url": "https://www.lww.com/", "description": "Best undergraduate radiology introduction — image-heavy with clinical context.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Radiology Masterclass — Free", "source": "Radiology Masterclass", "url": "https://www.radiologymasterclass.co.uk/", "description": "Free online radiology tutorials with interactive images — highly recommended.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Learning Radiology — University of Maryland", "source": "Learning Radiology", "url": "https://www.learningradiology.com/", "description": "Free pattern recognition approach to radiology. Classic cases for all modalities.", "free": True, "difficulty": "beginner"},
                {"type": "app", "title": "Radiopaedia — Radiology Reference", "source": "Radiopaedia", "url": "https://radiopaedia.org/", "description": "Free world-class radiology reference with cases — used by radiologists globally.", "free": True, "difficulty": "intermediate"},
            ],
        },
    },

    # ─────────────────────────────── YEAR 5 ──────────────────────────────────
    5: {
        "Family Medicine & Primary Care": {
            "icon": "👨‍👩‍👧", "color": "#38a169",
            "description": "Comprehensive primary care, chronic disease management, preventive medicine, and community health.",
            "key_topics": [
                "Consultation Skills", "Chronic Disease Management", "Preventive Screening",
                "Mental Health in Primary Care", "Palliative Care", "Geriatrics",
                "Health Promotion", "Oman Primary Care System"
            ],
            "resources": [
                {"type": "book", "title": "Oxford Handbook of General Practice (5th Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-general-practice-9780198808916", "description": "Pocket guide for primary care consultations — practical and evidence-based.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "Murtagh's General Practice (7th Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=2800", "description": "Systematic approach to undifferentiated presentations in primary care.", "free": False, "difficulty": "intermediate"},
                {"type": "guideline", "title": "MOH Oman Clinical Practice Guidelines", "source": "MOH Oman", "url": "https://www.moh.gov.om/", "description": "Official Ministry of Health Oman clinical guidelines for primary care settings.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Family Medicine Cases — FPnotebook", "source": "FPnotebook", "url": "https://fpnotebook.com/", "description": "Free primary care clinical reference with evidence-based recommendations.", "free": True, "difficulty": "intermediate"},
            ],
        },

        "Emergency Medicine": {
            "icon": "🚨", "color": "#e53e3e",
            "description": "Acute resuscitation, trauma, toxicology, medical emergencies, and emergency procedures.",
            "key_topics": [
                "ABCDE Approach", "Cardiac Arrest & CPR", "Trauma (ATLS)", "Sepsis",
                "Acute Stroke Protocol", "Toxicology & Poisoning", "Anaphylaxis",
                "Obstetric Emergencies", "Paediatric Emergencies"
            ],
            "resources": [
                {"type": "book", "title": "Tintinalli's Emergency Medicine (9th Ed)", "source": "McGraw-Hill", "url": "https://accessmedicine.mhmedical.com/book.aspx?bookID=2353", "description": "The definitive emergency medicine reference.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Oxford Handbook of Emergency Medicine (5th Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-emergency-medicine-9780198784043", "description": "Essential pocket guide for the emergency department.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "EMCrit — Emergency Medicine & Critical Care", "source": "YouTube / EMCrit", "url": "https://www.youtube.com/@EMCritProject", "description": "Advanced emergency medicine and critical care lectures by Scott Weingart.", "free": True, "difficulty": "advanced"},
                {"type": "video", "title": "ALS — Resuscitation Council UK", "source": "Resuscitation Council UK", "url": "https://www.resus.org.uk/", "description": "Free ALS algorithm guides and resuscitation training materials.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "2021 AHA/ERC Resuscitation Guidelines", "source": "AHA", "url": "https://www.ahajournals.org/doi/10.1161/CIR.0000000000001018", "description": "Latest cardiac arrest and resuscitation guidelines.", "free": True, "difficulty": "intermediate"},
                {"type": "app", "title": "MDCalc — Emergency Scores", "source": "MDCalc", "url": "https://www.mdcalc.com/", "description": "Free scoring calculators: HEART, TIMI, Glasgow, Wells — essential in ED.", "free": True, "difficulty": "beginner"},
            ],
        },

        "Ophthalmology": {
            "icon": "👁️", "color": "#3182ce",
            "description": "Eye examination, common ophthalmic conditions, red eye, and surgical procedures.",
            "key_topics": [
                "Visual Acuity & Fields", "Slit Lamp Examination", "Red Eye Differential",
                "Glaucoma", "Cataracts", "Retinal Conditions", "Diabetic Retinopathy",
                "Ocular Emergencies", "Strabismus & Paediatric Ophthalmology"
            ],
            "resources": [
                {"type": "book", "title": "Kanski's Clinical Ophthalmology (9th Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/books/kanski-clinical-ophthalmology/bowling/978-0-7020-7713-8", "description": "The standard ophthalmology text — richly illustrated.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Oxford Handbook of Ophthalmology (4th Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-ophthalmology-9780198759027", "description": "Pocket reference for clinical rotations.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "Ophthalmology — EyeWiki (American Academy)", "source": "EyeWiki / AAO", "url": "https://eyewiki.aao.org/", "description": "Free comprehensive ophthalmology wiki by the American Academy of Ophthalmology.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Ophthalmology Video — Osmosis", "source": "Osmosis", "url": "https://www.osmosis.org/learn/Ophthalmology", "description": "Animated videos on glaucoma, cataracts, and retinal diseases.", "free": False, "difficulty": "beginner"},
            ],
        },

        "ENT — Ear, Nose & Throat": {
            "icon": "👂", "color": "#d69e2e",
            "description": "Otolaryngology — hearing, balance, sinusitis, airway diseases, and head & neck conditions.",
            "key_topics": [
                "Ear Examination & Hearing Tests", "Otitis Media & Externa",
                "Sinusitis & Rhinitis", "Throat Infections & Tonsillitis",
                "Epistaxis", "Head & Neck Cancer", "Hearing Loss",
                "Voice Disorders", "Sleep Apnoea"
            ],
            "resources": [
                {"type": "book", "title": "Scott-Brown's Otorhinolaryngology (8th Ed)", "source": "CRC Press", "url": "https://www.crcpress.com/", "description": "The comprehensive ENT reference text.", "free": False, "difficulty": "advanced"},
                {"type": "book", "title": "Oxford Handbook of ENT & Head and Neck Surgery (3rd Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-ent-and-head-and-neck-surgery-9780198745716", "description": "Pocket guide for ENT clinical rotation.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "ENT UK Video Library", "source": "ENT UK", "url": "https://www.entuk.org/", "description": "Free ENT educational videos and patient information resources.", "free": True, "difficulty": "intermediate"},
                {"type": "video", "title": "Geeky Medics ENT OSCE Stations", "source": "YouTube / Geeky Medics", "url": "https://www.youtube.com/@Geekymedics", "description": "ENT examination stations with checklists for OSCE preparation.", "free": True, "difficulty": "beginner"},
            ],
        },

        "Orthopaedics & Trauma": {
            "icon": "🦴", "color": "#744210",
            "description": "Musculoskeletal conditions, fracture management, sports injuries, and orthopaedic surgery.",
            "key_topics": [
                "Fracture Classification & Management", "Spine Conditions", "Hip Conditions",
                "Knee Disorders", "Shoulder & Upper Limb", "Sports Injuries",
                "Paediatric Orthopaedics", "Bone Tumours", "Infection in Bone (Osteomyelitis)"
            ],
            "resources": [
                {"type": "book", "title": "Apley & Solomon's Orthopaedics & Trauma (10th Ed)", "source": "CRC Press", "url": "https://www.crcpress.com/", "description": "The standard orthopaedics text — systematic and well-illustrated.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "Oxford Handbook of Orthopaedics & Trauma (2nd Ed)", "source": "Oxford", "url": "https://global.oup.com/academic/product/oxford-handbook-of-orthopaedics-and-trauma-9780199561155", "description": "Pocket guide for orthopaedic ward rounds.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "OrthoBullets — Free Orthopaedic Education", "source": "OrthoBullets", "url": "https://www.orthobullets.com/", "description": "Free comprehensive orthopaedics question bank and educational content.", "free": True, "difficulty": "intermediate"},
            ],
        },
    },

    # ─────────────────────────────── YEAR 6 ──────────────────────────────────
    6: {
        "OMSB Part 1 Preparation": {
            "icon": "🎯", "color": "#e53e3e",
            "description": "Targeted preparation for the Oman Medical Speciality Board Part 1 licensing examination.",
            "key_topics": [
                "OMSB Exam Format & Blueprint", "High-Yield Basic Sciences Review",
                "Clinical Scenario Questions", "Integrated Organ System Review",
                "Time Management & Exam Strategy", "OMSB Past Papers Analysis"
            ],
            "resources": [
                {"type": "book", "title": "First Aid for the USMLE Step 1 (2024)", "source": "McGraw-Hill", "url": "https://www.firstaidteam.com/", "description": "The most widely used high-yield review book. Highly applicable to OMSB Part 1.", "free": False, "difficulty": "intermediate"},
                {"type": "book", "title": "First Aid for the USMLE Step 2 CK (2024)", "source": "McGraw-Hill", "url": "https://www.firstaidteam.com/", "description": "Clinical high-yield review — covers most OMSB clinical scenario content.", "free": False, "difficulty": "intermediate"},
                {"type": "mcq", "title": "AMBOSS Qbank — All Systems", "source": "AMBOSS", "url": "https://www.amboss.com/", "description": "Highest quality question bank — used by top scorers globally.", "free": False, "difficulty": "advanced"},
                {"type": "mcq", "title": "UWorld Qbank — Step 1 & Step 2", "source": "UWorld", "url": "https://www.uworld.com/", "description": "The gold standard practice question bank. Unmatched explanations.", "free": False, "difficulty": "advanced"},
                {"type": "mcq", "title": "PASTEST Medical Question Bank", "source": "PASTEST", "url": "https://www.pastest.com/", "description": "UK-based MCQ bank relevant to OMSB style questions.", "free": False, "difficulty": "advanced"},
                {"type": "notes", "title": "Anki Flashcard Decks (Zanki / Brosencephalon)", "source": "Anki", "url": "https://ankiweb.net/", "description": "Free spaced repetition decks covering all basic science and clinical content.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "OMSB Official Website & Exam Information", "source": "OMSB", "url": "https://www.omsb.org/", "description": "Official OMSB exam schedules, blueprints, and application information.", "free": True, "difficulty": "beginner"},
                {"type": "video", "title": "Boards & Beyond — Integrated Review", "source": "Boards & Beyond", "url": "https://www.boardsandbeyond.com/", "description": "Concise video lectures designed for board exam preparation.", "free": False, "difficulty": "intermediate"},
            ],
        },

        "Clinical Medicine Advanced": {
            "icon": "🏥", "color": "#2b6cb0",
            "description": "Advanced management of complex medical presentations and subspecialty integration.",
            "key_topics": [
                "Critical Care Medicine", "Multi-Organ Failure", "Complex Cardiology",
                "Oncology Basics", "Palliative Care", "Clinical Audit",
                "Rare Diseases", "Medically Unexplained Symptoms"
            ],
            "resources": [
                {"type": "book", "title": "Oxford Textbook of Medicine (6th Ed)", "source": "Oxford", "url": "https://oxfordmedicine.com/view/10.1093/med/9780198746690.001.0001/med-9780198746690", "description": "Exhaustive medical reference for complex cases.", "free": False, "difficulty": "advanced"},
                {"type": "clinical", "title": "UpToDate — Subspecialty Sections", "source": "UpToDate", "url": "https://www.uptodate.com/", "description": "The definitive clinical decision support tool.", "free": False, "difficulty": "advanced"},
                {"type": "video", "title": "The Curbsiders — Internal Medicine Podcast", "source": "The Curbsiders", "url": "https://thecurbsiders.com/", "description": "Free internal medicine podcast with expert faculty. Excellent for advanced learning.", "free": True, "difficulty": "advanced"},
                {"type": "guideline", "title": "ESC/AHA Cardiology Guidelines 2023–2024", "source": "ESC / AHA", "url": "https://www.escardio.org/Guidelines", "description": "Latest European cardiology clinical practice guidelines.", "free": True, "difficulty": "advanced"},
            ],
        },

        "Research & Evidence-Based Medicine": {
            "icon": "📚", "color": "#6b46c1",
            "description": "Research methodology, critical appraisal, systematic review, and scientific writing.",
            "key_topics": [
                "Study Design (RCT, Cohort, Case-Control)", "Critical Appraisal Tools",
                "Systematic Reviews & Meta-Analysis", "Statistical Analysis",
                "Research Ethics", "Scientific Writing", "Citation & Referencing",
                "Presenting Research"
            ],
            "resources": [
                {"type": "book", "title": "How to Read a Paper (Trisha Greenhalgh, 6th Ed)", "source": "BMJ Books", "url": "https://www.bmj.com/", "description": "The best introduction to evidence-based medicine and critical appraisal.", "free": False, "difficulty": "beginner"},
                {"type": "notes", "title": "Cochrane Handbook for Systematic Reviews (Free)", "source": "Cochrane", "url": "https://training.cochrane.org/handbook", "description": "Free comprehensive guide to conducting systematic reviews.", "free": True, "difficulty": "advanced"},
                {"type": "notes", "title": "PRISMA Guidelines — Systematic Review Reporting", "source": "PRISMA", "url": "http://www.prisma-statement.org/", "description": "Free standard reporting guidelines for systematic reviews and meta-analyses.", "free": True, "difficulty": "intermediate"},
                {"type": "app", "title": "Mendeley — Free Reference Manager", "source": "Mendeley", "url": "https://www.mendeley.com/", "description": "Free citation management software — essential for research projects.", "free": True, "difficulty": "beginner"},
            ],
        },

        "Internship Preparation": {
            "icon": "🩺", "color": "#2d6a4f",
            "description": "Practical skills, prescribing, handover communication, and ward life preparation.",
            "key_topics": [
                "Safe Prescribing", "Clinical Handover (SBAR)", "Ward Procedures",
                "Blood Results Interpretation", "Drug Calculations",
                "On-Call Emergencies", "Team Communication", "Self-Care & Wellbeing"
            ],
            "resources": [
                {"type": "book", "title": "The Hands-On Guide for Junior Doctors (5th Ed)", "source": "Wiley-Blackwell", "url": "https://www.wiley.com/", "description": "Practical survival guide for newly graduated doctors — essential reading.", "free": False, "difficulty": "beginner"},
                {"type": "book", "title": "On Call — Principles & Protocols (2nd Ed)", "source": "Elsevier", "url": "https://www.elsevier.com/", "description": "How to handle on-call emergencies as a junior doctor.", "free": False, "difficulty": "beginner"},
                {"type": "video", "title": "How to be a Doctor — Life as a Junior Doctor", "source": "YouTube / Medic Mind", "url": "https://www.youtube.com/@medicmindorg", "description": "Practical advice for newly qualified doctors from experienced clinicians.", "free": True, "difficulty": "beginner"},
                {"type": "notes", "title": "British National Formulary — Free Online", "source": "BNF", "url": "https://bnf.nice.org.uk/", "description": "Free prescribing reference — drug doses, interactions, and contraindications.", "free": True, "difficulty": "beginner"},
                {"type": "app", "title": "MDCalc — Clinical Calculators", "source": "MDCalc", "url": "https://www.mdcalc.com/", "description": "Free clinical decision tools — GCS, Padua, Wells scores and more.", "free": True, "difficulty": "beginner"},
                {"type": "guideline", "title": "OMSB Intern Guidelines — Oman", "source": "OMSB", "url": "https://www.omsb.org/", "description": "Official OMSB internship requirements and competency framework for Oman.", "free": True, "difficulty": "beginner"},
            ],
        },

        "USMLE & International Exam Prep": {
            "icon": "🌍", "color": "#c05621",
            "description": "Preparation for USMLE Step 1, Step 2 CK, PLAB, and other international licensing exams.",
            "key_topics": [
                "USMLE Step 1 High-Yield Topics", "USMLE Step 2 CK Clinical Scenarios",
                "PLAB Preparation", "MRCP PACES", "AMC Exams (Australia)",
                "MCCEE (Canada)", "Clinical Vignette Strategy"
            ],
            "resources": [
                {"type": "book", "title": "First Aid for the USMLE Step 1 (2024)", "source": "McGraw-Hill", "url": "https://www.firstaidteam.com/", "description": "Essential for all international-exam-bound Omani students.", "free": False, "difficulty": "intermediate"},
                {"type": "mcq", "title": "UWorld USMLE Step 1 & Step 2 Qbank", "source": "UWorld", "url": "https://www.uworld.com/", "description": "The premier practice question bank for USMLE preparation.", "free": False, "difficulty": "advanced"},
                {"type": "mcq", "title": "PLABABLE — PLAB Qbank", "source": "PLABABLE", "url": "https://www.plabable.com/", "description": "UK-focused question bank for PLAB 1 & 2 preparation.", "free": False, "difficulty": "advanced"},
                {"type": "video", "title": "Boards & Beyond — USMLE Video Lectures", "source": "Boards & Beyond", "url": "https://www.boardsandbeyond.com/", "description": "High-yield video reviews aligned with USMLE content outline.", "free": False, "difficulty": "intermediate"},
                {"type": "guideline", "title": "USMLE Official Website — Content Outlines", "source": "USMLE", "url": "https://www.usmle.org/", "description": "Official USMLE content specifications and past performance data.", "free": True, "difficulty": "intermediate"},
                {"type": "guideline", "title": "PLAB — GMC Requirements & Registration", "source": "GMC UK", "url": "https://www.gmc-uk.org/registration-and-licensing/join-the-register/plab", "description": "Official GMC PLAB examination information for UK registration.", "free": True, "difficulty": "intermediate"},
            ],
        },
    },
}

# ══════════════════════════════════════════════════════════════════════════════
# RESOURCE TYPE METADATA
# ══════════════════════════════════════════════════════════════════════════════

RESOURCE_TYPE_META = {
    "book":      {"icon": "📖", "label": "Textbook",  "color": "#3182ce"},
    "video":     {"icon": "🎥", "label": "Video",     "color": "#e53e3e"},
    "notes":     {"icon": "📝", "label": "Notes",     "color": "#38a169"},
    "mcq":       {"icon": "❓", "label": "MCQ Bank",  "color": "#6b46c1"},
    "app":       {"icon": "📱", "label": "App",       "color": "#dd6b20"},
    "guideline": {"icon": "📋", "label": "Guideline", "color": "#2c7873"},
    "clinical":  {"icon": "🏥", "label": "Clinical",  "color": "#c05621"},
}

YEAR_LABELS = {
    1: "Year 1 — Pre-clinical Foundations",
    2: "Year 2 — Para-clinical Sciences",
    3: "Year 3 — Early Clinical",
    4: "Year 4 — Core Clinical Rotations",
    5: "Year 5 — Advanced Clinical",
    6: "Year 6 — Final Year & Beyond",
}

YEAR_ICONS = {1: "🔬", 2: "⚗️", 3: "🩺", 4: "🏥", 5: "⚕️", 6: "🎓"}

# ══════════════════════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════════════════════════════

def _save_to_vault(resource: dict, subject_name: str, year: int):
    """Append a resource to the user's vault in session state."""
    if "vault_items" not in st.session_state:
        st.session_state.vault_items = []
    item = {
        "id":       f"{year}_{subject_name}_{resource['title'][:20]}_{int(time.time())}",
        "icon":     RESOURCE_TYPE_META.get(resource["type"], {}).get("icon", "📌"),
        "title":    resource["title"],
        "source":   resource.get("source", ""),
        "url":      resource.get("url", ""),
        "subject":  subject_name,
        "year":     year,
        "type":     resource["type"],
        "saved_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }
    # De-duplicate
    if not any(v["title"] == item["title"] for v in st.session_state.vault_items):
        st.session_state.vault_items.append(item)
        return True
    return False


def _is_saved(title: str) -> bool:
    vault = st.session_state.get("vault_items", [])
    return any(v["title"] == title for v in vault)


def _generate_ai_content(subject_name: str, topic: str, year: int) -> str:
    """Call Anthropic API to generate AI study content for a subject/topic."""
    if not _ANTHROPIC_OK:
        return "⚠️ Anthropic library not installed. Run: pip install anthropic"
    try:
        client = _anthropic_lib.Anthropic()
        prompt = f"""You are an expert medical educator creating study notes for Omani medical students.

Generate comprehensive but concise study notes for:
- Subject: {subject_name} (Year {year} Medical Student)
- Topic: {topic}

Include:
1. 🎯 Key Concepts (3-5 bullet points)
2. 🔑 High-Yield Facts for Exams (numbered list)
3. 💡 Clinical Pearls (2-3 practical points)
4. 🧠 Memory Aid / Mnemonic (if applicable)
5. ⚠️ Common Exam Pitfalls to avoid

Format with clear headers and emoji. Keep it concise and high-yield.
Tailor content to be relevant for Oman (OMSB exams) when possible."""

        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        return message.content[0].text
    except Exception as e:
        return f"❌ AI generation failed: {str(e)}\n\nPlease check your API connection."


# ══════════════════════════════════════════════════════════════════════════════
# MAIN PAGE FUNCTION
# ══════════════════════════════════════════════════════════════════════════════

def subjects_page(theme: dict):
    """Main subjects page — full resource library for all years."""
    p  = theme["primary"]
    bg = theme["card_bg"]
    bdr = theme["card_border"]
    txt = theme["text"]
    sub = theme["subtext"]
    grd = theme["gradient"]
    glo = theme["glow"]
    glb = theme["glass_bg"]
    glbdr = theme["glass_border"]
    sa  = theme.get("sidebar_accent", p)
    is_dark = theme.get("family") == "dark"

    # ── Page Header ────────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:16px;margin-bottom:1.4rem;">
        <div style="width:52px;height:52px;border-radius:16px;
            background:{grd};
            display:flex;align-items:center;justify-content:center;
            font-size:1.7rem;flex-shrink:0;
            box-shadow:{glo},0 8px 24px rgba(0,0,0,0.25);">📚</div>
        <div>
            <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
                <div style="font-family:'Bricolage Grotesque',sans-serif;
                    font-size:1.9rem;font-weight:900;
                    color:{txt};letter-spacing:-0.04em;line-height:1.1;">
                    Medical Library</div>
                <span style="background:{p}22;border:1px solid {p}44;
                    border-radius:999px;padding:3px 12px;
                    font-size:0.72rem;font-weight:800;color:{p};
                    letter-spacing:0.08em;text-transform:uppercase;">
                    ✦ All Years</span>
            </div>
            <div style="font-size:0.82rem;color:{sub};margin-top:2px;">
                Curated resources for every subject · Years 1–6 · AI-powered content generation
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Initialise session keys ────────────────────────────────────────────────
    if "subj_selected_year" not in st.session_state:
        # Default to user's year if logged in, else Year 1
        if st.session_state.get("logged_in") and st.session_state.get("user"):
            try:
                st.session_state.subj_selected_year = int(
                    st.session_state.user.get("year", 1))
            except Exception:
                st.session_state.subj_selected_year = 1
        else:
            st.session_state.subj_selected_year = 1

    if "subj_search" not in st.session_state:
        st.session_state.subj_search = ""
    if "subj_type_filter" not in st.session_state:
        st.session_state.subj_type_filter = "All"
    if "ai_generated" not in st.session_state:
        st.session_state.ai_generated = {}
    if "expanded_subject" not in st.session_state:
        st.session_state.expanded_subject = None

    # ── Stats bar ──────────────────────────────────────────────────────────────
    total_resources = sum(
        len(subj["resources"])
        for yr_data in SUBJECTS_LIBRARY.values()
        for subj in yr_data.values()
    )
    total_subjects = sum(len(yr) for yr in SUBJECTS_LIBRARY.values())
    saved_count = len(st.session_state.get("vault_items", []))

    c1, c2, c3, c4 = st.columns(4)
    for col, (ico, val, lbl, clr) in zip([c1, c2, c3, c4], [
        ("📚", total_subjects, "Total Subjects", p),
        ("🔗", total_resources, "Resources", theme.get("success", "#10d982")),
        ("🎓", "6", "Years Covered", sa),
        ("🏦", saved_count, "Saved Items", theme.get("warning", "#fbbf24")),
    ]):
        with col:
            st.markdown(f"""
            <div style="background:{bg};border:1px solid {bdr};
                border-top:3px solid {clr};border-radius:14px;
                padding:0.9rem;text-align:center;margin-bottom:1rem;">
                <div style="font-size:1.3rem;">{ico}</div>
                <div style="font-family:'Bricolage Grotesque',sans-serif;
                    font-size:1.6rem;font-weight:900;color:{clr};">{val}</div>
                <div style="font-size:0.7rem;color:{sub};
                    font-weight:700;text-transform:uppercase;letter-spacing:0.08em;">{lbl}</div>
            </div>
            """, unsafe_allow_html=True)

    # ── YEAR SELECTOR ──────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="font-size:0.65rem;font-weight:800;letter-spacing:0.14em;
        text-transform:uppercase;color:{sub};margin-bottom:0.5rem;">
        Select Academic Year
    </div>
    """, unsafe_allow_html=True)

    # Show user's year prominently if logged in
    if st.session_state.get("logged_in") and st.session_state.get("user"):
        user_year = st.session_state.user.get("year")
        if user_year:
            st.markdown(f"""
            <div style="background:{p}15;border:1px solid {p}33;
                border-radius:10px;padding:0.5rem 1rem;
                margin-bottom:0.6rem;display:inline-flex;
                align-items:center;gap:8px;">
                <span style="font-size:1.1rem;">🎓</span>
                <span style="font-size:0.82rem;color:{p};font-weight:700;">
                    Your Year: {YEAR_ICONS.get(int(user_year), '📚')} {YEAR_LABELS.get(int(user_year), f'Year {user_year}')}</span>
            </div>
            """, unsafe_allow_html=True)

    yr_cols = st.columns(6)
    for i, (yr_num, yr_label) in enumerate(YEAR_LABELS.items()):
        with yr_cols[i]:
            active = st.session_state.subj_selected_year == yr_num
            is_user_year = (
                st.session_state.get("logged_in")
                and st.session_state.get("user")
                and str(st.session_state.user.get("year", "")) == str(yr_num)
            )
            btn_label = f"{YEAR_ICONS[yr_num]} Y{yr_num}"
            if is_user_year:
                btn_label += " ★"
            if st.button(btn_label, key=f"yr_btn_{yr_num}",
                         use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state.subj_selected_year = yr_num
                st.session_state.expanded_subject = None
                st.rerun()

    selected_year = st.session_state.subj_selected_year
    year_data = SUBJECTS_LIBRARY.get(selected_year, {})

    # Year label
    st.markdown(f"""
    <div style="margin:1rem 0 0.8rem;padding:0.8rem 1.2rem;
        background:{grd};border-radius:12px;
        display:flex;align-items:center;gap:10px;">
        <span style="font-size:1.4rem;">{YEAR_ICONS[selected_year]}</span>
        <div>
            <div style="font-family:'Bricolage Grotesque',sans-serif;
                font-size:1.05rem;font-weight:900;color:#ffffff;">
                {YEAR_LABELS[selected_year]}</div>
            <div style="font-size:0.75rem;color:rgba(255,255,255,0.7);">
                {len(year_data)} subjects · {sum(len(s['resources']) for s in year_data.values())} resources available
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── SEARCH & FILTER ROW ────────────────────────────────────────────────────
    sc1, sc2 = st.columns([3, 1])
    with sc1:
        search = st.text_input(
            "🔍 Search subjects or resources",
            value=st.session_state.subj_search,
            placeholder="e.g. anatomy, pharmacology, heart failure...",
            key="subj_search_input",
            label_visibility="collapsed",
        )
        st.session_state.subj_search = search.lower().strip()

    with sc2:
        type_opts = ["All"] + list(RESOURCE_TYPE_META.keys())
        type_filter = st.selectbox(
            "Filter by type",
            type_opts,
            index=type_opts.index(st.session_state.subj_type_filter),
            key="subj_type_filter_sel",
            label_visibility="collapsed",
        )
        st.session_state.subj_type_filter = type_filter

    st.markdown(f"""
    <div style="height:1px;background:linear-gradient(90deg,transparent,
        {bdr},transparent);margin:0.6rem 0 1rem;"></div>
    """, unsafe_allow_html=True)

    # ── OTHER YEARS QUICK ACCESS ───────────────────────────────────────────────
    other_years = [yr for yr in SUBJECTS_LIBRARY if yr != selected_year]
    st.markdown(f"""
    <div style="font-size:0.62rem;font-weight:800;letter-spacing:0.14em;
        text-transform:uppercase;color:{sub};margin-bottom:0.4rem;">
        Browse Other Years
    </div>
    """, unsafe_allow_html=True)
    oy_cols = st.columns(len(other_years))
    for i, yr in enumerate(other_years):
        with oy_cols[i]:
            yr_subject_count = len(SUBJECTS_LIBRARY[yr])
            st.markdown(f"""
            <div style="background:{bg};border:1px solid {bdr};
                border-radius:10px;padding:0.5rem;text-align:center;
                margin-bottom:0.6rem;cursor:pointer;font-size:0.78rem;">
                <div style="font-size:1rem;">{YEAR_ICONS[yr]}</div>
                <div style="color:{txt};font-weight:700;">Year {yr}</div>
                <div style="color:{sub};font-size:0.68rem;">{yr_subject_count} subjects</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Go Y{yr}", key=f"other_yr_{yr}",
                         use_container_width=True):
                st.session_state.subj_selected_year = yr
                st.session_state.expanded_subject = None
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── SUBJECT GRID ───────────────────────────────────────────────────────────
    search_q = st.session_state.subj_search
    type_f   = st.session_state.subj_type_filter

    # Filter subjects based on search
    filtered_subjects = {}
    for subj_name, subj_data in year_data.items():
        # Check subject name match
        name_match = not search_q or search_q in subj_name.lower()
        # Check resource match
        resource_match = any(
            search_q in r["title"].lower()
            or search_q in r.get("description", "").lower()
            or search_q in r.get("source", "").lower()
            for r in subj_data["resources"]
        ) if search_q else True
        # Type filter
        type_match = type_f == "All" or any(
            r["type"] == type_f for r in subj_data["resources"]
        )
        if (name_match or resource_match) and type_match:
            filtered_subjects[subj_name] = subj_data

    if not filtered_subjects:
        st.markdown(f"""
        <div style="text-align:center;padding:3rem;
            background:{bg};border:1px dashed {bdr};
            border-radius:16px;margin:1rem 0;">
            <div style="font-size:2.5rem;margin-bottom:0.8rem;">🔍</div>
            <div style="color:{txt};font-weight:700;font-size:1.1rem;">No subjects found</div>
            <div style="color:{sub};font-size:0.85rem;margin-top:0.4rem;">
                Try a different search term or year.</div>
        </div>
        """, unsafe_allow_html=True)
        return

    # Render subjects as cards (2 per row for subject overview)
    subj_list = list(filtered_subjects.items())
    for row_start in range(0, len(subj_list), 2):
        cols = st.columns(2)
        for col_i, (subj_name, subj_data) in enumerate(
                subj_list[row_start: row_start + 2]):
            with cols[col_i]:
                _render_subject_card(
                    subj_name, subj_data, selected_year,
                    theme, search_q, type_f, p, bg, bdr, txt, sub, grd, glo, glb, glbdr, sa
                )


def _render_subject_card(
    subj_name, subj_data, year,
    theme, search_q, type_f,
    p, bg, bdr, txt, sub, grd, glo, glb, glbdr, sa
):
    """Render one subject card with expandable resources."""
    subj_color = subj_data.get("color", p)
    subj_icon  = subj_data.get("icon", "📖")
    resources  = subj_data.get("resources", [])
    key_topics = subj_data.get("key_topics", [])

    # Filter resources
    if type_f != "All":
        resources = [r for r in resources if r["type"] == type_f]
    if search_q:
        resources = [r for r in resources if
                     search_q in r["title"].lower()
                     or search_q in r.get("description", "").lower()
                     or search_q in r.get("source", "").lower()
                     or search_q in subj_name.lower()]

    free_count = sum(1 for r in subj_data["resources"] if r.get("free"))
    total_count = len(subj_data["resources"])

    # Subject Card Header
    st.markdown(f"""
    <div style="background:{bg};border:1px solid {bdr};
        border-left:4px solid {subj_color};
        border-radius:14px;padding:1rem 1.1rem 0.6rem;
        margin-bottom:0.3rem;
        box-shadow:0 2px 12px rgba(0,0,0,0.08);">
        <div style="display:flex;align-items:flex-start;gap:10px;">
            <div style="width:42px;height:42px;border-radius:12px;
                background:{subj_color}22;border:1px solid {subj_color}44;
                display:flex;align-items:center;justify-content:center;
                font-size:1.3rem;flex-shrink:0;">{subj_icon}</div>
            <div style="flex:1;min-width:0;">
                <div style="font-family:'Bricolage Grotesque',sans-serif;
                    font-size:0.98rem;font-weight:900;color:{txt};
                    line-height:1.2;margin-bottom:0.3rem;">{subj_name}</div>
                <div style="font-size:0.75rem;color:{sub};
                    line-height:1.4;margin-bottom:0.5rem;">
                    {subj_data.get('description','')[:100]}...</div>
                <div style="display:flex;gap:6px;flex-wrap:wrap;">
                    <span style="background:{subj_color}18;border:1px solid {subj_color}33;
                        border-radius:999px;padding:2px 8px;
                        font-size:0.65rem;font-weight:700;color:{subj_color};">
                        📚 {total_count} Resources</span>
                    <span style="background:rgba(16,217,130,0.12);border:1px solid rgba(16,217,130,0.25);
                        border-radius:999px;padding:2px 8px;
                        font-size:0.65rem;font-weight:700;color:#10d982;">
                        🆓 {free_count} Free</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Expandable detail section
    with st.expander(f"📖 Open {subj_name}", expanded=False):

        # Key Topics
        if key_topics:
            topic_tags = "".join(f"""
            <span style="background:{subj_color}15;border:1px solid {subj_color}30;
                border-radius:999px;padding:2px 9px;margin:2px;display:inline-block;
                font-size:0.7rem;font-weight:600;color:{subj_color};">
                {t}</span>""" for t in key_topics)
            st.markdown(f"""
            <div style="margin-bottom:1rem;">
                <div style="font-size:0.65rem;font-weight:800;letter-spacing:0.12em;
                    text-transform:uppercase;color:{sub};margin-bottom:0.4rem;">
                    Key Topics</div>
                <div style="display:flex;flex-wrap:wrap;gap:2px;">{topic_tags}</div>
            </div>
            """, unsafe_allow_html=True)

        # Resource Type filter tabs within subject
        st.markdown(f"""
        <div style="font-size:0.65rem;font-weight:800;letter-spacing:0.12em;
            text-transform:uppercase;color:{sub};margin-bottom:0.5rem;">
            Resources ({len(resources)} shown)
        </div>
        """, unsafe_allow_html=True)

        if not resources:
            st.info("No resources match your current filter.")
        else:
            for res in resources:
                _render_resource_row(res, subj_name, year, theme,
                                     p, bg, bdr, txt, sub, grd, glo, subj_color)

        # ── AI Content Generator ────────────────────────────────────────────
        st.markdown(f"""
        <div style="height:1px;background:linear-gradient(90deg,transparent,
            {bdr},transparent);margin:1rem 0 0.8rem;"></div>
        <div style="font-size:0.65rem;font-weight:800;letter-spacing:0.12em;
            text-transform:uppercase;color:{sub};margin-bottom:0.5rem;">
            🤖 AI Study Content Generator
        </div>
        """, unsafe_allow_html=True)

        ai_key = f"ai_topic_{subj_name}_{year}"
        ai_col1, ai_col2 = st.columns([3, 1])
        with ai_col1:
            ai_topic = st.text_input(
                "Topic to generate notes for",
                placeholder=f"e.g. {key_topics[0] if key_topics else subj_name}",
                key=f"ai_input_{subj_name}_{year}",
                label_visibility="collapsed",
            )
        with ai_col2:
            generate_btn = st.button(
                "🤖 Generate",
                key=f"ai_gen_btn_{subj_name}_{year}",
                use_container_width=True,
                type="primary",
            )

        if generate_btn:
            if not ai_topic.strip():
                ai_topic = subj_name
            cache_key = f"{subj_name}_{year}_{ai_topic}"
            with st.spinner(f"🧠 Generating AI notes for {ai_topic}..."):
                content = _generate_ai_content(subj_name, ai_topic, year)
                st.session_state.ai_generated[cache_key] = {
                    "content": content,
                    "topic":   ai_topic,
                    "subject": subj_name,
                    "time":    datetime.now().strftime("%H:%M"),
                }

        # Show any AI-generated content for this subject
        for cache_key, ai_data in st.session_state.ai_generated.items():
            if ai_data["subject"] == subj_name and str(year) in cache_key:
                st.markdown(f"""
                <div style="background:{subj_color}0d;border:1px solid {subj_color}25;
                    border-radius:12px;padding:1rem;margin-top:0.5rem;">
                    <div style="display:flex;justify-content:space-between;
                        align-items:center;margin-bottom:0.6rem;">
                        <div style="font-size:0.78rem;font-weight:800;
                            color:{subj_color};">🤖 AI Notes: {ai_data['topic']}</div>
                        <div style="font-size:0.65rem;color:{sub};">
                            Generated at {ai_data['time']}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.markdown(ai_data["content"])

                # Save AI notes to vault
                if st.button(f"🏦 Save to Vault",
                             key=f"save_ai_{cache_key}"):
                    saved = _save_to_vault({
                        "type": "notes",
                        "title": f"AI Notes: {ai_data['topic']} ({subj_name})",
                        "source": "MedStudy AI",
                        "url": "",
                        "description": ai_data["content"][:200],
                    }, subj_name, year)
                    if saved:
                        st.success("✅ Saved to vault!")
                    else:
                        st.info("Already in vault.")


def _render_resource_row(res, subj_name, year, theme,
                         p, bg, bdr, txt, sub, grd, glo, subj_color):
    """Render one resource entry with save button."""
    rtype = res.get("type", "notes")
    rmeta = RESOURCE_TYPE_META.get(rtype, {"icon": "📌", "label": rtype.title(), "color": p})
    is_free  = res.get("free", False)
    diff     = res.get("difficulty", "")
    url      = res.get("url", "")
    already_saved = _is_saved(res["title"])
    diff_colors = {
        "beginner":     "#10d982",
        "intermediate": "#f59e0b",
        "advanced":     "#ef4444",
    }
    diff_color = diff_colors.get(diff, sub)

    st.markdown(f"""
    <div style="display:flex;align-items:flex-start;gap:10px;
        background:{bg};border:1px solid {bdr};
        border-radius:12px;padding:0.75rem 0.9rem;
        margin-bottom:0.4rem;
        transition:all 0.2s ease;">
        <div style="width:32px;height:32px;border-radius:8px;
            background:{rmeta['color']}18;
            display:flex;align-items:center;justify-content:center;
            font-size:1rem;flex-shrink:0;">{rmeta['icon']}</div>
        <div style="flex:1;min-width:0;">
            <div style="font-size:0.85rem;font-weight:700;
                color:{txt};margin-bottom:2px;
                white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
                {res['title']}</div>
            <div style="font-size:0.72rem;color:{sub};
                line-height:1.4;margin-bottom:0.35rem;">
                {res.get('description','')[:120]}</div>
            <div style="display:flex;gap:5px;flex-wrap:wrap;align-items:center;">
                <span style="background:{rmeta['color']}18;border:1px solid {rmeta['color']}33;
                    border-radius:999px;padding:1px 7px;
                    font-size:0.62rem;font-weight:700;color:{rmeta['color']};">
                    {rmeta['icon']} {rmeta['label']}</span>
                <span style="background:rgba(100,100,100,0.1);border:1px solid rgba(100,100,100,0.2);
                    border-radius:999px;padding:1px 7px;
                    font-size:0.62rem;font-weight:600;color:{sub};">
                    📦 {res.get('source','')}</span>
                {'<span style="background:rgba(16,217,130,0.12);border:1px solid rgba(16,217,130,0.25);border-radius:999px;padding:1px 7px;font-size:0.62rem;font-weight:700;color:#10d982;">🆓 Free</span>' if is_free else '<span style="background:rgba(245,158,11,0.12);border:1px solid rgba(245,158,11,0.25);border-radius:999px;padding:1px 7px;font-size:0.62rem;font-weight:700;color:#f59e0b;">💳 Paid</span>'}
                {f'<span style="background:{diff_color}18;border:1px solid {diff_color}33;border-radius:999px;padding:1px 7px;font-size:0.62rem;font-weight:700;color:{diff_color};">{diff.title()}</span>' if diff else ''}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Action buttons row
    btn_cols = st.columns([2, 1, 1])
    with btn_cols[0]:
        if url:
            st.link_button(
                f"🔗 Open Resource",
                url=url,
                use_container_width=True,
            )
    with btn_cols[1]:
        if already_saved:
            st.markdown(f"""
            <div style="text-align:center;padding:0.38rem;
                background:rgba(16,217,130,0.12);
                border:1px solid rgba(16,217,130,0.30);
                border-radius:8px;font-size:0.75rem;
                font-weight:700;color:#10d982;">
                ✓ Saved</div>
            """, unsafe_allow_html=True)
        else:
            if st.button("🏦 Save", key=f"save_{subj_name}_{year}_{res['title'][:15]}",
                         use_container_width=True):
                if not st.session_state.get("logged_in"):
                    st.warning("🔒 Login to save resources to your vault.")
                else:
                    saved = _save_to_vault(res, subj_name, year)
                    if saved:
                        st.success("✅ Saved!")
                        st.rerun()
                    else:
                        st.info("Already saved.")
    with btn_cols[2]:
        pass  # spacer
