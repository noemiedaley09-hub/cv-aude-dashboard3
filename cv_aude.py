import streamlit as st
import plotly.express as px
import os
import qrcode
from PIL import Image

# --- CONFIGURATION PAGE ---
st.set_page_config(
    page_title="CV Aude Noémie FEVILIYE Daley",
    page_icon="💖",
    layout="wide"
)

# --- GÉNÉRATION QR CODE LINKEDIN ---
linkedin_url = "https://www.linkedin.com/in/audenoemiefeviliyedaley/"
if not os.path.exists("linkedin_qr.png"):
    qr = qrcode.make(linkedin_url)
    qr.save("linkedin_qr.png")

# --- STYLE CSS MODERNE ---
st.markdown("""
<style>
@keyframes fadeInUp {
    from { opacity: 0; transform: translateY(30px); }
    to { opacity: 1; transform: translateY(0); }
}

/* Fond général blanc */
.block-container {
    background-color: #ffffff !important;
    font-family: 'Helvetica', sans-serif;
    animation: fadeInUp 1s ease-in-out;
}

/* Titres */
h1, h2, h3 {
    color: #ff69b4;
    animation: fadeInUp 0.8s ease-in-out;
}

/* Onglets lilas */
[data-baseweb="tab"] {
    height: 55px;
    background: #c8a2ff;
    border-radius: 12px 12px 0 0;
    padding: 12px;
    font-weight: 600;
    color: white;
    transition: all 0.3s ease;
}
[data-baseweb="tab"]:hover {
    transform: translateY(-4px);
    background: #b28fff;
    color: white;
}
[aria-selected="true"] {
    background: #a366ff !important;
    color: white !important;
    font-size: 18px;
}

/* Sidebar silver */
[data-testid="stSidebar"] > div:first-child {
    background-color: #c0c0c0 !important;
    padding: 20px;
}

/* Expander hover */
.stExpander { transition: 0.3s ease; }
.stExpander:hover { transform: scale(1.01); }

/* Footer violet animé */
.footer {
    text-align: center;
    padding: 10px 0;
    color: #800080;
    animation: fadeInUp 1s ease-in-out;
}
.footer img {
    height: 40px;
    vertical-align: middle;
    margin-left: 10px;
}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.image("téléchargement.png", width=120)  # Logo EFREI sans arrondi
st.sidebar.markdown("## Etudiante à Efrei Paris ")
st.sidebar.caption("Alternance Marketing Digital / CRM")
st.sidebar.markdown("---")
st.sidebar.markdown("### 🔗 LinkedIn")
st.sidebar.image("linkedin_qr.png", width=140)
st.sidebar.markdown(
    "[Voir mon profil LinkedIn](https://www.linkedin.com/in/audenoemiefeviliyedaley/)",
    unsafe_allow_html=True
)
st.sidebar.markdown("---")
st.sidebar.info("📍 Recherche alternance 24 mois\n📅 Septembre 2026")

# Remerciements prof BI
st.sidebar.markdown(
    """
    <div style="background-color:#e6d6ff; padding:10px; border-radius:10px; text-align:center;">
    Merci à Mr <a href='https://www.linkedin.com/in/manomathew/' target='_blank'>Mano Joseph MATTHEW</a>  
    pour sa supervision et sa bienveillance sur ce projet.
    </div>
    """,
    unsafe_allow_html=True
)

# Compétences sidebar
st.sidebar.markdown("### 🛠 Compétences clés")
competences = {"Marketing": 90, "Data": 80, "Design & Ops": 75}
for comp, level in competences.items():
    st.sidebar.markdown(f"**{comp}**")
    st.sidebar.progress(level)

# --- HEADER PRINCIPAL ---
col1, col2 = st.columns([3, 1])
with col1:
    st.title("AUDE NOEMIE FEVILIYE DALEY")
    st.subheader("ASSISTANTE MARKETING DIGITAL / CRM – ALTERNANCE")
    st.markdown(
        "<h4 style='text-align:left; color:#ff1493; margin-top:-10px;'>💼 Disponible pour une alternance – Septembre 2026</h4>",
        unsafe_allow_html=True
    )

st.write("---")

# --- NAVIGATION PAR ONGLETS ---
tab1, tab2, tab3, tab4 = st.tabs([
    "🏠 Profil & Contact",
    "💼 Expériences",
    "🛠 Compétences",
    "🎓 Formation & Projets"
])

# --- PAGE 1 : PROFIL & CONTACT ---
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.header("📝 À propos")
        st.write("""
        Étudiante en 3e année d'ingénierie marketing & data à l'EFREI Paris,
        spécialisée en CRM, marketing automation et analyse de données.  
        Passionnée par la transformation digitale et l’optimisation des processus marketing, 
        j’ai travaillé sur plusieurs projets de dashboarding et reporting, en utilisant Power BI et Excel.  
        Recherche une alternance pour le Master 1 à partir de **septembre 2026**  
        (Rythme : 2 semaines entreprise / 1 semaine école).
        """)
    with col2:
        st.header("📍 Contact")
        st.write("📧 noemiedaley09@gmail.com")
        st.write("🏠 Chevilly-Larue, France")
        st.write("🌍 Français (C2) • Anglais (B1)")

# --- PAGE 2 : EXPÉRIENCES ---
with tab2:
    st.header("💼 Expériences professionnelles")
    st.markdown("📌 *Survolez pour découvrir les missions*")
    with st.expander("Assistante Marketing Digital (Alternance) – ARCHIA 365", expanded=True):
        st.caption("Nov 2025 – Présent | Paris")
        st.write("- Coordination d'événements")
        st.write("- Stratégie de communication")
        st.write("- Animation de communautés")
    with st.expander("Assistante Marketing Digital (Stage) – MWDDB"):
        st.caption("Juin – Août 2025 | Brazzaville")
        st.write("- Automatisation (Make.com, Apify)")
        st.write("- Reporting & Data Excel")
    with st.expander("Assistante Marketing Digital (Stage) – Pool Security Services"):
        st.caption("Mai – Août 2024 | Paris")
        st.write("- +10 % de visibilité digitale")
        st.write("- Création de contenus")

# --- PAGE 3 : COMPÉTENCES ---
with tab3:
    st.header("🛠 Expertise technique")
    fig = px.bar(
        x=list(competences.keys()),
        y=list(competences.values()),
        text=list(competences.values()),
        color=list(competences.keys()),
        color_discrete_sequence=['#ff69b4', '#ffb6c1', '#ff1493'],
        title="🛠 Mes compétences"
    )
    fig.update_layout(
        yaxis=dict(title="Niveau (%)", range=[0, 100]),
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#800080', size=14),
        transition_duration=500
    )
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 4 : FORMATION & PROJETS ---
with tab4:
    st.header("🎓 Parcours académique")
    st.write("**EFREI Paris** – Ingénierie Marketing & Data (2023–2026)")
    st.write("**APU Kuala Lumpur** – Mobilité internationale (2025)")
    st.info("Label Handimanagement – 2024")
    st.divider()
    st.header("🚀 Projets phares")
    projets = ["Dashboard VTC", "Power BI Tourisme", "UX/UI Tunnel"]
    temps = [40, 30, 30]
    fig2 = px.pie(
        names=projets,
        values=temps,
        color=projets,
        color_discrete_sequence=['#ff69b4', '#ffb6c1', '#ff1493'],
        title="🚀 Répartition des projets"
    )
    fig2.update_traces(textposition='inside', textinfo='percent+label')
    fig2.update_layout(
        paper_bgcolor='#ffffff',
        font=dict(color='#800080', size=14)
    )
    st.plotly_chart(fig2, use_container_width=True)

# --- FOOTER ---
st.markdown(
    """
    <div class="footer">
        <span>© 2026 Aude Noémie Feviliye Daley – EFREI Paris</span>
        <img src="téléchargement.png">
    </div>
    """,
    unsafe_allow_html=True
)
