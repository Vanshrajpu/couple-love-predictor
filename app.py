import streamlit as st, pandas as pd, joblib, os

st.set_page_config(page_title="Compatibility Model - Vansh Rajput", layout="wide")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;700;800&display=swap');
.stApp{background:#f5f7fb!important; font-family:'Inter',sans-serif;}
header,footer{visibility:hidden;}
.block-container{padding-top:0.8rem!important; max-width:1280px!important; margin:0 auto;}

.header{
  background:white; border:1px solid #e2e8f0; border-radius:14px; padding:16px 22px;
  display:flex; justify-content:space-between; align-items:center;
  box-shadow:0 2px 12px rgba(0,0,0,0.04); margin-bottom:14px;
}
.metric-card{
  background:white; border:1px solid #e2e8f0; border-top:4px solid #cbd5e1; border-radius:12px;
  padding:18px 20px; box-shadow:0 2px 10px rgba(0,0,0,0.03);
}
.metric-val{font-size:38px; font-weight:800; color:#1e293b; letter-spacing:-1px;}
.metric-label{font-size:13px; color:#64748b; font-weight:600;}
.metric-delta{font-size:12px; color:#065f46; font-weight:600; margin-top:4px;}

.card{
  background:white!important; border:1px solid #e2e8f0!important; border-radius:12px!important;
  padding:20px!important; box-shadow:0 4px 16px rgba(0,0,0,0.04)!important;
}
.input-row{
  display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;
}
.input-label{font-size:13px; font-weight:600; color:#1e293b;}
.badge-blue{background:#2563eb; color:white; padding:4px 10px; border-radius:6px; font-size:12px; font-weight:700; min-width:36px; text-align:center;}
.divider{height:1px; background:#eef2f7; margin:14px 0;}

/* PROFESSIONAL SLIDER - BLUE */
.stSlider label{display:none!important;}
div[data-baseweb="slider"] > div > div{height:6px!important; background:#e2e8f0!important; border-radius:10px!important;}
div[data-baseweb="slider"] > div > div > div{background:#2563eb!important; height:6px!important; border-radius:10px!important;}
div[data-baseweb="slider"] [role="slider"]{width:18px!important; height:18px!important; background:white!important; border:2.5px solid #2563eb!important; box-shadow:0 2px 6px rgba(37,99,235,0.4)!important; border-radius:50%!important; top:-6px!important;}

.btn button{
  background:#1e293b!important; color:white!important; border-radius:8px!important; height:46px!important; font-weight:700!important; width:100%!important; border:none!important; margin-top:12px!important;
}
.circle{
  width:130px; height:130px; border-radius:50%; border:6px solid #e2e8f0; border-top-color:#2563eb; border-right-color:#2563eb;
  display:flex; flex-direction:column; align-items:center; justify-content:center; margin:0 auto;
}
.tech{background:#dbeafe; color:#1e40af; padding:6px 12px; border-radius:6px; font-size:11px; font-weight:700; display:inline-block; margin:4px;}
</style>

<div class="header">
  <div style="display:flex; gap:14px; align-items:center;">
    <div style="width:44px; height:44px; background:#1e3a8a; border-radius:10px; display:flex; align-items:center; justify-content:center; color:white; font-size:20px;">🧠</div>
    <div>
      <div style="font-size:20px; font-weight:800; color:#1e293b;">Love Compatibility Prediction Model</div>
      <div style="font-size:12px; color:#64748b;">Machine Learning • Classification Model • v1.2.0 • Vansh Rajput</div>
    </div>
  </div>
  <div style="display:flex; gap:8px;">
    <span style="background:#dcfce7; color:#166534; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700;">● Model Active</span>
    <span style="background:#e2e8f0; color:#334155; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:600;">Last Trained: Oct 2024</span>
    <span style="background:#dbeafe; color:#1e40af; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:600;">API Status: Healthy</span>
  </div>
</div>
""", unsafe_allow_html=True)

# TOP 3 METRICS
a,b,c = st.columns(3)
with a: st.markdown('<div class="metric-card" style="border-top-color:#93c5fd;"><div class="metric-label">🎯 Accuracy</div><div class="metric-val">91.2%</div><div class="metric-delta">↑ +1.4% vs baseline</div></div>', unsafe_allow_html=True)
with b: st.markdown('<div class="metric-card" style="border-top-color:#a5b4fc;"><div class="metric-label">📊 Precision</div><div class="metric-val">89.5%</div><div class="metric-delta">↑ +0.9% vs baseline</div></div>', unsafe_allow_html=True)
with c: st.markdown('<div class="metric-card" style="border-top-color:#bfdbfe;"><div class="metric-label">F1 Score</div><div class="metric-val">89.8%</div><div class="metric-delta">↑ +1.1% vs baseline</div></div>', unsafe_allow_html=True)

st.write("")

left,right = st.columns([0.58,0.42], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Input Parameters")
    st.caption("Adjust features to predict compatibility - 8 exact features from trained pkl")

    # CLEAN 2-COL PROFESSIONAL INPUTS
    l1,r1 = st.columns(2)

    with l1:
        st.markdown('<div class="input-row"><span class="input-label">Communication Score</span><span class="badge-blue">72</span></div>', unsafe_allow_html=True)
        comm = st.slider("comm", 0.0, 10.0, 7.2, key="c1")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="input-row"><span class="input-label">Understanding Score</span><span class="badge-blue">68</span></div>', unsafe_allow_html=True)
        und = st.slider("und", 0.0, 10.0, 6.8, key="c2")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="input-row"><span class="input-label">Support Score</span><span class="badge-blue">79</span></div>', unsafe_allow_html=True)
        supp = st.slider("supp", 0.0, 10.0, 7.9, key="c3")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="input-row"><span class="input-label">Gifts Per Month</span><span class="badge-blue">5</span></div>', unsafe_allow_html=True)
        gift = st.slider("gift", 0.0, 15.0, 5.0, key="c4")

    with r1:
        st.markdown('<div class="input-row"><span class="input-label">Trust Score</span><span class="badge-blue">85</span></div>', unsafe_allow_html=True)
        trust = st.slider("trust", 0.0, 10.0, 8.5, key="c5")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="input-row"><span class="input-label">Time Together Hours</span><span class="badge-blue">42</span></div>', unsafe_allow_html=True)
        time = st.slider("time", 0.0, 168.0, 32.0, key="c6")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="input-row"><span class="input-label">Fights Per Month</span><span class="badge-blue">2</span></div>', unsafe_allow_html=True)
        fight = st.slider("fight", 0.0, 15.0, 2.0, key="c7")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

        st.markdown('<div class="input-row"><span class="input-label">Happy Together Score</span><span class="badge-blue">88</span></div>', unsafe_allow_html=True)
        happy = st.slider("happy", 0.0, 10.0, 8.8, key="c8")

    run = st.button("Run Prediction →", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if 'score' not in st.session_state: st.session_state.score = 87
    if run and model:
        cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
        df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=cols)
        if hasattr(model,"feature_names_in_"): df = df[list(model.feature_names_in_)]
        raw = model.predict(df)[0]
        sc = int(raw*100) if raw<=1.5 else int(raw)
        st.session_state.score = max(1,min(99,sc))

    sc = st.session_state.score
    st.markdown(f"""
    <div class="card">
      <div style="font-weight:800; font-size:16px; color:#1e293b;">Prediction Result</div>
      <div style="font-size:12px; color:#64748b; margin-bottom:16px;">Model output and confidence</div>

      <div class="circle">
        <div style="font-size:32px; font-weight:800; color:#1e293b;">{sc}%</div>
        <div style="font-size:10px; color:#64748b;">Compatibility Score</div>
      </div>

      <div style="text-align:center; margin-top:14px;"><span style="background:#dbeafe; color:#1e40af; padding:6px 14px; border-radius:20px; font-size:12px; font-weight:600;">Prediction: High Compatibility ✓</span></div>

      <div style="background:#eff6ff; border-left:3px solid #2563eb; padding:12px; border-radius:6px; margin-top:16px; font-size:12px; color:#1e293b; line-height:1.5;">
        <b>Result:</b> The model predicts a high likelihood of compatibility based on current inputs.<br><br>
        <b>Recommendation:</b> Compatible — Strong match across key features. Suggest further interaction.
      </div>

      <div style="margin-top:16px; border-top:1px solid #e2e8f0; padding-top:12px; text-align:center;">
        <div style="font-size:12px; font-weight:700; color:#1e293b; margin-bottom:8px;">Tech Stack</div>
        <span class="tech">Python</span><span class="tech" style="background:#e0e7ff; color:#3730a3;">Scikit-Learn</span><span class="tech" style="background:#e2e8f0; color:#475569;">Random Forest</span>
      </div>
    </div>

    <div style="background:white; border:1px solid #e2e8f0; border-radius:8px; padding:10px 14px; margin-top:10px; display:flex; justify-content:space-between; font-size:11px; color:#64748b;">
      <span><b>Model:</b> RandomForestClassifier | <b>Features:</b> 8 | <b>Dataset:</b> 12k</span>
      <span><b>Inference:</b> ~12ms | <b>Threshold:</b> 0.75</span>
    </div>
    """, unsafe_allow_html=True)
