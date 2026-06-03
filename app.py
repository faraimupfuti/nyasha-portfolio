import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Nyasha Mpofu | Electrical Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── Root Variables ── */
:root {
    --bg-dark:      #0a0f0d;
    --bg-card:      #111a14;
    --bg-card2:     #162019;
    --accent-lime:  #b5f23e;
    --accent-gold:  #f0c040;
    --accent-sky:   #5de3c8;
    --text-primary: #e8f0e9;
    --text-muted:   #7a9e80;
    --border:       #1e3523;
}

/* ── Base ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-primary);
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: var(--bg-card) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

/* Main area */
.main .block-container {
    padding: 2rem 2.5rem 3rem;
    max-width: 1100px;
}

/* ── Hero Banner ── */
.hero-wrapper {
    background: linear-gradient(135deg, #0d1f12 0%, #0a1a0e 50%, #071208 100%);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 3rem 3.5rem;
    position: relative;
    overflow: hidden;
    margin-bottom: 2rem;
}
.hero-wrapper::before {
    content: '';
    position: absolute;
    top: -80px; right: -80px;
    width: 320px; height: 320px;
    background: radial-gradient(circle, rgba(181,242,62,0.12) 0%, transparent 65%);
    border-radius: 50%;
}
.hero-wrapper::after {
    content: '';
    position: absolute;
    bottom: -60px; left: 30%;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(93,227,200,0.08) 0%, transparent 65%);
    border-radius: 50%;
}
.hero-tag {
    display: inline-block;
    background: rgba(181,242,62,0.12);
    border: 1px solid rgba(181,242,62,0.3);
    color: var(--accent-lime) !important;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    padding: 0.3rem 0.9rem;
    border-radius: 100px;
    margin-bottom: 1.1rem;
}
.hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.2rem, 5vw, 3.6rem);
    font-weight: 800;
    line-height: 1.05;
    margin: 0 0 0.5rem;
    color: var(--text-primary);
}
.hero-name span { color: var(--accent-lime); }
.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.15rem;
    font-weight: 500;
    color: var(--text-muted);
    margin-bottom: 1.4rem;
}
.hero-summary {
    font-size: 0.96rem;
    line-height: 1.75;
    color: #a8c4aa;
    max-width: 680px;
    margin-bottom: 2rem;
}
.hero-pills { display: flex; flex-wrap: wrap; gap: 0.6rem; }
.pill {
    background: var(--bg-card2);
    border: 1px solid var(--border);
    border-radius: 100px;
    padding: 0.35rem 1rem;
    font-size: 0.8rem;
    color: var(--text-muted);
    font-weight: 500;
}
.pill-highlight {
    background: rgba(93,227,200,0.1);
    border-color: rgba(93,227,200,0.3);
    color: var(--accent-sky) !important;
}

/* ── Section Headings ── */
.section-label {
    font-size: 0.7rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--accent-lime);
    font-weight: 700;
    margin-bottom: 0.4rem;
}
.section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 1.5rem;
    line-height: 1.2;
}

/* ── Cards ── */
.card {
    background: var(--bg-card);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.1rem;
    position: relative;
    transition: border-color 0.2s;
}
.card:hover { border-color: rgba(181,242,62,0.35); }
.card-accent-bar {
    position: absolute;
    left: 0; top: 18px; bottom: 18px;
    width: 3px;
    border-radius: 0 3px 3px 0;
    background: var(--accent-lime);
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.2rem;
}
.card-subtitle {
    font-size: 0.85rem;
    color: var(--accent-lime);
    font-weight: 600;
    margin-bottom: 0.15rem;
}
.card-meta {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin-bottom: 0.9rem;
}
.card-body {
    font-size: 0.88rem;
    color: #9ab89d;
    line-height: 1.7;
}
.card-body ul { margin: 0; padding-left: 1.3rem; }
.card-body ul li { margin-bottom: 0.4rem; }

/* ── Skill Chips ── */
.skills-grid { display: flex; flex-wrap: wrap; gap: 0.55rem; margin-top: 0.7rem; }
.skill-chip {
    background: var(--bg-card2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 0.4rem 0.9rem;
    font-size: 0.8rem;
    color: var(--text-muted);
    font-weight: 500;
}
.skill-chip.lime {
    background: rgba(181,242,62,0.08);
    border-color: rgba(181,242,62,0.25);
    color: var(--accent-lime);
}
.skill-chip.sky {
    background: rgba(93,227,200,0.08);
    border-color: rgba(93,227,200,0.25);
    color: var(--accent-sky);
}
.skill-chip.gold {
    background: rgba(240,192,64,0.08);
    border-color: rgba(240,192,64,0.25);
    color: var(--accent-gold);
}

/* ── Project Feature Card ── */
.project-card {
    background: linear-gradient(135deg, #0f1f13, #0d1a11);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.2rem;
    position: relative;
    overflow: hidden;
}
.project-card::before {
    content: '⚡';
    position: absolute;
    right: 1.5rem; top: 1.2rem;
    font-size: 3rem;
    opacity: 0.06;
}
.project-badge {
    display: inline-block;
    background: rgba(240,192,64,0.12);
    border: 1px solid rgba(240,192,64,0.3);
    color: var(--accent-gold);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    padding: 0.25rem 0.8rem;
    border-radius: 100px;
    margin-bottom: 0.8rem;
}
.project-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.35rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.7rem;
}
.project-desc {
    font-size: 0.9rem;
    color: #9ab89d;
    line-height: 1.7;
    margin-bottom: 1.2rem;
}

/* ── Stat Boxes ── */
.stats-row { display: flex; flex-wrap: wrap; gap: 0.8rem; margin: 1rem 0; }
.stat-box {
    background: var(--bg-card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.8rem 1.2rem;
    min-width: 110px;
    flex: 1;
    text-align: center;
}
.stat-val {
    font-family: 'Syne', sans-serif;
    font-size: 1.5rem;
    font-weight: 800;
    color: var(--accent-lime);
    display: block;
}
.stat-lbl {
    font-size: 0.72rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.08em;
    display: block;
    margin-top: 0.1rem;
}

/* ── Tech Spec Table ── */
.spec-table { width: 100%; border-collapse: collapse; margin-top: 0.8rem; }
.spec-table tr { border-bottom: 1px solid var(--border); }
.spec-table tr:last-child { border-bottom: none; }
.spec-table td {
    padding: 0.55rem 0.5rem;
    font-size: 0.85rem;
}
.spec-table td:first-child {
    color: var(--text-muted);
    font-weight: 500;
    width: 45%;
}
.spec-table td:last-child { color: var(--text-primary); font-weight: 600; }

/* ── Contact Bar ── */
.contact-row { display: flex; flex-wrap: wrap; gap: 0.7rem; margin-top: 0.5rem; }
.contact-chip {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    background: var(--bg-card2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.55rem 1.1rem;
    font-size: 0.85rem;
    color: var(--text-muted);
    text-decoration: none;
}

/* ── Sidebar Nav ── */
.nav-item {
    display: block;
    padding: 0.6rem 1rem;
    border-radius: 8px;
    font-size: 0.9rem;
    font-weight: 500;
    color: var(--text-muted);
    cursor: pointer;
    margin-bottom: 0.15rem;
    transition: background 0.15s;
    text-decoration: none;
}
.nav-item:hover, .nav-item.active {
    background: rgba(181,242,62,0.1);
    color: var(--accent-lime);
}

/* ── Divider ── */
.divider {
    border: none;
    border-top: 1px solid var(--border);
    margin: 1.8rem 0;
}

/* Streamlit overrides */
.stButton > button {
    background: var(--accent-lime) !important;
    color: #0a0f0d !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.55rem 1.5rem !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }
.stDownloadButton > button {
    background: transparent !important;
    border: 1px solid var(--accent-lime) !important;
    color: var(--accent-lime) !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
}
h1, h2, h3, h4 { color: var(--text-primary) !important; }
.stSelectbox label, .stRadio label { color: var(--text-muted) !important; }
[data-testid="stMetric"] { background: var(--bg-card2); border-radius: 10px; padding: 0.8rem; border: 1px solid var(--border); }
[data-testid="stMetricValue"] { color: var(--accent-lime) !important; font-family: 'Syne', sans-serif !important; }
[data-testid="stMetricLabel"] { color: var(--text-muted) !important; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1.5rem 0 1rem;'>
        <div style='width:80px;height:80px;border-radius:50%;background:linear-gradient(135deg,#b5f23e,#5de3c8);
                    margin:0 auto 1rem;display:flex;align-items:center;justify-content:center;
                    font-size:2rem;font-family:Syne,sans-serif;font-weight:800;color:#0a0f0d;'>N</div>
        <div style='font-family:Syne,sans-serif;font-size:1.05rem;font-weight:700;color:#e8f0e9;'>Nyasha Mpofu</div>
        <div style='font-size:0.78rem;color:#7a9e80;margin-top:0.2rem;'>Junior Electrical Engineer</div>
        <div style='font-size:0.75rem;color:#5de3c8;margin-top:0.3rem;'>⚡ Renewables & Power Systems</div>
    </div>
    <hr style='border:none;border-top:1px solid #1e3523;margin:0.5rem 0 1rem;'>
    """, unsafe_allow_html=True)

    page = st.radio(
        "Navigation",
        ["🏠  About", "💼  Experience", "🎓  Education", "🔧  Skills", "🌱  Projects", "📬  Contact"],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border:none;border-top:1px solid #1e3523;margin:1.5rem 0 1rem;'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.72rem;color:#4a7a50;padding:0 0.5rem;line-height:1.6;'>
        <b style='color:#7a9e80;'>ECSA Candidate Engineer</b><br>
        Reg. No. 2025209292<br><br>
        <b style='color:#7a9e80;'>SAQA Evaluation</b><br>
        NQF Level 8
    </div>
    """, unsafe_allow_html=True)

    # Download CV button placeholder
    st.markdown("<div style='margin-top:1.5rem;'>", unsafe_allow_html=True)
    cv_text = """NYASHA MPOFU
Junior Electrical Engineer
nyashampofu1@gmail.com | +26378 685 8523 | Harare, Zimbabwe

PROFESSIONAL SUMMARY
Electrical Engineering graduate with experience in commercial-scale renewable energy systems,
power distribution, and electrical design support. Proven exposure to solar PV and Battery Energy
Storage Systems (BESS), including commissioning, maintenance, and technical documentation.
Registered ECSA Candidate Engineer with a SAQA-evaluated qualification (NQF Level 8).

EDUCATION
BSc (Hons) Electrical Engineering | University of Zimbabwe | 2024
Classification: Second Class Upper Division (2.1) | SAQA: NQF Level 8

PROFESSIONAL REGISTRATION
ECSA Candidate Engineer (PrEng pathway) | Reg. 2025209292

EXPERIENCE
Power Life Energy — Junior Electrical Engineer (Feb 2026 – Present)
- Maintenance and fault diagnosis on 30kW–150kW inverter systems (Huawei, Sunsynk, Livoltek)
- Commissioning of solar PV and BESS systems
- Installation of ~150m of 2×120mm² 4-core LV cables
- Technical documentation: BOQs and solution proposals
- Produced AutoCAD electrical drawings and SLDs

Zimbabwe Electricity Transmission and Distribution Company (ZETDC)
Engineering Attaché (Nov 2022 – Oct 2023)
- Troubleshooting and maintenance of distribution systems, transformers, switchgear
- Site inspections for electrical safety compliance
- Motor control, circuit breakers, power system protection

KEY SKILLS
- Power system studies: load flow, short circuit, motor starting (ETAP)
- Solar PV and BESS system design and commissioning
- AutoCAD Electrical | ETAP (self-study) | MS Office
- Protection principles: relays, circuit breakers
- Technical documentation and reporting
"""
    st.download_button(
        "⬇ Download CV",
        data=cv_text,
        file_name="Nyasha_Mpofu_CV.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: ABOUT
# ═══════════════════════════════════════════════════════════════
if "About" in page:
    # Hero
    st.markdown("""
    <div class="hero-wrapper">
        <div class="hero-tag">⚡ Open to Opportunities</div>
        <div class="hero-name">Nyasha <span>Mpofu</span></div>
        <div class="hero-title">Junior Electrical Engineer — Renewables & Power Systems</div>
        <div class="hero-summary">
            Electrical Engineering graduate with hands-on experience in commercial-scale solar PV and
            Battery Energy Storage Systems. Registered ECSA Candidate Engineer on the Professional
            Engineer (Pr Eng) pathway, with a SAQA-recognised NQF Level 8 qualification. Passionate
            about advancing Zimbabwe's renewable energy transition.
        </div>
        <div class="hero-pills">
            <span class="pill pill-highlight">📍 Harare, Zimbabwe</span>
            <span class="pill">Solar PV &amp; BESS</span>
            <span class="pill">AutoCAD Electrical</span>
            <span class="pill">ETAP Power Analysis</span>
            <span class="pill">ECSA Candidate Eng.</span>
            <span class="pill">Willing to Relocate</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Experience", "1+ yr", "Active")
    with col2:
        st.metric("Systems Range", "30–160 kW", "Commercial")
    with col3:
        st.metric("Degree Class", "2.1", "Upper Second")
    with col4:
        st.metric("Registration", "ECSA", "Candidate Eng.")

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # What I Do
    st.markdown('<div class="section-label">What I Do</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Core Competencies</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar"></div>
            <div style='font-size:1.6rem;margin-bottom:0.7rem;'>☀️</div>
            <div class="card-title">Solar PV & BESS</div>
            <div class="card-body">Commissioning, functional testing, and performance verification of commercial
            solar PV systems from 30 kW to 160 kW. Hands-on with Huawei, Sunsynk, and Livoltek inverters.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
            <div style='font-size:1.6rem;margin-bottom:0.7rem;'>📐</div>
            <div class="card-title">Electrical Design</div>
            <div class="card-body">Production of Single Line Diagrams, solar PV layouts, and electrical drawings
            using AutoCAD 2021. Power system studies including load flow and short circuit analysis in ETAP.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-gold);"></div>
            <div style='font-size:1.6rem;margin-bottom:0.7rem;'>🔌</div>
            <div class="card-title">Power Distribution</div>
            <div class="card-body">LV cable installation, transformer maintenance, switchgear operation,
            and distribution system troubleshooting gained at ZETDC on national grid infrastructure.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div class="section-label">Professional Status</div>
    <div style='font-family:Syne,sans-serif;font-size:1.1rem;font-weight:600;color:#e8f0e9;margin-bottom:1rem;'>
        ECSA Candidate Engineer — Pr Eng Pathway
    </div>
    <div style='font-size:0.9rem;color:#9ab89d;line-height:1.75;max-width:720px;'>
        Registered with the Engineering Council of South Africa (ECSA) as a Candidate Engineer
        (Registration No. <b style='color:#b5f23e;'>2025209292</b>), working toward full Professional Engineer
        (Pr Eng) registration. Academic qualifications have been evaluated by SAQA at <b style='color:#b5f23e;'>NQF Level 8</b>,
        equivalent to an Honours-level degree internationally.
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: EXPERIENCE
# ═══════════════════════════════════════════════════════════════
elif "Experience" in page:
    st.markdown('<div class="section-label">Career History</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

    # Power Life Energy
    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-accent-bar"></div>
        <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;align-items:flex-start;">
            <div>
                <div class="card-title">Junior Electrical Engineer</div>
                <div class="card-subtitle">Power Life Energy</div>
                <div class="card-meta">📅 February 2026 – Present &nbsp;|&nbsp; 📍 Zimbabwe</div>
            </div>
            <span style="background:rgba(181,242,62,0.12);border:1px solid rgba(181,242,62,0.3);
                         color:#b5f23e;font-size:0.72rem;font-weight:700;letter-spacing:0.1em;
                         text-transform:uppercase;padding:0.3rem 0.9rem;border-radius:100px;height:fit-content;">
                Current Role
            </span>
        </div>
        <div class="card-body">
            <ul>
                <li>Performed <b>maintenance and fault diagnosis</b> on commercial-scale inverter systems (30 kW – 150 kW),
                    including Huawei, Sunsynk, and Livoltek platforms across multiple commercial installations.</li>
                <li>Participated in <b>commissioning and testing</b> of solar PV and BESS systems — conducting functional
                    testing, system validation, performance verification, and liaising with consulting engineers.</li>
                <li>Contributed to electrical infrastructure installation, including approximately <b>150 m of 2 × 120 mm²
                    4-core LV cables</b> from transformer to load points, with involvement in routing, termination,
                    and compliance with installation standards.</li>
                <li>Prepared <b>technical documentation</b> including Bills of Quantities (BOQs) and tailored solution
                    proposals based on client load profiles and operational requirements.</li>
                <li>Supported <b>tendering processes</b> through site assessments, data collection, and technical input
                    into system design and cost estimation.</li>
                <li>Produced <b>electrical drawings using AutoCAD 2021</b>, including solar PV layouts and Single Line
                    Diagrams (SLDs) for commercial-scale systems.</li>
            </ul>
        </div>
        <div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:0.5rem;">
            <span class="skill-chip lime">Solar PV</span>
            <span class="skill-chip lime">BESS</span>
            <span class="skill-chip sky">AutoCAD 2021</span>
            <span class="skill-chip sky">SLD Design</span>
            <span class="skill-chip gold">Commissioning</span>
            <span class="skill-chip gold">BOQ Preparation</span>
            <span class="skill-chip">Huawei Inverters</span>
            <span class="skill-chip">Sunsynk</span>
            <span class="skill-chip">LV Cable Installation</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ZETDC
    st.markdown("""
    <div class="card">
        <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
        <div>
            <div class="card-title">Engineering Attaché</div>
            <div class="card-subtitle" style="color:var(--accent-sky);">Zimbabwe Electricity Transmission and Distribution Company (ZETDC)</div>
            <div class="card-meta">📅 November 2022 – October 2023 &nbsp;|&nbsp; 📍 Zimbabwe</div>
        </div>
        <div class="card-body">
            <ul>
                <li>Assisted in <b>troubleshooting and maintaining electrical distribution systems</b>, including
                    transformers and switchgear across the national grid.</li>
                <li>Conducted <b>site inspections</b> to ensure compliance with electrical safety regulations
                    and industrial standards.</li>
                <li>Gained hands-on experience with <b>motor control, circuit breakers, and power system protection</b>
                    in a real-world utility environment.</li>
                <li>Provided <b>technical support</b> to engineering teams, ensuring stable power supply
                    for industrial consumers.</li>
                <li>Participated in <b>safety audits</b> and contributed to improving operational efficiency.</li>
            </ul>
        </div>
        <div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:0.5rem;">
            <span class="skill-chip sky">Power Distribution</span>
            <span class="skill-chip sky">Transformer Maintenance</span>
            <span class="skill-chip">Motor Control</span>
            <span class="skill-chip">Circuit Breakers</span>
            <span class="skill-chip">Safety Audits</span>
            <span class="skill-chip">Protection Systems</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">Timeline Overview</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="position:relative;padding-left:1.8rem;margin-top:1rem;">
        <div style="position:absolute;left:0.4rem;top:0;bottom:0;width:2px;background:var(--border);border-radius:2px;"></div>
        <div style="position:relative;margin-bottom:1.8rem;">
            <div style="position:absolute;left:-1.4rem;top:0.3rem;width:10px;height:10px;border-radius:50%;
                        background:var(--accent-lime);border:2px solid var(--bg-dark);"></div>
            <div style="font-family:Syne,sans-serif;font-size:0.95rem;font-weight:700;color:#e8f0e9;">Feb 2026 – Present</div>
            <div style="font-size:0.85rem;color:#7a9e80;">Junior Electrical Engineer · Power Life Energy</div>
        </div>
        <div style="position:relative;margin-bottom:1.8rem;">
            <div style="position:absolute;left:-1.4rem;top:0.3rem;width:10px;height:10px;border-radius:50%;
                        background:var(--accent-gold);border:2px solid var(--bg-dark);"></div>
            <div style="font-family:Syne,sans-serif;font-size:0.95rem;font-weight:700;color:#e8f0e9;">Jul 2024</div>
            <div style="font-size:0.85rem;color:#7a9e80;">BSc (Hons) Electrical Engineering Awarded · University of Zimbabwe</div>
        </div>
        <div style="position:relative;margin-bottom:1.8rem;">
            <div style="position:absolute;left:-1.4rem;top:0.3rem;width:10px;height:10px;border-radius:50%;
                        background:var(--accent-sky);border:2px solid var(--bg-dark);"></div>
            <div style="font-family:Syne,sans-serif;font-size:0.95rem;font-weight:700;color:#e8f0e9;">Nov 2022 – Oct 2023</div>
            <div style="font-size:0.85rem;color:#7a9e80;">Engineering Attaché · ZETDC</div>
        </div>
        <div style="position:relative;">
            <div style="position:absolute;left:-1.4rem;top:0.3rem;width:10px;height:10px;border-radius:50%;
                        background:var(--border);border:2px solid var(--bg-dark);"></div>
            <div style="font-family:Syne,sans-serif;font-size:0.95rem;font-weight:700;color:#e8f0e9;">Aug 2020</div>
            <div style="font-size:0.85rem;color:#7a9e80;">Commenced BSc Electrical Engineering · University of Zimbabwe</div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: EDUCATION
# ═══════════════════════════════════════════════════════════════
elif "Education" in page:
    st.markdown('<div class="section-label">Academic Background</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Education & Qualifications</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-accent-bar"></div>
        <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:0.5rem;">
            <div>
                <div class="card-title">BSc (Hons) Electrical Engineering</div>
                <div class="card-subtitle">University of Zimbabwe</div>
                <div class="card-meta">📅 August 2020 – July 2024 &nbsp;|&nbsp; 🎓 Awarded 12 July 2024</div>
            </div>
            <div style="text-align:right;">
                <div style="font-family:Syne,sans-serif;font-size:1.6rem;font-weight:800;color:var(--accent-lime);">2.1</div>
                <div style="font-size:0.72rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;">Upper Second</div>
            </div>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:1.2rem;margin:1.2rem 0;">
            <div><span style="color:var(--text-muted);font-size:0.8rem;">Classification</span><br>
                 <b style="color:var(--text-primary);">Second Class Upper Division (2.1)</b></div>
            <div><span style="color:var(--text-muted);font-size:0.8rem;">SAQA Evaluation</span><br>
                 <b style="color:var(--accent-lime);">NQF Level 8</b></div>
            <div><span style="color:var(--text-muted);font-size:0.8rem;">Research Focus</span><br>
                 <b style="color:var(--text-primary);">Software Engineering</b></div>
            <div><span style="color:var(--text-muted);font-size:0.8rem;">Project Title</span><br>
                 <b style="color:var(--text-primary);">ML for Predictive Maintenance of ZETDCS 33kV Feeders</b></div>
        </div>
        <div style="margin-top:1rem;">
            <div style="font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.7rem;font-weight:600;">Key Modules Completed</div>
            <div style="display:flex;flex-wrap:wrap;gap:0.45rem;">
                <span class="skill-chip lime">Power Systems 1</span>
                <span class="skill-chip lime">Power Systems Modelling & Control</span>
                <span class="skill-chip sky">Renewable Energy 1 & 2</span>
                <span class="skill-chip sky">Energy Conversion & Efficiency</span>
                <span class="skill-chip gold">Electromagnetics</span>
                <span class="skill-chip gold">Embedded Systems Engineering</span>
                <span class="skill-chip">Control Systems</span>
                <span class="skill-chip">Digital Electronics</span>
                <span class="skill-chip">Microwave Engineering</span>
                <span class="skill-chip">Computer Networks</span>
                <span class="skill-chip">Engineering Prof. Practice & Ethics</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
        <div class="card-title">University of the Witwatersrand (Wits)</div>
        <div class="card-subtitle" style="color:var(--accent-sky);">Bachelor of Science in Engineering (Electrical) — Prior Studies</div>
        <div class="card-meta">📅 2017 – 2019 &nbsp;|&nbsp; 📍 Johannesburg, South Africa</div>
        <div class="card-body">
            Completed two years of the BSc Engineering (Electrical) programme at Wits before transitioning
            to the University of Zimbabwe. Achieved a <b>Certificate of Merit in Critical Thinking (2017)</b> and
            gained a strong foundation in Electrical Engineering fundamentals.
        </div>
        <div style="margin-top:0.9rem;display:flex;flex-wrap:wrap;gap:0.45rem;">
            <span class="skill-chip">Electric Circuits</span>
            <span class="skill-chip">Electronics I</span>
            <span class="skill-chip">Electric & Magnetic Systems</span>
            <span class="skill-chip">Signals & Systems</span>
            <span class="skill-chip">Mathematics I & II</span>
            <span class="skill-chip">Physics (Electrical)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-accent-bar" style="background:var(--accent-gold);"></div>
        <div class="card-title">Professional Registration — ECSA</div>
        <div class="card-subtitle" style="color:var(--accent-gold);">Engineering Council of South Africa · Candidate Engineer</div>
        <div class="card-meta">🆔 Registration Number: 2025209292 &nbsp;|&nbsp; Pathway: Professional Engineer (Pr Eng)</div>
        <div class="card-body">
            Registered as an ECSA Candidate Engineer, actively accumulating supervised engineering experience
            toward full Professional Engineer registration. This pathway demonstrates commitment to excellence
            in engineering practice and professional ethics.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: SKILLS
# ═══════════════════════════════════════════════════════════════
elif "Skills" in page:
    st.markdown('<div class="section-label">Capabilities</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Technical Skills</div>', unsafe_allow_html=True)

    skill_categories = [
        {
            "title": "Power Systems & Analysis",
            "icon": "⚡",
            "color": "lime",
            "skills": ["Power System Fundamentals", "Load Flow Analysis", "Short Circuit Analysis",
                       "Motor Starting Studies", "Contingency Analysis", "System Reliability",
                       "Protection Principles", "Relay Coordination", "Circuit Breaker Selection"]
        },
        {
            "title": "Renewable Energy",
            "icon": "☀️",
            "color": "sky",
            "skills": ["Solar PV System Design", "BESS Integration", "Hybrid Inverter Systems",
                       "System Commissioning", "Performance Verification", "Functional Testing",
                       "Grid-Tied Systems", "Off-Grid Systems", "String Configuration"]
        },
        {
            "title": "Electrical Design & Drawings",
            "icon": "📐",
            "color": "gold",
            "skills": ["Single Line Diagrams (SLD)", "AutoCAD Electrical", "AutoCAD 2021",
                       "Solar PV Layouts", "Cable Sizing", "BOQ Preparation",
                       "Technical Proposals", "Schematic Design"]
        },
        {
            "title": "Inverter Platforms",
            "icon": "🔋",
            "color": "lime",
            "skills": ["Huawei SUN2000 Series", "Sunsynk 80K-SG02HP3", "Livoltek Inverters",
                       "Suness iRack-HVS 60 BESS", "Battery Combiner Boxes", "DC Isolators",
                       "Surge Protection Devices (SPD)"]
        },
        {
            "title": "Software & Tools",
            "icon": "💻",
            "color": "sky",
            "skills": ["ETAP (Self-Study)", "AutoCAD Electrical", "MS Office Suite",
                       "AutoCAD 2021", "Technical Documentation"]
        },
        {
            "title": "Field & Installation",
            "icon": "🔧",
            "color": "gold",
            "skills": ["LV Cable Installation & Termination", "Transformer Maintenance",
                       "Switchgear Operation", "Site Assessments", "Safety Audits",
                       "Fault Diagnosis", "Compliance Inspection"]
        },
    ]

    cols = st.columns(2)
    for i, cat in enumerate(skill_categories):
        with cols[i % 2]:
            chips_html = "".join([f'<span class="skill-chip {cat["color"]}">{s}</span>' for s in cat["skills"]])
            st.markdown(f"""
            <div class="card" style="margin-bottom:1rem;">
                <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.8rem;">
                    <span style="font-size:1.3rem;">{cat['icon']}</span>
                    <div class="card-title" style="margin:0;">{cat['title']}</div>
                </div>
                <div class="skills-grid">{chips_html}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">ETAP Portfolio</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-accent-bar"></div>
        <div class="card-title">ETAP Power System Analysis Portfolio</div>
        <div class="card-meta" style="margin-bottom:0.8rem;">Self-directed learning project demonstrating power system simulation skills</div>
        <div class="card-body">
            Developed a self-study ETAP portfolio covering load flow, short circuit, motor starting,
            and contingency analysis. This initiative demonstrates proactive skill development beyond
            formal employment requirements.
        </div>
        <div style="margin-top:1rem;">
            <a href="https://drive.google.com/drive/folders/1L6yLxnSvl1T40sCLLsexazplUqTUymKM"
               target="_blank"
               style="display:inline-flex;align-items:center;gap:0.5rem;
                      background:rgba(181,242,62,0.1);border:1px solid rgba(181,242,62,0.3);
                      color:var(--accent-lime);border-radius:8px;padding:0.5rem 1.2rem;
                      font-size:0.85rem;font-weight:600;text-decoration:none;">
                🔗 View ETAP Portfolio on Google Drive
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: PROJECTS
# ═══════════════════════════════════════════════════════════════
elif "Projects" in page:
    st.markdown('<div class="section-label">Featured Work</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Engineering Projects</div>', unsafe_allow_html=True)

    # Featured Project
    st.markdown("""
    <div class="project-card">
        <div class="project-badge">⚡ Featured Project</div>
        <div class="project-title">160 kW Hybrid Solar PV System — Commercial Installation</div>
        <div class="project-desc">
            Designed and documented a commercial-grade hybrid solar PV and Battery Energy Storage System
            using two parallel 80 kW Sunsynk inverters, 120 × 610 W solar panels across 24 strings,
            and 120 kWh of battery storage. Produced the complete Single Line Diagram (SLD) in AutoCAD 2021.
        </div>
        <div class="stats-row">
            <div class="stat-box"><span class="stat-val">160 kW</span><span class="stat-lbl">Total Inverter Output</span></div>
            <div class="stat-box"><span class="stat-val">120</span><span class="stat-lbl">610W Solar Panels</span></div>
            <div class="stat-box"><span class="stat-val">120 kWh</span><span class="stat-lbl">BESS Capacity</span></div>
            <div class="stat-box"><span class="stat-val">73.2 kWp</span><span class="stat-lbl">PV Array (per inverter)</span></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Technical breakdown
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card" style="height:100%;">
            <div class="card-accent-bar"></div>
            <div class="card-title">☀️ PV Array Configuration</div>
            <table class="spec-table">
                <tr><td>Panel Model</td><td>610 W Monocrystalline</td></tr>
                <tr><td>Total Panels</td><td>120 (2 × 60 panels)</td></tr>
                <tr><td>Strings per Inverter</td><td>12 strings</td></tr>
                <tr><td>Panels per String</td><td>15 panels</td></tr>
                <tr><td>String Fuse Rating</td><td>20 A</td></tr>
                <tr><td>DC Operating Voltage</td><td>Up to 1000 V DC</td></tr>
                <tr><td>DC Cable Size</td><td>6 mm² (1.5 kV rated)</td></tr>
                <tr><td>String Overvoltage Prot.</td><td>1000 V DC SPD</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card" style="height:100%;">
            <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
            <div class="card-title">🔋 Battery Storage System</div>
            <table class="spec-table">
                <tr><td>Battery Model</td><td>Suness iRack-HVS 60</td></tr>
                <tr><td>Units per Inverter</td><td>2 × 60 kWh units</td></tr>
                <tr><td>Total BESS Capacity</td><td>120 kWh (system-wide)</td></tr>
                <tr><td>Configuration</td><td>Parallel via combiner box</td></tr>
                <tr><td>Busbar Type</td><td>+ve / -ve DC busbars</td></tr>
                <tr><td>DC Isolation</td><td>160 A DC Isolator</td></tr>
                <tr><td>Battery Chemistry</td><td>High-Voltage Li-Ion</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-gold);"></div>
            <div class="card-title">⚙️ Inverter Specification</div>
            <table class="spec-table">
                <tr><td>Model</td><td>Sunsynk 80K-SG02HP3</td></tr>
                <tr><td>Quantity</td><td>2 × 80 kW (parallel)</td></tr>
                <tr><td>Total Output</td><td>160 kW AC</td></tr>
                <tr><td>Grid Voltage</td><td>0.4 kV (400 V AC)</td></tr>
                <tr><td>Comms</td><td>Inverter Parallel Cable</td></tr>
                <tr><td>AC Protection (per inv.)</td><td>160 A TP MCCB</td></tr>
                <tr><td>AC Input Bus Prot.</td><td>200 A TP MCCB</td></tr>
                <tr><td>Main Breaker</td><td>400 A TP MCCB</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
            <div class="card-title">🔌 AC Distribution & Cabling</div>
            <table class="spec-table">
                <tr><td>AC Bus</td><td>Combiner busbar + Input busbar</td></tr>
                <tr><td>Inv. AC Output Cable</td><td>95 mm² 4-Core + 50 mm² BCEW</td></tr>
                <tr><td>Main AC Feed Cable</td><td>185 mm² 4-Core + 95 mm² BCEW</td></tr>
                <tr><td>Grid Connection</td><td>0.4 kV (LV)</td></tr>
                <tr><td>Transfer Switch</td><td>ATS (Auto Transfer Switch)</td></tr>
                <tr><td>Load Type</td><td>Commercial LV Load</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Second project
    st.markdown("""
    <div class="project-card">
        <div class="project-badge">🎓 Final Year Project</div>
        <div class="project-title">Machine Learning for Predictive Maintenance of ZETDCS 33 kV Feeders</div>
        <div class="project-desc">
            Final-year research project applying machine learning techniques to predict failures and enable
            proactive maintenance scheduling on the ZETDC 33 kV distribution feeder network.
            This project bridged power engineering and data science, demonstrating capability across disciplines.
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.5rem;">
            <span class="skill-chip lime">Machine Learning</span>
            <span class="skill-chip lime">Predictive Maintenance</span>
            <span class="skill-chip sky">33 kV Feeders</span>
            <span class="skill-chip sky">ZETDC Grid</span>
            <span class="skill-chip gold">Data Science</span>
            <span class="skill-chip">Power Distribution</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-badge">📊 Self-Study Initiative</div>
        <div class="project-title">ETAP Power System Analysis Portfolio</div>
        <div class="project-desc">
            Self-directed power system modelling portfolio using ETAP software. Covers load flow studies,
            short circuit analysis, motor starting studies, and contingency analysis.
            Demonstrates proactive professional development aligned with ECSA competency requirements.
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.5rem;">
            <span class="skill-chip lime">ETAP</span>
            <span class="skill-chip lime">Load Flow</span>
            <span class="skill-chip sky">Short Circuit Analysis</span>
            <span class="skill-chip sky">Motor Starting</span>
            <span class="skill-chip gold">Contingency Analysis</span>
        </div>
        <div style="margin-top:1rem;">
            <a href="https://drive.google.com/drive/folders/1L6yLxnSvl1T40sCLLsexazplUqTUymKM"
               target="_blank"
               style="display:inline-flex;align-items:center;gap:0.5rem;
                      background:rgba(181,242,62,0.1);border:1px solid rgba(181,242,62,0.3);
                      color:var(--accent-lime);border-radius:8px;padding:0.5rem 1.2rem;
                      font-size:0.85rem;font-weight:600;text-decoration:none;">
                🔗 View Portfolio
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# PAGE: CONTACT
# ═══════════════════════════════════════════════════════════════
elif "Contact" in page:
    st.markdown('<div class="section-label">Get In Touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Contact Nyasha</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-body" style="font-size:0.95rem;color:#a8c4aa;margin-bottom:1.2rem;">
            Available for electrical engineering roles, renewable energy projects, and consulting engagements
            across Zimbabwe and the broader SADC region. Willing to travel and work onsite.
        </div>
        <div class="contact-row">
            <a class="contact-chip" href="mailto:nyashampofu1@gmail.com">
                📧 nyashampofu1@gmail.com
            </a>
            <a class="contact-chip" href="tel:+263786858523">
                📱 +263 78 685 8523
            </a>
            <span class="contact-chip">
                📍 Harare, Zimbabwe
            </span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar"></div>
            <div class="card-title">Professional Status</div>
            <table class="spec-table" style="margin-top:0.5rem;">
                <tr><td>Registration</td><td>ECSA Candidate Engineer</td></tr>
                <tr><td>Reg. Number</td><td>2025209292</td></tr>
                <tr><td>Pathway</td><td>Professional Engineer (Pr Eng)</td></tr>
                <tr><td>SAQA Level</td><td>NQF Level 8</td></tr>
                <tr><td>Languages</td><td>English (Fluent)</td></tr>
                <tr><td>Travel</td><td>Willing to travel & work onsite</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
            <div class="card-title">Key Interests</div>
            <div style="margin-top:0.8rem;">
                <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                    <span class="skill-chip lime">Commercial Solar PV</span>
                    <span class="skill-chip lime">BESS Systems</span>
                    <span class="skill-chip sky">Power System Design</span>
                    <span class="skill-chip sky">Renewable Energy</span>
                    <span class="skill-chip gold">ETAP Modelling</span>
                    <span class="skill-chip gold">AutoCAD Design</span>
                    <span class="skill-chip">ECSA Pr Eng Pathway</span>
                    <span class="skill-chip">Zimbabwe Grid</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center;padding:2rem 0;">
        <div style="font-family:Syne,sans-serif;font-size:1.3rem;font-weight:700;color:#e8f0e9;margin-bottom:0.5rem;">
            ⚡ Powering Zimbabwe's Renewable Future
        </div>
        <div style="font-size:0.88rem;color:#4a7a50;">
            Junior Electrical Engineer · ECSA Candidate · Solar PV & BESS Specialist
        </div>
    </div>
    """, unsafe_allow_html=True)
