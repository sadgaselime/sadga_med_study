"""
anatomy_3d.py — 3D Anatomy Atlas 🫁
Full interactive anatomy viewer with React frontend embedded via Streamlit components
"""

import streamlit as st
import streamlit.components.v1 as components

ANATOMY_HTML = r"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<style>
  * { margin:0; padding:0; box-sizing:border-box; }
  body { background:#0a0e1a; color:#e8f4ff; font-family:'Segoe UI',system-ui,sans-serif; overflow:hidden; }
  #app { display:flex; height:100vh; width:100vw; position:relative; }

  /* LEFT PANEL */
  #left-panel {
    width:220px; min-width:220px; background:#0d1120; border-right:1px solid #1e2a45;
    display:flex; flex-direction:column; z-index:10; overflow:hidden;
  }
  #left-panel h2 {
    font-size:11px; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
    color:#4a7fa5; padding:14px 14px 8px; border-bottom:1px solid #1e2a45;
  }
  #system-tabs { display:flex; flex-wrap:wrap; gap:4px; padding:10px; border-bottom:1px solid #1e2a45; }
  .sys-btn {
    font-size:10px; padding:4px 8px; border-radius:6px; border:1px solid #1e2a45;
    background:#111827; color:#7ba8c9; cursor:pointer; transition:all .15s;
    font-weight:600; letter-spacing:.04em;
  }
  .sys-btn:hover { background:#1e2a45; color:#e8f4ff; }
  .sys-btn.active { background:#1a3a5c; border-color:#2a6496; color:#60b3e8; }

  #part-list { flex:1; overflow-y:auto; padding:6px; }
  #part-list::-webkit-scrollbar { width:4px; }
  #part-list::-webkit-scrollbar-track { background:#0d1120; }
  #part-list::-webkit-scrollbar-thumb { background:#1e2a45; border-radius:2px; }

  .part-item {
    padding:7px 10px; border-radius:8px; cursor:pointer; font-size:12px;
    color:#a0bcd4; transition:all .15s; margin-bottom:2px;
    border:1px solid transparent; display:flex; align-items:center; gap:7px;
  }
  .part-item:hover { background:#111827; color:#e8f4ff; border-color:#1e2a45; }
  .part-item.selected { background:#0f2540; border-color:#2a6496; color:#60b3e8; font-weight:600; }
  .part-dot { width:8px; height:8px; border-radius:50%; flex-shrink:0; }

  /* CENTER VIEWER */
  #viewer { flex:1; position:relative; overflow:hidden; background:#060912; }
  #canvas-wrap { width:100%; height:100%; display:flex; align-items:center; justify-content:center; }
  #anatomy-svg { cursor:grab; user-select:none; max-height:100vh; }
  #anatomy-svg:active { cursor:grabbing; }

  /* ORIENTATION BUTTONS */
  #orientation-bar {
    position:absolute; top:14px; left:50%; transform:translateX(-50%);
    display:flex; gap:6px; background:rgba(13,17,32,.85); border:1px solid #1e2a45;
    border-radius:10px; padding:6px 10px; backdrop-filter:blur(8px);
  }
  .orient-btn {
    font-size:10px; font-weight:700; letter-spacing:.08em; text-transform:uppercase;
    padding:5px 12px; border-radius:6px; border:1px solid #1e2a45;
    background:transparent; color:#7ba8c9; cursor:pointer; transition:all .15s;
  }
  .orient-btn:hover { background:#1e2a45; color:#e8f4ff; }
  .orient-btn.active { background:#1a3a5c; border-color:#2a6496; color:#60b3e8; }

  /* CONTROLS */
  #controls-bar {
    position:absolute; bottom:14px; left:50%; transform:translateX(-50%);
    display:flex; gap:8px; background:rgba(13,17,32,.85); border:1px solid #1e2a45;
    border-radius:10px; padding:8px 14px; backdrop-filter:blur(8px);
    align-items:center;
  }
  .ctrl-btn {
    width:32px; height:32px; border-radius:8px; border:1px solid #1e2a45;
    background:#111827; color:#7ba8c9; cursor:pointer; font-size:14px;
    display:flex; align-items:center; justify-content:center; transition:all .15s;
  }
  .ctrl-btn:hover { background:#1e2a45; color:#e8f4ff; }
  #zoom-val { font-size:11px; color:#4a7fa5; min-width:38px; text-align:center; font-weight:600; }

  /* LABEL TOGGLE */
  #label-toggle {
    position:absolute; top:14px; right:14px;
    display:flex; gap:6px;
  }
  .toggle-btn {
    font-size:10px; font-weight:700; letter-spacing:.07em; text-transform:uppercase;
    padding:5px 11px; border-radius:7px; border:1px solid #1e2a45;
    background:rgba(13,17,32,.85); color:#7ba8c9; cursor:pointer; transition:all .15s;
    backdrop-filter:blur(8px);
  }
  .toggle-btn:hover { background:#1e2a45; color:#e8f4ff; }
  .toggle-btn.active { background:#1a3a5c; border-color:#2a6496; color:#60b3e8; }

  /* HOVER TOOLTIP */
  #tooltip {
    position:absolute; pointer-events:none; background:rgba(13,17,32,.95);
    border:1px solid #2a6496; border-radius:8px; padding:6px 10px;
    font-size:12px; color:#e8f4ff; white-space:nowrap; display:none;
    backdrop-filter:blur(12px); z-index:100; font-weight:600;
  }

  /* RIGHT DETAIL PANEL */
  #detail-panel {
    width:280px; min-width:280px; background:#0d1120; border-left:1px solid #1e2a45;
    display:flex; flex-direction:column; z-index:10; transition:all .3s;
  }
  #detail-header {
    padding:14px 16px 10px; border-bottom:1px solid #1e2a45;
    display:flex; align-items:center; gap:10px;
  }
  #detail-icon { font-size:22px; }
  #detail-name { font-size:15px; font-weight:700; color:#e8f4ff; line-height:1.2; }
  #detail-latin { font-size:10px; color:#4a7fa5; font-style:italic; margin-top:2px; }
  #detail-body { flex:1; overflow-y:auto; padding:14px; }
  #detail-body::-webkit-scrollbar { width:4px; }
  #detail-body::-webkit-scrollbar-track { background:#0d1120; }
  #detail-body::-webkit-scrollbar-thumb { background:#1e2a45; border-radius:2px; }

  .detail-section { margin-bottom:14px; }
  .detail-section h4 {
    font-size:10px; font-weight:700; letter-spacing:.12em; text-transform:uppercase;
    color:#2a6496; margin-bottom:7px; padding-bottom:4px;
    border-bottom:1px solid #1e2a45;
  }
  .detail-section p { font-size:12px; color:#a0bcd4; line-height:1.6; }
  .detail-tag {
    display:inline-block; background:#0f2540; border:1px solid #1e2a45;
    border-radius:5px; font-size:10px; color:#60b3e8; padding:3px 8px;
    margin:2px 3px 2px 0; font-weight:600;
  }
  .detail-row {
    display:flex; justify-content:space-between; align-items:center;
    padding:5px 0; border-bottom:1px solid #111827; font-size:11px;
  }
  .detail-row span:first-child { color:#4a7fa5; font-weight:600; }
  .detail-row span:last-child { color:#c0d8ea; }
  #detail-empty {
    flex:1; display:flex; flex-direction:column; align-items:center; justify-content:center;
    color:#2a4060; font-size:13px; gap:10px; padding:20px; text-align:center;
  }
  #detail-empty svg { opacity:.3; }

  /* SVG anatomy styles */
  .anatomy-part {
    cursor:pointer; transition:all .18s;
  }
  .anatomy-part:hover { filter:brightness(1.4) drop-shadow(0 0 6px rgba(96,179,232,.7)); }
  .anatomy-part.highlighted { filter:brightness(1.6) drop-shadow(0 0 10px rgba(96,179,232,1)); }
  .anatomy-label {
    font-family:'Segoe UI',sans-serif; font-size:9px; fill:#a0bcd4;
    pointer-events:none; text-anchor:middle; font-weight:600;
  }
  .label-line { stroke:#2a4060; stroke-width:.6; fill:none; pointer-events:none; }
</style>
</head>
<body>
<div id="app">

  <!-- LEFT PANEL: Systems + Part List -->
  <div id="left-panel">
    <h2>Body Systems</h2>
    <div id="system-tabs"></div>
    <div id="part-list"></div>
  </div>

  <!-- CENTER: Anatomy Viewer -->
  <div id="viewer">
    <div id="orientation-bar">
      <button class="orient-btn active" onclick="setView('anterior')">Anterior</button>
      <button class="orient-btn" onclick="setView('posterior')">Posterior</button>
      <button class="orient-btn" onclick="setView('lateral-r')">Right</button>
      <button class="orient-btn" onclick="setView('lateral-l')">Left</button>
      <button class="orient-btn" onclick="setView('superior')">Superior</button>
    </div>
    <div id="label-toggle">
      <button class="toggle-btn active" id="lbl-btn" onclick="toggleLabels()">Labels ON</button>
      <button class="toggle-btn" id="layers-btn" onclick="cycleLayer()">All Layers</button>
    </div>
    <div id="canvas-wrap">
      <svg id="anatomy-svg" viewBox="0 0 520 780" xmlns="http://www.w3.org/2000/svg"></svg>
    </div>
    <div id="controls-bar">
      <button class="ctrl-btn" onclick="adjustZoom(-0.15)" title="Zoom Out">−</button>
      <span id="zoom-val">100%</span>
      <button class="ctrl-btn" onclick="adjustZoom(0.15)" title="Zoom In">+</button>
      <button class="ctrl-btn" onclick="resetView()" title="Reset" style="margin-left:6px;">⟳</button>
    </div>
    <div id="tooltip"></div>
  </div>

  <!-- RIGHT PANEL: Part Details -->
  <div id="detail-panel">
    <div id="detail-header">
      <span id="detail-icon">🔬</span>
      <div>
        <div id="detail-name">Select a structure</div>
        <div id="detail-latin">Click any part to explore</div>
      </div>
    </div>
    <div id="detail-body">
      <div id="detail-empty">
        <svg width="60" height="60" viewBox="0 0 60 60" fill="none">
          <circle cx="30" cy="22" r="12" stroke="#2a6496" stroke-width="2"/>
          <path d="M14 50c0-8.8 7.2-16 16-16s16 7.2 16 16" stroke="#2a6496" stroke-width="2"/>
          <circle cx="30" cy="22" r="4" fill="#2a6496"/>
        </svg>
        <span>Click any anatomical structure on the model to view detailed information</span>
      </div>
      <div id="detail-content" style="display:none;"></div>
    </div>
  </div>
</div>

<script>
// ═══════════════════════════════════════════════════════
// ANATOMY DATABASE — All major + minor structures
// ═══════════════════════════════════════════════════════
const ANATOMY_DB = {
  // ── SKELETAL ─────────────────────────────────────────
  skull:         { name:"Skull",             latin:"Cranium",                 system:"Skeletal",  color:"#b8cfe8", icon:"🦷",
    desc:"The skull is a bony framework of the head, consisting of 22 bones that protect the brain and support the face.",
    function:"Protects the brain, houses sensory organs, provides attachment for facial muscles",
    components:["Frontal bone","Parietal bones (×2)","Temporal bones (×2)","Occipital bone","Sphenoid bone","Ethmoid bone"],
    blood_supply:"Internal carotid, vertebral arteries", innervation:"Cranial nerves I-XII",
    clinical:"Fractures, craniosynostosis, Paget's disease", size:"~21 cm length" },

  mandible:      { name:"Mandible",          latin:"Os mandibulae",           system:"Skeletal",  color:"#b8cfe8", icon:"🦷",
    desc:"The lower jaw bone, the only movable bone of the skull. Houses the lower teeth and articulates with the temporal bone.",
    function:"Mastication, speech, lower dental arch support",
    components:["Body","Ramus","Condyle","Coronoid process","Mental protuberance"],
    blood_supply:"Inferior alveolar artery", innervation:"Inferior alveolar nerve (V3)",
    clinical:"Fractures, TMJ disorders, osteonecrosis", size:"~10 cm width" },

  vertebral_column: { name:"Vertebral Column", latin:"Columna vertebralis", system:"Skeletal", color:"#b8cfe8", icon:"🦴",
    desc:"The spine consists of 33 vertebrae: 7 cervical, 12 thoracic, 5 lumbar, 5 sacral (fused), 4 coccygeal (fused).",
    function:"Axial support, spinal cord protection, movement, weight transmission",
    components:["Cervical vertebrae C1-C7","Thoracic vertebrae T1-T12","Lumbar vertebrae L1-L5","Sacrum","Coccyx"],
    blood_supply:"Segmental spinal arteries", innervation:"Spinal nerves",
    clinical:"Herniated disc, scoliosis, spinal stenosis, fractures", size:"~72 cm length" },

  clavicle:      { name:"Clavicle",          latin:"Clavicula",               system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The collarbone; an S-shaped bone connecting the sternum to the scapula. The only bony attachment of the upper limb to the axial skeleton.",
    function:"Transmits forces from upper limb to sternum, protects neurovascular structures",
    components:["Sternal end","Shaft","Acromial end"],
    blood_supply:"Suprascapular artery, thoracoacromial artery", innervation:"Supraclavicular nerves",
    clinical:"Most commonly fractured bone; shoulder injuries", size:"~15 cm length" },

  sternum:       { name:"Sternum",           latin:"Sternum",                 system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The flat bone in the center of the chest, articulating with the clavicles and ribs 1-7.",
    function:"Protects heart and great vessels, attachment for ribs",
    components:["Manubrium","Body (gladiolus)","Xiphoid process","Sternal angle of Louis"],
    blood_supply:"Internal thoracic arteries", innervation:"Intercostal nerves",
    clinical:"Sternal fracture, median sternotomy for cardiac surgery", size:"~17 cm length" },

  ribs:          { name:"Ribs",              latin:"Costae",                  system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"12 pairs of curved bones forming the rib cage. True ribs (1-7) attach directly to sternum; false (8-10) via costal cartilage; floating (11-12) free anteriorly.",
    function:"Protect thoracic organs, respiratory mechanics",
    components:["True ribs 1-7","False ribs 8-10","Floating ribs 11-12","Costal cartilage","Costal groove"],
    blood_supply:"Posterior intercostal arteries", innervation:"Intercostal nerves",
    clinical:"Rib fractures, flail chest, costochondritis", size:"Varies 14-24 cm" },

  humerus:       { name:"Humerus",           latin:"Humerus",                 system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The long bone of the upper arm, articulating with the scapula at the shoulder and the radius/ulna at the elbow.",
    function:"Upper limb support, attachment for arm muscles",
    components:["Head","Greater tuberosity","Lesser tuberosity","Anatomical neck","Surgical neck","Deltoid tuberosity","Medial/lateral epicondyles","Capitulum","Trochlea"],
    blood_supply:"Anterior/posterior circumflex humeral arteries", innervation:"Radial nerve in spiral groove",
    clinical:"Proximal fractures (surgical neck), shaft fractures (radial nerve palsy)", size:"~33 cm length" },

  radius:        { name:"Radius",            latin:"Radius",                  system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The lateral bone of the forearm; wider distally, articulates with the carpal bones at the wrist.",
    function:"Forearm rotation, wrist support",
    components:["Head","Neck","Radial tuberosity","Styloid process","Lister's tubercle"],
    blood_supply:"Radial artery", innervation:"Radial nerve",
    clinical:"Colles' fracture (most common adult fracture), Smith's fracture", size:"~24 cm length" },

  ulna:          { name:"Ulna",              latin:"Ulna",                    system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The medial bone of the forearm; wider proximally, forms the elbow joint with the humerus.",
    function:"Elbow stability, forearm rotation",
    components:["Olecranon","Trochlear notch","Coronoid process","Radial notch","Styloid process"],
    blood_supply:"Ulnar artery", innervation:"Ulnar nerve",
    clinical:"Monteggia fracture, olecranon bursitis", size:"~26 cm length" },

  pelvis:        { name:"Pelvis",            latin:"Pelvis",                  system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The bony ring formed by the sacrum and two hip bones (os coxae). Transmits weight to lower limbs and protects pelvic organs.",
    function:"Weight transmission, pelvic organ protection, lower limb attachment",
    components:["Ilium","Ischium","Pubis","Acetabulum","Sacrum","Pubic symphysis","Sacroiliac joints"],
    blood_supply:"Internal iliac artery branches", innervation:"Lumbosacral plexus",
    clinical:"Pelvic fractures, hip dysplasia; sex differences important in obstetrics", size:"Male narrower/deeper; female wider/shallower" },

  femur:         { name:"Femur",             latin:"Femur",                   system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The longest and strongest bone in the body, forming the thigh.",
    function:"Lower limb support, hip and knee joint formation",
    components:["Head","Neck","Greater trochanter","Lesser trochanter","Shaft","Medial/lateral condyles","Intercondylar notch","Linea aspera"],
    blood_supply:"Medial/lateral circumflex femoral arteries, profunda femoris", innervation:"Femoral nerve",
    clinical:"Femoral neck fractures (elderly), shaft fractures, AVN of head", size:"~46 cm length; ~1/4 of body height" },

  patella:       { name:"Patella",           latin:"Patella",                 system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The kneecap; the largest sesamoid bone, embedded in the quadriceps tendon.",
    function:"Increases mechanical advantage of quadriceps, protects knee",
    components:["Articular surface","Apex","Base","Medial/lateral facets"],
    blood_supply:"Genicular arteries", innervation:"Femoral/saphenous nerves",
    clinical:"Patellar fracture, chondromalacia, patellar dislocation", size:"~5 cm diameter" },

  tibia:         { name:"Tibia",             latin:"Tibia",                   system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The larger, weight-bearing bone of the leg (shin bone), articulating with femur, fibula, and talus.",
    function:"Weight bearing, ankle/knee joint formation",
    components:["Medial/lateral condyles","Tibial plateau","Tibial tuberosity","Anterior crest","Medial malleolus"],
    blood_supply:"Anterior/posterior tibial arteries", innervation:"Deep peroneal nerve",
    clinical:"Tibial shaft fractures, Osgood-Schlatter, stress fractures", size:"~38 cm length" },

  fibula:        { name:"Fibula",            latin:"Fibula",                  system:"Skeletal",  color:"#b8cfe8", icon:"🦴",
    desc:"The slender lateral bone of the leg; non-weight bearing but important for ankle stability.",
    function:"Ankle stability, muscle attachment",
    components:["Head","Neck","Shaft","Lateral malleolus"],
    blood_supply:"Peroneal artery", innervation:"Common peroneal nerve at neck",
    clinical:"Lateral malleolus fractures (most common ankle fracture), fibular neck injury (peroneal nerve)", size:"~36 cm length" },

  // ── MUSCULAR ─────────────────────────────────────────
  deltoid:       { name:"Deltoid",           latin:"M. deltoideus",           system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Triangular muscle forming the rounded contour of the shoulder, composed of anterior, middle, and posterior parts.",
    function:"Arm abduction (main); flexion (anterior), extension (posterior)",
    components:["Anterior part (clavicular)","Middle part (acromial)","Posterior part (spinous)"],
    blood_supply:"Anterior circumflex humeral artery, thoracoacromial artery", innervation:"Axillary nerve (C5-C6)",
    clinical:"Deltoid injection site; axillary nerve injury causes deltoid paralysis ('square shoulder')", size:"~18 cm wide" },

  biceps_brachii:{ name:"Biceps Brachii",    latin:"M. biceps brachii",       system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Two-headed muscle of the anterior compartment of the arm; crosses both shoulder and elbow joints.",
    function:"Forearm supination (strongest), elbow flexion, shoulder flexion",
    components:["Long head (supraglenoid tubercle)","Short head (coracoid process)","Bicipital aponeurosis"],
    blood_supply:"Brachial artery", innervation:"Musculocutaneous nerve (C5-C6)",
    clinical:"Distal biceps tendon rupture ('Popeye sign'); bicipital tendinitis", size:"~14 cm contracted length" },

  triceps:       { name:"Triceps Brachii",   latin:"M. triceps brachii",      system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Three-headed posterior arm muscle; the only extensor of the elbow.",
    function:"Elbow extension, shoulder extension (long head)",
    components:["Long head","Lateral head","Medial head"],
    blood_supply:"Deep brachial artery", innervation:"Radial nerve (C6-C8)",
    clinical:"Radial nerve palsy causes wrist drop; triceps tendon rupture rare", size:"~15 cm" },

  pectoralis_major:{ name:"Pectoralis Major", latin:"M. pectoralis major",   system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Large fan-shaped muscle of the anterior chest wall with clavicular and sternocostal heads.",
    function:"Adduction, medial rotation, flexion of arm",
    components:["Clavicular head","Sternocostal head","Abdominal part"],
    blood_supply:"Pectoral branches of thoracoacromial artery", innervation:"Medial and lateral pectoral nerves (C5-T1)",
    clinical:"Rupture in weightlifters; radical mastectomy involves this muscle", size:"~20 cm" },

  latissimus_dorsi:{ name:"Latissimus Dorsi", latin:"M. latissimus dorsi",  system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Largest muscle of the back, arising from lower thoracic, lumbar, and sacral regions.",
    function:"Arm adduction, extension, medial rotation; 'swimming muscle'",
    components:["Vertebral part","Scapular part","Iliac part","Costal slips"],
    blood_supply:"Thoracodorsal artery", innervation:"Thoracodorsal nerve (C6-C8)",
    clinical:"Used in breast reconstruction (TRAM/latissimus flaps), shoulder dislocations", size:"~40 cm" },

  quadriceps:    { name:"Quadriceps",        latin:"M. quadriceps femoris",   system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Group of four muscles occupying the anterior thigh, converging into the quadriceps tendon and patellar ligament.",
    function:"Knee extension; hip flexion (rectus femoris)",
    components:["Rectus femoris","Vastus lateralis","Vastus medialis","Vastus intermedius"],
    blood_supply:"Femoral artery branches", innervation:"Femoral nerve (L2-L4)",
    clinical:"Quadriceps tendon rupture; patellofemoral syndrome; VMO in knee rehab", size:"Largest muscle group in body" },

  hamstrings:    { name:"Hamstrings",        latin:"Mm. ischiocruales",       system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Three posterior thigh muscles arising from the ischial tuberosity.",
    function:"Knee flexion, hip extension",
    components:["Biceps femoris (long + short head)","Semimembranosus","Semitendinosus"],
    blood_supply:"Perforating arteries of profunda femoris", innervation:"Sciatic nerve (L5-S2)",
    clinical:"Most common muscle strain in athletes; proximal hamstring avulsion", size:"~35 cm" },

  gastrocnemius: { name:"Gastrocnemius",     latin:"M. gastrocnemius",        system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"Superficial two-headed calf muscle forming the rounded contour of the lower leg.",
    function:"Plantarflexion, knee flexion",
    components:["Medial head","Lateral head"],
    blood_supply:"Sural arteries", innervation:"Tibial nerve (S1-S2)",
    clinical:"'Tennis leg' (muscle tear), DVT mimicry, Achilles tendon pathology", size:"~20 cm" },

  diaphragm:     { name:"Diaphragm",         latin:"Diaphragma",              system:"Muscular",  color:"#e88a8a", icon:"💪",
    desc:"The dome-shaped musculotendinous partition separating the thoracic and abdominal cavities; the primary muscle of respiration.",
    function:"Inspiration (contracts and flattens), rises in expiration",
    components:["Central tendon","Sternal part","Costal part","Lumbar part","Aortic hiatus T12","Esophageal hiatus T10","Caval opening T8"],
    blood_supply:"Phrenic arteries, musculophrenic artery", innervation:"Phrenic nerve (C3-C5) — 'C3,4,5 keeps the diaphragm alive'",
    clinical:"Hiatal hernia, diaphragmatic hernia (Bochdalek/Morgagni), hiccups", size:"~28 cm diameter" },

  // ── CARDIOVASCULAR ───────────────────────────────────
  heart:         { name:"Heart",             latin:"Cor",                     system:"Cardiovascular", color:"#e85a5a", icon:"❤️",
    desc:"A hollow muscular organ located in the mediastinum, slightly left of center. It has 4 chambers and pumps ~5L/min at rest.",
    function:"Pumps oxygenated blood to body (left side) and deoxygenated blood to lungs (right side)",
    components:["Right atrium","Left atrium","Right ventricle","Left ventricle","SA node","AV node","Bundle of His","Tricuspid valve","Mitral valve","Pulmonary valve","Aortic valve"],
    blood_supply:"Right coronary artery (RCA), Left anterior descending (LAD), Left circumflex (LCx)",
    innervation:"Vagus nerve (parasympathetic), sympathetic cardiac nerves",
    clinical:"MI, heart failure, valvular disease, arrhythmias", size:"~12×9×6 cm; ~300g" },

  aorta:         { name:"Aorta",             latin:"Aorta",                   system:"Cardiovascular", color:"#e85a5a", icon:"🩸",
    desc:"The largest artery in the body, arising from the left ventricle and distributing oxygenated blood to the entire body.",
    function:"Main conduit for systemic circulation",
    components:["Aortic root","Ascending aorta","Aortic arch","Descending thoracic aorta","Abdominal aorta","Common iliac arteries"],
    blood_supply:"Vasa vasorum", innervation:"Sympathetic and sensory fibers",
    clinical:"Aortic dissection, aortic aneurysm, coarctation, aortitis", size:"~2.5 cm diameter; 40 cm length" },

  pulmonary_vessels:{ name:"Pulmonary Vessels", latin:"Vasa pulmonalia",     system:"Cardiovascular", color:"#e85a5a", icon:"🩸",
    desc:"The pulmonary trunk and arteries carry deoxygenated blood to the lungs; pulmonary veins return oxygenated blood to the left atrium.",
    function:"Pulmonary circulation",
    components:["Pulmonary trunk","Right pulmonary artery","Left pulmonary artery","Right pulmonary veins (×2)","Left pulmonary veins (×2)"],
    blood_supply:"Bronchial arteries", innervation:"Pulmonary plexus",
    clinical:"Pulmonary embolism, pulmonary hypertension, ASD/VSD", size:"Pulmonary trunk ~5 cm" },

  carotid:       { name:"Carotid Arteries",  latin:"Aa. carotides",           system:"Cardiovascular", color:"#e85a5a", icon:"🩸",
    desc:"The common carotid arteries on each side of the neck divide at C4 into the internal (brain) and external (face) carotid arteries.",
    function:"Blood supply to brain, face, and neck",
    components:["Common carotid artery","Internal carotid artery","External carotid artery","Carotid sinus","Carotid body"],
    blood_supply:"Subclavian artery (right: brachiocephalic; left: directly from aorta)",
    innervation:"Sympathetic fibers, glossopharyngeal nerve (sinus)",
    clinical:"Carotid stenosis, stroke, TIA, carotid endarterectomy", size:"~6 mm diameter" },

  // ── RESPIRATORY ──────────────────────────────────────
  lungs:         { name:"Lungs",             latin:"Pulmones",                system:"Respiratory", color:"#e8a05a", icon:"🫁",
    desc:"Two spongy organs occupying the pleural cavities. Right lung has 3 lobes; left has 2 (with cardiac notch).",
    function:"Gas exchange: O₂ uptake, CO₂ removal",
    components:["Right upper/middle/lower lobes","Left upper/lower lobes","Hilum","Pleura (visceral/parietal)","Alveoli (~500 million)","Bronchopulmonary segments"],
    blood_supply:"Pulmonary arteries (gas exchange), bronchial arteries (nutrition)",
    innervation:"Pulmonary plexus (vagal parasympathetic + sympathetic)",
    clinical:"Pneumonia, COPD, lung cancer, pneumothorax, pulmonary embolism", size:"Right ~700g; left ~600g" },

  trachea:       { name:"Trachea",           latin:"Trachea",                 system:"Respiratory", color:"#e8a05a", icon:"🫁",
    desc:"The windpipe; a cartilaginous and muscular tube connecting the larynx to the bronchi, ~11 cm long, bifurcating at T4/T5 (carina).",
    function:"Air conduction to lungs, mucociliary clearance",
    components:["C-shaped cartilaginous rings (16-20)","Trachealis muscle","Carina","Right/left main bronchi"],
    blood_supply:"Inferior thyroid artery", innervation:"Recurrent laryngeal nerve, vagus",
    clinical:"Tracheal intubation, tracheostomy, tracheal stenosis, foreign body aspiration", size:"~11 cm × 2 cm" },

  larynx:        { name:"Larynx",            latin:"Larynx",                  system:"Respiratory", color:"#e8a05a", icon:"🎤",
    desc:"The voice box; a cartilaginous structure between the pharynx and trachea, containing the vocal folds.",
    function:"Phonation, airway protection, cough reflex",
    components:["Thyroid cartilage","Cricoid cartilage","Arytenoid cartilages","Epiglottis","Vocal folds (true/false)","Glottis"],
    blood_supply:"Superior and inferior laryngeal arteries", innervation:"Superior and recurrent laryngeal nerves (CN X)",
    clinical:"Laryngeal cancer, vocal cord polyps, laryngospasm, intubation landmarks", size:"~5 cm length" },

  // ── DIGESTIVE ────────────────────────────────────────
  liver:         { name:"Liver",             latin:"Hepar",                   system:"Digestive",   color:"#c8782a", icon:"🫀",
    desc:"The largest internal organ (~1.5 kg), located in the right hypochondrium. Divided into 8 functional Couinaud segments.",
    function:"Metabolism, detoxification, bile production, protein synthesis, glycogen storage",
    components:["Right lobe","Left lobe","Caudate lobe","Quadrate lobe","Gallbladder","Portal triad (portal vein, hepatic artery, bile duct)","Hepatic veins"],
    blood_supply:"Portal vein (75%), hepatic artery (25%)", innervation:"Celiac plexus (T7-T9)",
    clinical:"Cirrhosis, hepatitis, hepatocellular carcinoma, portal hypertension", size:"~1500 g; 15-17 cm span" },

  stomach:       { name:"Stomach",           latin:"Gaster / Ventriculus",    system:"Digestive",   color:"#c8782a", icon:"🫀",
    desc:"J-shaped dilated portion of the GI tract between the esophagus and duodenum, located in the left hypochondrium/epigastrium.",
    function:"Mechanical and chemical digestion, HCl secretion, intrinsic factor production",
    components:["Cardia","Fundus","Body (corpus)","Antrum","Pylorus","Lesser curvature","Greater curvature","Rugae"],
    blood_supply:"Celiac trunk branches (left/right gastric, gastroepiploic, short gastric arteries)",
    innervation:"Vagus nerve, celiac plexus",
    clinical:"Peptic ulcer, gastric cancer, GERD, pyloric stenosis", size:"~25 cm; 1-2L capacity" },

  small_intestine:{ name:"Small Intestine",  latin:"Intestinum tenue",        system:"Digestive",   color:"#c8782a", icon:"🫀",
    desc:"6-7 meter tube with three parts: duodenum, jejunum, ileum. Site of most nutrient absorption.",
    function:"Digestion and absorption of nutrients",
    components:["Duodenum (25 cm; 4 parts)","Jejunum (~2.5 m)","Ileum (~3.5 m)","Villi & microvilli","Peyer's patches","Ileocecal valve"],
    blood_supply:"Superior mesenteric artery", innervation:"Vagus nerve, superior mesenteric plexus",
    clinical:"Crohn's disease, celiac disease, intestinal obstruction, intussusception", size:"~6.5 m total" },

  large_intestine:{ name:"Large Intestine",  latin:"Intestinum crassum",      system:"Digestive",   color:"#c8782a", icon:"🫀",
    desc:"The final ~1.5 m of the GI tract; absorbs water and electrolytes, forming feces.",
    function:"Water/electrolyte absorption, feces formation, gut flora habitat",
    components:["Cecum + appendix","Ascending colon","Transverse colon","Descending colon","Sigmoid colon","Rectum","Anal canal","Taeniae coli","Haustra"],
    blood_supply:"Superior (right side) + inferior (left side) mesenteric arteries", innervation:"Vagus (proximal), pelvic splanchnic nerves (distal)",
    clinical:"Colorectal cancer, diverticulitis, appendicitis, UC, Hirschsprung's", size:"~1.5 m; 6 cm diameter" },

  pancreas:      { name:"Pancreas",          latin:"Pancreas",                system:"Digestive",   color:"#c8782a", icon:"🫀",
    desc:"Both exocrine and endocrine gland lying retroperitoneally behind the stomach.",
    function:"Exocrine: digestive enzymes. Endocrine: insulin (β), glucagon (α), somatostatin (δ)",
    components:["Head (in duodenal curve)","Neck","Body","Tail (near spleen)","Islets of Langerhans","Acinar cells","Main pancreatic duct (of Wirsung)"],
    blood_supply:"Splenic artery, superior/inferior pancreaticoduodenal arteries", innervation:"Celiac plexus, vagus",
    clinical:"Pancreatitis, pancreatic cancer (poor prognosis), diabetes mellitus", size:"~15 cm length; ~70-100g" },

  // ── NERVOUS SYSTEM ───────────────────────────────────
  brain:         { name:"Brain",             latin:"Encephalon",              system:"Nervous",     color:"#d4a0e8", icon:"🧠",
    desc:"The control center of the nervous system, comprising ~86 billion neurons. Weighs ~1.4 kg and consumes 20% of body's oxygen.",
    function:"Cognition, movement, sensation, autonomic regulation, endocrine control",
    components:["Cerebrum (frontal/parietal/temporal/occipital lobes)","Cerebellum","Brainstem (midbrain/pons/medulla)","Limbic system","Basal ganglia","Thalamus","Hypothalamus","Ventricles","Corpus callosum"],
    blood_supply:"Internal carotid arteries (anterior circulation), vertebral/basilar arteries (posterior circulation), Circle of Willis",
    innervation:"Cranial nerves I-XII",
    clinical:"Stroke, brain tumors, epilepsy, Alzheimer's, Parkinson's, TBI", size:"~1400 g; ~1400 cc volume" },

  spinal_cord:   { name:"Spinal Cord",       latin:"Medulla spinalis",        system:"Nervous",     color:"#d4a0e8", icon:"🧠",
    desc:"The cylindrical nerve tract within the vertebral canal extending from the medulla oblongata to the conus medullaris at L1-L2.",
    function:"Conduit for sensory/motor signals; reflex arcs",
    components:["31 spinal nerve segments","Cervical enlargement","Lumbar enlargement","Conus medullaris","Cauda equina","Filum terminale","Gray/white matter","Anterior/posterior horns"],
    blood_supply:"Anterior spinal artery (single), posterior spinal arteries (paired), Artery of Adamkiewicz",
    innervation:"31 pairs of spinal nerves",
    clinical:"Spinal cord injury, MS, syringomyelia, spinal stenosis", size:"~45 cm length; ~1 cm diameter" },

  // ── URINARY ──────────────────────────────────────────
  kidneys:       { name:"Kidneys",           latin:"Renes",                   system:"Urinary",     color:"#7a9ee8", icon:"🫘",
    desc:"Two bean-shaped retroperitoneal organs at T12-L3 level, each ~150 g, filtering ~180L of plasma per day.",
    function:"Blood filtration, urine production, BP regulation (RAAS), erythropoietin, Vit D activation",
    components:["Cortex","Medulla","Pyramids","Columns of Bertin","Calyces (major/minor)","Renal pelvis","Glomerulus","Nephron (~1 million per kidney)","Juxtaglomerular apparatus"],
    blood_supply:"Renal arteries (directly from aorta at L1-L2)", innervation:"Renal plexus (T10-L1)",
    clinical:"Renal failure, nephrolithiasis, UTI, renal cell carcinoma, HTN", size:"~11×6×3 cm; ~150 g" },

  bladder:       { name:"Urinary Bladder",   latin:"Vesica urinaria",         system:"Urinary",     color:"#7a9ee8", icon:"🫘",
    desc:"A hollow muscular organ in the pelvic cavity that stores urine, capable of holding 400-600 mL.",
    function:"Urine storage and micturition",
    components:["Detrusor muscle","Trigone","Internal urethral sphincter","Ureteral orifices","Dome","Neck"],
    blood_supply:"Superior and inferior vesical arteries (internal iliac)", innervation:"Pelvic splanchnic nerves (S2-S4), hypogastric plexus",
    clinical:"UTI, bladder cancer (TCC most common), overactive bladder, urinary retention", size:"~400-600 mL capacity" },

  // ── ENDOCRINE ────────────────────────────────────────
  thyroid:       { name:"Thyroid Gland",     latin:"Glandula thyreoidea",     system:"Endocrine",   color:"#78d4a0", icon:"🔬",
    desc:"Butterfly-shaped endocrine gland in the anterior neck, at C5-T1 level, consisting of two lobes connected by an isthmus.",
    function:"Produces T3/T4 (metabolism, growth), calcitonin (calcium homeostasis)",
    components:["Right lobe","Left lobe","Isthmus","Pyramidal lobe (50%)","Follicular cells","Parafollicular (C) cells"],
    blood_supply:"Superior thyroid artery (ECA), inferior thyroid artery (thyrocervical trunk)", innervation:"Sympathetic via superior/middle cervical ganglia",
    clinical:"Hypothyroidism, hyperthyroidism (Graves'), thyroid cancer, goiter", size:"~25 g total; 4-5 cm each lobe" },

  adrenal_glands:{ name:"Adrenal Glands",    latin:"Glandulae suprarenales",  system:"Endocrine",   color:"#78d4a0", icon:"🔬",
    desc:"Two triangular glands (right pyramidal, left semilunar) capping the kidneys retroperitoneally. Each ~5g.",
    function:"Cortex: cortisol, aldosterone, DHEA. Medulla: adrenaline (epinephrine), noradrenaline",
    components:["Cortex: zona glomerulosa/fasciculata/reticularis","Medulla: chromaffin cells"],
    blood_supply:"Superior/middle/inferior suprarenal arteries", innervation:"Splanchnic nerves (greater/lesser)",
    clinical:"Cushing's syndrome, Addison's disease, pheochromocytoma, Conn's syndrome", size:"~5 cm × 3 cm × 1 cm each" },

  pituitary:     { name:"Pituitary Gland",   latin:"Hypophysis cerebri",      system:"Endocrine",   color:"#78d4a0", icon:"🔬",
    desc:"The 'master gland'; a pea-sized structure at the sella turcica of the sphenoid bone, connected to the hypothalamus.",
    function:"Anterior: GH, TSH, ACTH, FSH, LH, prolactin. Posterior: ADH, oxytocin",
    components:["Anterior pituitary (adenohypophysis)","Posterior pituitary (neurohypophysis)","Pituitary stalk (infundibulum)"],
    blood_supply:"Hypophyseal portal system (anterior), inferior hypophyseal artery (posterior)",
    innervation:"Hypothalamic-hypophyseal tract",
    clinical:"Pituitary adenoma, acromegaly, Cushing's, diabetes insipidus, craniopharyngioma", size:"~1 cm × 1 cm; ~0.5 g" },

  // ── REPRODUCTIVE (basic) ─────────────────────────────
  testes:        { name:"Testes",            latin:"Testes",                  system:"Reproductive", color:"#d4c878", icon:"🔬",
    desc:"Paired male gonads in the scrotum, descended from the abdomen during development.",
    function:"Spermatogenesis (FSH-dependent), testosterone production (LH-dependent)",
    components:["Seminiferous tubules","Leydig cells","Sertoli cells","Epididymis","Tunica albuginea","Rete testis"],
    blood_supply:"Testicular artery (from aorta at L2)", innervation:"Genital branch of genitofemoral nerve, sympathetic plexus",
    clinical:"Testicular torsion (emergency), orchitis, seminoma (most common testicular cancer)", size:"~4.5×3×2.5 cm; 20g each" },

  // ── LYMPHATIC ────────────────────────────────────────
  spleen:        { name:"Spleen",            latin:"Lien / Splen",            system:"Lymphatic",   color:"#a078d4", icon:"🔬",
    desc:"The largest lymphoid organ (~150g), located in the left hypochondrium between ribs 9-11.",
    function:"Blood filtration, immune response, blood cell reservoir, fetal hematopoiesis",
    components:["White pulp (lymphoid)","Red pulp (blood filtration)","Splenic sinuses","Splenic cords of Billroth","Capsule + trabeculae"],
    blood_supply:"Splenic artery (largest branch of celiac trunk)", innervation:"Celiac plexus",
    clinical:"Splenomegaly, splenic rupture (trauma — emergency splenectomy), hypersplenism", size:"~11×7×4 cm; ~150 g" },

  lymph_nodes:   { name:"Lymph Nodes",       latin:"Nodi lymphoidei",         system:"Lymphatic",   color:"#a078d4", icon:"🔬",
    desc:"Small oval structures (~600 in body) distributed along lymphatic vessels, acting as immunological filters.",
    function:"Filter lymph, mount immune responses, B and T cell activation",
    components:["Cortex (B cells, follicles)","Paracortex (T cells)","Medulla","Afferent/efferent lymphatics","Hilum"],
    blood_supply:"Small arterioles via hilum", innervation:"Autonomic nerve fibers",
    clinical:"Lymphadenopathy, lymphoma (Hodgkin's/non-Hodgkin's), metastatic nodes, reactive lymphadenitis", size:"2-25 mm; varies greatly" },

  thymus:        { name:"Thymus",            latin:"Thymus",                  system:"Lymphatic",   color:"#a078d4", icon:"🔬",
    desc:"Bilobed lymphoid organ in the anterior superior mediastinum; large in childhood, involutes after puberty.",
    function:"T-lymphocyte maturation and selection (positive/negative selection)",
    components:["Lobules","Cortex (immature T cells)","Medulla (mature T cells)","Hassall's corpuscles","Thymic epithelial cells"],
    blood_supply:"Internal thoracic artery, inferior thyroid artery", innervation:"Vagus, phrenic nerves",
    clinical:"Thymoma (associated with myasthenia gravis), DiGeorge syndrome, T cell immunodeficiency", size:"~30g in puberty; regresses with age" },

  // ── EYE / EAR ────────────────────────────────────────
  eye:           { name:"Eye",               latin:"Oculus",                  system:"Sensory",     color:"#58d4c8", icon:"👁️",
    desc:"The organ of vision; a sphere ~24mm in diameter, containing optical and neural structures.",
    function:"Image formation and transduction to neural signals",
    components:["Cornea","Anterior/posterior chambers","Iris","Lens","Vitreous humour","Retina (rods/cones)","Optic nerve (CN II)","Choroid","Sclera","Macula lutea","Fovea centralis"],
    blood_supply:"Ophthalmic artery (from ICA), central retinal artery", innervation:"CN II (optic), CN III/IV/VI (extraocular), CN V (cornea)",
    clinical:"Glaucoma, cataract, retinal detachment, macular degeneration, diabetic retinopathy", size:"~24 mm diameter" },

  ear:           { name:"Ear",               latin:"Auris",                   system:"Sensory",     color:"#58d4c8", icon:"👂",
    desc:"The organ of hearing and equilibrium, divided into external, middle, and inner ear.",
    function:"Sound transduction, spatial orientation/balance",
    components:["External: auricle, EAC, tympanic membrane","Middle: malleus, incus, stapes, Eustachian tube","Inner: cochlea (hearing), vestibular system (balance), CN VIII"],
    blood_supply:"External carotid artery branches, labyrinthine artery (AICA branch)",
    innervation:"CN VIII (vestibulocochlear), CN V, VII, X",
    clinical:"Otitis media, sensorineural hearing loss, Meniere's disease, vestibular schwannoma", size:"Cochlea ~3 cm diameter" },
};

// ═══════════════════════════════════════════════════════
// SYSTEMS CONFIG
// ═══════════════════════════════════════════════════════
const SYSTEMS = {
  "All":          { color:"#60b3e8" },
  "Skeletal":     { color:"#b8cfe8" },
  "Muscular":     { color:"#e88a8a" },
  "Cardiovascular":{ color:"#e85a5a" },
  "Respiratory":  { color:"#e8a05a" },
  "Digestive":    { color:"#c8782a" },
  "Nervous":      { color:"#d4a0e8" },
  "Urinary":      { color:"#7a9ee8" },
  "Endocrine":    { color:"#78d4a0" },
  "Reproductive": { color:"#d4c878" },
  "Lymphatic":    { color:"#a078d4" },
  "Sensory":      { color:"#58d4c8" },
};

// ═══════════════════════════════════════════════════════
// VIEW DEFINITIONS (SVG shapes per view + system)
// ═══════════════════════════════════════════════════════
// Each view draws the body outline + placed organs
// We use a single anterior view with pan/zoom

let currentSystem = "All";
let currentView = "anterior";
let selectedPart = null;
let zoom = 1;
let panX = 0, panY = 0;
let isDragging = false, dragStartX, dragStartY;
let showLabels = true;
let showLayer = "all"; // all / skeletal / soft / organs
let layerNames = ["All Layers","Skeletal","Muscular","Organs"];
let layerKeys  = ["all","skeletal","muscular","organs"];
let layerIdx   = 0;

// ─── SVG PARTS: path data for anterior view ───────────────
// Each part: { id, paths:[], cx, cy (label pos), labelText }
// Coordinates designed for 520×780 viewBox

const ANTERIOR_PARTS = [
  // ── BODY OUTLINE ────────
  { id:"__body_outline", system:"",
    paths:[{d:"M180,30 Q200,20 260,20 Q320,20 340,30 L355,80 Q370,100 375,130 L378,160 Q385,200 382,230 L378,300 Q375,360 370,390 L368,440 Q365,480 360,500 L340,580 Q330,630 325,680 L320,740 310,760 Q295,775 260,775 Q225,775 210,760 L200,740 195,680 Q190,630 180,580 L160,500 Q155,480 152,440 L150,390 Q145,360 142,300 L138,230 Q135,200 142,160 L145,130 Q150,100 165,80 Z", fill:"#0a1628", stroke:"#2a4060", sw:1.5}], cx:260,cy:400,label:"",system:""
  },

  // ── HEAD/SKULL ────────
  { id:"skull", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M220,28 Q260,8 300,28 Q325,45 328,72 Q330,95 315,108 Q290,120 260,122 Q230,120 205,108 Q190,95 192,72 Q195,45 220,28 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:1, op:0.7}],
    cx:260, cy:65, label:"Skull" },

  // ── MANDIBLE ────────
  { id:"mandible", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M225,108 Q260,118 295,108 Q305,120 305,130 Q295,145 260,147 Q225,145 215,130 Q215,120 225,108 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.7}],
    cx:260, cy:127, label:"Mandible" },

  // ── BRAIN (visible through skull in cutaway) ────────
  { id:"brain", system:"Nervous", layer:"organs",
    paths:[{d:"M222,30 Q260,15 298,30 Q318,45 320,68 Q318,90 305,102 Q285,114 260,115 Q235,114 215,102 Q202,90 200,68 Q202,45 222,30 Z", fill:"#d4a0e8", stroke:"#b080cc", sw:0.8, op:0.75}],
    cx:260, cy:65, label:"Brain" },

  // ── EYES ────────
  { id:"eye", system:"Sensory", layer:"organs",
    paths:[
      {d:"M230,78 Q240,73 250,78 Q240,83 230,78 Z", fill:"#58d4c8", stroke:"#38b4a8", sw:0.6},
      {d:"M270,78 Q280,73 290,78 Q280,83 270,78 Z", fill:"#58d4c8", stroke:"#38b4a8", sw:0.6},
    ],
    cx:260, cy:78, label:"Eye" },

  // ── EAR ────────
  { id:"ear", system:"Sensory", layer:"organs",
    paths:[
      {d:"M195,90 Q188,93 188,100 Q188,107 195,110 Q200,108 202,100 Q200,93 195,90 Z", fill:"#58d4c8", stroke:"#38b4a8", sw:0.6},
      {d:"M325,90 Q332,93 332,100 Q332,107 325,110 Q320,108 318,100 Q320,93 325,90 Z", fill:"#58d4c8", stroke:"#38b4a8", sw:0.6},
    ],
    cx:260, cy:100, label:"Ear" },

  // ── NECK / TRACHEA ────────
  { id:"trachea", system:"Respiratory", layer:"organs",
    paths:[{d:"M252,148 Q256,145 268,148 L270,178 Q266,183 260,183 Q254,183 250,178 Z", fill:"#e8a05a", stroke:"#c87030", sw:0.7, op:0.8}],
    cx:260, cy:163, label:"Trachea" },

  // ── THYROID ────────
  { id:"thyroid", system:"Endocrine", layer:"organs",
    paths:[{d:"M240,155 Q250,150 260,152 Q270,150 280,155 Q278,165 268,168 Q260,170 252,168 Q242,165 240,155 Z", fill:"#78d4a0", stroke:"#50b078", sw:0.7, op:0.85}],
    cx:260, cy:160, label:"Thyroid" },

  // ── CLAVICLE ────────
  { id:"clavicle", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M175,148 Q210,138 240,142 Q250,144 252,148 Q240,152 205,155 Q182,155 175,148 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.7},
      {d:"M268,148 Q270,144 280,142 Q310,138 345,148 Q338,155 318,155 Q283,152 268,148 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.7},
    ],
    cx:260, cy:148, label:"Clavicle" },

  // ── STERNUM ────────
  { id:"sternum", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M248,150 Q260,148 272,150 L274,250 Q265,254 260,254 Q255,254 246,250 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.65}],
    cx:260, cy:200, label:"Sternum" },

  // ── RIBS ────────
  { id:"ribs", system:"Skeletal", layer:"skeletal",
    paths:[
      // Right ribs (from viewer's perspective: left side of SVG)
      {d:"M248,158 Q215,162 185,170 Q182,175 185,178 Q215,172 248,168 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M248,168 Q213,174 183,185 Q180,190 183,193 Q213,184 248,178 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M248,178 Q210,186 182,200 Q180,206 183,208 Q212,196 248,188 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M248,188 Q210,200 184,216 Q182,222 186,224 Q212,210 248,198 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M248,198 Q212,212 188,230 Q186,237 190,239 Q215,224 248,210 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M248,208 Q215,225 192,244 Q190,251 195,253 Q218,238 248,220 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M248,218 Q218,238 198,258 Q196,264 201,266 Q222,252 248,230 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      // Left ribs
      {d:"M272,158 Q305,162 335,170 Q338,175 335,178 Q305,172 272,168 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M272,168 Q307,174 337,185 Q340,190 337,193 Q307,184 272,178 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M272,178 Q310,186 338,200 Q340,206 337,208 Q308,196 272,188 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M272,188 Q310,200 336,216 Q338,222 334,224 Q308,210 272,198 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M272,198 Q308,212 332,230 Q334,237 330,239 Q305,224 272,210 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M272,208 Q305,225 328,244 Q330,251 325,253 Q302,238 272,220 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
      {d:"M272,218 Q302,238 322,258 Q324,264 319,266 Q298,252 272,230 Z", fill:"none", stroke:"#b8cfe8", sw:1.2, op:0.7},
    ],
    cx:208, cy:205, label:"Ribs" },

  // ── SCAPULA (visible from anterior, just shoulder area) ────────
  { id:"clavicle", system:"Skeletal", layer:"skeletal",
    paths:[], cx:200,cy:180, label:"" }, // merged above

  // ── LUNGS ────────
  { id:"lungs", system:"Respiratory", layer:"organs",
    paths:[
      {d:"M205,162 Q192,170 186,200 Q182,230 184,265 Q186,285 195,295 Q210,305 225,300 Q240,295 245,280 L248,255 L248,162 Q228,158 205,162 Z", fill:"#e8a05a", stroke:"#c07828", sw:0.8, op:0.65},
      {d:"M315,162 Q328,170 334,200 Q338,230 336,265 Q334,285 325,295 Q310,305 295,300 Q280,295 275,280 L272,255 L272,162 Q292,158 315,162 Z", fill:"#e8a05a", stroke:"#c07828", sw:0.8, op:0.65},
    ],
    cx:260, cy:220, label:"Lungs" },

  // ── HEART ────────
  { id:"heart", system:"Cardiovascular", layer:"organs",
    paths:[{d:"M248,175 Q245,172 238,174 Q228,178 226,188 Q224,200 232,210 Q240,220 260,232 Q280,220 288,210 Q296,200 294,188 Q292,178 282,174 Q275,172 272,175 Q268,170 260,170 Q252,170 248,175 Z", fill:"#e85a5a", stroke:"#c03030", sw:1, op:0.85}],
    cx:260, cy:200, label:"Heart" },

  // ── AORTA ────────
  { id:"aorta", system:"Cardiovascular", layer:"organs",
    paths:[{d:"M260,170 Q270,165 280,168 Q280,175 272,180 L272,185 Q278,182 285,185 Q290,195 288,210 Q284,204 272,202 L272,260 L268,275 L260,280 L252,275 L248,260 L248,202 Q236,204 232,210 Q230,195 235,185 Q242,182 248,185 L248,180 Q240,175 240,168 Q250,165 260,170 Z", fill:"#e85a5a", stroke:"#c03030", sw:0.6, op:0.4}],
    cx:260, cy:235, label:"Aorta" },

  // ── PULMONARY VESSELS ────────
  { id:"pulmonary_vessels", system:"Cardiovascular", layer:"organs",
    paths:[
      {d:"M248,178 Q240,178 228,183 Q224,190 226,196 Q232,195 248,192 Z", fill:"#7a9ee8", stroke:"#4a7ec8", sw:0.7, op:0.7},
      {d:"M272,178 Q280,178 292,183 Q296,190 294,196 Q288,195 272,192 Z", fill:"#e85a5a", stroke:"#c03030", sw:0.7, op:0.7},
    ],
    cx:260, cy:188, label:"Pulm. Vessels" },

  // ── CAROTID ARTERIES ────────
  { id:"carotid", system:"Cardiovascular", layer:"organs",
    paths:[
      {d:"M248,148 L244,172 Q246,175 249,172 L251,148 Z", fill:"#e85a5a", stroke:"#c03030", sw:0.7, op:0.8},
      {d:"M272,148 L276,172 Q274,175 271,172 L269,148 Z", fill:"#e85a5a", stroke:"#c03030", sw:0.7, op:0.8},
    ],
    cx:255, cy:160, label:"Carotid" },

  // ── DIAPHRAGM ────────
  { id:"diaphragm", system:"Muscular", layer:"muscular",
    paths:[{d:"M182,295 Q220,310 260,312 Q300,310 338,295 Q335,305 320,315 Q295,325 260,326 Q225,325 200,315 Q185,305 182,295 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.7}],
    cx:260, cy:308, label:"Diaphragm" },

  // ── DELTOID ────────
  { id:"deltoid", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M158,158 Q145,170 143,195 Q145,215 158,220 Q168,215 178,200 Q182,185 178,165 Q170,155 158,158 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.7},
      {d:"M362,158 Q375,170 377,195 Q375,215 362,220 Q352,215 342,200 Q338,185 342,165 Q350,155 362,158 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.7},
    ],
    cx:165, cy:190, label:"Deltoid" },

  // ── PECTORALIS MAJOR ────────
  { id:"pectoralis_major", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M180,163 Q205,158 248,163 L248,255 Q235,260 215,255 Q195,245 182,230 Q172,215 180,163 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.55},
      {d:"M340,163 Q315,158 272,163 L272,255 Q285,260 305,255 Q325,245 338,230 Q348,215 340,163 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.55},
    ],
    cx:215, cy:210, label:"Pect. Major" },

  // ── BICEPS BRACHII ────────
  { id:"biceps_brachii", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M143,225 Q138,240 138,270 Q140,300 145,315 Q152,318 158,315 Q165,300 166,270 Q165,240 160,225 Q152,218 143,225 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
      {d:"M377,225 Q382,240 382,270 Q380,300 375,315 Q368,318 362,315 Q355,300 354,270 Q355,240 360,225 Q368,218 377,225 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
    ],
    cx:150, cy:270, label:"Biceps" },

  // ── TRICEPS ────────
  { id:"triceps", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M136,230 Q128,248 128,280 Q130,310 136,325 Q140,316 142,280 Q142,248 140,230 Q138,225 136,230 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.7, op:0.5},
      {d:"M384,230 Q392,248 392,280 Q390,310 384,325 Q380,316 378,280 Q378,248 380,230 Q382,225 384,230 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.7, op:0.5},
    ],
    cx:133, cy:277, label:"Triceps" },

  // ── HUMERUS ────────
  { id:"humerus", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M152,220 Q146,240 146,290 Q148,330 155,345 Q158,338 160,290 Q160,240 156,220 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.6},
      {d:"M368,220 Q374,240 374,290 Q372,330 365,345 Q362,338 360,290 Q360,240 364,220 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.6},
    ],
    cx:150, cy:285, label:"Humerus" },

  // ── RADIUS / ULNA ────────
  { id:"radius", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M148,348 L150,440 Q152,442 154,440 L155,348 Q152,344 148,348 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.7, op:0.65},
      {d:"M372,348 L370,440 Q368,442 366,440 L365,348 Q368,344 372,348 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.7, op:0.65},
    ],
    cx:150, cy:393, label:"Radius" },

  { id:"ulna", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M157,345 L158,440 Q161,442 164,440 L164,345 Q161,341 157,345 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.7, op:0.65},
      {d:"M363,345 L362,440 Q359,442 356,440 L356,345 Q359,341 363,345 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.7, op:0.65},
    ],
    cx:162, cy:390, label:"Ulna" },

  // ── LIVER ────────
  { id:"liver", system:"Digestive", layer:"organs",
    paths:[{d:"M185,300 Q195,296 240,298 Q258,298 265,302 Q272,310 270,335 Q268,355 250,365 Q228,370 205,362 Q185,350 180,328 Q177,312 185,300 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.75}],
    cx:225, cy:335, label:"Liver" },

  // ── STOMACH ────────
  { id:"stomach", system:"Digestive", layer:"organs",
    paths:[{d:"M265,302 Q285,296 298,305 Q312,318 310,345 Q308,365 292,372 Q275,376 265,368 Q255,358 255,340 Q255,318 265,302 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.75}],
    cx:284, cy:338, label:"Stomach" },

  // ── SPLEEN ────────
  { id:"spleen", system:"Lymphatic", layer:"organs",
    paths:[{d:"M318,310 Q332,308 340,318 Q344,330 340,342 Q334,350 322,348 Q312,342 310,330 Q308,318 318,310 Z", fill:"#a078d4", stroke:"#7850b0", sw:0.8, op:0.75}],
    cx:327, cy:330, label:"Spleen" },

  // ── PANCREAS ────────
  { id:"pancreas", system:"Digestive", layer:"organs",
    paths:[{d:"M230,362 Q248,358 268,360 Q285,362 295,370 Q298,378 290,383 Q272,385 248,382 Q228,378 222,370 Q220,363 230,362 Z", fill:"#c8782a", stroke:"#a05010", sw:0.7, op:0.7}],
    cx:258, cy:373, label:"Pancreas" },

  // ── SMALL INTESTINE ────────
  { id:"small_intestine", system:"Digestive", layer:"organs",
    paths:[{d:"M215,385 Q225,378 240,382 Q248,388 250,408 Q248,430 240,448 Q232,460 220,458 Q208,452 204,438 Q200,420 205,402 Q208,390 215,385 Z", fill:"#c8782a", stroke:"#a05010", sw:0.7, op:0.6},
           {d:"M250,390 Q262,383 272,388 Q280,395 282,415 Q280,435 272,450 Q262,458 252,455 Q242,448 240,432 Q238,412 244,398 Q246,392 250,390 Z", fill:"#c8782a", stroke:"#a05010", sw:0.7, op:0.6},
           {d:"M283,392 Q294,387 302,393 Q308,400 308,418 Q306,435 298,447 Q290,454 280,450 Q272,444 272,428 Q272,410 277,399 Q279,394 283,392 Z", fill:"#c8782a", stroke:"#a05010", sw:0.7, op:0.6},
    ],
    cx:256, cy:420, label:"Small Int." },

  // ── LARGE INTESTINE ────────
  { id:"large_intestine", system:"Digestive", layer:"organs",
    paths:[
      // Ascending colon
      {d:"M190,450 Q184,468 184,490 Q186,510 192,520 Q200,524 208,518 Q214,508 214,490 Q213,468 208,450 Q200,444 190,450 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.65},
      // Transverse colon
      {d:"M208,452 Q232,444 260,442 Q288,444 312,452 Q314,460 310,465 Q286,457 260,455 Q234,457 210,465 Q206,460 208,452 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.65},
      // Descending colon
      {d:"M310,454 Q316,470 316,492 Q314,512 308,522 Q300,526 292,520 Q286,510 286,490 Q287,470 292,454 Q300,447 310,454 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.65},
      // Sigmoid
      {d:"M286,520 Q280,535 268,545 Q255,550 245,545 Q235,538 232,525 Q236,520 244,523 Q252,530 262,526 Q272,522 278,516 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.65},
    ],
    cx:245, cy:480, label:"Large Int." },

  // ── PELVIS ────────
  { id:"pelvis", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M178,510 Q195,500 230,496 Q260,493 290,496 Q325,500 342,510 Q350,525 348,545 Q340,565 310,575 Q280,582 260,582 Q240,582 210,575 Q180,565 172,545 Q170,525 178,510 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:1, op:0.5}],
    cx:260, cy:538, label:"Pelvis" },

  // ── KIDNEYS ────────
  { id:"kidneys", system:"Urinary", layer:"organs",
    paths:[
      {d:"M192,370 Q180,375 178,392 Q178,408 190,415 Q202,418 210,410 Q216,400 214,385 Q210,370 192,370 Z", fill:"#7a9ee8", stroke:"#5070c8", sw:0.8, op:0.8},
      {d:"M328,370 Q340,375 342,392 Q342,408 330,415 Q318,418 310,410 Q304,400 306,385 Q310,370 328,370 Z", fill:"#7a9ee8", stroke:"#5070c8", sw:0.8, op:0.8},
    ],
    cx:260, cy:392, label:"Kidneys" },

  // ── ADRENAL GLANDS ────────
  { id:"adrenal_glands", system:"Endocrine", layer:"organs",
    paths:[
      {d:"M186,362 Q192,358 198,362 Q200,370 196,376 Q190,378 186,373 Q184,367 186,362 Z", fill:"#78d4a0", stroke:"#50b078", sw:0.6, op:0.85},
      {d:"M322,362 Q328,358 334,362 Q336,370 332,376 Q326,378 322,373 Q320,367 322,362 Z", fill:"#78d4a0", stroke:"#50b078", sw:0.6, op:0.85},
    ],
    cx:260, cy:368, label:"Adrenal" },

  // ── BLADDER ────────
  { id:"bladder", system:"Urinary", layer:"organs",
    paths:[{d:"M242,542 Q248,535 260,534 Q272,535 278,542 Q282,554 278,564 Q270,572 260,572 Q250,572 242,564 Q238,554 242,542 Z", fill:"#7a9ee8", stroke:"#5070c8", sw:0.8, op:0.8}],
    cx:260, cy:553, label:"Bladder" },

  // ── TESTES ────────
  { id:"testes", system:"Reproductive", layer:"organs",
    paths:[
      {d:"M248,578 Q244,583 244,590 Q244,598 250,600 Q256,602 260,598 Q258,590 256,582 Q253,577 248,578 Z", fill:"#d4c878", stroke:"#a89850", sw:0.6, op:0.75},
      {d:"M272,578 Q276,583 276,590 Q276,598 270,600 Q264,602 260,598 Q262,590 264,582 Q267,577 272,578 Z", fill:"#d4c878", stroke:"#a89850", sw:0.6, op:0.75},
    ],
    cx:260, cy:590, label:"Testes" },

  // ── FEMUR ────────
  { id:"femur", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M210,580 Q205,610 205,660 Q206,700 208,720 Q212,725 218,720 Q220,700 220,660 Q219,610 216,580 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.65},
      {d:"M310,580 Q315,610 315,660 Q314,700 312,720 Q308,725 302,720 Q300,700 300,660 Q301,610 304,580 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.65},
    ],
    cx:215, cy:650, label:"Femur" },

  // ── QUADRICEPS ────────
  { id:"quadriceps", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M202,582 Q195,610 195,660 Q197,700 202,720 Q208,725 210,720 Q205,700 205,660 Q206,610 207,582 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.7, op:0.6},
      {d:"M318,582 Q325,610 325,660 Q323,700 318,720 Q312,725 310,720 Q315,700 315,660 Q314,610 313,582 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.7, op:0.6},
    ],
    cx:200, cy:645, label:"Quadriceps" },

  // ── PATELLA ────────
  { id:"patella", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M206,722 Q212,718 220,722 Q222,730 218,736 Q212,738 207,734 Q204,728 206,722 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.7, op:0.75},
      {d:"M300,722 Q306,718 314,722 Q316,730 312,736 Q306,738 301,734 Q298,728 300,722 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.7, op:0.75},
    ],
    cx:213, cy:728, label:"Patella" },

  // ── TIBIA ────────
  { id:"tibia", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M208,738 L210,775 Q212,777 215,775 L216,738 Q213,734 208,738 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.65},
      {d:"M312,738 L310,775 Q308,777 305,775 L304,738 Q307,734 312,738 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.65},
    ],
    cx:210, cy:756, label:"Tibia" },

  // ── FIBULA ────────
  { id:"fibula", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M218,738 L220,775 Q222,777 224,775 L224,738 Q222,734 218,738 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.6, op:0.55},
      {d:"M302,738 L300,775 Q298,777 296,775 L296,738 Q298,734 302,738 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.6, op:0.55},
    ],
    cx:222, cy:756, label:"Fibula" },

  // ── GASTROCNEMIUS ────────
  { id:"gastrocnemius", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M202,740 Q196,755 197,765 Q199,774 206,776 Q208,770 208,756 Q208,742 204,738 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.7, op:0.55},
      {d:"M318,740 Q324,755 323,765 Q321,774 314,776 Q312,770 312,756 Q312,742 316,738 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.7, op:0.55},
    ],
    cx:200, cy:758, label:"Gastrocnemius" },

  // ── HAMSTRINGS (visible as posterior, showing shadows) ────────
  { id:"hamstrings", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M194,580 Q188,610 188,660 Q190,700 195,720 Q200,724 202,720 Q197,700 197,660 Q198,610 200,582 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.5, op:0.3},
      {d:"M326,580 Q332,610 332,660 Q330,700 325,720 Q320,724 318,720 Q323,700 323,660 Q322,610 320,582 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.5, op:0.3},
    ],
    cx:192, cy:645, label:"Hamstrings" },

  // ── VERTEBRAL COLUMN ────────
  { id:"vertebral_column", system:"Skeletal", layer:"skeletal",
    paths:[
      // Cervical
      {d:"M256,148 L264,148 L265,175 L255,175 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.6, op:0.4},
      // Thoracic
      {d:"M255,178 L265,178 L266,295 L254,295 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.6, op:0.3},
      // Lumbar
      {d:"M254,298 L266,298 L267,365 L253,365 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.6, op:0.35},
      // Sacrum
      {d:"M252,368 Q256,365 264,365 Q268,368 268,385 Q264,390 256,390 Q252,390 252,385 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.6, op:0.4},
    ],
    cx:260, cy:260, label:"Vertebral Column" },

  // ── PITUITARY ────────
  { id:"pituitary", system:"Endocrine", layer:"organs",
    paths:[{d:"M257,80 Q260,77 263,80 Q265,83 263,86 Q260,88 257,86 Q255,83 257,80 Z", fill:"#78d4a0", stroke:"#50b078", sw:0.5, op:0.9}],
    cx:260, cy:82, label:"Pituitary" },

  // ── THYMUS ────────
  { id:"thymus", system:"Lymphatic", layer:"organs",
    paths:[{d:"M248,155 Q255,150 260,151 Q265,150 272,155 Q270,168 264,172 Q260,174 256,172 Q250,168 248,155 Z", fill:"#a078d4", stroke:"#7050b0", sw:0.7, op:0.7}],
    cx:260, cy:162, label:"Thymus" },

  // ── LYMPH NODES (cervical, axillary, inguinal) ────────
  { id:"lymph_nodes", system:"Lymphatic", layer:"organs",
    paths:[
      {d:"M242,138 Q238,135 236,138 Q235,143 239,145 Q243,143 242,138 Z", fill:"#a078d4", stroke:"#7050b0", sw:0.5, op:0.7},
      {d:"M278,138 Q282,135 284,138 Q285,143 281,145 Q277,143 278,138 Z", fill:"#a078d4", stroke:"#7050b0", sw:0.5, op:0.7},
      {d:"M168,255 Q164,252 163,256 Q163,261 167,262 Q171,260 168,255 Z", fill:"#a078d4", stroke:"#7050b0", sw:0.5, op:0.7},
      {d:"M352,255 Q356,252 357,256 Q357,261 353,262 Q349,260 352,255 Z", fill:"#a078d4", stroke:"#7050b0", sw:0.5, op:0.7},
      {d:"M195,520 Q191,517 190,521 Q190,526 194,527 Q198,525 195,520 Z", fill:"#a078d4", stroke:"#7050b0", sw:0.5, op:0.7},
      {d:"M325,520 Q329,517 330,521 Q330,526 326,527 Q322,525 325,520 Z", fill:"#a078d4", stroke:"#7050b0", sw:0.5, op:0.7},
    ],
    cx:242, cy:138, label:"Lymph Nodes" },

  // ── SPINAL CORD ────────
  { id:"spinal_cord", system:"Nervous", layer:"organs",
    paths:[
      {d:"M258,148 L262,148 L263,368 L257,368 Z", fill:"#d4a0e8", stroke:"#b080cc", sw:0.5, op:0.35},
    ],
    cx:260, cy:258, label:"Spinal Cord" },
];

// ───────────────────────────────────────────────────────
// POSTERIOR VIEW PARTS (simplified mirror + back-specific)
// ───────────────────────────────────────────────────────
const POSTERIOR_PARTS = [
  { id:"__body_outline", system:"",
    paths:[{d:"M180,30 Q200,20 260,20 Q320,20 340,30 L355,80 Q370,100 375,130 L378,160 Q385,200 382,230 L378,300 Q375,360 370,390 L368,440 Q365,480 360,500 L340,580 Q330,630 325,680 L320,740 310,760 Q295,775 260,775 Q225,775 210,760 L200,740 195,680 Q190,630 180,580 L160,500 Q155,480 152,440 L150,390 Q145,360 142,300 L138,230 Q135,200 142,160 L145,130 Q150,100 165,80 Z", fill:"#0a1628", stroke:"#2a4060", sw:1.5}], cx:260,cy:400,label:""},
  },
  { id:"skull", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M220,28 Q260,8 300,28 Q325,45 328,72 Q330,95 315,108 Q290,120 260,122 Q230,120 205,108 Q190,95 192,72 Q195,45 220,28 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:1, op:0.7}],
    cx:260, cy:65, label:"Skull (posterior)" },
  { id:"vertebral_column", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M253,148 L267,148 L268,180 L252,180 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.7},
      {d:"M252,183 L268,183 L268,295 L252,295 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.7},
      {d:"M253,298 L267,298 L267,365 L253,365 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.7},
      {d:"M251,368 Q260,363 269,368 L269,400 Q260,405 251,400 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.7},
    ],
    cx:260, cy:260, label:"Vertebral Column" },
  { id:"latissimus_dorsi", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M175,200 Q190,190 248,200 L248,310 Q230,325 210,320 Q190,310 175,290 Q162,270 175,200 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.6},
      {d:"M345,200 Q330,190 272,200 L272,310 Q290,325 310,320 Q330,310 345,290 Q358,270 345,200 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.6},
    ],
    cx:210, cy:255, label:"Latissimus Dorsi" },
  { id:"hamstrings", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M192,580 Q185,620 185,680 Q187,720 192,740 Q198,745 205,740 Q210,720 210,680 Q209,620 205,580 Q200,574 192,580 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
      {d:"M328,580 Q335,620 335,680 Q333,720 328,740 Q322,745 315,740 Q310,720 310,680 Q311,620 315,580 Q320,574 328,580 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
    ],
    cx:195, cy:655, label:"Hamstrings" },
  { id:"gastrocnemius", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M192,745 Q186,762 187,772 Q190,778 198,778 Q204,772 204,758 Q204,745 200,742 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
      {d:"M328,745 Q334,762 333,772 Q330,778 322,778 Q316,772 316,758 Q316,745 320,742 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
    ],
    cx:195, cy:762, label:"Gastrocnemius" },
  { id:"triceps", system:"Muscular", layer:"muscular",
    paths:[
      {d:"M135,225 Q128,248 128,285 Q130,315 137,330 Q142,325 143,285 Q143,248 142,225 Q139,220 135,225 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
      {d:"M385,225 Q392,248 392,285 Q390,315 383,330 Q378,325 377,285 Q377,248 378,225 Q381,220 385,225 Z", fill:"#e88a8a", stroke:"#c05050", sw:0.8, op:0.75},
    ],
    cx:132, cy:275, label:"Triceps Brachii" },
  { id:"kidneys", system:"Urinary", layer:"organs",
    paths:[
      {d:"M190,340 Q178,346 176,363 Q176,380 188,387 Q200,390 208,382 Q214,372 212,356 Q208,340 190,340 Z", fill:"#7a9ee8", stroke:"#5070c8", sw:0.8, op:0.8},
      {d:"M330,340 Q342,346 344,363 Q344,380 332,387 Q320,390 312,382 Q306,372 308,356 Q312,340 330,340 Z", fill:"#7a9ee8", stroke:"#5070c8", sw:0.8, op:0.8},
    ],
    cx:260, cy:363, label:"Kidneys (posterior)" },
];

// ───────────────────────────────────────────────────────
// LATERAL RIGHT VIEW
// ───────────────────────────────────────────────────────
const LATERAL_R_PARTS = [
  { id:"__body_outline", system:"",
    paths:[{d:"M220,30 Q250,15 280,25 Q300,40 305,70 L308,130 Q315,165 318,200 L316,260 Q318,320 316,380 L312,440 Q308,490 305,520 L298,580 Q290,640 288,700 L285,760 Q278,775 260,775 Q246,775 242,760 L240,700 Q238,640 228,580 L218,520 Q214,490 210,440 L206,380 Q204,320 204,260 L202,200 Q205,165 212,130 L215,70 Q218,40 220,30 Z", fill:"#0a1628", stroke:"#2a4060", sw:1.5}],
    cx:260, cy:400, label:"" },
  { id:"skull", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M218,28 Q255,10 290,28 Q310,48 312,75 Q308,100 292,114 Q270,126 252,124 Q230,120 215,105 Q205,90 207,68 Q210,45 218,28 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:1, op:0.7}],
    cx:258, cy:67, label:"Skull" },
  { id:"brain", system:"Nervous", layer:"organs",
    paths:[{d:"M220,30 Q255,15 288,30 Q306,48 308,72 Q306,95 292,108 Q270,120 252,118 Q232,115 218,102 Q208,88 210,66 Q213,44 220,30 Z", fill:"#d4a0e8", stroke:"#b080cc", sw:0.8, op:0.7}],
    cx:258, cy:67, label:"Brain" },
  { id:"ear", system:"Sensory", layer:"organs",
    paths:[{d:"M302,88 Q310,92 312,100 Q312,108 304,112 Q297,110 295,102 Q295,94 302,88 Z", fill:"#58d4c8", stroke:"#38b4a8", sw:0.6}],
    cx:303, cy:100, label:"Ear" },
  { id:"larynx", system:"Respiratory", layer:"organs",
    paths:[{d:"M250,126 Q258,122 268,126 L272,150 Q266,156 258,157 Q250,156 248,150 Z", fill:"#e8a05a", stroke:"#c07828", sw:0.7, op:0.8}],
    cx:258, cy:140, label:"Larynx" },
  { id:"vertebral_column", system:"Skeletal", layer:"skeletal",
    paths:[
      {d:"M242,126 Q248,122 254,126 L256,395 Q250,400 243,395 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.6},
    ],
    cx:248, cy:260, label:"Vertebral Column" },
  { id:"heart", system:"Cardiovascular", layer:"organs",
    paths:[{d:"M240,180 Q236,176 230,178 Q220,183 219,194 Q218,206 226,216 Q240,226 255,220 Q268,212 270,200 Q270,188 262,182 Q255,178 248,180 Q245,176 240,180 Z", fill:"#e85a5a", stroke:"#c03030", sw:1, op:0.85}],
    cx:244, cy:198, label:"Heart" },
  { id:"lungs", system:"Respiratory", layer:"organs",
    paths:[{d:"M265,162 Q278,158 290,168 Q300,182 300,215 Q298,250 286,268 Q272,278 258,272 Q248,264 248,248 L255,168 Z", fill:"#e8a05a", stroke:"#c07828", sw:0.8, op:0.65}],
    cx:272, cy:218, label:"Lung" },
  { id:"liver", system:"Digestive", layer:"organs",
    paths:[{d:"M254,295 Q268,290 280,296 Q290,305 290,330 Q288,350 274,360 Q258,365 246,356 Q234,344 234,320 Q236,300 254,295 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.75}],
    cx:262, cy:327, label:"Liver" },
  { id:"stomach", system:"Digestive", layer:"organs",
    paths:[{d:"M230,298 Q246,292 252,300 Q256,312 254,338 Q250,355 238,360 Q225,362 218,350 Q212,336 215,315 Q220,300 230,298 Z", fill:"#c8782a", stroke:"#a05010", sw:0.8, op:0.7}],
    cx:232, cy:328, label:"Stomach" },
  { id:"kidneys", system:"Urinary", layer:"organs",
    paths:[{d:"M244,350 Q252,344 262,348 Q270,356 268,374 Q264,388 252,390 Q240,390 234,378 Q230,364 238,354 Z", fill:"#7a9ee8", stroke:"#5070c8", sw:0.8, op:0.8}],
    cx:250, cy:367, label:"Kidney" },
  { id:"femur", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M245,530 Q240,570 240,630 Q242,670 246,690 Q250,695 256,690 Q260,670 260,630 Q258,570 254,530 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.65}],
    cx:248, cy:610, label:"Femur" },
  { id:"tibia", system:"Skeletal", layer:"skeletal",
    paths:[{d:"M244,698 L246,775 Q249,777 252,775 L254,698 Z", fill:"#b8cfe8", stroke:"#8ab0cc", sw:0.8, op:0.65}],
    cx:249, cy:736, label:"Tibia" },
];

// ═══════════════════════════════════════════════════════
// STATE + RENDER
// ═══════════════════════════════════════════════════════
let viewParts = { anterior: ANTERIOR_PARTS, posterior: POSTERIOR_PARTS, 'lateral-r': LATERAL_R_PARTS, 'lateral-l': LATERAL_R_PARTS, superior: ANTERIOR_PARTS };

function getVisibleParts() {
  const parts = viewParts[currentView] || ANTERIOR_PARTS;
  return parts.filter(p => {
    if (currentSystem !== "All" && p.system && p.system !== currentSystem) return false;
    if (showLayer !== "all" && p.layer && p.layer !== showLayer && p.id !== "__body_outline") return false;
    return true;
  });
}

function renderSVG() {
  const svg = document.getElementById("anatomy-svg");
  svg.innerHTML = "";

  // Transform group for zoom/pan
  const g = document.createElementNS("http://www.w3.org/2000/svg","g");
  g.setAttribute("transform",`translate(${panX},${panY}) scale(${zoom})`);

  const parts = getVisibleParts();

  parts.forEach(part => {
    if (!part.paths || part.paths.length === 0) return;
    const sys = ANATOMY_DB[part.id];
    const isSelected = selectedPart === part.id;
    const isInteractive = !!sys;

    part.paths.forEach(path => {
      const el = document.createElementNS("http://www.w3.org/2000/svg","path");
      el.setAttribute("d", path.d);

      let fill = path.fill || "#1e3a5a";
      let stroke = path.stroke || "#2a6496";
      let opacity = path.op || 1;

      if (isSelected && isInteractive) {
        fill = lighten(fill, 1.5);
        stroke = "#60b3e8";
        opacity = Math.min(opacity + 0.2, 1);
      }

      el.setAttribute("fill", fill);
      el.setAttribute("stroke", stroke);
      el.setAttribute("stroke-width", (path.sw || 1) / zoom);
      el.setAttribute("opacity", opacity);

      if (isInteractive) {
        el.style.cursor = "pointer";
        el.classList.add("anatomy-part");
        if (isSelected) el.classList.add("highlighted");

        el.addEventListener("mouseenter", (e) => {
          showTooltip(e, sys.name);
          if (!isSelected) el.setAttribute("opacity", Math.min(opacity + 0.25, 1));
        });
        el.addEventListener("mouseleave", () => {
          hideTooltip();
          if (!isSelected) el.setAttribute("opacity", opacity);
        });
        el.addEventListener("mousemove", moveTooltip);
        el.addEventListener("click", (e) => {
          e.stopPropagation();
          selectPart(part.id);
        });
      }

      g.appendChild(el);
    });

    // Label
    if (showLabels && isInteractive && sys && part.cx && part.label) {
      drawLabel(g, part.cx, part.cy - 10, part.label, sys.color || "#60b3e8");
    }
  });

  svg.appendChild(g);
}

function lighten(hex, factor) {
  try {
    const r = parseInt(hex.slice(1,3),16);
    const gr = parseInt(hex.slice(3,5),16);
    const b = parseInt(hex.slice(5,7),16);
    const lr = Math.min(255, Math.round(r * factor));
    const lg = Math.min(255, Math.round(gr * factor));
    const lb = Math.min(255, Math.round(b * factor));
    return `#${lr.toString(16).padStart(2,'0')}${lg.toString(16).padStart(2,'0')}${lb.toString(16).padStart(2,'0')}`;
  } catch(e) { return hex; }
}

function drawLabel(g, x, y, text, color) {
  const t = document.createElementNS("http://www.w3.org/2000/svg","text");
  t.setAttribute("x", x);
  t.setAttribute("y", y);
  t.setAttribute("text-anchor","middle");
  t.setAttribute("font-size", Math.round(9 / zoom));
  t.setAttribute("font-family","'Segoe UI',sans-serif");
  t.setAttribute("font-weight","600");
  t.setAttribute("fill", color || "#a0bcd4");
  t.setAttribute("paint-order","stroke");
  t.setAttribute("stroke","#060912");
  t.setAttribute("stroke-width", 2 / zoom);
  t.textContent = text;
  g.appendChild(t);
}

// ─── TOOLTIP ────────────────────────────────────────────
const tooltip = document.getElementById("tooltip");
function showTooltip(e, name) { tooltip.textContent = name; tooltip.style.display = "block"; moveTooltip(e); }
function hideTooltip() { tooltip.style.display = "none"; }
function moveTooltip(e) {
  const viewer = document.getElementById("viewer");
  const rect = viewer.getBoundingClientRect();
  let x = e.clientX - rect.left + 14;
  let y = e.clientY - rect.top - 30;
  if (x + 180 > rect.width) x = e.clientX - rect.left - 180;
  tooltip.style.left = x+"px";
  tooltip.style.top  = y+"px";
}

// ─── SELECT PART ────────────────────────────────────────
function selectPart(id) {
  selectedPart = id;
  highlightList(id);
  showDetail(id);
  renderSVG();
}

function highlightList(id) {
  document.querySelectorAll(".part-item").forEach(el => {
    el.classList.toggle("selected", el.dataset.id === id);
    if (el.dataset.id === id) el.scrollIntoView({behavior:"smooth",block:"nearest"});
  });
}

function showDetail(id) {
  const d = ANATOMY_DB[id];
  if (!d) return;

  document.getElementById("detail-icon").textContent = d.icon || "🔬";
  document.getElementById("detail-name").textContent = d.name;
  document.getElementById("detail-latin").textContent = d.latin;
  document.getElementById("detail-empty").style.display = "none";

  const content = document.getElementById("detail-content");
  content.style.display = "block";

  const comps = (d.components || []).map(c => `<span class="detail-tag">${c}</span>`).join("");
  const clinTags = (d.clinical || "").split(",").map(c => `<span class="detail-tag" style="background:#200a0a;border-color:#5a1010;color:#e88080;">${c.trim()}</span>`).join("");

  content.innerHTML = `
    <div class="detail-section">
      <h4>Overview</h4>
      <p>${d.desc}</p>
    </div>
    <div class="detail-section">
      <h4>Function</h4>
      <p>${d.function}</p>
    </div>
    <div class="detail-section">
      <h4>Key Components</h4>
      <div>${comps}</div>
    </div>
    <div class="detail-section">
      <div class="detail-row"><span>System</span><span>${d.system}</span></div>
      <div class="detail-row"><span>Size / Weight</span><span>${d.size || 'Variable'}</span></div>
      <div class="detail-row"><span>Blood Supply</span><span style="font-size:10px;max-width:160px;text-align:right;line-height:1.4;">${d.blood_supply || '—'}</span></div>
      <div class="detail-row"><span>Innervation</span><span style="font-size:10px;max-width:160px;text-align:right;line-height:1.4;">${d.innervation || '—'}</span></div>
    </div>
    <div class="detail-section">
      <h4>Clinical Relevance</h4>
      <div>${clinTags}</div>
    </div>
  `;
}

// ═══════════════════════════════════════════════════════
// CONTROLS
// ═══════════════════════════════════════════════════════
function setView(v) {
  currentView = v;
  selectedPart = null;
  document.querySelectorAll(".orient-btn").forEach(b => {
    b.classList.toggle("active", b.textContent.toLowerCase().replace(" ","").includes(v.replace("-","").toLowerCase().substring(0,3)));
  });
  renderSVG();
}

function adjustZoom(delta) {
  zoom = Math.max(0.4, Math.min(3.5, zoom + delta));
  document.getElementById("zoom-val").textContent = Math.round(zoom*100)+"%";
  renderSVG();
}

function resetView() {
  zoom = 1; panX = 0; panY = 0;
  document.getElementById("zoom-val").textContent = "100%";
  renderSVG();
}

function toggleLabels() {
  showLabels = !showLabels;
  const btn = document.getElementById("lbl-btn");
  btn.textContent = showLabels ? "Labels ON" : "Labels OFF";
  btn.classList.toggle("active", showLabels);
  renderSVG();
}

function cycleLayer() {
  layerIdx = (layerIdx + 1) % layerKeys.length;
  showLayer = layerKeys[layerIdx];
  const btn = document.getElementById("layers-btn");
  btn.textContent = layerNames[layerIdx];
  btn.classList.toggle("active", showLayer !== "all");
  renderSVG();
}

// ─── PAN ────────────────────────────────────────────────
const svgEl = document.getElementById("anatomy-svg");
svgEl.addEventListener("mousedown", e => { isDragging = true; dragStartX = e.clientX - panX; dragStartY = e.clientY - panY; });
window.addEventListener("mousemove", e => { if (isDragging) { panX = e.clientX - dragStartX; panY = e.clientY - dragStartY; renderSVG(); }});
window.addEventListener("mouseup", () => { isDragging = false; });
svgEl.addEventListener("wheel", e => { e.preventDefault(); adjustZoom(e.deltaY < 0 ? 0.12 : -0.12); }, {passive:false});
svgEl.addEventListener("click", e => {
  if (e.target === svgEl || e.target.closest("g") === svgEl.querySelector("g")) { /* clicking body outline — deselect */ }
});

// ─── TOUCH ──────────────────────────────────────────────
let lastTouchDist = null;
svgEl.addEventListener("touchstart", e => {
  if (e.touches.length === 1) { isDragging = true; dragStartX = e.touches[0].clientX - panX; dragStartY = e.touches[0].clientY - panY; }
  if (e.touches.length === 2) { lastTouchDist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY); }
}, {passive:true});
svgEl.addEventListener("touchmove", e => {
  if (e.touches.length === 1 && isDragging) { panX = e.touches[0].clientX - dragStartX; panY = e.touches[0].clientY - dragStartY; renderSVG(); }
  if (e.touches.length === 2 && lastTouchDist) {
    const dist = Math.hypot(e.touches[0].clientX - e.touches[1].clientX, e.touches[0].clientY - e.touches[1].clientY);
    adjustZoom((dist - lastTouchDist) * 0.005);
    lastTouchDist = dist;
  }
}, {passive:true});
svgEl.addEventListener("touchend", () => { isDragging = false; lastTouchDist = null; });

// ═══════════════════════════════════════════════════════
// BUILD LEFT PANEL
// ═══════════════════════════════════════════════════════
function buildSystemTabs() {
  const container = document.getElementById("system-tabs");
  Object.keys(SYSTEMS).forEach(sys => {
    const btn = document.createElement("button");
    btn.className = "sys-btn" + (sys === currentSystem ? " active" : "");
    btn.textContent = sys === "All" ? "All" : sys.substring(0,4);
    btn.title = sys;
    btn.onclick = () => {
      currentSystem = sys;
      document.querySelectorAll(".sys-btn").forEach(b => b.classList.toggle("active", b.title === sys));
      buildPartList();
      renderSVG();
    };
    container.appendChild(btn);
  });
}

function buildPartList() {
  const container = document.getElementById("part-list");
  container.innerHTML = "";
  const filtered = Object.entries(ANATOMY_DB).filter(([id, d]) => currentSystem === "All" || d.system === currentSystem);
  filtered.sort((a,b) => a[1].system.localeCompare(b[1].system) || a[1].name.localeCompare(b[1].name));

  let lastSys = "";
  filtered.forEach(([id, d]) => {
    if (d.system !== lastSys) {
      const header = document.createElement("div");
      header.style.cssText = "font-size:9px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#2a6496;padding:8px 8px 4px;";
      header.textContent = d.system;
      container.appendChild(header);
      lastSys = d.system;
    }
    const item = document.createElement("div");
    item.className = "part-item" + (selectedPart === id ? " selected" : "");
    item.dataset.id = id;
    const dot = document.createElement("div");
    dot.className = "part-dot";
    dot.style.background = d.color || SYSTEMS[d.system]?.color || "#60b3e8";
    item.appendChild(dot);
    const label = document.createElement("span");
    label.textContent = d.name;
    item.appendChild(label);
    item.addEventListener("click", () => selectPart(id));
    container.appendChild(item);
  });
}

// ═══════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════
buildSystemTabs();
buildPartList();
renderSVG();

// keyboard shortcuts
document.addEventListener("keydown", e => {
  if (e.key === "+" || e.key === "=") adjustZoom(0.12);
  if (e.key === "-") adjustZoom(-0.12);
  if (e.key === "r" || e.key === "R") resetView();
  if (e.key === "l" || e.key === "L") toggleLabels();
  if (e.key === "1") setView("anterior");
  if (e.key === "2") setView("posterior");
  if (e.key === "3") setView("lateral-r");
  if (e.key === "4") setView("lateral-l");
});
</script>
</body>
</html>
"""


def anatomy_3d_page(theme):
    st.markdown(
        f"<h2 style='color:{theme['text']};font-family:\"Bricolage Grotesque\",sans-serif;"
        f"font-size:1.6rem;font-weight:900;margin-bottom:0.3rem;'>🫁 3D Anatomy Atlas</h2>",
        unsafe_allow_html=True
    )
    st.markdown(
        f"<p style='color:{theme['subtext']};font-size:0.85rem;margin-bottom:1rem;'>"
        "Interactive atlas · All body systems · Click any structure for details</p>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <style>
    .stApp iframe { border-radius: 16px; border: 1px solid rgba(42,100,150,0.3); }
    </style>
    """, unsafe_allow_html=True)

    components.html(ANATOMY_HTML, height=700, scrolling=False)

    with st.expander("⌨️ Keyboard Shortcuts & Controls"):
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("**Views**\n\n`1` Anterior · `2` Posterior · `3` Right Lateral · `4` Left")
        with c2:
            st.markdown("**Zoom**\n\n`+` Zoom in · `-` Zoom out · `R` Reset view")
        with c3:
            st.markdown("**Display**\n\n`L` Toggle labels · Mouse drag to pan · Scroll to zoom")
