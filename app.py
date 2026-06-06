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

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-primary);
}

[data-testid="stSidebar"] {
    background: var(--bg-card) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--text-primary) !important; }

.main .block-container {
    padding: 2rem 2.5rem 3rem;
    max-width: 1100px;
}

/* Hero */
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
    max-width: 720px;
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
.pill-green {
    background: rgba(181,242,62,0.1);
    border-color: rgba(181,242,62,0.3);
    color: var(--accent-lime) !important;
}

/* Section headings */
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

/* Cards */
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
.card-subtitle { font-size: 0.85rem; color: var(--accent-lime); font-weight: 600; margin-bottom: 0.15rem; }
.card-meta { font-size: 0.78rem; color: var(--text-muted); margin-bottom: 0.9rem; }
.card-body { font-size: 0.88rem; color: #9ab89d; line-height: 1.7; }
.card-body ul { margin: 0; padding-left: 1.3rem; }
.card-body ul li { margin-bottom: 0.4rem; }

/* Skill chips */
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
.skill-chip.lime { background: rgba(181,242,62,0.08); border-color: rgba(181,242,62,0.25); color: var(--accent-lime); }
.skill-chip.sky  { background: rgba(93,227,200,0.08);  border-color: rgba(93,227,200,0.25);  color: var(--accent-sky); }
.skill-chip.gold { background: rgba(240,192,64,0.08);  border-color: rgba(240,192,64,0.25);  color: var(--accent-gold); }

/* Project cards */
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
.project-badge.sky {
    background: rgba(93,227,200,0.12);
    border-color: rgba(93,227,200,0.3);
    color: var(--accent-sky);
}
.project-badge.lime {
    background: rgba(181,242,62,0.12);
    border-color: rgba(181,242,62,0.3);
    color: var(--accent-lime);
}
.project-title { font-family: 'Syne', sans-serif; font-size: 1.25rem; font-weight: 700; color: var(--text-primary); margin-bottom: 0.6rem; }
.project-desc  { font-size: 0.9rem; color: #9ab89d; line-height: 1.7; margin-bottom: 1rem; }
.project-value {
    display: inline-block;
    background: rgba(240,192,64,0.1);
    border: 1px solid rgba(240,192,64,0.25);
    color: var(--accent-gold);
    font-size: 0.8rem;
    font-weight: 700;
    padding: 0.3rem 0.8rem;
    border-radius: 6px;
    margin-bottom: 0.8rem;
}

/* Stats */
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
.stat-val { font-family: 'Syne', sans-serif; font-size: 1.5rem; font-weight: 800; color: var(--accent-lime); display: block; }
.stat-lbl { font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.08em; display: block; margin-top: 0.1rem; }

/* Spec table */
.spec-table { width: 100%; border-collapse: collapse; margin-top: 0.8rem; }
.spec-table tr { border-bottom: 1px solid var(--border); }
.spec-table tr:last-child { border-bottom: none; }
.spec-table td { padding: 0.55rem 0.5rem; font-size: 0.85rem; }
.spec-table td:first-child { color: var(--text-muted); font-weight: 500; width: 45%; }
.spec-table td:last-child { color: var(--text-primary); font-weight: 600; }

/* Contact */
.contact-row { display: flex; flex-wrap: wrap; gap: 0.7rem; margin-top: 0.5rem; }
.contact-chip {
    display: flex; align-items: center; gap: 0.5rem;
    background: var(--bg-card2); border: 1px solid var(--border);
    border-radius: 10px; padding: 0.55rem 1.1rem;
    font-size: 0.85rem; color: var(--text-muted); text-decoration: none;
}

/* Divider */
.divider { border: none; border-top: 1px solid var(--border); margin: 1.8rem 0; }

/* Timeline */
.tl-wrap { position: relative; padding-left: 1.8rem; margin-top: 1rem; }
.tl-line { position: absolute; left: 0.4rem; top: 0; bottom: 0; width: 2px; background: var(--border); border-radius: 2px; }
.tl-item { position: relative; margin-bottom: 1.8rem; }
.tl-item:last-child { margin-bottom: 0; }
.tl-dot { position: absolute; left: -1.4rem; top: 0.35rem; width: 10px; height: 10px; border-radius: 50%; border: 2px solid var(--bg-dark); }
.tl-dot-lime  { background: var(--accent-lime); }
.tl-dot-gold  { background: var(--accent-gold); }
.tl-dot-sky   { background: var(--accent-sky); }
.tl-dot-muted { background: var(--border); }
.tl-date { font-family: 'Syne', sans-serif; font-size: 0.95rem; font-weight: 700; color: #e8f0e9; }
.tl-role { font-size: 0.85rem; color: #7a9e80; margin-top: 0.1rem; }

/* Streamlit overrides */
.stButton > button {
    background: var(--accent-lime) !important; color: #0a0f0d !important;
    border: none !important; border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important; font-weight: 700 !important;
    font-size: 0.9rem !important; padding: 0.55rem 1.5rem !important;
}
.stDownloadButton > button {
    background: transparent !important; border: 1px solid var(--accent-lime) !important;
    color: var(--accent-lime) !important; border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important; font-weight: 600 !important;
}
h1, h2, h3, h4 { color: var(--text-primary) !important; }
[data-testid="stMetric"] { background: var(--bg-card2); border-radius: 10px; padding: 0.8rem; border: 1px solid var(--border); }
[data-testid="stMetricValue"] { color: var(--accent-lime) !important; font-family: 'Syne', sans-serif !important; }
[data-testid="stMetricLabel"] { color: var(--text-muted) !important; }
</style>
""", unsafe_allow_html=True)


# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style='text-align:center; padding: 1.5rem 0 1rem;'>
        <div style='width:80px;height:80px;border-radius:50%;
                    background:linear-gradient(135deg,#b5f23e,#5de3c8);
                    margin:0 auto 1rem;display:flex;align-items:center;justify-content:center;
                    font-size:2rem;font-family:Syne,sans-serif;font-weight:800;color:#0a0f0d;'>N</div>
        <div style='font-family:Syne,sans-serif;font-size:1.05rem;font-weight:700;color:#e8f0e9;'>Nyasha Mpofu</div>
        <div style='font-size:0.78rem;color:#7a9e80;margin-top:0.2rem;'>Electrical Engineer</div>
        <div style='font-size:0.75rem;color:#5de3c8;margin-top:0.3rem;'>⚡ Power Systems &amp; Renewables</div>
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
    <div style='font-size:0.72rem;color:#4a7a50;padding:0 0.5rem;line-height:1.8;'>
        <b style='color:#7a9e80;'>ECSA Candidate Engineer</b><br>
        Reg. No. 2025209292<br><br>
        <b style='color:#7a9e80;'>SAQA Evaluation</b><br>
        NQF Level 8<br><br>
        <b style='color:#7a9e80;'>Driver's Licence</b><br>
        Valid · Clean Record
    </div>
    """, unsafe_allow_html=True)

    cv_text = """NYASHA MPOFU
Electrical Engineer
nyashampofu1@gmail.com | +263 78 685 8523 | Harare, Zimbabwe

PROFESSIONAL PROFILE
Electrical Engineer with experience in power systems, electrical distribution networks, renewable
energy, and solar PV systems. Skilled in the installation, commissioning, troubleshooting, and
maintenance of residential, commercial, and industrial solar systems, as well as utility operations.
Experienced in solar project assessment, technical analysis, fault diagnosis, and energy infrastructure
projects, with exposure to grid distribution systems, machine learning-based predictive maintenance,
and commercial solar installations. Passionate about energy access, power system modernization,
renewable energy development, and sustainable infrastructure across Zimbabwe and the wider SADC region.

CORE COMPETENCIES
- Power Systems and Electrical Distribution Networks
- Solar PV Systems Installation, Commissioning and Maintenance
- Electrical Troubleshooting and Fault Diagnosis
- Technical Site Assessments and System Audits
- Electrical Safety and Compliance
- Solar System Performance Analysis
- Project Coordination and Technical Reporting
- Client Engagement and Stakeholder Management
- Data Analysis and Predictive Maintenance Applications
- Renewable Energy and Energy Infrastructure Development

Software & Technical Tools: AutoCAD Electrical | PVSyst | Microsoft Office Suite

EDUCATION
BSc (Hons) Electrical Engineering | University of Zimbabwe | 2024
Classification: Second Class Upper Division (2.1) | SAQA: NQF Level 8

PROFESSIONAL REGISTRATION
ECSA Candidate Engineer (PrEng pathway) | Reg. 2025209292

EXPERIENCE
Power Life Energy — Graduate Electrical Engineer (February 2026 – April 2026)
Participated in the installation, commissioning, troubleshooting, and maintenance of residential and
commercial solar PV systems utilizing Huawei, Sunsynk, and Deye inverter platforms. Conducted site
assessments, technical evaluations, preventative maintenance, and electrical troubleshooting, while
supporting electrical infrastructure works, project coordination, client engagement, system handovers,
and after-sales support in compliance with safety and operational standards.

Coalition for Market and Liberal Solutions (COMALISO)
Electrical Energy Policy Researcher (February 2025 – Present) [Part-time]
Led policy advocacy efforts to promote reforms enabling increased private sector participation in
Zimbabwe's electricity sector. Stakeholder engagement with Ministry of Energy, ZESA, and ZERA.
Authored the COMALISO Electricity Sector Privatization Blueprint.

Zimbabwe Electricity Transmission and Distribution Company (ZETDC)
Engineering Attaché (November 2022 – October 2023)
Assisted in troubleshooting and maintaining electrical distribution systems, transformers and switchgear.
Conducted site inspections, motor control, circuit breakers, and power system protection.

PROJECTS
1. ML for Predictive Maintenance of 33kV Distribution Feeders | University of Zimbabwe
2. Millennium Heights, Borrowdale West (~USD $55,000) | Power Life Energy
3. Millennium Heights Padel Court (~USD $2,000) | Power Life Energy
4. The Hills Gold Estate, Warren Hills (~USD $6,500) | Power Life Energy

ADDITIONAL INFORMATION
Professional registration: ECSA Candidate Engineer
Valid driver's licence (clean driving record)
"""
    st.markdown("<div style='margin-top:1.5rem;'>", unsafe_allow_html=True)
    st.download_button(
        "⬇ Download CV",
        data=cv_text,
        file_name="Nyasha_Mpofu_CV.txt",
        mime="text/plain",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# PAGE: ABOUT
# ═══════════════════════════════════════════════════════
if "About" in page:
    st.markdown("""
    <div class="hero-wrapper">
        <div class="hero-tag">⚡ Open to Opportunities</div>
        <div class="hero-name">Nyasha <span>Mpofu</span></div>
        <div class="hero-title">Electrical Engineer — Power Systems &amp; Renewable Energy</div>
        <div class="hero-summary">
            Electrical Engineer with experience in power systems, electrical distribution networks,
            renewable energy, and solar PV systems. Skilled in the installation, commissioning,
            troubleshooting, and maintenance of residential, commercial, and industrial solar systems.
            Experienced in solar project assessment, technical analysis, fault diagnosis, and energy
            infrastructure — with additional exposure to policy research and grid reform advocacy.
            Passionate about advancing energy access and sustainable infrastructure across Zimbabwe
            and the SADC region.
        </div>
        <div class="hero-pills">
            <span class="pill pill-highlight">📍 Harare, Zimbabwe</span>
            <span class="pill pill-green">Solar PV &amp; BESS</span>
            <span class="pill">Power Distribution</span>
            <span class="pill">AutoCAD Electrical</span>
            <span class="pill">PVSyst</span>
            <span class="pill">ECSA Candidate Eng.</span>
            <span class="pill">🚗 Valid Driver's Licence</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Experience", "1+ yrs", "Incl. Attaché")
    with col2:
        st.metric("Projects", "3+", "Named Deliveries")
    with col3:
        st.metric("Degree Class", "2.1", "Upper Second")
    with col4:
        st.metric("Registration", "ECSA", "Candidate Eng.")

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)
    st.markdown('<div class="section-label">What I Do</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Core Competencies</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar"></div>
            <div style='font-size:1.6rem;margin-bottom:0.7rem;'>☀️</div>
            <div class="card-title">Solar PV &amp; Renewables</div>
            <div class="card-body">Installation, commissioning, troubleshooting, and maintenance
            of residential and commercial solar PV systems using Huawei, Sunsynk, and Deye
            inverter platforms. Solar system performance analysis using PVSyst.</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
            <div style='font-size:1.6rem;margin-bottom:0.7rem;'>📐</div>
            <div class="card-title">Electrical Design</div>
            <div class="card-body">Production of Single Line Diagrams, solar PV layouts and
            electrical schematics using AutoCAD Electrical. Technical site assessments, BOQ
            preparation, and project coordination from design through to handover.</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-gold);"></div>
            <div style='font-size:1.6rem;margin-bottom:0.7rem;'>🔌</div>
            <div class="card-title">Power Distribution</div>
            <div class="card-body">Distribution network experience gained at ZETDC including
            transformer maintenance, switchgear, motor control, circuit breakers, and protection
            systems on national grid infrastructure.</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # New: policy work highlight
    st.markdown('<div class="section-label">Beyond the Field</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-accent-bar" style="background:var(--accent-gold);"></div>
        <div style="display:flex;align-items:flex-start;gap:1rem;flex-wrap:wrap;">
            <div style="font-size:2rem;">🏛️</div>
            <div>
                <div class="card-title">Electricity Sector Policy Research — COMALISO</div>
                <div class="card-meta" style="margin-bottom:0.6rem;">Coalition for Market and Liberal Solutions · Part-time · Feb 2025 – Present</div>
                <div class="card-body">
                    Nyasha brings both hands-on engineering and policy-level thinking to the energy sector.
                    As Electrical Energy Policy Researcher at COMALISO, she leads advocacy for private sector
                    participation in Zimbabwe's electricity sector, engaging with the Ministry of Energy,
                    ZESA, and ZERA — and authoring the COMALISO Electricity Sector Privatisation Blueprint.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size:0.9rem;color:#9ab89d;line-height:1.75;max-width:720px;margin-top:1rem;'>
        Registered with the Engineering Council of South Africa (ECSA) as a Candidate Engineer
        (Reg. No. <b style='color:#b5f23e;'>2025209292</b>), working toward full Professional Engineer
        (Pr Eng) registration. Academic qualifications evaluated by SAQA at <b style='color:#b5f23e;'>NQF Level 8</b>.
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# PAGE: EXPERIENCE
# ═══════════════════════════════════════════════════════
elif "Experience" in page:
    st.markdown('<div class="section-label">Career History</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Professional Experience</div>', unsafe_allow_html=True)

    # Power Life Energy
    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-accent-bar"></div>
        <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;align-items:flex-start;">
            <div>
                <div class="card-title">Graduate Electrical Engineer</div>
                <div class="card-subtitle">Power Life Energy</div>
                <div class="card-meta">📅 February 2026 – April 2026 &nbsp;|&nbsp; 📍 Zimbabwe</div>
            </div>
        </div>
        <div class="card-body">
            Participated in the installation, commissioning, troubleshooting, and maintenance of
            residential and commercial solar PV systems utilizing <b>Huawei, Sunsynk, and Deye</b>
            inverter platforms. Conducted site assessments, technical evaluations, preventative
            maintenance, and electrical troubleshooting, while supporting electrical infrastructure
            works, project coordination, client engagement, system handovers, and after-sales support
            in compliance with safety and operational standards.
        </div>
        <div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:0.5rem;">
            <span class="skill-chip lime">Solar PV</span>
            <span class="skill-chip lime">Commissioning</span>
            <span class="skill-chip sky">Huawei</span>
            <span class="skill-chip sky">Sunsynk</span>
            <span class="skill-chip sky">Deye</span>
            <span class="skill-chip gold">Site Assessment</span>
            <span class="skill-chip gold">Client Liaison</span>
            <span class="skill-chip">AutoCAD Electrical</span>
            <span class="skill-chip">Safety Compliance</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # COMALISO — new role
    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-accent-bar" style="background:var(--accent-gold);"></div>
        <div style="display:flex;justify-content:space-between;flex-wrap:wrap;gap:0.5rem;align-items:flex-start;">
            <div>
                <div class="card-title">Electrical Energy Policy Researcher</div>
                <div class="card-subtitle" style="color:var(--accent-gold);">
                    Coalition for Market and Liberal Solutions (COMALISO)
                </div>
                <div class="card-meta">📅 February 2025 – Present &nbsp;|&nbsp; Part-time &nbsp;|&nbsp; 📍 Zimbabwe</div>
            </div>
            <span style="background:rgba(240,192,64,0.12);border:1px solid rgba(240,192,64,0.3);
                         color:#f0c040;font-size:0.72rem;font-weight:700;letter-spacing:0.1em;
                         text-transform:uppercase;padding:0.3rem 0.9rem;border-radius:100px;height:fit-content;">
                Part-Time · Active
            </span>
        </div>
        <div class="card-body">
            <ul>
                <li>Led <b>policy advocacy efforts</b> under COMALISO to promote reforms enabling increased
                    private sector participation in Zimbabwe's electricity sector.</li>
                <li>Conducted <b>stakeholder engagement</b> with the Ministry of Energy and Power Development,
                    ZESA, and ZERA to present and discuss proposed regulatory changes.</li>
                <li>Authored the <b>COMALISO Electricity Sector Privatisation Blueprint</b>, which was
                    circulated among key stakeholders and featured in CITEZW coverage.</li>
                <li>Contributed to <b>national discourse on electricity sector reform</b>, bridging technical
                    engineering expertise with energy policy advocacy.</li>
            </ul>
        </div>
        <div style="margin-top:1rem;display:flex;flex-wrap:wrap;gap:0.5rem;">
            <span class="skill-chip gold">Energy Policy</span>
            <span class="skill-chip gold">Sector Reform</span>
            <span class="skill-chip sky">Stakeholder Engagement</span>
            <span class="skill-chip sky">ZESA / ZERA</span>
            <span class="skill-chip">Policy Authoring</span>
            <span class="skill-chip">Privatisation Blueprint</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ZETDC
    st.markdown("""
    <div class="card">
        <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
        <div>
            <div class="card-title">Engineering Attaché</div>
            <div class="card-subtitle" style="color:var(--accent-sky);">
                Zimbabwe Electricity Transmission and Distribution Company (ZETDC)
            </div>
            <div class="card-meta">📅 November 2022 – October 2023 &nbsp;|&nbsp; 📍 Zimbabwe</div>
        </div>
        <div class="card-body">
            <ul>
                <li>Assisted in troubleshooting and maintaining <b>electrical distribution systems</b>,
                    including transformers and switchgear across the national grid.</li>
                <li>Conducted <b>site inspections</b> to ensure compliance with electrical safety regulations
                    and industrial standards.</li>
                <li>Hands-on experience with <b>motor control, circuit breakers, and power system
                    protection</b> in a live utility environment.</li>
                <li>Provided <b>technical support</b> to engineering teams ensuring reliable power supply
                    for industrial consumers.</li>
                <li>Participated in <b>safety audits</b> and contributed to improvements in operational
                    efficiency.</li>
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
    st.markdown('<div class="section-label">Timeline</div>', unsafe_allow_html=True)
    st.markdown("""<div class="tl-wrap"><div class="tl-line"></div><div class="tl-item"><div class="tl-dot tl-dot-gold"></div><div class="tl-date">Feb 2025 – Present</div><div class="tl-role">Policy Researcher · COMALISO (Part-time)</div></div><div class="tl-item"><div class="tl-dot tl-dot-lime"></div><div class="tl-date">Feb – Apr 2026</div><div class="tl-role">Graduate Electrical Engineer · Power Life Energy</div></div><div class="tl-item"><div class="tl-dot tl-dot-gold"></div><div class="tl-date">Jul 2024</div><div class="tl-role">BSc (Hons) Electrical Engineering Awarded · University of Zimbabwe</div></div><div class="tl-item"><div class="tl-dot tl-dot-sky"></div><div class="tl-date">Nov 2022 – Oct 2023</div><div class="tl-role">Engineering Attaché · ZETDC</div></div><div class="tl-item"><div class="tl-dot tl-dot-muted"></div><div class="tl-date">Aug 2020</div><div class="tl-role">Commenced BSc Electrical Engineering · University of Zimbabwe</div></div></div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# PAGE: EDUCATION
# ═══════════════════════════════════════════════════════
elif "Education" in page:
    st.markdown('<div class="section-label">Academic Background</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Education &amp; Qualifications</div>', unsafe_allow_html=True)

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
            <div><span style="color:var(--text-muted);font-size:0.8rem;">Final Year Project</span><br>
                 <b style="color:var(--text-primary);">ML Predictive Maintenance — ZETDCS 33kV Feeders</b></div>
        </div>
        <div style="margin-top:1rem;">
            <div style="font-size:0.8rem;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.1em;margin-bottom:0.7rem;font-weight:600;">Key Modules</div>
            <div style="display:flex;flex-wrap:wrap;gap:0.45rem;">
                <span class="skill-chip lime">Power Systems 1</span>
                <span class="skill-chip lime">Power Systems Modelling &amp; Control</span>
                <span class="skill-chip sky">Renewable Energy 1 &amp; 2</span>
                <span class="skill-chip sky">Energy Conversion &amp; Efficiency</span>
                <span class="skill-chip gold">Electromagnetics</span>
                <span class="skill-chip gold">Embedded Systems Engineering</span>
                <span class="skill-chip">Control Systems</span>
                <span class="skill-chip">Digital Electronics</span>
                <span class="skill-chip">Microwave Engineering</span>
                <span class="skill-chip">Computer Networks</span>
                <span class="skill-chip">Engineering Ethics &amp; Practice</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
        <div class="card-title">University of the Witwatersrand, Johannesburg</div>
        <div class="card-subtitle" style="color:var(--accent-sky);">BSc Engineering (Electrical) — Prior Studies (2017–2019)</div>
        <div class="card-meta">📅 2017–2019 &nbsp;|&nbsp; 📍 Johannesburg, South Africa</div>
        <div class="card-body">
            Completed two years of the BSc Engineering (Electrical) programme at Wits before
            transitioning to the University of Zimbabwe. Awarded a
            <b>Certificate of Merit in Critical Thinking (2017)</b> and built a strong foundation
            in electrical engineering fundamentals.
        </div>
        <div style="margin-top:0.9rem;display:flex;flex-wrap:wrap;gap:0.45rem;">
            <span class="skill-chip">Electric Circuits</span>
            <span class="skill-chip">Electronics I</span>
            <span class="skill-chip">Electric &amp; Magnetic Systems</span>
            <span class="skill-chip">Signals &amp; Systems</span>
            <span class="skill-chip">Mathematics I &amp; II</span>
            <span class="skill-chip">Physics (Electrical)</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-accent-bar" style="background:var(--accent-gold);"></div>
        <div class="card-title">Professional Registration — ECSA</div>
        <div class="card-subtitle" style="color:var(--accent-gold);">Engineering Council of South Africa · Candidate Engineer</div>
        <div class="card-meta">🆔 Registration No: 2025209292 &nbsp;|&nbsp; Pathway: Professional Engineer (Pr Eng)</div>
        <div class="card-body">
            Registered as an ECSA Candidate Engineer, accumulating supervised engineering experience
            toward full Professional Engineer (Pr Eng) registration. Demonstrates commitment to engineering
            excellence and professional ethics across the SADC region.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# PAGE: SKILLS
# ═══════════════════════════════════════════════════════
elif "Skills" in page:
    st.markdown('<div class="section-label">Capabilities</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Technical Skills &amp; Competencies</div>', unsafe_allow_html=True)

    skill_categories = [
        {
            "title": "Power Systems &amp; Distribution",
            "icon": "⚡",
            "color": "lime",
            "skills": ["Power System Fundamentals", "Electrical Distribution Networks",
                       "Load Flow Analysis", "Short Circuit Analysis", "Contingency Analysis",
                       "System Reliability", "Protection Principles", "Relay Coordination",
                       "Circuit Breaker Selection", "Motor Control"]
        },
        {
            "title": "Solar PV &amp; Renewable Energy",
            "icon": "☀️",
            "color": "sky",
            "skills": ["Solar PV System Design", "System Installation", "Commissioning &amp; Testing",
                       "Performance Verification", "Preventative Maintenance",
                       "Residential &amp; Commercial Systems", "Grid-Tied Systems", "String Configuration",
                       "BESS Integration", "After-Sales Support"]
        },
        {
            "title": "Electrical Design &amp; Documentation",
            "icon": "📐",
            "color": "gold",
            "skills": ["Single Line Diagrams (SLD)", "AutoCAD Electrical", "Electrical Schematics",
                       "Solar PV Layouts", "BOQ Preparation", "Technical Proposals",
                       "Project Coordination", "Technical Reporting"]
        },
        {
            "title": "Inverter &amp; Equipment Platforms",
            "icon": "🔋",
            "color": "lime",
            "skills": ["Huawei SUN2000 Series", "Sunsynk Inverters", "Deye Inverters",
                       "Livoltek Inverters", "Suness iRack-HVS BESS",
                       "DC Isolators", "Surge Protection Devices (SPD)", "ATS Systems"]
        },
        {
            "title": "Software &amp; Technical Tools",
            "icon": "💻",
            "color": "sky",
            "skills": ["AutoCAD Electrical", "PVSyst", "Microsoft Office Suite",
                       "Technical Documentation"]
        },
        {
            "title": "Field, Assessment &amp; Soft Skills",
            "icon": "🔧",
            "color": "gold",
            "skills": ["Site Assessments &amp; Audits", "Fault Diagnosis", "Insulation Resistance Testing",
                       "Cable Installation &amp; Termination", "Safety Compliance", "Client Engagement",
                       "Stakeholder Management", "Data Analysis", "Policy Research",
                       "Valid Driver's Licence"]
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
    st.markdown('<div class="section-label">Solar Design Tool</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <div class="card-accent-bar"></div>
        <div style="display:flex;align-items:center;gap:1rem;flex-wrap:wrap;">
            <div style="font-size:2.2rem;">🌞</div>
            <div>
                <div class="card-title">PVSyst — Solar System Design &amp; Validation</div>
                <div class="card-body" style="margin-top:0.4rem;">
                    Proficient in PVSyst for solar system design validation and performance analysis —
                    enabling accurate energy yield simulations, shading analysis, and system sizing
                    for commercial and residential PV installations.
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# PAGE: PROJECTS
# ═══════════════════════════════════════════════════════
elif "Projects" in page:
    st.markdown('<div class="section-label">Delivered Work</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Engineering Projects</div>', unsafe_allow_html=True)

    # Project 1 – Millennium Heights (major cable installation)
    st.markdown("""
    <div class="project-card">
        <div class="project-badge">🏗️ Infrastructure · Power Life Energy</div>
        <div class="project-value">Project Value: ~USD $55,000</div>
        <div class="project-title">Millennium Heights — Borrowdale West, Harare</div>
        <div class="project-desc">
            Installed and commissioned <b>2 × 150 m runs of 120 mm² 4-core SWA cable and 95 mm² BCEW</b>
            from the substation to Block 4. Performed full cable commissioning including insulation
            resistance testing (Megger) and coordinated directly with client consultants during
            site inspection and formal project handover.
        </div>
        <div class="stats-row">
            <div class="stat-box"><span class="stat-val">2 × 150m</span><span class="stat-lbl">Cable Runs</span></div>
            <div class="stat-box"><span class="stat-val">120 mm²</span><span class="stat-lbl">SWA Cable</span></div>
            <div class="stat-box"><span class="stat-val">Megger</span><span class="stat-lbl">IR Testing</span></div>
            <div class="stat-box"><span class="stat-val">~$55k</span><span class="stat-lbl">Project Value</span></div>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.5rem;">
            <span class="skill-chip lime">SWA Cable Installation</span>
            <span class="skill-chip lime">Cable Commissioning</span>
            <span class="skill-chip sky">Insulation Resistance Testing</span>
            <span class="skill-chip sky">Client Coordination</span>
            <span class="skill-chip gold">Project Handover</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Project 2 – 160kW Solar PV (featured from SLD)
    st.markdown("""
    <div class="project-card">
        <div class="project-badge sky">⚡ Featured Design · Power Life Energy</div>
        <div class="project-title">160 kW Hybrid Solar PV System — Commercial Installation</div>
        <div class="project-desc">
            Designed and documented a commercial-grade hybrid solar PV and BESS using two parallel
            80 kW Sunsynk inverters, 120 × 610 W solar panels across 24 strings, and 120 kWh of
            battery storage (2 × Suness iRack-HVS 60 per inverter). Produced the complete SLD in
            AutoCAD 2021.
        </div>
        <div class="stats-row">
            <div class="stat-box"><span class="stat-val">160 kW</span><span class="stat-lbl">Total Output</span></div>
            <div class="stat-box"><span class="stat-val">120</span><span class="stat-lbl">610W Panels</span></div>
            <div class="stat-box"><span class="stat-val">120 kWh</span><span class="stat-lbl">BESS Capacity</span></div>
            <div class="stat-box"><span class="stat-val">24</span><span class="stat-lbl">Strings Total</span></div>
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.5rem;">
            <span class="skill-chip lime">Solar PV Design</span>
            <span class="skill-chip lime">BESS Integration</span>
            <span class="skill-chip sky">AutoCAD SLD</span>
            <span class="skill-chip sky">Sunsynk 80K</span>
            <span class="skill-chip gold">Hybrid Systems</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Project 3 – Padel Court
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="project-card" style="height:100%;">
            <div class="project-badge lime">🎾 Distribution Design · Power Life Energy</div>
            <div class="project-value">Project Value: ~USD $2,000</div>
            <div class="project-title">Millennium Heights Padel Court</div>
            <div class="project-desc">
                Designed, costed, and oversaw the installation of the <b>electrical distribution panel</b>
                supplying all electrical loads for the padel court facility at Borrowdale West, Harare.
                Ensured compliance with site requirements and safe system operation.
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.5rem;">
                <span class="skill-chip lime">Panel Design</span>
                <span class="skill-chip sky">Load Analysis</span>
                <span class="skill-chip gold">Cost Estimation</span>
                <span class="skill-chip">Site Compliance</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="project-card" style="height:100%;">
            <div class="project-badge">🏡 Distribution Infrastructure · Power Life Energy</div>
            <div class="project-value">Project Value: ~USD $6,500</div>
            <div class="project-title">The Hills Gold Estate — Warren Hills, Harare</div>
            <div class="project-desc">
                Supervised <b>strut replacement and installation works</b> on a 0.4 kV distribution line.
                Managed procurement, fabrication of struts, factory inspections during manufacturing,
                on-site installation, stakeholder coordination, and client liaison through to handover.
            </div>
            <div style="display:flex;flex-wrap:wrap;gap:0.5rem;margin-top:0.5rem;">
                <span class="skill-chip lime">0.4 kV Distribution</span>
                <span class="skill-chip sky">Procurement</span>
                <span class="skill-chip gold">Site Supervision</span>
                <span class="skill-chip">Stakeholder Mgmt</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    # Final Year Project & Policy
    st.markdown("""
    <div class="project-card">
        <div class="project-badge sky">🎓 Final Year Research · University of Zimbabwe</div>
        <div class="project-title">Machine Learning for Predictive Maintenance of 33 kV Distribution Feeders</div>
        <div class="project-desc">
            Developed a machine learning-based predictive maintenance system for 33 kV feeders using
            historical fault and weather data. Work included model training, validation, and GUI
            development focused on fault prediction for utility distribution networks — bridging
            power engineering and data science.
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
            <span class="skill-chip lime">Machine Learning</span>
            <span class="skill-chip lime">Predictive Maintenance</span>
            <span class="skill-chip sky">33 kV Feeders</span>
            <span class="skill-chip sky">ZETDC Grid</span>
            <span class="skill-chip gold">Data Science</span>
            <span class="skill-chip">GUI Development</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
        <div class="project-badge" style="background:rgba(181,242,62,0.12);border-color:rgba(181,242,62,0.3);color:var(--accent-lime);">
            🏛️ Policy Research · COMALISO
        </div>
        <div class="project-title">COMALISO Electricity Sector Privatisation Blueprint</div>
        <div class="project-desc">
            Authored a comprehensive sector reform document advocating for increased private sector
            participation in Zimbabwe's electricity sector. The blueprint was circulated among key
            stakeholders including the Ministry of Energy and Power Development, ZESA, and ZERA,
            and was featured in CITEZW coverage — contributing to national discourse on electricity
            sector reform.
        </div>
        <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
            <span class="skill-chip gold">Energy Policy</span>
            <span class="skill-chip gold">Sector Reform</span>
            <span class="skill-chip sky">ZESA / ZERA</span>
            <span class="skill-chip sky">Stakeholder Engagement</span>
            <span class="skill-chip">CITEZW Coverage</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════
# PAGE: CONTACT
# ═══════════════════════════════════════════════════════
elif "Contact" in page:
    st.markdown('<div class="section-label">Get In Touch</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Contact Nyasha</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="card" style="margin-bottom:1.5rem;">
        <div class="card-body" style="font-size:0.95rem;color:#a8c4aa;margin-bottom:1.2rem;">
            Available for electrical engineering roles, renewable energy projects, and consulting
            engagements across Zimbabwe and the broader SADC region.
            Willing to travel and work onsite. Valid driver's licence.
        </div>
        <div class="contact-row">
            <a class="contact-chip" href="mailto:nyashampofu1@gmail.com">
                📧 nyashampofu1@gmail.com
            </a>
            <a class="contact-chip" href="tel:+263786858523">
                📱 +263 78 685 8523
            </a>
            <span class="contact-chip">📍 Harare, Zimbabwe</span>
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
                <tr><td>Driver's Licence</td><td>Valid · Clean Record</td></tr>
                <tr><td>Travel</td><td>Willing to travel &amp; work onsite</td></tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-accent-bar" style="background:var(--accent-sky);"></div>
            <div class="card-title">Areas of Interest</div>
            <div style="margin-top:0.8rem;">
                <div style="display:flex;flex-wrap:wrap;gap:0.5rem;">
                    <span class="skill-chip lime">Commercial Solar PV</span>
                    <span class="skill-chip lime">BESS Systems</span>
                    <span class="skill-chip sky">Power System Design</span>
                    <span class="skill-chip sky">Renewable Energy</span>
                    <span class="skill-chip gold">Energy Policy</span>
                    <span class="skill-chip gold">Sector Reform</span>
                    <span class="skill-chip">PVSyst Modelling</span>
                    <span class="skill-chip">AutoCAD Design</span>
                    <span class="skill-chip">ECSA Pr Eng Pathway</span>
                    <span class="skill-chip">SADC Region</span>
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
            Electrical Engineer · ECSA Candidate · Solar PV Specialist · Energy Policy Researcher
        </div>
    </div>
    """, unsafe_allow_html=True)
