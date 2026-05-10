"""
anatomy_3d.py — 3D Anatomy Atlas
Interactive atlas using HTML5 Canvas — guaranteed to render
"""

import streamlit as st
import streamlit.components.v1 as components

ANATOMY_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<style>
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:100%;height:100%;background:#080c18;overflow:hidden;font-family:'Segoe UI',sans-serif;color:#e0eeff;}
#root{display:flex;width:100vw;height:100vh;}

#left{width:200px;min-width:200px;background:#0b0f1e;border-right:1px solid #1a2640;display:flex;flex-direction:column;overflow:hidden;}
#left-title{font-size:10px;font-weight:800;letter-spacing:.13em;text-transform:uppercase;color:#3a6a8a;padding:12px 12px 8px;border-bottom:1px solid #1a2640;}
#sys-tabs{display:flex;flex-wrap:wrap;gap:3px;padding:8px;border-bottom:1px solid #1a2640;}
.stab{font-size:9px;font-weight:700;padding:3px 6px;border-radius:5px;border:1px solid #1a2640;background:#0d1220;color:#5a8aaa;cursor:pointer;letter-spacing:.04em;}
.stab:hover{background:#1a2640;color:#ddeeff;}
.stab.on{background:#0f2035;border-color:#2060a0;color:#50aaee;}
#part-list{flex:1;overflow-y:auto;padding:4px;}
#part-list::-webkit-scrollbar{width:3px;}
#part-list::-webkit-scrollbar-thumb{background:#1a2640;border-radius:2px;}
.pgrp{font-size:8px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#204060;padding:7px 8px 3px;}
.pitem{display:flex;align-items:center;gap:6px;padding:5px 8px;border-radius:6px;cursor:pointer;font-size:11px;color:#7090a8;border:1px solid transparent;margin-bottom:1px;}
.pitem:hover{background:#0d1828;color:#ddeeff;}
.pitem.sel{background:#0a1c30;border-color:#1a5080;color:#50aaee;font-weight:700;}
.pdot{width:7px;height:7px;border-radius:50%;flex-shrink:0;}

#center{flex:1;position:relative;background:#060a14;overflow:hidden;}
#c{display:block;width:100%;height:100%;}

#topbar{position:absolute;top:10px;left:50%;transform:translateX(-50%);display:flex;gap:5px;background:rgba(8,12,24,.92);border:1px solid #1a2640;border-radius:9px;padding:5px 8px;backdrop-filter:blur(8px);z-index:10;}
.vbtn{font-size:9px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;padding:4px 10px;border-radius:5px;border:1px solid #1a2640;background:transparent;color:#5a8aaa;cursor:pointer;}
.vbtn:hover{background:#1a2640;color:#ddeeff;}
.vbtn.on{background:#0f2035;border-color:#2060a0;color:#50aaee;}

#topright{position:absolute;top:10px;right:10px;display:flex;gap:5px;z-index:10;}
.tbtn{font-size:9px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;padding:4px 10px;border-radius:6px;border:1px solid #1a2640;background:rgba(8,12,24,.92);color:#5a8aaa;cursor:pointer;}
.tbtn:hover{background:#1a2640;color:#ddeeff;}
.tbtn.on{background:#0f2035;border-color:#2060a0;color:#50aaee;}

#botbar{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);display:flex;gap:6px;align-items:center;background:rgba(8,12,24,.92);border:1px solid #1a2640;border-radius:9px;padding:6px 12px;backdrop-filter:blur(8px);z-index:10;}
.zbtn{width:28px;height:28px;border-radius:6px;border:1px solid #1a2640;background:#0d1220;color:#5a8aaa;cursor:pointer;font-size:16px;display:flex;align-items:center;justify-content:center;}
.zbtn:hover{background:#1a2640;color:#ddeeff;}
#zval{font-size:11px;color:#3a6a8a;min-width:38px;text-align:center;font-weight:700;}

#tip{position:absolute;pointer-events:none;background:rgba(8,14,28,.97);border:1px solid #2060a0;border-radius:7px;padding:5px 10px;font-size:11px;font-weight:700;color:#ddeeff;white-space:nowrap;display:none;z-index:99;}

#right{width:260px;min-width:260px;background:#0b0f1e;border-left:1px solid #1a2640;display:flex;flex-direction:column;}
#dhead{padding:12px 14px 10px;border-bottom:1px solid #1a2640;display:flex;align-items:flex-start;gap:8px;}
#dicon{font-size:20px;margin-top:1px;}
#dname{font-size:13px;font-weight:800;color:#ddeeff;line-height:1.2;}
#dlatin{font-size:10px;color:#3a6a8a;font-style:italic;margin-top:2px;}
#dbody{flex:1;overflow-y:auto;padding:12px;}
#dbody::-webkit-scrollbar{width:3px;}
#dbody::-webkit-scrollbar-thumb{background:#1a2640;border-radius:2px;}
.dsec{margin-bottom:12px;}
.dsec h4{font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#1a5080;margin-bottom:6px;padding-bottom:3px;border-bottom:1px solid #1a2640;}
.dsec p{font-size:11px;color:#8090a8;line-height:1.6;}
.dtag{display:inline-block;background:#0a1828;border:1px solid #1a2640;border-radius:4px;font-size:9px;color:#50aaee;padding:2px 6px;margin:2px 2px 2px 0;font-weight:600;}
.ctag{display:inline-block;background:#180808;border:1px solid #501010;border-radius:4px;font-size:9px;color:#e07070;padding:2px 6px;margin:2px 2px 2px 0;font-weight:600;}
.drow{display:flex;justify-content:space-between;align-items:flex-start;padding:4px 0;border-bottom:1px solid #0d1220;font-size:10px;}
.drow span:first-child{color:#3a6a8a;font-weight:700;flex-shrink:0;margin-right:6px;}
.drow span:last-child{color:#a0b8c8;text-align:right;line-height:1.4;}
#dempty{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#1a3050;font-size:12px;gap:8px;padding:16px;text-align:center;line-height:1.5;}
</style>
</head>
<body>
<div id="root">

<div id="left">
  <div id="left-title">Body Systems</div>
  <div id="sys-tabs"></div>
  <div id="part-list"></div>
</div>

<div id="center">
  <div id="topbar">
    <button class="vbtn on" data-v="ant">Anterior</button>
    <button class="vbtn" data-v="pos">Posterior</button>
    <button class="vbtn" data-v="latr">Rt. Lateral</button>
    <button class="vbtn" data-v="latl">Lt. Lateral</button>
    <button class="vbtn" data-v="sup">Superior</button>
  </div>
  <div id="topright">
    <button class="tbtn on" id="lblbtn">Labels ON</button>
    <button class="tbtn on" id="laybtn">All Layers</button>
  </div>
  <canvas id="c"></canvas>
  <div id="botbar">
    <button class="zbtn" id="zminus">−</button>
    <span id="zval">100%</span>
    <button class="zbtn" id="zplus">+</button>
    <button class="zbtn" id="zreset" style="margin-left:4px;font-size:13px;">⟳</button>
  </div>
  <div id="tip"></div>
</div>

<div id="right">
  <div id="dhead">
    <span id="dicon">🔬</span>
    <div>
      <div id="dname">Select a structure</div>
      <div id="dlatin">Click any part to explore</div>
    </div>
  </div>
  <div id="dbody">
    <div id="dempty">
      <svg width="48" height="48" viewBox="0 0 48 48" fill="none">
        <circle cx="24" cy="18" r="10" stroke="#1a5080" stroke-width="1.5"/>
        <path d="M10 42c0-7.7 6.3-14 14-14s14 6.3 14 14" stroke="#1a5080" stroke-width="1.5"/>
        <circle cx="24" cy="18" r="3.5" fill="#1a5080"/>
      </svg>
      Click any anatomical structure on the model to view detailed information
    </div>
    <div id="dcontent" style="display:none"></div>
  </div>
</div>

</div>
<script>
// ═══════════════════════════════════════════
// ANATOMY DATABASE
// ═══════════════════════════════════════════
const DB = {
  skull:{name:"Skull",latin:"Cranium",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"22 bones protecting the brain and supporting the face. Neurocranium (8 bones) + viscerocranium (14 bones).",
    fn:"Brain protection, sensory organ housing, facial muscle attachment, mastication",
    parts:["Frontal bone","Parietal ×2","Temporal ×2","Occipital","Sphenoid","Ethmoid","Maxilla ×2","Zygomatic ×2","Nasal ×2","Lacrimal ×2","Palatine ×2","Vomer","Inf. nasal conchae ×2","Mandible"],
    blood:"Internal carotid + vertebral arteries",nerve:"Cranial nerves I–XII",
    clinical:"Skull fractures, craniosynostosis, Paget's disease, basal skull fracture (Battle's sign)",size:"~21 cm length"},
  mandible:{name:"Mandible",latin:"Os mandibulae",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Only movable bone of the skull — the lower jaw. Forms the TMJ (temporomandibular joint) with the temporal bone.",
    fn:"Mastication, speech, lower dental arch support",
    parts:["Body","Ramus ×2","Condyle","Coronoid process","Mental protuberance","Alveolar process","Mandibular foramen"],
    blood:"Inferior alveolar artery",nerve:"Inferior alveolar nerve (V3 — mandibular branch of trigeminal)",
    clinical:"Fractures (most common facial bone after nasal), TMJ disorders, osteonecrosis of jaw (bisphosphonate-related)",size:"~10 cm width"},
  vertebral_column:{name:"Vertebral Column",latin:"Columna vertebralis",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"33 vertebrae: 7 cervical, 12 thoracic, 5 lumbar, 5 sacral (fused), 4 coccygeal (fused). Four physiological curves.",
    fn:"Axial support, spinal cord protection, movement, weight transmission to lower limbs",
    parts:["Cervical C1–C7 (atlas + axis)","Thoracic T1–T12","Lumbar L1–L5","Sacrum S1–S5","Coccyx","Intervertebral discs","Anterior/posterior longitudinal ligaments","Ligamentum flavum","Facet joints"],
    blood:"Segmental spinal arteries from aorta",nerve:"31 pairs of spinal nerves",
    clinical:"Herniated disc, scoliosis, spinal stenosis, osteoporotic compression fracture, ankylosing spondylitis",size:"~72 cm; 4 curves (cervical/lumbar lordosis, thoracic/sacral kyphosis)"},
  clavicle:{name:"Clavicle",latin:"Clavicula",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"S-shaped bone; only bony connection of upper limb to axial skeleton. Most frequently fractured bone in the body.",
    fn:"Transmits forces from upper limb to sternum, protects subclavian vessels and brachial plexus",
    parts:["Sternal end","Shaft","Acromial end","Conoid tubercle","Costoclavicular ligament attachment"],
    blood:"Thoracoacromial + suprascapular arteries",nerve:"Supraclavicular nerves C3–C4",
    clinical:"Most commonly fractured bone (fall on outstretched hand/shoulder); shoulder separation (AC joint injury)",size:"~15 cm length"},
  sternum:{name:"Sternum",latin:"Sternum",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Flat midline bone of the anterior thorax. Articulates with clavicles and costal cartilages of ribs 1–7.",
    fn:"Protects heart and great vessels; rib and pectoral muscle attachment",
    parts:["Manubrium","Body (gladiolus)","Xiphoid process","Sternal angle of Louis (T4/T5 — rib 2, aortic arch, carina)"],
    blood:"Internal thoracic arteries",nerve:"Intercostal nerves",
    clinical:"Sternal fracture (seat-belt injury), median sternotomy, sternal bone marrow biopsy, pectus excavatum/carinatum",size:"~17 cm length"},
  ribs:{name:"Ribs",latin:"Costae",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"12 pairs. True (1–7): direct sternal attachment. False (8–10): costal cartilage. Floating (11–12): free end.",
    fn:"Thoracic organ protection, respiratory mechanics (bucket-handle and pump-handle movements)",
    parts:["True ribs 1–7","False ribs 8–10","Floating ribs 11–12","Costal cartilage","Costal groove (VAN: vein above, artery middle, nerve below)","Head, neck, tubercle, angle, shaft"],
    blood:"Posterior intercostal arteries (from aorta)",nerve:"Intercostal nerves T1–T11",
    clinical:"Fractures (flail chest if ≥3 consecutive), costochondritis (Tietze syndrome), pleural effusion landmarks",size:"Varies 14–24 cm"},
  humerus:{name:"Humerus",latin:"Humerus",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Long bone of the upper arm. Proximal end articulates at shoulder (glenohumeral joint); distal end forms elbow.",
    fn:"Upper limb lever, muscle attachment, shoulder + elbow joint formation",
    parts:["Head","Anatomical neck","Surgical neck","Greater tuberosity","Lesser tuberosity","Intertubercular (bicipital) groove","Deltoid tuberosity","Radial (spiral) groove","Medial epicondyle","Lateral epicondyle","Capitulum","Trochlea","Olecranon fossa"],
    blood:"Anterior + posterior circumflex humeral arteries",nerve:"Radial nerve in spiral groove; axillary nerve at surgical neck",
    clinical:"Surgical neck fracture → axillary nerve injury; spiral groove fracture → radial nerve palsy (wrist drop); supracondylar fracture (children) → anterior interosseous nerve",size:"~33 cm length"},
  radius:{name:"Radius",latin:"Radius",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Lateral forearm bone; wider distally. Pivots around ulna during pronation/supination.",
    fn:"Forearm rotation (pronation/supination), wrist joint formation",
    parts:["Head (circular — for rotation)","Neck","Radial tuberosity (biceps insertion)","Shaft","Styloid process","Lister's tubercle","Carpal articular surface"],
    blood:"Radial artery branches",nerve:"Superficial radial nerve (sensory), posterior interosseous (motor)",
    clinical:"Colles' fracture (dorsal displacement — dinner fork deformity, most common adult fracture), Smith's fracture (volar), Galeazzi fracture",size:"~24 cm length"},
  ulna:{name:"Ulna",latin:"Ulna",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Medial forearm bone; wider proximally. Forms the stable hinge of the elbow joint.",
    fn:"Elbow hinge stability, forearm rotation",
    parts:["Olecranon (triceps insertion)","Trochlear notch","Coronoid process","Radial notch","Ulnar tuberosity","Shaft","Styloid process","Head"],
    blood:"Ulnar artery",nerve:"Ulnar nerve passes posterior to medial epicondyle",
    clinical:"Monteggia fracture (proximal ulna + radial head dislocation), olecranon fracture, olecranon bursitis",size:"~26 cm length"},
  pelvis:{name:"Pelvis",latin:"Pelvis",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Bony ring: 2 hip bones (ilium+ischium+pubis each) + sacrum + coccyx. Major sex differences relevant in obstetrics.",
    fn:"Weight transmission, pelvic organ protection, lower limb attachment",
    parts:["Ilium (largest — iliac crest)","Ischium (ischial tuberosity — sit bone)","Pubis","Acetabulum (socket for femoral head)","Sacrum","Pubic symphysis","Sacroiliac joints","Greater + lesser sciatic notches","Obturator foramen (largest foramen in body)"],
    blood:"Internal iliac artery and branches",nerve:"Lumbosacral plexus L1–S4",
    clinical:"Pelvic ring fractures, hip dysplasia, obstetric pelvis types (gynecoid most common/favourable), AVN of femoral head, sacral fracture",size:"Female: wider, shallower, larger outlet. Male: narrower, deeper"},
  femur:{name:"Femur",latin:"Femur",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Longest and strongest bone in the body. Angle of inclination ~126°, anteversion ~10–15°.",
    fn:"Lower limb weight bearing, hip + knee joint formation",
    parts:["Head","Fovea capitis (ligamentum teres)","Neck","Greater trochanter","Lesser trochanter","Intertrochanteric line (ant) / crest (post)","Shaft","Linea aspera","Medial + lateral condyles","Intercondylar notch","Adductor tubercle"],
    blood:"Medial circumflex femoral (main femoral head supply), lateral circumflex femoral, profunda femoris",nerve:"Femoral, obturator, sciatic nerve branches",
    clinical:"Femoral neck fracture (AVN risk, especially displaced), shaft fracture (significant blood loss ~1500mL), SCFE in adolescents, condylar fracture",size:"~46 cm; 1/4 of body height"},
  patella:{name:"Patella",latin:"Patella",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Largest sesamoid bone. Embedded in quadriceps tendon, articulates with femoral trochlea.",
    fn:"Increases quadriceps lever arm by ~50%, protects anterior knee, transmits tendon forces",
    parts:["Base (superior border)","Apex (inferior)","Medial + lateral facets (articular)","Anterior non-articular surface","Odd facet (extreme medial)"],
    blood:"Genicular arterial anastomosis",nerve:"Femoral + saphenous nerve branches",
    clinical:"Patellar fracture (transverse most common), chondromalacia patellae, patellar dislocation (lateral), patellofemoral syndrome, bipartite patella (normal variant)",size:"~4–5 cm diameter; ~22 g"},
  tibia:{name:"Tibia",latin:"Tibia",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Medial, weight-bearing bone of the leg (~85% of load). Second longest bone in the body.",
    fn:"Weight bearing, knee + ankle (mortise) joint formation, muscle attachment",
    parts:["Medial + lateral condyles","Tibial plateau","Tibial tuberosity (patellar ligament)","Gerdy's tubercle (IT band)","Anterior crest (shin)","Soleal line","Medial malleolus","Fibular notch"],
    blood:"Anterior + posterior tibial arteries",nerve:"Deep peroneal nerve (anterior compartment), tibial nerve (posterior)",
    clinical:"Tibial shaft fracture (high energy), Osgood-Schlatter disease (tibial tuberosity apophysitis), stress fracture, tibial plateau fracture (valgus force)",size:"~38 cm length"},
  fibula:{name:"Fibula",latin:"Fibula",sys:"Skeletal",col:"#90b8d8",icon:"🦴",
    desc:"Slender lateral leg bone. Not weight-bearing but critical for ankle mortise integrity.",
    fn:"Ankle stability (lateral malleolus), peroneal muscle origin, fibular graft donor site",
    parts:["Head","Neck (common peroneal nerve)","Shaft","Lateral malleolus"],
    blood:"Peroneal (fibular) artery",nerve:"Common peroneal nerve winds around fibular neck",
    clinical:"Lateral malleolus fracture (most common ankle fracture — Weber A/B/C), fibular neck fracture → foot drop, free fibular flap for jaw reconstruction",size:"~36 cm length"},
  heart:{name:"Heart",latin:"Cor",sys:"Cardiovascular",col:"#d04040",icon:"❤️",
    desc:"Hollow muscular pump in the middle mediastinum. ~100,000 beats/day, ~5L/min cardiac output at rest.",
    fn:"Pumps oxygenated blood to body (left) and deoxygenated blood to lungs (right)",
    parts:["Right atrium + auricle","Left atrium + auricle","Right ventricle","Left ventricle","SA node (pacemaker — right atrium)","AV node","Bundle of His + Purkinje fibres","Tricuspid valve (3 cusps — right)","Mitral/bicuspid valve (2 cusps — left)","Pulmonary valve","Aortic valve","Coronary sinus","Fossa ovalis","Chordae tendineae + papillary muscles"],
    blood:"RCA (right coronary), LAD (left anterior descending), LCx (left circumflex)",nerve:"Vagus X (↓HR), sympathetic cardiac nerves (↑HR, contractility)",
    clinical:"Myocardial infarction, heart failure (HFrEF/HFpEF), valvular disease, arrhythmias, cardiac tamponade, pericarditis",size:"~12×9×6 cm; ~300 g; fist-sized"},
  aorta:{name:"Aorta",latin:"Aorta",sys:"Cardiovascular",col:"#c03030",icon:"🩸",
    desc:"Largest artery. Arises from LV, arches left, descends through thorax and abdomen to bifurcate at L4.",
    fn:"Main arterial conduit for systemic oxygenated blood distribution",
    parts:["Aortic root + sinuses of Valsalva","Ascending aorta","Aortic arch (brachiocephalic, L common carotid, L subclavian)","Descending thoracic aorta","Abdominal aorta","Celiac, SMA, renal, IMA, common iliac branches"],
    blood:"Vasa vasorum (vessel wall)",nerve:"Aortic plexus",
    clinical:"Aortic dissection (Type A — ascending, surgical; Type B — descending, medical), abdominal aortic aneurysm (>5.5cm → surgery), coarctation, Marfan syndrome",size:"~3 cm diameter; ~40 cm length"},
  carotid:{name:"Carotid Arteries",latin:"Aa. carotides",sys:"Cardiovascular",col:"#c03040",icon:"🩸",
    desc:"Common carotid arteries divide at C4 level into ICA (brain, ~70% cerebral supply) and ECA (face/neck).",
    fn:"Cerebral blood supply (ICA → anterior circulation), face and neck (ECA)",
    parts:["CCA (common carotid)","ICA (internal — no branches in neck)","ECA (external — 8 branches: STA, facial, lingual, occipital, maxillary, etc.)","Carotid sinus (baroreceptor — CN IX)","Carotid body (chemoreceptor — O2/CO2/pH)","Carotid sheath (with IJV, vagus)"],
    blood:"Right: brachiocephalic trunk. Left: directly from aortic arch",nerve:"Glossopharyngeal IX (sinus reflex), sympathetic carotid plexus",
    clinical:"Carotid atherosclerosis (TIA/stroke), carotid endarterectomy, carotid body tumour (paraganglioma), carotid dissection",size:"~6 mm diameter"},
  pulmonary_vessels:{name:"Pulmonary Vessels",latin:"Vasa pulmonalia",sys:"Cardiovascular",col:"#5050c8",icon:"🩸",
    desc:"Unique: arteries carry deoxygenated blood TO lungs; veins return oxygenated blood FROM lungs to LA.",
    fn:"Pulmonary circulation — gas exchange loop",
    parts:["Pulmonary trunk (from RV)","Right pulmonary artery","Left pulmonary artery","Right pulmonary veins ×2 (superior + inferior)","Left pulmonary veins ×2"],
    blood:"Bronchial arteries (vessel wall nutrition)",nerve:"Pulmonary plexus (vagal + sympathetic)",
    clinical:"Pulmonary embolism (DVT→PE), pulmonary hypertension, Eisenmenger syndrome (ASD/VSD), pulmonary oedema",size:"Pulmonary trunk ~3 cm; normal PA pressure 25/8 mmHg"},
  lungs:{name:"Lungs",latin:"Pulmones",sys:"Respiratory",col:"#c07030",icon:"🫁",
    desc:"Right: 3 lobes, 10 bronchopulmonary segments. Left: 2 lobes, 8–9 segments (cardiac notch + lingula). ~500M alveoli.",
    fn:"O₂ uptake + CO₂ elimination. ~500mL tidal volume, TLC ~6L, FRC ~2.5L",
    parts:["Right: upper/middle/lower lobes","Left: upper/lower lobes","Hilum (bronchus, PA, pulmonary veins, lymphatics, nerve)","Visceral + parietal pleura","Bronchopulmonary segments (surgical units)","Alveoli (type I pneumocytes — gas exchange; type II — surfactant)","Carina at T4/T5"],
    blood:"Pulmonary arteries (gas exchange) + bronchial arteries (nutrition)",nerve:"Pulmonary plexus T2–T5 (sympathetic: bronchodilation) + vagus (bronchoconstriction)",
    clinical:"Pneumonia, COPD (emphysema/chronic bronchitis), lung cancer (#1 cancer death), pneumothorax, TB, pulmonary fibrosis",size:"Right ~700g, Left ~600g; TLC ~6L"},
  trachea:{name:"Trachea",latin:"Trachea",sys:"Respiratory",col:"#c07030",icon:"🫁",
    desc:"~11 cm × 2 cm cartilaginous tube. 16–20 C-shaped rings of hyaline cartilage. Bifurcates at carina (T4/T5).",
    fn:"Air conduction, mucociliary escalator (ciliated pseudostratified columnar epithelium)",
    parts:["16–20 C-shaped cartilage rings","Trachealis muscle (posterior — allows oesophageal expansion)","Carina (sensitive reflex zone)","Right main bronchus (wider, shorter, more vertical — foreign body site)","Left main bronchus (longer, more horizontal)"],
    blood:"Inferior thyroid artery",nerve:"Recurrent laryngeal nerve, vagus nerve",
    clinical:"Endotracheal intubation landmarks, tracheostomy (between rings 2–4), tracheal stenosis, right-sided foreign body aspiration, COPD",size:"~11 cm long; ~2 cm diameter; narrowest at cricoid in children"},
  larynx:{name:"Larynx",latin:"Larynx",sys:"Respiratory",col:"#c07030",icon:"🎤",
    desc:"Voice box at C3–C6. Contains the glottis (true vocal folds) — narrowest part of adult airway.",
    fn:"Phonation, airway protection (epiglottis during swallowing), cough reflex",
    parts:["Thyroid cartilage (Adam's apple)","Cricoid cartilage (only complete ring — landmark for cricothyroidotomy)","Arytenoid cartilages ×2","Epiglottis","True vocal folds/cords (glottis)","False vocal folds (vestibular folds)","Aryepiglottic folds","Subglottis"],
    blood:"Superior + inferior laryngeal arteries",nerve:"Superior laryngeal nerve (internal: sensation; external: cricothyroid muscle) + RLN (all other intrinsic muscles). Both from CN X.",
    clinical:"Laryngeal cancer (supraglottic/glottic/subglottic), vocal cord polyps, laryngospasm, RLN palsy after thyroid surgery → hoarseness",size:"~5 cm length; male larynx larger (puberty hormones)"},
  thyroid:{name:"Thyroid Gland",latin:"Glandula thyreoidea",sys:"Endocrine",col:"#60d890",icon:"🔬",
    desc:"Butterfly-shaped gland at C5–T1, anterior to trachea. Largest purely endocrine gland.",
    fn:"T3/T4 production (metabolism, growth, thermogenesis, cardiac rate). Calcitonin (↓serum Ca²⁺).",
    parts:["Right lobe","Left lobe","Isthmus (over tracheal rings 2–3)","Pyramidal lobe (50% have)","Follicular cells (T3/T4)","Parafollicular C cells (calcitonin)","Thyroid follicles (colloid)","Parathyroid glands ×4 (on posterior surface)"],
    blood:"Superior thyroid artery (1st branch ECA) + inferior thyroid artery (thyrocervical trunk of subclavian)",nerve:"Sympathetic from superior/middle cervical ganglia. RLN runs in tracheoesophageal groove.",
    clinical:"Hypothyroidism (Hashimoto's), hyperthyroidism (Graves'), papillary/follicular/medullary/anaplastic cancer, goitre, thyroid storm",size:"~25–30g; 4–5 cm each lobe"},
  adrenal_glands:{name:"Adrenal Glands",latin:"Glandulae suprarenales",sys:"Endocrine",col:"#60d890",icon:"🔬",
    desc:"Two glands atop kidneys. Right: pyramidal (overlaps IVC). Left: crescent-shaped. Cortex + medulla have different embryology.",
    fn:"Cortex: cortisol (stress), aldosterone (Na⁺/K⁺/BP), DHEA (androgens). Medulla: epinephrine + norepinephrine (fight-or-flight).",
    parts:["Cortex — zona glomerulosa (aldosterone → salt)","Cortex — zona fasciculata (cortisol → sugar)","Cortex — zona reticularis (androgens → sex) — GFR: salt/sugar/sex","Medulla — chromaffin cells (catecholamines)"],
    blood:"Superior suprarenal (inferior phrenic) + middle suprarenal (aorta) + inferior suprarenal (renal artery). Venous: R→IVC, L→left renal vein.",
    nerve:"Greater splanchnic nerve (pre-ganglionic sympathetic direct to medulla)",
    clinical:"Cushing's syndrome (↑cortisol), Addison's disease (adrenal insufficiency), pheochromocytoma (medulla), Conn's (hyperaldosteronism)",size:"~5×3×1 cm; ~5g each"},
  pituitary:{name:"Pituitary Gland",latin:"Hypophysis cerebri",sys:"Endocrine",col:"#60d890",icon:"🔬",
    desc:"'Master gland' in sella turcica of sphenoid bone. Connected to hypothalamus via infundibulum (stalk). Optic chiasm lies immediately above.",
    fn:"Anterior (adenohypophysis): GH, TSH, ACTH, FSH, LH, prolactin. Posterior (neurohypophysis): ADH + oxytocin (made in hypothalamus, stored here).",
    parts:["Anterior pituitary (adenohypophysis)","Posterior pituitary (neurohypophysis)","Pars intermedia","Infundibulum/stalk","Sella turcica","Cavernous sinus (lateral — CN III/IV/V1/V2/VI)"],
    blood:"Hypophyseal portal system (anterior — unique portal blood supply). Inferior hypophyseal artery (posterior).",
    nerve:"Hypothalamic–hypophyseal axons (ADH/oxytocin). Dopamine (portal) inhibits prolactin.",
    clinical:"Pituitary adenoma (prolactinoma #1), acromegaly (GH excess), Cushing's disease (ACTH), diabetes insipidus (ADH deficiency), bitemporal hemianopia (optic chiasm compression)",size:"~1×1 cm; ~0.6 g"},
  brain:{name:"Brain",latin:"Encephalon",sys:"Nervous",col:"#c080e0",icon:"🧠",
    desc:"~86 billion neurons, ~100 trillion synapses, ~1.4 kg. Uses 20% of body O₂ and glucose despite being 2% of body weight.",
    fn:"Cognition, memory, language, movement, sensation, autonomic regulation, endocrine control",
    parts:["Frontal lobe (motor cortex, Broca's area, personality)","Parietal lobe (somatosensory, spatial)","Temporal lobe (Wernicke's, memory, hearing)","Occipital lobe (visual cortex)","Cerebellum (coordination, balance, fine motor)","Midbrain (CN III/IV, substantia nigra, red nucleus)","Pons (CN V/VI/VII/VIII, respiratory centre)","Medulla (CN IX–XII, cardiac/respiratory/vasomotor centres)","Thalamus (relay station)","Hypothalamus (autonomic, endocrine, temperature)","Basal ganglia (movement initiation)","Corpus callosum","Limbic system (emotion, memory)","4 ventricles (CSF)"],
    blood:"Anterior circulation: ICA → ACA + MCA. Posterior: vertebral → basilar → PCA. Circle of Willis (anastomosis).",
    nerve:"Cranial nerves I–XII",
    clinical:"Ischaemic stroke (MCA most common), haemorrhagic stroke, brain tumour (GBM most malignant), epilepsy, Alzheimer's, Parkinson's, meningitis, TBI",size:"~1400g; ~1350mL volume; ~1.4L CSF/day produced"},
  spinal_cord:{name:"Spinal Cord",latin:"Medulla spinalis",sys:"Nervous",col:"#c080e0",icon:"🧠",
    desc:"Extends from medulla oblongata to conus medullaris at L1–L2. Cauda equina (L2–S5 roots) continues below in the dural sac.",
    fn:"Two-way signal conduit (ascending sensory / descending motor); spinal reflex arcs",
    parts:["31 spinal segments: 8C 12T 5L 5S 1Co","Cervical enlargement C4–T1 (brachial plexus)","Lumbar enlargement L2–S3 (lumbosacral plexus)","Conus medullaris (~L1-L2)","Cauda equina (L2–S5 nerve roots)","Filum terminale","Grey matter H (dorsal = sensory; ventral = motor)","White matter tracts (spinothalamic, corticospinal, dorsal columns)"],
    blood:"Anterior spinal artery (single — motor), posterior spinal arteries ×2 (sensory), artery of Adamkiewicz (T9–L1)",
    nerve:"31 pairs of mixed spinal nerves",
    clinical:"Spinal cord injury (ASIA grading), multiple sclerosis, syringomyelia, cauda equina syndrome (emergency), spinal stenosis",size:"~45 cm length; ~1 cm diameter"},
  liver:{name:"Liver",latin:"Hepar",sys:"Digestive",col:"#a06018",icon:"🫀",
    desc:"Largest internal organ (~1.5 kg). Right hypochondrium. 8 functional Couinaud segments; dual blood supply.",
    fn:"Metabolism (glucose/lipid/protein), detoxification, bile (600–1200mL/day), clotting factors (II,V,VII,IX,X,XI), albumin, glycogen storage, drug metabolism (CYP450)",
    parts:["Right lobe","Left lobe","Caudate lobe (Sg I)","Quadrate lobe","Gallbladder (stores + concentrates bile)","Portal triad (portal vein + hepatic artery + bile duct)","Hepatic veins → IVC","Glisson's capsule","Kupffer cells (macrophages)","Hepatocyte lobule"],
    blood:"Portal vein 75% (nutrient-rich) + hepatic artery 25% (oxygenated)",
    nerve:"Celiac plexus T7–T9, vagus",
    clinical:"Cirrhosis, viral hepatitis A/B/C, hepatocellular carcinoma, portal hypertension (varices, ascites, splenomegaly), NAFLD",size:"~1500g; 15–17 cm span"},
  stomach:{name:"Stomach",latin:"Gaster",sys:"Digestive",col:"#a06018",icon:"🫀",
    desc:"J-shaped dilated GI segment (cardia→pylorus). Left hypochondrium + epigastrium. Capacity 1–2L.",
    fn:"Mechanical churning, HCl secretion (pH 1–3), pepsinogen, intrinsic factor (B12 absorption), food reservoir",
    parts:["Cardia","Fundus","Body/corpus","Antrum","Pylorus + pyloric sphincter","Lesser curvature (left gastric + right gastric arteries)","Greater curvature (gastroepiploic arteries)","Rugae","Parietal cells (HCl + intrinsic factor)","Chief cells (pepsinogen)","G cells (gastrin)","D cells (somatostatin)"],
    blood:"Celiac trunk branches: left/right gastric, left/right gastroepiploic, short gastric arteries",
    nerve:"Vagus X (parasympathetic — ↑secretion + motility), celiac plexus (sympathetic)",
    clinical:"Peptic ulcer disease (H. pylori + NSAIDs), gastric cancer (intestinal/diffuse), GERD, gastroparesis, pyloric stenosis (infants — olive mass)",size:"~25 cm length; 1–2L capacity"},
  small_intestine:{name:"Small Intestine",latin:"Intestinum tenue",sys:"Digestive",col:"#a06018",icon:"🫀",
    desc:"6–7 m tube: duodenum (25 cm), jejunum (~2.5 m), ileum (~3.5 m). 90% of nutrient absorption occurs here.",
    fn:"Digestion (bile + pancreatic enzymes) + absorption (villi + microvilli = ×600 surface area increase)",
    parts:["Duodenum D1–D4 (retroperitoneal D2–D4)","Ampulla of Vater (bile + pancreatic duct)","Jejunum (tall villi, prominent plicae circulares)","Ileum (Peyer's patches, ileocecal valve)","Villi (enterocytes, goblet cells, enteroendocrine)","Microvilli/brush border","Crypts of Lieberkühn","Brunner's glands (duodenum — alkaline mucus)"],
    blood:"Superior mesenteric artery (SMA)",nerve:"Vagus (proximal), superior mesenteric plexus (distal)",
    clinical:"Crohn's disease (skip lesions, transmural), celiac disease (gluten), SBO, Meckel's diverticulum (2 inches, 2 feet from IC valve, 2% population), intussusception",size:"~6.5 m total; ~2.5 cm diameter"},
  large_intestine:{name:"Large Intestine",latin:"Intestinum crassum",sys:"Digestive",col:"#804010",icon:"🫀",
    desc:"~1.5 m. Wider (~6 cm) than small intestine. Absorbs water + electrolytes; forms faeces. Has taeniae coli, haustra, appendices epiploicae.",
    fn:"Water + electrolyte absorption, gut microbiome fermentation, faeces formation and continence",
    parts:["Caecum (blind pouch)","Appendix (lymphoid — lymphatic organ; McBurney's point)","Ascending colon","Hepatic (right colic) flexure","Transverse colon (intraperitoneal)","Splenic (left colic) flexure","Descending colon","Sigmoid colon","Rectum","Anal canal (dentate line — columnar above, squamous below)","Taeniae coli (3 bands)","Haustra"],
    blood:"SMA (ileocolic, right colic, middle colic — right side) + IMA (left colic, sigmoid, superior rectal — left side). Watershed: Griffiths point (splenic flexure) + Sudeck's point.",
    nerve:"Vagus to splenic flexure; pelvic splanchnic S2–S4 distal",
    clinical:"Colorectal cancer (#2 cancer death), diverticulitis, appendicitis (obstructed lumen), UC (continuous, mucosal), volvulus, Hirschsprung's disease",size:"~1.5 m; 6 cm diameter"},
  pancreas:{name:"Pancreas",latin:"Pancreas",sys:"Digestive",col:"#a06018",icon:"🫀",
    desc:"Mixed exocrine/endocrine retroperitoneal gland. C-curve of duodenum to splenic hilum. 95% exocrine (acini), 5% endocrine (islets of Langerhans).",
    fn:"Exocrine: amylase, lipase, proteases (trypsin/chymotrypsin/elastase) in alkaline (HCO₃⁻) juice. Endocrine: insulin (β), glucagon (α), somatostatin (δ), PP (γ).",
    parts:["Head (in duodenal C-curve)","Uncinate process (behind SMA/SMV)","Neck","Body","Tail (near splenic hilum)","Main duct of Wirsung → ampulla of Vater","Accessory duct of Santorini → minor papilla","Islets of Langerhans","Acinar cells"],
    blood:"Splenic artery (body/tail), superior + inferior pancreaticoduodenal arteries (head)",
    nerve:"Celiac plexus, vagus",
    clinical:"Acute pancreatitis (gallstones + alcohol = 80%), chronic pancreatitis, PDAC (pancreatic ductal adenocarcinoma — poor prognosis, Courvoisier's sign), insulinoma, VIPoma",size:"~15–20 cm length; ~70–100 g"},
  kidneys:{name:"Kidneys",latin:"Renes",sys:"Urinary",col:"#4060c8",icon:"🫘",
    desc:"Retroperitoneal at T12–L3 (right lower due to liver). Filter 180L plasma/day; produce 1–2L urine. Each has ~1 million nephrons.",
    fn:"Filtration + urine production, BP regulation (RAAS), erythropoietin (EPO), active Vitamin D (1,25-OH₂D₃), acid-base balance",
    parts:["Renal cortex (glomeruli, PCT, DCT)","Renal medulla + pyramids (loops of Henle, collecting ducts)","Columns of Bertin","Minor → major calyces → renal pelvis → ureter","Nephron (glomerulus + tubules)","Bowman's capsule","PCT → loop of Henle → DCT → collecting duct","Juxtaglomerular apparatus (renin secretion)","Hilum (renal artery, vein, ureter, lymphatics — anterior to posterior: VUA)"],
    blood:"Renal arteries direct from aorta at L1–L2; receive 25% of cardiac output (1250mL/min)",
    nerve:"Renal plexus T10–L1; pain referred to groin (T10–L1 dermatomal distribution)",
    clinical:"AKI/CKD, nephrolithiasis (calcium oxalate most common), UTI/pyelonephritis, renal cell carcinoma (haematuria + flank pain + mass), PCKD, renovascular HTN",size:"~11×6×3 cm; ~150 g each"},
  bladder:{name:"Urinary Bladder",latin:"Vesica urinaria",sys:"Urinary",col:"#4060c8",icon:"🫘",
    desc:"Hollow muscular organ behind pubic symphysis. Capacity 400–600 mL; urge to void at ~300 mL.",
    fn:"Urine storage (storage/filling phase) and controlled micturition (voiding phase)",
    parts:["Detrusor muscle (smooth — 3 layers)","Trigone (fixed triangle — ureteric orifices + internal urethral orifice)","Internal urethral sphincter (smooth — involuntary — sympathetic L1–L2)","External urethral sphincter (skeletal — voluntary — pudendal nerve S2–S4)","Dome","Neck","Urothelium (transitional epithelium)"],
    blood:"Superior + inferior vesical arteries (internal iliac)",
    nerve:"Parasympathetic S2–S4 (detrusor contraction/voiding), sympathetic L1–L2 (storage + IUS), pudendal S2–S4 (EUS)",
    clinical:"UTI/cystitis, bladder cancer (urothelial TCC #1 — haematuria), overactive bladder, urinary retention, bladder trauma (pelvic fracture)",size:"~400–600 mL capacity; ~8 cm when full"},
  spleen:{name:"Spleen",latin:"Lien",sys:"Lymphatic",col:"#7040a8",icon:"🔬",
    desc:"Largest lymphoid organ (~150g). Left hypochondrium, ribs 9–11. Notched anterior border. Not essential for life.",
    fn:"Blood filtration (removes senescent RBCs + platelets), immune response (IgM opsonins), blood reservoir, fetal haematopoiesis (until 5th month)",
    parts:["White pulp (lymphoid: B cells in follicles, T cells in PALS)","Red pulp (sinusoids + cords of Billroth — blood filtration)","Marginal zone","Trabecular framework","Splenic capsule (can rupture with blunt trauma)"],
    blood:"Splenic artery (largest branch of celiac trunk); drains via splenic vein → portal vein",
    nerve:"Celiac plexus",
    clinical:"Splenomegaly (malaria, EBV, portal HTN, lymphoma), splenic rupture (trauma — most commonly injured abdominal organ), post-splenectomy sepsis (encapsulated bacteria — pneumococcus, meningococcus, H.influenzae)",size:"~11×7×4 cm; ~150 g"},
  lymph_nodes:{name:"Lymph Nodes",latin:"Nodi lymphoidei",sys:"Lymphatic",col:"#7040a8",icon:"🔬",
    desc:"~600 bean-shaped immunological filters along lymphatics. Major groups: cervical, axillary, inguinal, mesenteric, mediastinal, para-aortic.",
    fn:"Filter lymph fluid, trap pathogens/antigens, B and T cell activation, antibody production",
    parts:["Cortex (B cell follicles + germinal centres)","Paracortex (T cells + dendritic cells)","Medulla (plasma cells, macrophages, medullary cords/sinuses)","Afferent lymphatics (multiple)","Efferent lymphatic (single, at hilum)","Subcapsular sinus","High endothelial venules (lymphocyte recirculation)"],
    blood:"Small arterioles via hilum",nerve:"Autonomic fibres",
    clinical:"Reactive lymphadenopathy (infection), Hodgkin's (Reed-Sternberg cells) vs non-Hodgkin's lymphoma, metastatic nodes (cancer staging — sentinel node biopsy), lymphoedema",size:"2–25 mm; cervical most accessible clinically"},
  thymus:{name:"Thymus",latin:"Thymus",sys:"Lymphatic",col:"#7040a8",icon:"🔬",
    desc:"Bilobed lymphoid organ, anterior superior mediastinum. Large in infancy (~30g at puberty), involutes after puberty.",
    fn:"T-lymphocyte maturation: positive selection (MHC recognition) and negative selection (self-tolerance/clonal deletion)",
    parts:["Two lobes","Cortex (immature thymocytes — positive selection)","Medulla (mature T cells — negative selection)","Hassall's corpuscles (medulla)","Thymic epithelial cells","Blood–thymus barrier"],
    blood:"Internal thoracic + inferior thyroid arteries",nerve:"Vagus, phrenic nerves",
    clinical:"Thymoma (associated with myasthenia gravis, pure red cell aplasia), DiGeorge syndrome (22q11.2 deletion — absent thymus + parathyroids), T cell immunodeficiency, SCID",size:"~30g at puberty; replaced by fat in adults"},
  deltoid:{name:"Deltoid",latin:"M. deltoideus",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Triangular muscle forming the rounded shoulder contour. Three distinct heads with different actions.",
    fn:"Middle (acromial): arm abduction 15°–90° (with supraspinatus initiating 0°–15°). Anterior: flexion + medial rotation. Posterior: extension + lateral rotation.",
    parts:["Anterior/clavicular head","Middle/acromial head","Posterior/spinous head","Deltoid tuberosity (humerus) — insertion","Subdeltoid bursa"],
    blood:"Anterior circumflex humeral artery, thoracoacromial artery",nerve:"Axillary nerve C5–C6 (via quadrilateral space — accompanied by posterior circumflex humeral artery)",
    clinical:"Axillary nerve injury → deltoid paralysis + lateral shoulder numbness ('regimental badge' area), IM injection site (middle deltoid), rotator cuff disease",size:"~18 cm wide; key shoulder muscle"},
  pectoralis_major:{name:"Pectoralis Major",latin:"M. pectoralis major",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Large fan-shaped anterior chest muscle. Two heads converge on bicipital groove.",
    fn:"Adduction + medial rotation of arm (primary). Clavicular: arm flexion. Sternocostal: arm extension from flexed position. Accessory inspiratory muscle.",
    parts:["Clavicular head (upper — anterior clavicle)","Sternocostal head (lower — sternum + costal cartilages 1–6)","Abdominal part","Insertion: crest of greater tubercle (intertubercular groove)"],
    blood:"Pectoral branches of thoracoacromial artery, lateral thoracic artery, anterior intercostal arteries",nerve:"Medial pectoral nerve (sternocostal) + lateral pectoral nerve (clavicular) — C5–T1",
    clinical:"Rupture in weightlifters (anterior axillary fold gap), radical mastectomy, pectoralis major flap for reconstruction",size:"~20 cm fan-shaped; key pushing/climbing muscle"},
  biceps_brachii:{name:"Biceps Brachii",latin:"M. biceps brachii",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Two-headed anterior arm muscle crossing both shoulder and elbow joints. Most powerful supinator.",
    fn:"Forearm supination (strongest — 'turn the corkscrew'), elbow flexion, weak shoulder flexion (long head)",
    parts:["Long head (supraglenoid tubercle — intraarticular tendon, prone to tenosynovitis)","Short head (coracoid process — with coracobrachialis)","Bicipital aponeurosis (lacertus fibrosus — protects brachial artery)","Radial tuberosity (insertion)"],
    blood:"Brachial artery branches",nerve:"Musculocutaneous nerve C5–C6",
    clinical:"Distal biceps tendon rupture → 'Popeye sign' (proximal bunching), bicipital tendinitis, SLAP lesion (long head origin), Speed's test",size:"~14 cm contracted length"},
  triceps:{name:"Triceps Brachii",latin:"M. triceps brachii",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Three-headed posterior arm muscle. Sole elbow extensor. Long head crosses the glenohumeral joint.",
    fn:"Elbow extension (primary — all 3 heads). Long head: shoulder extension + adduction.",
    parts:["Long head (infraglenoid tubercle of scapula)","Lateral head (posterior humerus — above and lateral to radial groove)","Medial head (posterior humerus — below radial groove, deepest)","Olecranon process (insertion)"],
    blood:"Deep brachial (profunda brachii) artery",nerve:"Radial nerve C6–C8 (all 3 heads; branches given off proximal to spiral groove for medial head and long head)",
    clinical:"Radial nerve palsy in spiral groove → wrist drop (triceps often spared); triceps tendon rupture (rare, 1% of tendon ruptures); olecranon bursitis",size:"~15 cm length; only elbow extensor"},
  latissimus_dorsi:{name:"Latissimus Dorsi",latin:"M. latissimus dorsi",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Widest muscle of the back. Broad flat muscle from lower trunk inserting into intertubercular groove of humerus.",
    fn:"Arm adduction, extension, medial rotation — 'the swimming/climbing muscle'. Accessory expiration. 'Coughing muscle'.",
    parts:["Vertebral part (T7–T12 spinous processes)","Iliac part (posterior iliac crest)","Costal part (ribs 9–12)","Scapular part (inferior angle)","Intertubercular groove insertion (anterior to teres major — 'Lady Between Two Majors')"],
    blood:"Thoracodorsal artery (branch of subscapular from axillary artery)",nerve:"Thoracodorsal nerve C6–C8",
    clinical:"Latissimus dorsi flap (breast reconstruction after mastectomy, mandibular reconstruction), 'swimmer's muscle', key in crutch-walking, shoulder rehabilitation",size:"~40×20 cm; largest back muscle"},
  quadriceps:{name:"Quadriceps Femoris",latin:"M. quadriceps femoris",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Four anterior thigh muscles converging into quadriceps tendon → patella → patellar ligament → tibial tuberosity. Largest muscle group.",
    fn:"Knee extension (all 4 heads). Hip flexion (rectus femoris only — only part crossing hip joint).",
    parts:["Rectus femoris (AIIS — crosses hip joint)","Vastus lateralis (largest head)","Vastus medialis (VMO — oblique fibres stabilise patella)","Vastus intermedius (deepest, under rectus femoris)","Quadriceps tendon","Patellar ligament","Medial + lateral retinacula"],
    blood:"Femoral artery, lateral circumflex femoral artery (descending branch)",nerve:"Femoral nerve L2–L4",
    clinical:"Quadriceps tendon rupture (>40yo), patellar tendon rupture (<40yo), patellofemoral syndrome, VMO wasting in knee injury, ACL rehab",size:"Largest muscle group in body; quadriceps to hamstrings ratio ~3:2"},
  hamstrings:{name:"Hamstrings",latin:"Mm. ischiocruales",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Three posterior thigh muscles from ischial tuberosity (except short head BF from linea aspera). Biarticular (except short head).",
    fn:"Knee flexion (primary). Hip extension. BF: lateral rotation. ST/SM: medial rotation of knee.",
    parts:["Biceps femoris — long head (ischial tuberosity)","Biceps femoris — short head (linea aspera) — only uniarticular hamstring","Semitendinosus (long cord-like tendon, part of pes anserinus)","Semimembranosus (flat membranous origin, posteromedial capsule insertion)","Popliteal fossa (diamond-shaped space)"],
    blood:"Perforating arteries from profunda femoris (femoral artery)",nerve:"Sciatic nerve: tibial division (long head BF, ST, SM) + common peroneal division (short head BF)",
    clinical:"Most common athletic muscle strain (proximal myotendinous junction), proximal hamstring avulsion (water skiers), posterior knee tightness in low back pain",size:"~35 cm length; 60% of quadriceps strength"},
  gastrocnemius:{name:"Gastrocnemius",latin:"M. gastrocnemius",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Superficial two-headed calf muscle. Forms the rounded lower leg contour. Part of triceps surae (with soleus).",
    fn:"Plantarflexion — most powerful when knee extended (biarticular). Weak knee flexion.",
    parts:["Medial head (larger — medial femoral condyle)","Lateral head (lateral femoral condyle)","Achilles tendon (calcaneal tendon — with soleus) — thickest tendon in body","Calcaneal insertion"],
    blood:"Sural arteries (from popliteal artery)",nerve:"Tibial nerve S1–S2",
    clinical:"'Tennis leg' (medial head tear — sudden calf pain), DVT vs muscle tear (ultrasound), Achilles tendinopathy, sural nerve (lateral cutaneous), DVT",size:"~20 cm length; combined calf ~5 cm diameter"},
  diaphragm:{name:"Diaphragm",latin:"Diaphragma",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Dome-shaped musculotendinous partition separating thorax from abdomen. Primary inspiratory muscle (~75% tidal volume).",
    fn:"Inspiration (contracts → descends → ↑thoracic volume → ↓pressure → air in). Also increases abdominal pressure for defaecation, micturition, parturition.",
    parts:["Central tendon (fibrous — no muscle here)","Sternal part (xiphoid process)","Costal part (ribs 7–12, costal cartilages)","Lumbar crura (right + left)","Aortic hiatus T12 (aorta, thoracic duct, azygos vein — 12 letters)","Oesophageal hiatus T10 (oesophagus, vagal trunks — 10 letters)","Caval opening T8 (IVC — 8 letters in 'vena cava')","Left phrenic nerve pierces muscle; right pierces central tendon"],
    blood:"Superior + inferior phrenic arteries, musculophrenic artery",nerve:"Phrenic nerve C3–C5 (motor + central sensory). 'C3,4,5 keeps the diaphragm alive.' Peripheral sensory: lower intercostals (T6–T11).",
    clinical:"Hiatus hernia (sliding — GERD; rolling/paraesophageal), congenital diaphragmatic hernia (Bochdalek/Morgagni), hiccups (phrenic irritation), referred shoulder pain C4",size:"~28 cm diameter; dome reaches T8 on right, T9 on left"},
  eye:{name:"Eye",latin:"Oculus",sys:"Sensory",col:"#40c8c0",icon:"👁️",
    desc:"Sphere ~24 mm. Contains refracting media and photoreceptor retina (~120M rods, ~6M cones). Protected by orbit, eyelids, tears.",
    fn:"Focuses light onto retina (cornea ~70%, lens ~30%); rods (low light/monochromatic), cones (colour/acuity); signals via CN II to occipital cortex",
    parts:["Cornea (refracts ~70% of light, avascular)","Anterior + posterior chambers (aqueous humour)","Iris + ciliary body","Lens (accommodation — CN III)","Vitreous humour (posterior segment)","Retina: macula lutea + fovea centralis (highest acuity)","Optic nerve (CN II)","Choroid (vascular layer)","Sclera (white coat)","Conjunctiva","Extraocular muscles ×6 (CN III/IV/VI)","Lacrimal apparatus"],
    blood:"Ophthalmic artery (1st branch ICA) → central retinal artery (end artery)",nerve:"CN II (vision), CN III (medial/inferior/superior rectus, IO, levator, pupil constriction), CN IV (SO), CN VI (lateral rectus), CN V1 (corneal sensation — afferent blink reflex), CN VII (orbicularis — efferent blink)",
    clinical:"Glaucoma (↑IOP), cataract (lens opacity), retinal detachment, AMD, diabetic retinopathy, CRAO (central retinal artery occlusion — painless sudden vision loss), papilloedema",size:"~24 mm AP diameter; IOP normal 10–21 mmHg"},
  ear:{name:"Ear",latin:"Auris",sys:"Sensory",col:"#40c8c0",icon:"👂",
    desc:"Organ of hearing + vestibular balance. Three compartments: external, middle, inner.",
    fn:"Sound: pinna → EAC → tympanic membrane → ossicles → oval window → cochlea → CN VIII → temporal lobe. Balance: semicircular canals + utricle/saccule → vestibular nuclei → cerebellum.",
    parts:["External: pinna/auricle, EAC (S-shaped), tympanic membrane (cone-shaped, light reflex at 5 o'clock)","Middle: malleus, incus, stapes (ossicles — smallest bones in body), Eustachian tube (equalises pressure, connects to nasopharynx), tensor tympani (CN V3), stapedius (CN VII — protects against loud sounds)","Inner: cochlea (organ of Corti — hair cells), vestibule, 3 semicircular canals (anterior/posterior/lateral), round + oval windows","CN VIII vestibulocochlear"],
    blood:"External ear: ECA branches. Inner ear: labyrinthine artery (AICA branch — end artery, hence sudden SNHL with AICA infarct).",
    nerve:"CN VIII (vestibulocochlear), CN V3 (tensor tympani), CN VII (stapedius + chorda tympani), CN X (Arnold's nerve — ear cough reflex), CN IX (Jacobson's nerve)",
    clinical:"Otitis media (children, Eustachian tube more horizontal), SNHL (noise/age/drugs), Menière's (vertigo+SNHL+tinnitus+aural fullness), vestibular schwannoma (CN VIII), otosclerosis (stapes fixation)",size:"Cochlea ~3 cm diameter; ~2.5 turns; audible range 20–20,000 Hz"},
  testes:{name:"Testes",latin:"Testes",sys:"Reproductive",col:"#c8b040",icon:"🔬",
    desc:"Paired male gonads in scrotum (~2–3°C below body temperature for spermatogenesis). Descended by week 28.",
    fn:"Spermatogenesis (FSH-stimulated, ~1000 sperm/second from puberty). Testosterone production (LH → Leydig cells). Inhibin B (negative feedback on FSH).",
    parts:["Seminiferous tubules (spermatogenesis — 250–300 lobules)","Sertoli cells (support, blood-testis barrier, AMH, inhibin)","Leydig cells (testosterone — interstitial)","Rete testis","Epididymis (maturation ~12 days, storage)","Vas deferens","Tunica albuginea (fibrous capsule)","Tunica vaginalis"],
    blood:"Testicular arteries direct from aorta at L2 (hence torsion = ischaemia = surgical emergency within 6 hours)",
    nerve:"Genitofemoral nerve L1–L2 (cremaster reflex), sympathetic testicular plexus — pain referred to L1 (loin/groin)",
    clinical:"Testicular torsion (EMERGENCY within 6h — sudden onset, high-riding testis, absent cremasteric reflex), orchitis (mumps), varicocele, hydrocele, testicular germ cell tumours (seminoma vs NSGCT, peak 20–35yo)",size:"~4.5×3×2.5 cm; ~20 g each"},
  trapezius:{name:"Trapezius",latin:"M. trapezius",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Large flat triangular back muscle covering the posterior neck and thorax. Three functional parts.",
    fn:"Upper: elevates + upwardly rotates scapula. Middle: retracts scapula. Lower: depresses + upwardly rotates scapula. Together: stabilise scapula.",
    parts:["Upper part (occipital bone + ligamentum nuchae)","Middle part (C7–T3 spinous processes)","Lower part (T4–T12 spinous processes)","Insertion: lateral 1/3 of clavicle, acromion, spine of scapula"],
    blood:"Superficial cervical artery, dorsal scapular artery",nerve:"Accessory nerve CN XI (motor) + C3–C4 (proprioception)",
    clinical:"CN XI palsy → trapezius paralysis + scapular winging (worse with arm abduction, unlike serratus anterior winging), shoulder drop, difficulty shrugging",size:"~40×30 cm; key postural muscle"},
  gluteus_maximus:{name:"Gluteus Maximus",latin:"M. gluteus maximus",sys:"Muscular",col:"#d06060",icon:"💪",
    desc:"Largest muscle in the body by volume. Forms the buttock. Most powerful hip extensor.",
    fn:"Hip extension (primary — critical for stairs, rising from sitting, running). Lateral rotation. Lower fibres: hip adduction. Upper fibres: abduction.",
    parts:["Origin: ilium (posterior), sacrum, coccyx, sacrotuberous ligament","Insertion: gluteal tuberosity of femur (deep fibres) + iliotibial tract (superficial fibres)","IT band (via tensor fascia lata)"],
    blood:"Superior + inferior gluteal arteries (internal iliac)",nerve:"Inferior gluteal nerve L5–S2",
    clinical:"Trendelenburg gait (if gluteus medius also weak), deep gluteal syndrome, piriformis syndrome, superior gluteal nerve injury (gluteus medius paralysis → Trendelenburg)",size:"Largest muscle in body by volume"},
};

// ═══════════════════════════════════════════
// SYSTEMS
// ═══════════════════════════════════════════
const SYSCOLS = {
  All:"#50a0d8",Skeletal:"#90b8d8",Muscular:"#d06060",
  Cardiovascular:"#d04040",Respiratory:"#c07030",Digestive:"#a86020",
  Nervous:"#a060c0",Urinary:"#4060c8",Endocrine:"#40b870",
  Reproductive:"#b0902a",Lymphatic:"#7040a8",Sensory:"#30a8a0"
};

// ═══════════════════════════════════════════
// SHAPE DATA — all coordinates 0–1 (fraction of canvas)
// Body centred in viewing area
// ═══════════════════════════════════════════
// ANT = anterior view shapes
const ANT=[
  {id:"__bg",sys:"",col:"#0b1628",pts:[[.37,.02],[.42,.01],[.50,.01],[.58,.01],[.63,.02],[.67,.05],[.69,.09],[.70,.14],[.70,.18],[.71,.22],[.71,.30],[.70,.36],[.70,.42],[.69,.48],[.68,.54],[.67,.60],[.66,.68],[.64,.74],[.62,.80],[.60,.87],[.58,.93],[.57,.97],[.50,.985],[.43,.97],[.42,.93],[.40,.87],[.38,.80],[.36,.74],[.34,.68],[.33,.60],[.32,.54],[.31,.48],[.30,.42],[.30,.36],[.29,.30],[.29,.22],[.30,.18],[.30,.14],[.31,.09],[.33,.05]]},
  {id:"skull",sys:"Skeletal",col:"#90b8d8",cx:.500,cy:.052,pts:[[.43,.02],[.50,.006],[.57,.02],[.605,.05],[.615,.085],[.610,.108],[.500,.125],[.390,.108],[.385,.085],[.395,.05]]},
  {id:"brain",sys:"Nervous",col:"#c080e0",cx:.500,cy:.052,pts:[[.442,.022],[.500,.008],[.558,.022],[.592,.052],[.598,.084],[.586,.108],[.500,.118],[.414,.108],[.402,.084],[.408,.052]]},
  {id:"pituitary",sys:"Endocrine",col:"#60d890",cx:.500,cy:.060,pts:[[.488,.056],[.500,.050],[.512,.056],[.510,.066],[.500,.070],[.490,.066]]},
  {id:"mandible",sys:"Skeletal",col:"#90b8d8",cx:.500,cy:.115,pts:[[.436,.110],[.500,.124],[.564,.110],[.576,.122],[.568,.138],[.500,.146],[.432,.138],[.424,.122]]},
  {id:"eye",sys:"Sensory",col:"#40c8c0",cx:.465,cy:.074,pts:[[.432,.070],[.465,.064],[.476,.074],[.468,.082],[.435,.078]]},
  {id:"ear",sys:"Sensory",col:"#40c8c0",cx:.378,cy:.088,pts:[[.372,.080],[.364,.086],[.362,.096],[.366,.104],[.374,.106],[.382,.100],[.382,.088]]},
  {id:"trachea",sys:"Respiratory",col:"#c07030",cx:.500,cy:.158,pts:[[.487,.145],[.513,.145],[.515,.168],[.513,.178],[.500,.180],[.487,.178],[.485,.168]]},
  {id:"larynx",sys:"Respiratory",col:"#c07030",cx:.500,cy:.136,pts:[[.478,.126],[.492,.120],[.508,.120],[.522,.126],[.524,.140],[.518,.152],[.500,.156],[.482,.152],[.476,.140]]},
  {id:"thyroid",sys:"Endocrine",col:"#60d890",cx:.500,cy:.157,pts:[[.466,.148],[.488,.142],[.512,.142],[.534,.148],[.532,.162],[.520,.170],[.500,.172],[.480,.170],[.468,.162]]},
  {id:"thymus",sys:"Lymphatic",col:"#7040a8",cx:.500,cy:.163,pts:[[.480,.154],[.490,.149],[.510,.149],[.520,.154],[.518,.170],[.510,.176],[.500,.178],[.490,.176],[.482,.170]]},
  {id:"clavicle",sys:"Skeletal",col:"#90b8d8",cx:.400,cy:.149,pts:[[.345,.148],[.400,.134],[.462,.140],[.488,.148],[.462,.156],[.400,.159],[.348,.155]]},
  {id:"sternum",sys:"Skeletal",col:"#90b8d8",cx:.500,cy:.210,pts:[[.483,.148],[.517,.148],[.519,.252],[.500,.256],[.481,.252]]},
  {id:"ribs",sys:"Skeletal",col:"#90b8d8",cx:.375,cy:.206,pts:[[.335,.162],[.370,.158],[.481,.162],[.481,.172],[.370,.168],[.338,.176]]},
  {id:"vertebral_column",sys:"Skeletal",col:"#a0c0d8",cx:.500,cy:.320,pts:[[.492,.144],[.508,.144],[.510,.542],[.500,.547],[.490,.542]]},
  {id:"spinal_cord",sys:"Nervous",col:"#c080e0",cx:.500,cy:.295,pts:[[.495,.147],[.505,.147],[.506,.500],[.500,.504],[.494,.500]]},
  {id:"lungs",sys:"Respiratory",col:"#c07030",cx:.395,cy:.225,pts:[[.358,.162],[.344,.174],[.336,.202],[.335,.238],[.340,.268],[.352,.284],[.370,.292],[.392,.290],[.406,.276],[.481,.272],[.481,.162]]},
  {id:"heart",sys:"Cardiovascular",col:"#d04040",cx:.476,cy:.203,pts:[[.458,.176],[.447,.173],[.438,.178],[.430,.189],[.430,.204],[.440,.216],[.460,.226],[.482,.232],[.504,.224],[.518,.212],[.516,.197],[.506,.184],[.494,.178],[.484,.174]]},
  {id:"aorta",sys:"Cardiovascular",col:"#c03030",cx:.510,cy:.240,pts:[[.490,.176],[.500,.170],[.512,.174],[.520,.184],[.522,.202],[.516,.225],[.508,.262],[.502,.278],[.498,.278],[.492,.262],[.486,.240],[.483,.212],[.482,.182]]},
  {id:"carotid",sys:"Cardiovascular",col:"#c03040",cx:.462,cy:.158,pts:[[.457,.147],[.462,.147],[.467,.178],[.462,.181],[.456,.178]]},
  {id:"pulmonary_vessels",sys:"Cardiovascular",col:"#5050c8",cx:.448,cy:.194,pts:[[.458,.184],[.440,.188],[.428,.193],[.428,.200],[.438,.202],[.460,.197]]},
  {id:"diaphragm",sys:"Muscular",col:"#d06060",cx:.500,cy:.300,pts:[[.338,.290],[.382,.307],[.422,.314],[.500,.316],[.578,.314],[.618,.307],[.662,.290],[.655,.305],[.625,.317],[.580,.327],[.500,.329],[.420,.327],[.375,.317],[.345,.305]]},
  {id:"deltoid",sys:"Muscular",col:"#d06060",cx:.322,cy:.188,pts:[[.300,.153],[.292,.172],[.290,.196],[.296,.218],[.308,.220],[.322,.210],[.332,.194],[.330,.164],[.318,.152]]},
  {id:"pectoralis_major",sys:"Muscular",col:"#d06060",cx:.394,cy:.214,pts:[[.346,.162],[.398,.157],[.481,.162],[.481,.258],[.454,.263],[.430,.255],[.398,.242],[.368,.226],[.346,.210]]},
  {id:"biceps_brachii",sys:"Muscular",col:"#d06060",cx:.282,cy:.268,pts:[[.290,.222],[.282,.240],[.277,.272],[.280,.304],[.286,.320],[.298,.322],[.308,.318],[.310,.300],[.307,.268],[.302,.238],[.296,.222]]},
  {id:"humerus",sys:"Skeletal",col:"#90b8d8",cx:.292,cy:.282,pts:[[.295,.217],[.288,.240],[.284,.280],[.288,.330],[.296,.344],[.304,.342],[.310,.328],[.309,.278],[.306,.238],[.300,.217]]},
  {id:"triceps",sys:"Muscular",col:"#d06060",cx:.272,cy:.274,pts:[[.278,.228],[.268,.255],[.265,.292],[.268,.320],[.276,.332],[.286,.326],[.282,.290],[.280,.255],[.279,.228]]},
  {id:"radius",sys:"Skeletal",col:"#90b8d8",cx:.284,cy:.390,pts:[[.284,.344],[.279,.392],[.280,.441],[.286,.445],[.290,.441],[.291,.392],[.288,.344]]},
  {id:"ulna",sys:"Skeletal",col:"#90b8d8",cx:.296,cy:.387,pts:[[.296,.342],[.292,.388],[.294,.441],[.300,.445],[.303,.441],[.302,.390],[.300,.342]]},
  {id:"liver",sys:"Digestive",col:"#a06018",cx:.426,cy:.342,pts:[[.356,.294],[.390,.288],[.462,.292],[.512,.298],[.522,.309],[.519,.337],[.511,.356],[.488,.368],[.460,.372],[.430,.367],[.398,.356],[.368,.343],[.350,.326],[.347,.308]]},
  {id:"stomach",sys:"Digestive",col:"#a06018",cx:.540,cy:.338,pts:[[.512,.297],[.542,.291],[.572,.298],[.590,.313],[.592,.340],[.584,.360],[.566,.370],[.546,.373],[.520,.365],[.510,.350],[.510,.328]]},
  {id:"spleen",sys:"Lymphatic",col:"#7040a8",cx:.622,cy:.327,pts:[[.600,.306],[.622,.302],[.640,.308],[.646,.322],[.642,.338],[.634,.347],[.620,.350],[.607,.342],[.601,.326],[.602,.314]]},
  {id:"adrenal_glands",sys:"Endocrine",col:"#60d890",cx:.374,cy:.356,pts:[[.356,.350],[.373,.344],[.384,.350],[.387,.363],[.380,.372],[.367,.374],[.356,.368],[.352,.357]]},
  {id:"pancreas",sys:"Digestive",col:"#a06018",cx:.500,cy:.373,pts:[[.440,.364],[.468,.359],[.512,.361],[.548,.364],[.566,.373],[.562,.383],[.540,.387],[.506,.385],[.472,.380],[.444,.374]]},
  {id:"kidneys",sys:"Urinary",col:"#4060c8",cx:.372,cy:.387,pts:[[.350,.366],[.338,.374],[.335,.392],[.338,.410],[.350,.420],[.367,.422],[.380,.414],[.384,.400],[.380,.381],[.367,.368]]},
  {id:"small_intestine",sys:"Digestive",col:"#a06018",cx:.478,cy:.428,pts:[[.406,.382],[.436,.378],[.582,.380],[.602,.390],[.602,.428],[.596,.466],[.578,.482],[.548,.490],[.488,.492],[.428,.488],[.398,.472],[.394,.445],[.400,.412]]},
  {id:"large_intestine",sys:"Digestive",col:"#804010",cx:.398,cy:.468,pts:[[.368,.458],[.356,.468],[.352,.490],[.356,.514],[.368,.528],[.386,.532],[.402,.530],[.420,.520],[.602,.518],[.620,.512],[.626,.492],[.620,.470],[.606,.458],[.594,.454],[.578,.458],[.418,.458]]},
  {id:"pelvis",sys:"Skeletal",col:"#90b8d8",cx:.500,cy:.543,pts:[[.344,.504],[.374,.494],[.420,.490],[.500,.488],[.580,.490],[.626,.494],[.656,.504],[.662,.526],[.656,.550],[.638,.566],[.608,.576],[.568,.582],[.500,.584],[.432,.582],[.392,.576],[.362,.566],[.344,.550],[.338,.526]]},
  {id:"bladder",sys:"Urinary",col:"#4060c8",cx:.500,cy:.552,pts:[[.468,.538],[.500,.532],[.532,.538],[.540,.555],[.534,.570],[.520,.578],[.500,.580],[.480,.578],[.466,.570],[.460,.555]]},
  {id:"testes",sys:"Reproductive",col:"#c8b040",cx:.500,cy:.590,pts:[[.462,.578],[.480,.570],[.498,.576],[.498,.594],[.488,.602],[.474,.600],[.464,.590]]},
  {id:"femur",sys:"Skeletal",col:"#90b8d8",cx:.416,cy:.648,pts:[[.402,.581],[.395,.622],[.393,.670],[.396,.712],[.402,.730],[.410,.733],[.418,.731],[.421,.712],[.420,.670],[.417,.622],[.412,.581]]},
  {id:"quadriceps",sys:"Muscular",col:"#d06060",cx:.396,cy:.645,pts:[[.384,.582],[.377,.622],[.375,.670],[.379,.712],[.387,.730],[.402,.581]]},
  {id:"hamstrings",sys:"Muscular",col:"#d06060",cx:.374,cy:.645,pts:[[.370,.582],[.362,.622],[.360,.670],[.364,.712],[.372,.730],[.384,.582]]},
  {id:"patella",sys:"Skeletal",col:"#90b8d8",cx:.408,cy:.731,pts:[[.396,.727],[.408,.722],[.422,.727],[.426,.737],[.420,.746],[.408,.748],[.397,.744],[.393,.735]]},
  {id:"tibia",sys:"Skeletal",col:"#90b8d8",cx:.406,cy:.778,pts:[[.396,.747],[.399,.775],[.401,.985],[.409,.990],[.414,.985],[.413,.775],[.410,.747]]},
  {id:"fibula",sys:"Skeletal",col:"#90b8d8",cx:.424,cy:.774,pts:[[.420,.747],[.422,.775],[.424,.981],[.429,.984],[.432,.981],[.430,.775],[.427,.747]]},
  {id:"gastrocnemius",sys:"Muscular",col:"#d06060",cx:.390,cy:.768,pts:[[.383,.747],[.378,.770],[.378,.822],[.384,.864],[.392,.878],[.400,.878],[.407,.874],[.410,.860],[.406,.820],[.401,.770],[.397,.747]]},
  {id:"lymph_nodes",sys:"Lymphatic",col:"#7040a8",cx:.440,cy:.139,pts:[[.432,.133],[.441,.129],[.449,.133],[.449,.141],[.441,.145],[.432,.141]]},
];

const POST=[
  {id:"__bg",sys:"",col:"#0b1628",pts:[[.37,.02],[.42,.01],[.50,.01],[.58,.01],[.63,.02],[.67,.05],[.69,.09],[.70,.14],[.70,.18],[.71,.22],[.71,.30],[.70,.36],[.70,.42],[.69,.48],[.68,.54],[.67,.60],[.66,.68],[.64,.74],[.62,.80],[.60,.87],[.58,.93],[.57,.97],[.50,.985],[.43,.97],[.42,.93],[.40,.87],[.38,.80],[.36,.74],[.34,.68],[.33,.60],[.32,.54],[.31,.48],[.30,.42],[.30,.36],[.29,.30],[.29,.22],[.30,.18],[.30,.14],[.31,.09],[.33,.05]]},
  {id:"skull",sys:"Skeletal",col:"#90b8d8",cx:.500,cy:.052,pts:[[.43,.02],[.50,.006],[.57,.02],[.605,.05],[.612,.088],[.600,.112],[.500,.126],[.400,.112],[.388,.088],[.395,.05]]},
  {id:"brain",sys:"Nervous",col:"#c080e0",cx:.500,cy:.052,pts:[[.442,.022],[.500,.008],[.558,.022],[.595,.052],[.600,.086],[.588,.110],[.500,.120],[.412,.110],[.400,.086],[.405,.052]]},
  {id:"vertebral_column",sys:"Skeletal",col:"#a0c0d8",cx:.500,cy:.320,pts:[[.486,.134],[.514,.134],[.516,.546],[.500,.552],[.484,.546]]},
  {id:"spinal_cord",sys:"Nervous",col:"#c080e0",cx:.500,cy:.295,pts:[[.493,.137],[.507,.137],[.508,.501],[.500,.505],[.492,.501]]},
  {id:"trapezius",sys:"Muscular",col:"#d06060",cx:.500,cy:.170,pts:[[.448,.145],[.500,.128],[.552,.145],[.572,.168],[.556,.190],[.513,.196],[.487,.196],[.444,.190],[.428,.168]]},
  {id:"latissimus_dorsi",sys:"Muscular",col:"#d06060",cx:.406,cy:.255,pts:[[.350,.198],[.382,.187],[.487,.197],[.487,.308],[.466,.320],[.438,.325],[.408,.320],[.380,.308],[.354,.290],[.340,.268],[.340,.233]]},
  {id:"gluteus_maximus",sys:"Muscular",col:"#d06060",cx:.428,cy:.553,pts:[[.358,.503],[.402,.493],[.458,.490],[.490,.493],[.490,.542],[.478,.567],[.458,.580],[.428,.584],[.398,.580],[.368,.567],[.350,.543],[.348,.518]]},
  {id:"kidneys",sys:"Urinary",col:"#4060c8",cx:.378,cy:.364,pts:[[.348,.339],[.336,.347],[.333,.368],[.337,.388],[.350,.398],[.366,.400],[.378,.392],[.382,.374],[.378,.354],[.365,.341]]},
  {id:"adrenal_glands",sys:"Endocrine",col:"#60d890",cx:.350,cy:.330,pts:[[.333,.325],[.350,.318],[.362,.325],[.365,.337],[.358,.346],[.344,.348],[.333,.340]]},
  {id:"hamstrings",sys:"Muscular",col:"#d06060",cx:.406,cy:.648,pts:[[.388,.580],[.380,.622],[.378,.670],[.382,.712],[.392,.732],[.406,.734],[.418,.732],[.422,.712],[.420,.670],[.416,.622],[.408,.580]]},
  {id:"gastrocnemius",sys:"Muscular",col:"#d06060",cx:.398,cy:.768,pts:[[.384,.747],[.374,.772],[.372,.834],[.378,.876],[.392,.886],[.408,.884],[.420,.872],[.424,.832],[.418,.772],[.410,.747]]},
  {id:"triceps",sys:"Muscular",col:"#d06060",cx:.278,cy:.273,pts:[[.278,.224],[.268,.250],[.265,.288],[.268,.320],[.277,.334],[.290,.330],[.297,.316],[.294,.280],[.290,.248],[.284,.224]]},
  {id:"femur",sys:"Skeletal",col:"#90b8d8",cx:.416,cy:.648,pts:[[.402,.582],[.395,.622],[.393,.670],[.396,.712],[.402,.730],[.410,.733],[.418,.731],[.421,.712],[.420,.670],[.417,.622],[.412,.582]]},
  {id:"tibia",sys:"Skeletal",col:"#90b8d8",cx:.406,cy:.778,pts:[[.398,.747],[.400,.775],[.402,.985],[.410,.990],[.414,.985],[.413,.775],[.408,.747]]},
  {id:"fibula",sys:"Skeletal",col:"#90b8d8",cx:.424,cy:.774,pts:[[.420,.747],[.422,.775],[.424,.981],[.429,.984],[.432,.981],[.430,.775],[.427,.747]]},
];

const LATR=[
  {id:"__bg",sys:"",col:"#0b1628",pts:[[.38,.02],[.44,.008],[.54,.012],[.60,.03],[.64,.07],[.65,.13],[.64,.18],[.62,.24],[.61,.32],[.60,.42],[.60,.52],[.59,.62],[.58,.70],[.57,.78],[.56,.86],[.55,.93],[.52,.98],[.48,.98],[.45,.93],[.44,.86],[.43,.78],[.42,.70],[.41,.62],[.40,.52],[.39,.42],[.38,.32],[.37,.24],[.36,.18],[.35,.13],[.36,.07]]},
  {id:"skull",sys:"Skeletal",col:"#90b8d8",cx:.508,cy:.055,pts:[[.418,.027],[.448,.009],[.508,.005],[.568,.011],[.610,.037],[.626,.067],[.618,.097],[.592,.115],[.558,.125],[.518,.128],[.478,.121],[.438,.107],[.412,.083],[.408,.058]]},
  {id:"brain",sys:"Nervous",col:"#c080e0",cx:.508,cy:.055,pts:[[.424,.029],[.454,.011],[.508,.007],[.562,.013],[.602,.039],[.618,.067],[.610,.095],[.586,.111],[.556,.121],[.518,.124],[.480,.117],[.442,.105],[.418,.081],[.414,.061]]},
  {id:"ear",sys:"Sensory",col:"#40c8c0",cx:.620,cy:.090,pts:[[.612,.079],[.626,.074],[.635,.080],[.638,.092],[.634,.104],[.623,.108],[.612,.100],[.609,.088]]},
  {id:"larynx",sys:"Respiratory",col:"#c07030",cx:.480,cy:.142,pts:[[.458,.128],[.474,.122],[.492,.126],[.498,.142],[.494,.157],[.479,.163],[.463,.157],[.456,.143]]},
  {id:"trachea",sys:"Respiratory",col:"#c07030",cx:.474,cy:.168,pts:[[.466,.162],[.482,.158],[.490,.163],[.490,.180],[.480,.183],[.468,.180],[.465,.163]]},
  {id:"thyroid",sys:"Endocrine",col:"#60d890",cx:.488,cy:.155,pts:[[.466,.147],[.486,.141],[.508,.145],[.518,.156],[.514,.168],[.499,.174],[.482,.169],[.470,.160]]},
  {id:"vertebral_column",sys:"Skeletal",col:"#a0c0d8",cx:.416,cy:.320,pts:[[.408,.127],[.426,.127],[.428,.548],[.416,.552],[.406,.548]]},
  {id:"spinal_cord",sys:"Nervous",col:"#c080e0",cx:.414,cy:.295,pts:[[.410,.130],[.422,.130],[.423,.502],[.416,.506],[.410,.502]]},
  {id:"heart",sys:"Cardiovascular",col:"#d04040",cx:.500,cy:.204,pts:[[.478,.182],[.465,.179],[.452,.184],[.444,.196],[.445,.211],[.458,.224],[.477,.232],[.499,.236],[.522,.226],[.532,.212],[.530,.197],[.518,.185],[.502,.180]]},
  {id:"lungs",sys:"Respiratory",col:"#c07030",cx:.530,cy:.224,pts:[[.498,.167],[.518,.161],[.546,.167],[.567,.184],[.574,.215],[.570,.253],[.556,.273],[.535,.282],[.510,.273],[.495,.255],[.491,.224],[.494,.194]]},
  {id:"liver",sys:"Digestive",col:"#a06018",cx:.488,cy:.330,pts:[[.453,.293],[.490,.284],[.536,.292],[.559,.307],[.562,.332],[.554,.356],[.534,.369],[.507,.373],[.479,.362],[.456,.344],[.443,.317]]},
  {id:"stomach",sys:"Digestive",col:"#a06018",cx:.448,cy:.328,pts:[[.432,.293],[.456,.286],[.476,.296],[.481,.320],[.477,.348],[.460,.363],[.437,.367],[.416,.354],[.408,.330],[.413,.307]]},
  {id:"kidneys",sys:"Urinary",col:"#4060c8",cx:.413,cy:.368,pts:[[.396,.346],[.410,.338],[.432,.342],[.444,.357],[.441,.376],[.429,.388],[.411,.390],[.396,.380],[.390,.363]]},
  {id:"adrenal_glands",sys:"Endocrine",col:"#60d890",cx:.404,cy:.336,pts:[[.392,.330],[.406,.323],[.418,.330],[.420,.342],[.413,.350],[.398,.352],[.388,.343]]},
  {id:"femur",sys:"Skeletal",col:"#90b8d8",cx:.480,cy:.648,pts:[[.472,.581],[.464,.622],[.461,.670],[.464,.712],[.470,.730],[.480,.733],[.490,.730],[.492,.712],[.491,.670],[.488,.622],[.484,.581]]},
  {id:"patella",sys:"Skeletal",col:"#90b8d8",cx:.478,cy:.730,pts:[[.466,.726],[.478,.721],[.490,.726],[.494,.736],[.488,.745],[.478,.747],[.467,.743],[.463,.734]]},
  {id:"tibia",sys:"Skeletal",col:"#90b8d8",cx:.476,cy:.778,pts:[[.469,.747],[.470,.775],[.472,.985],[.480,.990],[.484,.985],[.483,.775],[.479,.747]]},
  {id:"gastrocnemius",sys:"Muscular",col:"#d06060",cx:.492,cy:.768,pts:[[.484,.747],[.475,.774],[.473,.836],[.479,.880],[.492,.888],[.506,.882],[.512,.862],[.508,.822],[.499,.774],[.492,.747]]},
  {id:"quadriceps",sys:"Muscular",col:"#d06060",cx:.462,cy:.645,pts:[[.454,.582],[.446,.622],[.444,.670],[.448,.712],[.456,.730],[.472,.581]]},
  {id:"hamstrings",sys:"Muscular",col:"#d06060",cx:.496,cy:.645,pts:[[.490,.582],[.498,.622],[.500,.670],[.496,.712],[.490,.730],[.480,.733],[.490,.580]]},
];

// Mirror LATR for left lateral
const LATL=LATR.map(r=>({...r,pts:r.pts.map(([x,y])=>[1-x,y]),cx:r.cx!==undefined?1-r.cx:undefined}));

const SUP=[
  {id:"__bg",sys:"",col:"#0b1628",pts:[[.20,.20],[.50,.10],[.80,.20],[.88,.50],[.80,.80],[.50,.90],[.20,.80],[.12,.50]]},
  {id:"skull",sys:"Skeletal",col:"#90b8d8",cx:.500,cy:.500,pts:[[.25,.25],[.50,.13],[.75,.25],[.82,.50],[.75,.75],[.50,.87],[.25,.75],[.18,.50]]},
  {id:"brain",sys:"Nervous",col:"#c080e0",cx:.500,cy:.500,pts:[[.28,.28],[.50,.17],[.72,.28],[.78,.50],[.72,.72],[.50,.83],[.28,.72],[.22,.50]]},
  {id:"eye",sys:"Sensory",col:"#40c8c0",cx:.396,cy:.378,pts:[[.368,.363],[.398,.350],[.428,.363],[.426,.380],[.398,.388],[.370,.380]]},
  {id:"ear",sys:"Sensory",col:"#40c8c0",cx:.204,cy:.500,pts:[[.183,.468],[.175,.500],[.183,.532],[.204,.540],[.215,.532],[.215,.468]]},
  {id:"pituitary",sys:"Endocrine",col:"#60d890",cx:.500,cy:.500,pts:[[.488,.488],[.500,.480],[.512,.488],[.512,.512],[.500,.520],[.488,.512]]},
];

const VIEWS={ant:ANT,pos:POST,latr:LATR,latl:LATL,sup:SUP};

// ═══════════════════════════════════════════
// STATE
// ═══════════════════════════════════════════
let curView='ant',curSys='All',selId=null;
let zoom=1,panX=0,panY=0;
let drag=false,dragX=0,dragY=0;
let showLabels=true,layerIdx=0;
const LAYER_KEYS=['all','skeletal','muscular','organs'];
const LAYER_LABELS=['All Layers','Skeletal','Muscular','Organs'];
const LAYER_SYS={skeletal:['Skeletal'],muscular:['Muscular'],organs:['Cardiovascular','Respiratory','Digestive','Nervous','Urinary','Endocrine','Reproductive','Lymphatic','Sensory'],all:null};

// ═══════════════════════════════════════════
// CANVAS
// ═══════════════════════════════════════════
const canvas=document.getElementById('c');
const ctx=canvas.getContext('2d');

function resize(){canvas.width=canvas.offsetWidth;canvas.height=canvas.offsetHeight;draw();}
window.addEventListener('resize',resize);

// ═══════════════════════════════════════════
// DRAW
// ═══════════════════════════════════════════
function draw(){
  const W=canvas.width,H=canvas.height;
  ctx.clearRect(0,0,W,H);
  ctx.fillStyle='#060a14';ctx.fillRect(0,0,W,H);
  ctx.save();
  ctx.translate(W/2+panX,H/2+panY);ctx.scale(zoom,zoom);ctx.translate(-W/2,-H/2);
  const parts=VIEWS[curView]||ANT;
  const lk=LAYER_KEYS[layerIdx];
  const allowedSys=LAYER_SYS[lk];
  parts.forEach(part=>{
    if(!part.pts||part.pts.length<3)return;
    if(part.id!=='__bg'){
      if(curSys!=='All'&&part.sys!==curSys)return;
      if(allowedSys&&!allowedSys.includes(part.sys))return;
    }
    const pts=part.pts.map(([x,y])=>[x*W,y*H]);
    ctx.beginPath();ctx.moveTo(pts[0][0],pts[0][1]);
    for(let i=1;i<pts.length;i++)ctx.lineTo(pts[i][0],pts[i][1]);
    ctx.closePath();
    if(part.id==='__bg'){ctx.fillStyle='#0c1830';ctx.strokeStyle='#1e3050';ctx.lineWidth=1.5;ctx.fill();ctx.stroke();return;}
    const isSel=selId===part.id;
    ctx.globalAlpha=isSel?1.0:0.75;
    ctx.fillStyle=part.col||'#4a7a9a';
    ctx.strokeStyle=isSel?'#70d0ff':lighten(part.col||'#4a7a9a',0.5);
    ctx.lineWidth=(isSel?2:0.8)/zoom;
    ctx.fill();ctx.stroke();
    if(isSel){
      ctx.save();ctx.beginPath();
      pts.forEach(([x,y],i)=>i===0?ctx.moveTo(x,y):ctx.lineTo(x,y));
      ctx.closePath();ctx.strokeStyle='#80e0ff';ctx.lineWidth=3/zoom;ctx.globalAlpha=0.45;ctx.stroke();ctx.restore();
    }
    ctx.globalAlpha=1;
    if(showLabels&&DB[part.id]&&part.cx!==undefined&&part.id!=='__bg'){
      const lx=part.cx*W,ly=part.cy*H;
      const fs=Math.max(7,Math.min(11,10/zoom));
      const nm=DB[part.id].name;
      const txt=nm.length>16?nm.split(' ')[0]:nm;
      ctx.font=`700 ${fs}px Segoe UI,sans-serif`;ctx.textAlign='center';ctx.textBaseline='middle';
      const tw=ctx.measureText(txt).width;
      ctx.fillStyle='rgba(5,9,18,0.78)';ctx.fillRect(lx-tw/2-2,ly-fs/2-2,tw+4,fs+4);
      ctx.fillStyle=isSel?'#80e0ff':(part.col||'#80b0d0');ctx.fillText(txt,lx,ly);
    }
  });
  ctx.restore();
}

function lighten(hex,amt){
  try{const r=parseInt(hex.slice(1,3),16),g=parseInt(hex.slice(3,5),16),b=parseInt(hex.slice(5,7),16);return `#${Math.min(255,Math.round(r+(255-r)*amt)).toString(16).padStart(2,'0')}${Math.min(255,Math.round(g+(255-g)*amt)).toString(16).padStart(2,'0')}${Math.min(255,Math.round(b+(255-b)*amt)).toString(16).padStart(2,'0')}`;}catch{return hex;}
}

// ═══════════════════════════════════════════
// HIT TEST
// ═══════════════════════════════════════════
function worldXY(cx,cy){const W=canvas.width,H=canvas.height;return[(cx-W/2-panX)/zoom+W/2,(cy-H/2-panY)/zoom+H/2];}

function pip(px,py,pts,W,H){
  let inside=false;
  for(let i=0,j=pts.length-1;i<pts.length;j=i++){
    const xi=pts[i][0]*W,yi=pts[i][1]*H,xj=pts[j][0]*W,yj=pts[j][1]*H;
    if(((yi>py)!==(yj>py))&&(px<(xj-xi)*(py-yi)/(yj-yi)+xi))inside=!inside;
  }
  return inside;
}

function hitTest(cx,cy){
  const [wx,wy]=worldXY(cx,cy);
  const W=canvas.width,H=canvas.height;
  const parts=VIEWS[curView]||ANT;
  const lk=LAYER_KEYS[layerIdx];
  const allowedSys=LAYER_SYS[lk];
  for(let i=parts.length-1;i>=0;i--){
    const p=parts[i];
    if(!p.pts||p.id==='__bg'||!DB[p.id])continue;
    if(curSys!=='All'&&p.sys!==curSys)continue;
    if(allowedSys&&!allowedSys.includes(p.sys))continue;
    if(pip(wx,wy,p.pts,W,H))return p.id;
  }
  return null;
}

// ═══════════════════════════════════════════
// POINTER EVENTS
// ═══════════════════════════════════════════
const tip=document.getElementById('tip');
canvas.addEventListener('mousemove',e=>{
  const r=canvas.getBoundingClientRect();
  const cx=e.clientX-r.left,cy=e.clientY-r.top;
  if(drag){panX+=e.movementX;panY+=e.movementY;draw();return;}
  const id=hitTest(cx,cy);
  if(id&&DB[id]){
    canvas.style.cursor='pointer';
    tip.style.display='block';tip.textContent=DB[id].name;
    let tx=cx+14,ty=cy-28;
    if(tx+180>canvas.offsetWidth)tx=cx-180;
    tip.style.left=tx+'px';tip.style.top=ty+'px';
  }else{canvas.style.cursor='default';tip.style.display='none';}
});
canvas.addEventListener('mouseleave',()=>{tip.style.display='none';drag=false;});
canvas.addEventListener('mousedown',e=>{drag=true;dragX=e.clientX;dragY=e.clientY;});
canvas.addEventListener('mouseup',e=>{
  if(Math.abs(e.clientX-dragX)<4&&Math.abs(e.clientY-dragY)<4){
    const r=canvas.getBoundingClientRect();
    const id=hitTest(e.clientX-r.left,e.clientY-r.top);
    if(id&&DB[id]){selId=id;showDetail(id);highlightList(id);draw();}
    else{selId=null;clearDetail();draw();}
  }
  drag=false;
});
canvas.addEventListener('wheel',e=>{e.preventDefault();zoom=Math.max(.35,Math.min(4,zoom*(e.deltaY<0?1.1:0.9)));document.getElementById('zval').textContent=Math.round(zoom*100)+'%';draw();},{passive:false});

// Touch
let lastDist=null,touchStartX=0,touchStartY=0;
canvas.addEventListener('touchstart',e=>{if(e.touches.length===1){drag=true;touchStartX=dragX=e.touches[0].clientX;touchStartY=dragY=e.touches[0].clientY;}if(e.touches.length===2)lastDist=Math.hypot(e.touches[0].clientX-e.touches[1].clientX,e.touches[0].clientY-e.touches[1].clientY);},{passive:true});
canvas.addEventListener('touchmove',e=>{if(e.touches.length===1&&drag){panX+=e.touches[0].clientX-dragX;panY+=e.touches[0].clientY-dragY;dragX=e.touches[0].clientX;dragY=e.touches[0].clientY;draw();}if(e.touches.length===2&&lastDist){const d=Math.hypot(e.touches[0].clientX-e.touches[1].clientX,e.touches[0].clientY-e.touches[1].clientY);zoom=Math.max(.35,Math.min(4,zoom*(d/lastDist)));lastDist=d;document.getElementById('zval').textContent=Math.round(zoom*100)+'%';draw();}},{passive:true});
canvas.addEventListener('touchend',e=>{if(e.changedTouches.length===1){const t=e.changedTouches[0];if(Math.abs(t.clientX-touchStartX)<8&&Math.abs(t.clientY-touchStartY)<8){const r=canvas.getBoundingClientRect();const id=hitTest(t.clientX-r.left,t.clientY-r.top);if(id&&DB[id]){selId=id;showDetail(id);highlightList(id);draw();}}}drag=false;lastDist=null;});

// ═══════════════════════════════════════════
// CONTROLS
// ═══════════════════════════════════════════
document.querySelectorAll('.vbtn').forEach(b=>b.addEventListener('click',()=>{
  curView=b.dataset.v;document.querySelectorAll('.vbtn').forEach(x=>x.classList.remove('on'));b.classList.add('on');selId=null;clearDetail();draw();
}));
document.getElementById('zplus').addEventListener('click',()=>{zoom=Math.min(4,zoom*1.2);document.getElementById('zval').textContent=Math.round(zoom*100)+'%';draw();});
document.getElementById('zminus').addEventListener('click',()=>{zoom=Math.max(.35,zoom/1.2);document.getElementById('zval').textContent=Math.round(zoom*100)+'%';draw();});
document.getElementById('zreset').addEventListener('click',()=>{zoom=1;panX=0;panY=0;document.getElementById('zval').textContent='100%';draw();});
document.getElementById('lblbtn').addEventListener('click',function(){showLabels=!showLabels;this.textContent=showLabels?'Labels ON':'Labels OFF';this.classList.toggle('on',showLabels);draw();});
document.getElementById('laybtn').addEventListener('click',function(){layerIdx=(layerIdx+1)%LAYER_KEYS.length;this.textContent=LAYER_LABELS[layerIdx];this.classList.toggle('on',layerIdx===0);draw();});
document.addEventListener('keydown',e=>{
  if(e.key==='1')document.querySelector('[data-v="ant"]').click();
  if(e.key==='2')document.querySelector('[data-v="pos"]').click();
  if(e.key==='3')document.querySelector('[data-v="latr"]').click();
  if(e.key==='4')document.querySelector('[data-v="latl"]').click();
  if(e.key==='+'||e.key==='=')document.getElementById('zplus').click();
  if(e.key==='-')document.getElementById('zminus').click();
  if(e.key==='r'||e.key==='R')document.getElementById('zreset').click();
  if(e.key==='l'||e.key==='L')document.getElementById('lblbtn').click();
});

// ═══════════════════════════════════════════
// LEFT PANEL
// ═══════════════════════════════════════════
function buildSysTabs(){
  const c=document.getElementById('sys-tabs');c.innerHTML='';
  Object.keys(SYSCOLS).forEach(s=>{
    const b=document.createElement('button');b.className='stab'+(s===curSys?' on':'');b.title=s;b.textContent=s==='All'?'All':s.substring(0,4);
    b.addEventListener('click',()=>{curSys=s;document.querySelectorAll('.stab').forEach(x=>x.classList.toggle('on',x.title===s));buildPartList();draw();});
    c.appendChild(b);
  });
}
function buildPartList(){
  const c=document.getElementById('part-list');c.innerHTML='';
  const entries=Object.entries(DB).filter(([,d])=>curSys==='All'||d.sys===curSys);
  entries.sort((a,b)=>a[1].sys.localeCompare(b[1].sys)||a[1].name.localeCompare(b[1].name));
  let lastSys='';
  entries.forEach(([id,d])=>{
    if(d.sys!==lastSys){const g=document.createElement('div');g.className='pgrp';g.textContent=d.sys;c.appendChild(g);lastSys=d.sys;}
    const item=document.createElement('div');item.className='pitem'+(selId===id?' sel':'');item.dataset.id=id;
    const dot=document.createElement('div');dot.className='pdot';dot.style.background=d.col||SYSCOLS[d.sys]||'#508080';item.appendChild(dot);
    const lbl=document.createElement('span');lbl.textContent=d.name;item.appendChild(lbl);
    item.addEventListener('click',()=>{selId=id;showDetail(id);highlightList(id);draw();});
    c.appendChild(item);
  });
}
function highlightList(id){document.querySelectorAll('.pitem').forEach(el=>{el.classList.toggle('sel',el.dataset.id===id);if(el.dataset.id===id)el.scrollIntoView({behavior:'smooth',block:'nearest'});});}

// ═══════════════════════════════════════════
// DETAIL PANEL
// ═══════════════════════════════════════════
function showDetail(id){
  const d=DB[id];if(!d)return;
  document.getElementById('dicon').textContent=d.icon||'🔬';
  document.getElementById('dname').textContent=d.name;
  document.getElementById('dlatin').textContent=d.latin;
  document.getElementById('dempty').style.display='none';
  const cont=document.getElementById('dcontent');cont.style.display='block';
  const comps=(d.parts||[]).map(p=>`<span class="dtag">${p}</span>`).join('');
  const clin=(d.clinical||'').split(',').map(c=>`<span class="ctag">${c.trim()}</span>`).join('');
  cont.innerHTML=`
    <div class="dsec"><h4>Overview</h4><p>${d.desc}</p></div>
    <div class="dsec"><h4>Function</h4><p>${d.fn}</p></div>
    <div class="dsec"><h4>Key Components</h4><div>${comps}</div></div>
    <div class="dsec">
      <div class="drow"><span>System</span><span>${d.sys}</span></div>
      <div class="drow"><span>Size / Weight</span><span>${d.size||'Variable'}</span></div>
      <div class="drow"><span>Blood Supply</span><span>${d.blood||'—'}</span></div>
      <div class="drow"><span>Innervation</span><span>${d.nerve||'—'}</span></div>
    </div>
    <div class="dsec"><h4>Clinical Relevance</h4><div>${clin}</div></div>`;
}
function clearDetail(){
  document.getElementById('dname').textContent='Select a structure';
  document.getElementById('dlatin').textContent='Click any part to explore';
  document.getElementById('dempty').style.display='flex';
  document.getElementById('dcontent').style.display='none';
}

// ═══════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════
buildSysTabs();buildPartList();
setTimeout(resize,60);
</script>
</body>
</html>"""


def anatomy_3d_page(theme):
    st.markdown(
        f"<h2 style='color:{theme['text']};font-family:\"Bricolage Grotesque\",sans-serif;"
        f"font-size:1.6rem;font-weight:900;margin-bottom:0.3rem;'>🫁 3D Anatomy Atlas</h2>",
        unsafe_allow_html=True,
    )
    st.markdown(
        f"<p style='color:{theme['subtext']};font-size:0.85rem;margin-bottom:1rem;'>"
        "Interactive atlas · 45+ structures · 11 body systems · Click any part for full details</p>",
        unsafe_allow_html=True,
    )
    components.html(ANATOMY_HTML, height=720, scrolling=False)
    with st.expander("⌨️ Keyboard Shortcuts & Controls"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("`1` Anterior · `2` Posterior · `3` Right Lateral · `4` Left Lateral")
        with c2:
            st.markdown("`+` Zoom in · `-` Zoom out · `R` Reset view")
        with c3:
            st.markdown("`L` Toggle labels · Drag to pan · Scroll wheel to zoom")
