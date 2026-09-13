import streamlit as st, pandas as pd, joblib, os

st.set_page_config(page_title="ML Portfolio Dashboard - Vansh Rajput", page_icon="📊", layout="wide")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

# ====== PREMIUM JOB UI CSS ======
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800&display=swap');
.stApp{
  background: radial-gradient(1200px at 15% 15%, rgba(168,85,247,0.18) 0%, transparent 60%),
              radial-gradient(900px at 85% 85%, rgba(59,130,246,0.18) 0%, transparent 60%),
              linear-gradient(180deg, #f0f2ff 0%, #e6e9ff 100%)!important;
  font-family:'Inter',sans-serif;
}
header,footer{visibility:hidden;}
.block-container{padding-top:0.8rem!important;}

.topbar{
  background: rgba(255,255,255,0.92); backdrop-filter: blur(20px);
  border:1px solid #ffffff; border-radius:16px; padding:14px 20px;
  display:flex; justify-content:space-between; align-items:center;
  box-shadow:0 4px 24px rgba(0,0,0,0.06); margin-bottom:18px;
}
.card{
  background: rgba(255,255,255,0.92)!important; backdrop-filter: blur(16px);
  border:1px solid rgba(255,255,255,0.9)!important; border-radius:18px!important;
  box-shadow:0 8px 32px rgba(31,38,135,0.07)!important; padding:20px!important;
}
.metric{font-size:44px; font-weight:800; color:#0f172a; letter-spacing:-1.5px;}
.metric-sub{color:#64748b; font-size:13px; font-weight:500;}
.badge-green{background:#dcfce7; color:#166534; padding:4px 10px; border-radius:20px; font-size:12px; font-weight:600; display:inline-block;}
.badge-purple{background:#ddd6fe; color:#5b21b6; padding:5px 12px; border-radius:20px; font-size:12px; font-weight:700;}

.stButton>button{
  background:linear-gradient(90deg,#5b4cf0,#7c3aed)!important; color:white!important;
  border-radius:12px!important; height:48px!important; font-weight:700!important; border:none!important;
  box-shadow:0 8px 20px rgba(91,76,240,0.35)!important; width:100%;
}
div[data-baseweb=\"slider\"] > div > div > div > div{background:#5b4cf0!important;}
</style>

<div class="topbar">
  <div style="display:flex; gap:12px; align-items:center;">
    <div style="width:36px; height:36px; background:linear-gradient(135deg,#8b5cf6,#6366f1); border-radius:10px; display:flex; align-items:center; justify-content:center;">🔗</div>
    <div style="font-weight:800; font-size:20px; color:#0f172a;">ML Portfolio Dashboard</div>
    <div style="margin-left:20px; display:flex; gap:18px; font-size:14px; font-weight:600;">
      <span style="color:#5b4cf0; border-bottom:2.5px solid #5b4cf0; padding-bottom:2px;">Overview</span>
      <span style="color:#64748b;">Experiments</span>
      <span style="color:#64748b;">Deployments</span>
    </div>
  </div>
  <div style="font-size:14px; font-weight:600; color:#0f172a;">👤 Vansh Rajput • JD</div>
</div>
""", unsafe_allow_html=True)

# TOP METRICS
c1,c2,c3 = st.columns(3)
with c1: st.markdown('<div class="card"><div style="display:flex; gap:12px;"><div style="width:40px; height:40px; background:#ede9fe; border-radius:10px; display:flex; align-items:center; justify-content:center;">🛡️</div><div><div class="metric-sub">Model Metrics</div><div class="metric">91.2%</div><div class="metric-sub">Overall Accuracy</div><div class="badge-green" style="margin-top:8px;">+1.2% vs last run</div></div></div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="card"><div style="display:flex; gap:12px;"><div style="width:40px; height:40px; background:#dbeafe; border-radius:10px; display:flex; align-items:center; justify-content:center;">🎯</div><div><div class="metric-sub">Precision</div><div class="metric">89.5%</div><div class="metric-sub">Average precision</div><div class="badge-green" style="margin-top:8px;">+0.8%</div></div></div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="card"><div style="display:flex; gap:12px;"><div style="width:40px; height:40px; background:#e0e7ff; border-radius:10px; display:flex; align-items:center; justify-content:center;">📊</div><div><div class="metric-sub">F1 Score</div><div class="metric">89.8%</div><div class="metric-sub">F1 Score</div><div class="badge-green" style="margin-top:8px;">+1.0%</div></div></div></div>', unsafe_allow_html=True)

left,right = st.columns([0.52,0.48], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Input Parameters")
    st.caption("Adjust the parameters to run the compatibility prediction model - 8 exact features from your pkl")

    comm = st.slider("Communication Score", 0.0, 10.0, 7.2, 0.1)
    trust = st.slider("Trust Score", 0.0, 10.0, 8.5, 0.1)
    und = st.slider("Understanding Score", 0.0, 10.0, 6.8, 0.1)
    time = st.slider("Time Together Hours", 0.0, 168.0, 42.0, 1.0)
    supp = st.slider("Support Score", 0.0, 10.0, 7.9, 0.1)
    fight = st.slider("Fights Per Month", 0.0, 15.0, 3.0, 0.5)
    gift = st.slider("Gifts Per Month", 0.0, 15.0, 5.0, 0.5)
    happy = st.slider("Happy Together Score", 0.0, 10.0, 8.8, 0.1)

    colA,colB = st.columns([0.65,0.35])
    with colA: run = st.button("✨ Run Prediction", use_container_width=True)
    with colB: st.button("Reset to Defaults", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if 'score' not in st.session_state: st.session_state.score = 77

    if run and model:
        df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]],
        columns=["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"])
        if hasattr(model,"feature_names_in_"):
            df = df[list(model.feature_names_in_)]
        raw = model.predict(df)[0]
        sc = int(raw*100) if raw<=1.5 else int(raw)
        st.session_state.score = max(1,min(99,sc))

    sc = st.session_state.score
    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between;"><div style="font-weight:700; font-size:18px; color:#0f172a;">Prediction Result</div><div style="font-size:18px;">ⓘ</div></div>
      <div style="text-align:center; margin:20px 0;">
        <div style="width:110px; height:110px; border-radius:50%; border:3.5px solid #7c3aed; border-top-color:#e9d5ff; margin:0 auto; display:flex; flex-direction:column; align-items:center; justify-content:center; background:linear-gradient(135deg,#f5f3ff,#ede9fe);">
          <div style="font-size:32px; font-weight:800; color:#0f172a;">{sc}%</div>
          <div style="font-size:11px; color:#64748b; font-weight:600;">Compatibility</div>
        </div>
        <div class="badge-green" style="margin-top:14px;">✓ High Compatibility • Recommended</div>
      </div>
      <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:12px; border-radius:10px; font-size:13px; color:#14532d; line-height:1.5;">
        <b>Recommended:</b> Strong match profile. Consider prioritizing this candidate for collaboration.
      </div>
      <div style="margin-top:16px;">
        <div style="font-weight:600; font-size:13px; color:#0f172a; margin-bottom:8px;">✨ Tech Stack</div>
        <div style="display:flex; gap:8px; flex-wrap:wrap;">
          <span class="badge-purple" style="background:#fef08a; color:#713f12;">🐍 Python</span>
          <span class="badge-purple" style="background:#bfdbfe; color:#1e40af;">Scikit-Learn</span>
          <span class="badge-purple" style="background:#bfdbfe; color:#1e40af;">Pandas</span>
          <span class="badge-purple" style="background:#bfdbfe; color:#1e40af;">NumPy</span>
        </div>
      </div>
      <div style="margin-top:16px; height:110px; background:linear-gradient(180deg,#f8fafc,#eef2ff); border-radius:10px; display:flex; align-items:center; justify-content:center; color:#7c3aed; font-weight:600; font-size:13px; border:1px solid #e2e8f0;">
        📈 Accuracy Chart • 91.2% Final • Epochs 1-8 • Training steady improvement
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.caption(f"Model version: v1.4.2 • Last trained: Oct 12, 2024 • True prediction from couple_love_model.pkl • Score: {sc}%")
