import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

# ---- DARK NEON CSS ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;700&display=swap');
.stApp { background: #080810; font-family: 'Poppins'; }
[data-testid="stSidebar"] { display:none; }
.card {
  background: rgba(20,20,35,0.8); border: 1px solid rgba(255,80,200,0.3);
  border-radius: 22px; padding: 22px; backdrop-filter: blur(15px);
  box-shadow: 0 0 30px rgba(255,0,150,0.15);
}
.glow-heart {
  background: radial-gradient(circle at 30% 30%, #ff5ac8, #8a2bff);
  width: 160px; height: 150px; margin: auto; border-radius: 30% 30% 50% 50%;
  display: flex; align-items: center; justify-content: center;
  color: white; font-size: 48px; font-weight: 900;
  box-shadow: 0 0 50px #ff3b9d, inset 0 0 20px rgba(255,255,255,0.5);
  clip-path: path('M 80 25 C 40 -10 0 30 80 120 C 160 30 120 -10 80 25 Z');
  /* Fallback heart shape */
  border-radius: 50%; /* simple fallback */
}
.pink-btn button {
  background: linear-gradient(90deg, #ff4da6, #8a2bff)!important;
  color: white!important; border-radius: 14px!important; height: 54px;
  font-weight: 700; font-size: 17px; border: none!important;
  box-shadow: 0 5px 20px rgba(255,77,166,0.4);
}
.tag { background: rgba(255,77,166,0.15); border:1px solid #ff4da6; color:#ff8ec7; padding:5px 12px; border-radius:20px; font-size:12px; margin:2px; display:inline-block; }
.tag.active { background: linear-gradient(90deg,#ff4da6,#8a2bff); color:white; }
.progress-track { background: rgba(255,255,255,0.1); height: 8px; border-radius: 10px; }
.progress-fill { background: linear-gradient(90deg,#ff4da6,#8a2bff); height: 100%; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model(): return joblib.load("couple_love_model.pkl")
model = load_model()

# Header
st.markdown("""
<div style="display:flex; justify-content:space-between; align-items:center; background:rgba(20,20,35,0.6); padding:12px 25px; border-radius:15px; border:1px solid rgba(255,255,255,0.1);">
  <div style="display:flex; align-items:center; gap:12px;"><span style="font-size:30px;">💠</span><div><h2 style="margin:0; color:#ff6ec7;">Love Prediction</h2><p style="margin:0; color:#8a8aa8; font-size:13px;">Some connections are meant to be.</p></div></div>
  <div style="color:white; display:flex; gap:18px;">🔔 ⚙️ 🟣</div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.9, 1.3, 1.6])

with c1:
    st.markdown('<div class="card">💠 <b style="color:#d8a0ff;">Love Prediction</b><br><br><div style="background:linear-gradient(90deg,#ff4da6,#8a2bff); padding:10px 15px; border-radius:12px; color:white;">🏠 Home</div><br>♡ Prediction<br><br>🧠 About Model<br><br>❓ How It Works<br><br><br><br><br><div style="color:#888;">🟣 Alex Morgan</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><h3>Enter Your Details <span style="float:right;">📝</span></h3>', unsafe_allow_html=True)
    gender = st.radio("Gender", ["Male","Female","Other"], horizontal=True, index=1)
    age = st.number_input("Age", 18, 60, 26)
    rel = st.selectbox("Relationship Type", ["Dating","Married","Long Distance","Crush"])
    st.write("Common Interests")
    interests = st.multiselect("", ["Music","Travel","Food","Arts","Fitness"], default=["Music","Travel","Food"], label_visibility="collapsed")

    comm_per = st.slider("Communication Style", 0, 100, 75)
    trust_per = st.slider("Trust Level", 0, 100, 82)

    st.markdown('<div class="pink-btn">', unsafe_allow_html=True)
    do_pred = st.button("Generate Prediction", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c3:
    # Prediction logic
    if do_pred:
        comm_score = int(comm_per/10)
        trust_score = int(trust_per/10)
        df = pd.DataFrame([{
            "communication_score": max(1,comm_score), "trust_score": max(1,trust_score),
            "understanding_score": 8 if len(interests)>=3 else 6,
            "time_together_hours": 7, "support_score": 8,
            "fights_per_month": 2, "gifts_per_month": len(interests)+1,
            "happy_together_score": 9
        }])
        score = max(0, min(100, float(model.predict(df)[0])))
    else:
        score = 87

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between;"><h3>Prediction Result</h3>✨</div>
      <div style="text-align:center; margin:15px 0;">
        <div style="font-size:60px; color:#ff7ad0; text-shadow: 0 0 20px #ff3b9d;">♡</div>
        <div style="font-size:62px; font-weight:900; color:white; margin-top:-50px; text-shadow:0 0 15px #ff4da6;">{int(score)}%</div>
        <h3 style="color:#c084ff; margin-top:10px;">High Compatibility</h3>
      </div>
      <div style="display:flex; justify-content:space-between; font-size:13px; color:#aaa;"><span>Compatibility Score</span><span>{int(score)}/100</span></div>
      <div class="progress-track"><div class="progress-fill" style="width:{score}%"></div></div>
      <br><b>Key Insights</b>
      <div style="display:grid; grid-template-columns:1fr 1fr; gap:10px; margin:10px 0;">
        <div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:12px;">💬 Communication <br><span style="background:#3a3; color:white; padding:2px 8px; border-radius:10px; font-size:12px;">High</span></div>
        <div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:12px;">🔗 Shared Interests <br><span style="background:#d46cff; color:white; padding:2px 8px; border-radius:10px; font-size:12px;">High</span></div>
        <div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:12px;">🛡️ Trust <br><span style="background:#c084ff; color:white; padding:2px 8px; border-radius:10px; font-size:12px;">High</span></div>
        <div style="background:rgba(255,255,255,0.05); padding:10px; border-radius:12px;">💖 Emotional Bond <br><span style="background:#ff6eb4; color:white; padding:2px 8px; border-radius:10px; font-size:12px;">High</span></div>
      </div>
      <div style="background:rgba(255,255,255,0.05); padding:12px; border-radius:12px;">
        <b>💡 Why This Prediction</b>
        <ul style="font-size:12px; color:#aaa; padding-left:15px;">
          <li>Strong communication patterns align with mutual engagement.</li>
          <li>Shared interests strengthen emotional resonance.</li>
          <li>Consistent trust indicators suggest stability.</li>
          <li>Emotional bond trending upward +12% this month.</li>
        </ul>
      </div>
      <br><div style="text-align:center; border:1px solid #ff4da6; padding:8px; border-radius:12px; color:#ff8ec7;">View Detailed Report →</div>
    </div>
    """, unsafe_allow_html=True)

# Ab bas ye file + model pkl GitHub pe daal ke deploy kar de. Live link aate hi bhej!
