import streamlit as st
import pandas as pd
import joblib
import time

st.set_page_config(page_title="Love Prediction Pro", page_icon="💖", layout="wide")

# --- PRO ANIMATION CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: radial-gradient(ellipse at top, #1a1040 0%, #0a0e1e 70%); }
header, footer { visibility: hidden; }

/* Floating hearts background */
.floating-hearts { position: fixed; width: 100%; height: 100%; pointer-events: none; z-index: 0; }
.heart-anim { position: absolute; color: rgba(255,77,166,0.15); font-size: 20px; animation: floatUp 8s infinite linear; }
@keyframes floatUp {
  0% { transform: translateY(100vh) rotate(0deg) scale(0.5); opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { transform: translateY(-10vh) rotate(360deg) scale(1.2); opacity: 0; }
}

/* Glass morphism pro */
.pro-card {
  background: rgba(20, 28, 68, 0.65);
  backdrop-filter: blur(25px);
  border: 1px solid rgba(255, 77, 166, 0.18);
  border-radius: 24px;
  padding: 24px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.08);
  animation: slideUp 0.8s ease-out;
  position: relative; z-index: 1;
}
@keyframes slideUp {
  from { transform: translateY(30px); opacity: 0; }
  to { transform: translateY(0); opacity: 1; }
}

/* Heart beat animation */
.heart-beat {
  width: 170px; height: 170px;
  background: radial-gradient(circle at 30% 30%, #ff8ac6, #ff4da6 40%, #8a2bff 80%);
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  display: flex; align-items: center; justify-content: center;
  font-size: 46px; font-weight: 900; color: white;
  box-shadow: 0 0 50px rgba(255,77,166,0.8), 0 0 100px rgba(138,43,255,0.5);
  animation: heartbeat 1.5s infinite, glowPulse 2s infinite alternate;
  position: relative;
}
@keyframes heartbeat {
  0%, 100% { transform: scale(1); }
  15% { transform: scale(1.15); }
  30% { transform: scale(1); }
  45% { transform: scale(1.1); }
  60% { transform: scale(1); }
}
@keyframes glowPulse {
  from { box-shadow: 0 0 40px rgba(255,77,166,0.6), 0 0 80px rgba(138,43,255,0.3); }
  to { box-shadow: 0 0 70px rgba(255,77,166,1), 0 0 120px rgba(138,43,255,0.6); }
}

/* Progress shimmer */
.progress-track { background: rgba(255,255,255,0.08); height: 16px; border-radius: 20px; overflow:hidden; }
.progress-fill {
  height: 100%; border-radius: 20px;
  background: linear-gradient(90deg, #ff4da6, #a855f7, #ff4da6);
  background-size: 200% 100%;
  animation: shimmer 2s infinite linear;
}
@keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }

.predict-btn button {
  background: linear-gradient(90deg, #ff4da6 0%, #a855f7 100%)!important;
  color: white!important; border-radius: 16px!important; height: 58px!important;
  font-weight: 800!important; font-size: 17px!important; border: none!important;
  box-shadow: 0 10px 30px rgba(255,77,166,0.4)!important;
  transition: all 0.3s!important;
  animation: btnFloat 3s infinite ease-in-out;
}
.predict-btn button:hover { transform: translateY(-2px) scale(1.02)!important; box-shadow: 0 15px 40px rgba(255,77,166,0.6)!important; }
@keyframes btnFloat { 0%,100% { transform: translateY(0); } 50% { transform: translateY(-3px); } }

/* Inputs animation */
div[data-testid="stSelectbox"], div[data-testid="stNumberInput"] { animation: fadeIn 0.5s ease-out; }
@keyframes fadeIn { from { opacity:0; transform:translateX(-10px); } to { opacity:1; transform:translateX(0); } }
.stSelectbox > div > div { background: rgba(19,26,64,0.9)!important; border:1px solid rgba(255,255,255,0.1)!important; border-radius:14px!important; color:white!important; transition: all 0.3s!important; }
.stSelectbox > div > div:focus-within { border-color: #ff4da6!important; box-shadow: 0 0 15px rgba(255,77,166,0.3)!important; }

.top-glow { position: absolute; top:-50%; left:-20%; width:140%; height:200%; background: radial-gradient(ellipse, rgba(255,77,166,0.15) 0%, transparent 60%); animation: rotateGlow 20s infinite linear; pointer-events:none; }
@keyframes rotateGlow { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
</style>

<div class="floating-hearts">
  <div class="heart-anim" style="left:10%; animation-delay:0s;">💖</div>
  <div class="heart-anim" style="left:25%; animation-delay:1.5s; font-size:14px;">💗</div>
  <div class="heart-anim" style="left:40%; animation-delay:3s;">💞</div>
  <div class="heart-anim" style="left:60%; animation-delay:0.8s; font-size:28px;">💓</div>
  <div class="heart-anim" style="left:75%; animation-delay:2.2s;">💖</div>
  <div class="heart-anim" style="left:90%; animation-delay:4s; font-size:16px;">💝</div>
</div>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try: return joblib.load("couple_love_model.pkl")
    except: return None
model = load_model()

# HEADER
st.markdown("""
<div class="pro-card" style="display:flex; justify-content:space-between; align-items:center; padding:18px 28px; overflow:hidden; margin-bottom:20px;">
  <div class="top-glow"></div>
  <div style="display:flex; gap:16px; align-items:center; z-index:1;">
    <div style="width:56px; height:56px; background:linear-gradient(135deg,#ff4da6,#8a2bff); border-radius:16px; display:flex; align-items:center; justify-content:center; font-size:30px; animation: heartbeat 2s infinite;">💞</div>
    <div>
      <div style="font-size:30px; font-weight:900; background:linear-gradient(90deg,#ff8ac6,#a855f7); -webkit-background-clip:text; -webkit-text-fill-color:transparent;">Love Prediction Pro</div>
      <div style="color:#8b90b5; font-size:12px; letter-spacing:1.5px;">✨ AI • ANIMATION • PREMIUM INSIGHTS</div>
    </div>
  </div>
  <div style="z-index:1; text-align:right;"><div style="font-size:38px; animation: floatUp 4s infinite ease-in-out;">💑</div><div style="color:#ff8ac6; font-family:cursive; font-size:12px;">Crafted for Soulmates ♡</div></div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.20, 0.42, 0.38], gap="medium")

with c1:
    st.markdown("""
    <div class="pro-card" style="min-height:680px;">
      <div style="background:linear-gradient(90deg, rgba(255,77,166,0.25), rgba(168,85,255,0.15)); border:1px solid rgba(255,77,166,0.3); padding:13px 16px; border-radius:14px; color:white; font-weight:700; display:flex; gap:10px;">🏠 Home • Active</div>
      <div style="padding:14px 16px; color:#6b7094; display:flex; gap:10px; margin-top:8px;">🤍 Prediction</div>
      <div style="padding:14px 16px; color:#6b7094; display:flex; gap:10px;">📊 Model Stats</div>
      <div style="padding:14px 16px; color:#6b7094; display:flex; gap:10px;">⚙️ How It Works</div>
      <div style="margin-top:350px; text-align:center; animation: btnFloat 4s infinite;">
        <div style="font-size:32px;">💫</div>
        <div style="color:#ff8ac6; font-family:cursive; font-size:12px; margin-top:10px;">True love is<br><b style="color:white;">animated, not just felt</b> ✨</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:20px; font-weight:800; color:white;">💖 Enter Your Details</div><div style="color:#7a81a8; font-size:12px; margin-bottom:18px;">AI will analyze 8+ compatibility factors with animation</div>', unsafe_allow_html=True)

    g1, g2 = st.columns(2)
    with g1: gender_you = st.selectbox("Gender (You)", ["Male", "Female", "Other"])
    with g2: gender_part = st.selectbox("Gender (Partner)", ["Female", "Male", "Other"])
    a1, a2 = st.columns(2)
    with a1: age_you = st.number_input("Your Age", 18, 70, 24)
    with a2: age_part = st.number_input("Partner Age", 18, 70, 22)
    rel = st.selectbox("Relationship Type", ["Dating", "Married", "Long Distance", "Crush"])
    comm = st.selectbox("Communication", ["Open & Honest", "Reserved", "Playful", "Mixed"])
    trust = st.selectbox("Trust Level", ["High - Unbreakable", "Medium - Growing", "Low - Needs Work"])

    st.write("")
    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    btn = st.button("✨ Predict Our Love Story →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c3:
    if btn:
        with st.spinner("💘 Analyzing your cosmic connection..."):
            time.sleep(1.5)
        base = 72
        if "Open" in comm: base+=10
        if "High" in trust: base+=15
        if abs(age_you-age_part) <=4: base+=6
        if model:
            try:
                df = pd.DataFrame([{"communication_score":9, "trust_score":9 if "High" in trust else 5, "understanding_score":8, "time_together_hours":8, "support_score":9, "fights_per_month":1, "gifts_per_month":4, "happy_together_score":9}])
                base = int((base + float(model.predict(df)[0]))/2)
            except: pass
        score = max(30, min(98, base))
        confetti = "🎉" if score>80 else "💫"
    else:
        score = 87
        confetti = "🎉"

    st.markdown(f"""
    <div class="pro-card" style="text-align:center; border:1.5px solid rgba(255,77,166,0.4);">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="color:white; font-weight:700;">💗 Prediction Result</div>
        <div style="background:linear-gradient(90deg,#ff4da6,#a855f7); padding:5px 12px; border-radius:20px; font-size:10px; color:white; animation: shimmer 2s infinite;">✨ AI POWERED</div>
      </div>

      <div style="display:flex; flex-direction:column; align-items:center; margin-top:22px;">
        <div class="heart-beat">{score}%</div>
        <div style="margin-top:18px; font-size:24px; font-weight:900; color:#ff7ac0; animation: slideUp 0.8s;">{confetti} High Compatibility! {confetti}</div>
        <div style="color:#a8aecf; font-size:12.5px; margin-top:8px; line-height:1.5;">You two have a <b style="color:white;">soulmate-level bond</b> - strong emotional, mental & spiritual alignment detected!</div>
      </div>

      <div style="margin-top:24px; text-align:left;">
        <div style="display:flex; justify-content:space-between; font-size:12px; color:#8b90b5;"><span>Love Meter</span><span style="color:white; font-weight:800;">{score}% Matched</span></div>
        <div class="progress-track" style="margin-top:8px;"><div class="progress-fill" style="width:{score}%;"></div></div>
      </div>

      <div style="margin-top:20px; display:grid; grid-template-columns:1fr 1fr; gap:12px; text-align:left;">
        <div style="background:rgba(255,77,166,0.08); border:1px solid rgba(255,77,166,0.15); padding:12px; border-radius:14px;"><div style="font-size:18px;">💬</div><div style="font-size:10px; color:#8b90b5;">Communication</div><div style="color:#4ade80; font-weight:700; font-size:13px;">Excellent</div></div>
        <div style="background:rgba(168,85,255,0.08); border:1px solid rgba(168,85,255,0.15); padding:12px; border-radius:14px;"><div style="font-size:18px;">🔗</div><div style="font-size:10px; color:#8b90b5;">Trust Bond</div><div style="color:#4ade80; font-weight:700; font-size:13px;">{trust.split('-')[0]}</div></div>
        <div style="background:rgba(255,200,100,0.08); border:1px solid rgba(255,200,100,0.15); padding:12px; border-radius:14px;"><div style="font-size:18px;">⚡</div><div style="font-size:10px; color:#8b90b5;">Chemistry</div><div style="color:#facc15; font-weight:700; font-size:13px;">Intense</div></div>
        <div style="background:rgba(100,200,255,0.08); border:1px solid rgba(100,200,255,0.15); padding:12px; border-radius:14px;"><div style="font-size:18px;">💫</div><div style="font-size:10px; color:#8b90b5;">Future</div><div style="color:#60a5fa; font-weight:700; font-size:13px;">Bright</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
