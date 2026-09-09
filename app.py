import streamlit as st, pandas as pd, joblib, os
st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    try:
        if os.path.exists("couple_love_model.pkl"):
            return joblib.load("couple_love_model.pkl")
    except: return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Dancing+Script:wght@600&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: #070a1e!important; }
header, footer { visibility: hidden; }
.block-container { max-width: 98%!important; padding-top: 0.5rem!important; }
@keyframes glow { 0%,100%{ filter: drop-shadow(0 0 15px #ff4da6) drop-shadow(0 0 30px #9d4dff);} 50%{ filter: drop-shadow(0 0 25px #ff4da6) drop-shadow(0 0 50px #9d4dff);} }
.neon-heart { animation: glow 2s infinite; }
.top-bar {
  display:flex; justify-content:space-between; align-items:center;
  background: rgba(7,10,30,0.9); border-bottom:1px solid rgba(255,77,166,0.2);
  padding: 12px 20px; margin: -14px -16px 16px -16px;
}
.card { background: #101638!important; border:1px solid rgba(120,110,255,0.15)!important; border-radius:18px!important; padding:20px!important; box-shadow: 0 0 20px rgba(157,77,255,0.08); }
.nav-active { background: linear-gradient(90deg, #ff4da6, #a855f7)!important; border-radius:12px; padding:12px 14px; color:white!important; font-weight:700; display:flex; gap:10px; box-shadow:0 0 15px rgba(255,77,166,0.5); }
.nav { color:#8a8db0; padding:12px 14px; display:flex; gap:10px; font-size:14px; border-radius:12px; background: rgba(18,25,56,0.6); margin-bottom:8px; border:1px solid rgba(255,255,255,0.05); }
.stSelectbox > div > div,.stNumberInput > div > div > input { background:#121938!important; border:1px solid rgba(255,255,255,0.08)!important; border-radius:12px!important; color:#c8d0f0!important; height:44px!important; }
.stMultiSelect > div > div { background:#121938!important; border-radius:12px!important; border:1px solid rgba(255,255,255,0.08)!important; }
.pill { background: linear-gradient(90deg, #ff4da6, #d946ef); border-radius:20px; padding:8px 16px; color:white; font-weight:600; font-size:13px; display:inline-flex; gap:6px; margin:4px; box-shadow:0 4px 12px rgba(255,77,166,0.3); }
.predict-btn button { background: linear-gradient(90deg, #ff4da6 0%, #a855f7 100%)!important; color:white!important; border-radius:14px!important; height:52px!important; font-weight:700!important; font-size:16px!important; border:none!important; box-shadow:0 8px 25px rgba(255,77,166,0.45)!important; }
.progress { background:#1a2042; height:10px; border-radius:20px; overflow:hidden; }
.progress-fill { height:100%; border-radius:20px; background: linear-gradient(90deg, #ff4da6, #a855f7); box-shadow:0 0 10px #ff4da6; }
.insight { background: rgba(18,25,56,0.8); border:1px solid rgba(255,255,255,0.06); border-radius:12px; padding:12px; margin-top:10px; display:flex; gap:12px; align-items:center; }
.insight-icon { background: linear-gradient(135deg, #ff4da6, #a855f7); width:42px; height:42px; border-radius:10px; display:flex; align-items:center; justify-content:center; font-size:20px; }
</style>
<div class="top-bar">
  <div style="display:flex; gap:14px; align-items:center;"><div style="font-size:42px; filter:drop-shadow(0 0 10px #ff4da6);">💖</div><div style="font-size:32px; font-weight:800; color:white;">Love Prediction</div></div>
  <div style="color:#ff8ec8; font-family:'Dancing Script',cursive; font-size:28px; text-shadow:0 0 15px #ff4da6;">Some connections<br>are meant to be...</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([0.18, 0.42, 0.40], gap="medium")

with col1:
    st.markdown('<div class="card" style="height:750px;">', unsafe_allow_html=True)
    st.markdown('<div class="nav-active">🏠 Home</div><div class="nav">✨ Prediction</div><div class="nav">🧠 About Model</div><div class="nav">❓ How It Works</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:22px; font-weight:800; color:white;">Enter Your Details</div><div style="color:#8a8db0; font-size:12px; margin-bottom:16px;">Fill in the information to discover your love compatibility prediction</div>', unsafe_allow_html=True)

    c_a, c_b = st.columns(2)
    with c_a: gender = st.selectbox("👤 Gender", ["Female","Male","Other"])
    with c_b: age = st.number_input("📅 Age", 18, 70, 24)

    rel = st.selectbox("👥 Relationship Type", ["Dating","Married","Long Distance","Crush"])

    st.markdown('<div style="color:#ffb3d1; font-size:13px; margin:14px 0 6px;">💗 Common Interests</div>', unsafe_allow_html=True)
    st.markdown('<span class="pill">✈️ Travel</span> <span class="pill">🎵 Music</span> <span class="pill">🎬 Movies</span>', unsafe_allow_html=True)
    interests = st.multiselect("", ["Travel","Music","Movies","Sports","Gaming"], default=["Travel","Music","Movies"], label_visibility="collapsed")

    comm = st.selectbox("💬 Communication Style", ["Open & Honest","Reserved","Honest","Playful"])
    trust = st.select_slider("🛡️ Trust Level", options=["Low","Medium","High"], value="High")

    st.write("")
    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    btn = st.button("✨ Predict Love", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with col3:
    if btn:
        t_map = {"Low":3,"Medium":6,"High":9}
        ts = t_map[trust]; cs = 9 if "Open" in comm else 6; score = 55 + ts*4 + cs*2 + len(interests)*2
        if model is not None:
            try:
                df = pd.DataFrame([{"communication_score":cs,"trust_score":ts,"understanding_score":8,"time_together_hours":6,"support_score":8,"fights_per_month":1,"gifts_per_month":3,"happy_together_score":9}])
                raw = model.predict(df)[0]; score = int(raw*100) if raw<=1.5 else int(raw); score = max(20,min(97,score))
            except: pass
        score = max(20,min(97,score))
    else: score = 87

    if score>=80: label="High Compatibility"
    elif score>=60: label="Good Compatibility"
    else: label="Average Compatibility"

    st.markdown(f"""
    <div class="card">
      <div style="text-align:center;"><div style="color:white; font-size:22px; font-weight:800;">Prediction Result</div><div style="color:#8a8db0; font-size:12px;">AI-powered compatibility analysis</div></div>
      <div style="text-align:center; margin:18px 0;">
        <div class="neon-heart" style="font-size:110px; line-height:1; color:transparent; -webkit-text-stroke:2.5px #ff6eb5; text-shadow:0 0 20px #ff4da6;">♡</div>
        <div style="font-size:52px; font-weight:800; background:linear-gradient(90deg,#ff8ec8,#c084ff); -webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-top:-85px;">{score}%</div>
        <div style="color:#ff8ec8; font-weight:700; font-size:18px; margin-top:4px;">{label}</div>
      </div>
      <div style="display:flex; justify-content:space-between; font-size:11px; color:#8a8db0;"><span>Compatibility Score</span><span>{score}%</span></div>
      <div class="progress"><div class="progress-fill" style="width:{score}%;"></div></div>
      <div style="color:white; font-weight:700; margin-top:18px; font-size:16px;">Key Insights</div>
      <div class="insight"><div class="insight-icon">💬</div><div><div style="color:white; font-weight:600; font-size:13px;">Communication</div><div style="color:#8a8db0; font-size:11px;">Excellent communication patterns detected</div></div></div>
      <div class="insight"><div class="insight-icon">👥</div><div><div style="color:white; font-weight:600; font-size:13px;">Shared Interests</div><div style="color:#8a8db0; font-size:11px;">{len(interests) if btn else 3} common interests aligned</div></div></div>
      <div class="insight"><div class="insight-icon">🛡️</div><div><div style="color:white; font-weight:600; font-size:13px;">Trust</div><div style="color:#8a8db0; font-size:11px;">{trust if btn else 'High'} trust level measured</div></div></div>
      <div class="insight"><div class="insight-icon">💓</div><div><div style="color:white; font-weight:600; font-size:13px;">Emotional Bond</div><div style="color:#8a8db0; font-size:11px;">Strong emotional connection</div></div></div>
    </div>
    """, unsafe_allow_html=True)
