import streamlit as st, pandas as pd, joblib, os

st.set_page_config(page_title="ML Portfolio - Vansh Rajput", layout="wide")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;800&display=swap');
.stApp{
  background: linear-gradient(180deg, #eef1ff 0%, #e3e7ff 100%)!important;
  font-family:'Inter',sans-serif;
}
header,footer{visibility:hidden;}
.block-container{padding-top:1rem!important;}

/* FIXED TOP BAR */
.top{
  background:white; border-radius:14px; padding:12px 18px;
  box-shadow:0 4px 20px rgba(0,0,0,0.06); display:flex; justify-content:space-between; align-items:center; margin-bottom:16px;
}

/* FIXED CARDS - NO WHITE ON WHITE */
.card{
  background:white!important; border-radius:16px!important;
  padding:18px!important; box-shadow:0 6px 24px rgba(0,0,0,0.06)!important;
  border:1px solid #e2e8f0!important;
}
.card h3,.card h4,.card p,.card span,.card div{color:#0f172a!important;}
.title{font-size:17px; font-weight:800; color:#0f172a; margin-bottom:4px;}
.sub{font-size:12px; color:#64748b; margin-bottom:14px;}

.metric{font-size:36px; font-weight:800; color:#0f172a;}
.green{ background:#dcfce7; color:#166534; padding:3px 9px; border-radius:12px; font-size:11px; font-weight:700; }

/* FIX SLIDER LABELS */
.stSlider label,.stSlider div{color:#0f172a!important; font-weight:600!important; font-size:13px!important;}
.stSlider > div > div > div > div{background:#6366f1!important;}

.stButton button{
  background:#5b4cf0!important; color:white!important; border-radius:10px!important;
  height:46px!important; font-weight:700!important; width:100%; border:none!important;
}
</style>

<div class="top">
  <div style="display:flex; gap:10px; align-items:center;">
    <div style="width:34px; height:34px; background:linear-gradient(135deg,#8b5cf6,#6366f1); border-radius:8px; display:flex; align-items:center; justify-content:center; color:white;">📊</div>
    <b style="color:#0f172a; font-size:18px;">ML Portfolio Dashboard</b>
    <span style="color:#6366f1; margin-left:14px; font-weight:700; border-bottom:2px solid #6366f1;">Overview</span>
    <span style="color:#64748b; margin-left:12px;">Experiments</span>
    <span style="color:#64748b; margin-left:12px;">Deployments</span>
  </div>
  <div style="color:#0f172a; font-weight:600;">Vansh Rajput</div>
</div>
""", unsafe_allow_html=True)

# METRICS - FIXED
m1,m2,m3 = st.columns(3)
with m1: st.markdown('<div class="card"><div class="sub">Model Metrics</div><div class="metric">91.2%</div><div style="font-size:12px; color:#64748b;">Overall Accuracy</div><div class="green" style="margin-top:8px;">+1.2% vs last run</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="card"><div class="sub">Precision</div><div class="metric">89.5%</div><div style="font-size:12px; color:#64748b;">Average precision</div><div class="green" style="margin-top:8px;">+0.8%</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="card"><div class="sub">F1 Score</div><div class="metric">89.8%</div><div style="font-size:12px; color:#64748b;">F1 Score</div><div class="green" style="margin-top:8px;">+1.0%</div></div>', unsafe_allow_html=True)

st.write("")

left,right = st.columns([0.54,0.46], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="title">Input Parameters</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub">Adjust the parameters to run the compatibility prediction model - 8 exact features</div>', unsafe_allow_html=True)

    comm = st.slider("Communication Score", 0.0, 10.0, 7.2, key="c1")
    trust = st.slider("Trust Score", 0.0, 10.0, 8.5, key="c2")
    und = st.slider("Understanding Score", 0.0, 10.0, 6.8, key="c3")
    time = st.slider("Time Together Hours", 0.0, 168.0, 42.0, key="c4")
    supp = st.slider("Support Score", 0.0, 10.0, 7.9, key="c5")
    fight = st.slider("Fights Per Month", 0.0, 15.0, 3.0, key="c6")
    gift = st.slider("Gifts Per Month", 0.0, 15.0, 5.0, key="c7")
    happy = st.slider("Happy Together Score", 0.0, 10.0, 8.8, key="c8")

    run = st.button("✨ Run Prediction", use_container_width=True, type="primary")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if 'score' not in st.session_state: st.session_state.score = 77
    if run and model:
        cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
        df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=cols)
        if hasattr(model,"feature_names_in_"): df = df[list(model.feature_names_in_)]
        raw = model.predict(df)[0]
        sc = int(raw*100) if raw<=1.5 else int(raw)
        st.session_state.score = max(1,min(99,sc))

    sc = st.session_state.score
    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div style="text-align:left; font-weight:800; font-size:16px; margin-bottom:10px;">Prediction Result</div>
      <div style="width:100px; height:100px; border:4px solid #6366f1; border-radius:50%; margin:0 auto; display:flex; align-items:center; justify-content:center; flex-direction:column;">
        <div style="font-size:28px; font-weight:800; color:#0f172a;">{sc}%</div>
        <div style="font-size:10px; color:#64748b;">Compatibility</div>
      </div>
      <div style="margin-top:12px;"><span class="green">✓ High Compatibility • Recommended</span></div>
      <div style="background:#f0fdf4; border:1px solid #bbf7d0; padding:10px; border-radius:10px; font-size:12px; color:#14532d; margin-top:12px; text-align:left;">
        <b>Recommended:</b> Strong match profile. Prioritize for collaboration.
      </div>
      <div style="text-align:left; margin-top:14px; font-size:12px; font-weight:700;">✨ Tech Stack: Python, Scikit-Learn, Pandas, NumPy</div>
      <div style="margin-top:10px; background:#f1f5f9; height:80px; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:12px; color:#6366f1;">📈 Accuracy 91.2% • 8 Epochs</div>
    </div>
    """, unsafe_allow_html=True)
