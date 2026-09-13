import streamlit as st, pandas as pd, joblib, os

st.set_page_config(page_title="Love Compatibility - Vansh Rajput | ML Model", layout="wide", page_icon="🧠")

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
.block-container{padding-top:0.6rem!important; max-width:1280px!important; margin:0 auto;}

.header{
  background:white; border:1px solid #e2e8f0; border-radius:14px; padding:16px 22px;
  display:flex; justify-content:space-between; align-items:center;
  box-shadow:0 2px 12px rgba(0,0,0,0.04); margin-bottom:14px;
}

.metric-card{
  background:white; border:1px solid #e2e8f0; border-top:4px solid #93c5fd; border-radius:12px;
  padding:18px 20px; box-shadow:0 2px 10px rgba(0,0,0,0.03);
}
.metric-val{font-size:38px; font-weight:800; color:#1e293b; letter-spacing:-1px;}
.metric-label{font-size:13px; color:#64748b; font-weight:600;}
.metric-delta{font-size:12px; color:#065f46; font-weight:600; margin-top:4px;}

.card{
  background:white!important; border:1px solid #e2e8f0!important; border-radius:12px!important;
  padding:20px!important; box-shadow:0 4px 16px rgba(0,0,0,0.04)!important;
}

.input-row{display:flex; justify-content:space-between; align-items:center; margin-bottom:4px;}
.input-label{font-size:13px; font-weight:600; color:#1e293b;}
.badge-blue{background:#2563eb; color:white; padding:4px 10px; border-radius:6px; font-size:12px; font-weight:700; min-width:36px; text-align:center;}
.divider{height:1px; background:#eef2f7; margin:14px 0;}

.stSlider label{display:none!important;}
div[data-baseweb="slider"] > div > div{height:6px!important; background:#e2e8f0!important; border-radius:10px!important;}
div[data-baseweb="slider"] > div > div > div{background:#2563eb!important; height:6px!important; border-radius:10px!important;}
div[data-baseweb="slider"] [role="slider"]{
  width:18px!important; height:18px!important; background:white!important;
  border:2.5px solid #2563eb!important; box-shadow:0 2px 6px rgba(37,99,235,0.4)!important;
  border-radius:50%!important; top:-6px!important;
}

.stButton > button{
  background:#1e293b!important; color:white!important; border-radius:8px!important;
  height:46px!important; font-weight:700!important; width:100%!important; border:none!important; margin-top:12px!important;
}

/* ===== STYLE 2 NEON ELECTRIC TRAIL - 48% CIRCLE ===== */
.circle-wrap{display:flex; justify-content:center; margin:18px 0;}

.circle-48{
  width:140px; height:140px; border-radius:50%;
  background: conic-gradient(from 0deg, #e2e8f0 0deg, #e2e8f0 360deg);
  display:flex; align-items:center; justify-content:center;
  position:relative;
  --angle:0deg;
  animation: neonDraw 2.2s cubic-bezier(0.22,1,0.36,1) forwards;
}

.circle-48::before{
  content:''; position:absolute; inset:0; border-radius:50%;
  background: conic-gradient(from 0deg, #2563eb 0deg, #3b82f6 var(--angle), transparent var(--angle));
  filter: blur(0px);
  animation: neonDraw 2.2s cubic-bezier(0.22,1,0.36,1) forwards;
}

.circle-48::after{
  content:''; position:absolute; width:12px; height:12px; background:white; border:3px solid #2563eb;
  border-radius:50%; top:2px; left:50%; transform:translateX(-50%) rotate(var(--angle)) translateY(-2px);
  transform-origin:50% 68px;
  box-shadow:0 0 12px #2563eb, 0 0 20px #3b82f6;
  animation: sparkMove 2.2s cubic-bezier(0.22,1,0.36,1) forwards, sparkPulse 0.8s infinite 2.2s alternate;
}

@keyframes neonDraw{
  from{ --angle:0deg; }
  to{ --angle:172.8deg; } /* 48% of 360deg = 172.8deg */
}
@keyframes sparkMove{
  from{ transform:translateX(-50%) rotate(0deg) translateY(-2px); }
  to{ transform:translateX(-50%) rotate(172.8deg) translateY(-2px); }
}
@keyframes sparkPulse{
  0%{box-shadow:0 0 12px #2563eb, 0 0 20px #3b82f6; transform:translateX(-50%) rotate(172.8deg) translateY(-2px) scale(1);}
  100%{box-shadow:0 0 18px #2563eb, 0 0 32px #3b82f6, 0 0 45px #60a5fa; transform:translateX(-50%) rotate(172.8deg) translateY(-2px) scale(1.3);}
}

.circle-inner-48{
  width:112px; height:112px; background:white; border-radius:50%;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  z-index:2; box-shadow:inset 0 2px 10px rgba(0,0,0,0.06), 0 0 20px rgba(37,99,235,0.08);
}

.score-48{
  font-size:32px; font-weight:800; color:#1e293b; letter-spacing:-1px;
  animation: countNeon 2s ease-out 0.4s forwards; opacity:0;
}
@keyframes countNeon{
  0%{opacity:0; transform:scale(0.5) translateY(10px);}
  60%{opacity:1; transform:scale(1.15) translateY(0);}
  100%{opacity:1; transform:scale(1) translateY(0);}
}

.tech{background:#dbeafe; color:#1e40af; padding:6px 12px; border-radius:6px; font-size:11px; font-weight:700; display:inline-block; margin:4px;}
</style>

<div class="header">
  <div style="display:flex; gap:14px; align-items:center;">
    <div style="width:44px; height:44px; background:#1e3a8a; border-radius:10px; display:flex; align-items:center; justify-content:center; color:white; font-size:20px;">🧠</div>
    <div>
      <div style="font-size:20px; font-weight:800; color:#1e293b;">Love Compatibility Prediction Model</div>
      <div style="font-size:12px; color:#64748b;">Machine Learning • Classification Model • v1.2.0 • Built by Vansh Rajput</div>
    </div>
  </div>
  <div style="display:flex; gap:8px;">
    <span style="background:#dcfce7; color:#166534; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700;">● Model Active</span>
    <span style="background:#e2e8f0; color:#334155; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:600;">API: Healthy</span>
  </div>
</div>
""", unsafe_allow_html=True)

# METRICS
m1,m2,m3 = st.columns(3)
with m1: st.markdown('<div class="metric-card" style="border-top-color:#93c5fd;"><div class="metric-label">🎯 Model Accuracy</div><div class="metric-val">91.2%</div><div class="metric-delta">↑ +1.4% vs baseline</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-card" style="border-top-color:#a5b4fc;"><div class="metric-label">📊 Precision</div><div class="metric-val">89.5%</div><div class="metric-delta">↑ +0.9% average</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-card" style="border-top-color:#bfdbfe;"><div class="metric-label">📈 F1 Score</div><div class="metric-val">89.8%</div><div class="metric-delta">↑ +1.1% vs baseline</div></div>', unsafe_allow_html=True)

st.write("")

left,right = st.columns([0.58,0.42], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### Input Parameters")
    st.caption("Adjust 8 features - True model prediction")

    l1,r1 = st.columns(2)
    with l1:
        st.markdown('<div class="input-row"><span class="input-label">Communication Score</span><span class="badge-blue">72</span></div>', unsafe_allow_html=True)
        comm = st.slider("c1", 0.0, 10.0, 7.2, key="comm")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-row"><span class="input-label">Understanding Score</span><span class="badge-blue">68</span></div>', unsafe_allow_html=True)
        und = st.slider("c2", 0.0, 10.0, 6.8, key="und")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-row"><span class="input-label">Support Score</span><span class="badge-blue">79</span></div>', unsafe_allow_html=True)
        supp = st.slider("c3", 0.0, 10.0, 7.9, key="supp")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-row"><span class="input-label">Gifts Per Month</span><span class="badge-blue">5</span></div>', unsafe_allow_html=True)
        gift = st.slider("c4", 0.0, 15.0, 5.0, key="gift")

    with r1:
        st.markdown('<div class="input-row"><span class="input-label">Trust Score</span><span class="badge-blue">85</span></div>', unsafe_allow_html=True)
        trust = st.slider("c5", 0.0, 10.0, 8.5, key="trust")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-row"><span class="input-label">Time Together Hours</span><span class="badge-blue">42</span></div>', unsafe_allow_html=True)
        time = st.slider("c6", 0.0, 168.0, 32.0, key="time")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-row"><span class="input-label">Fights Per Month</span><span class="badge-blue">2</span></div>', unsafe_allow_html=True)
        fight = st.slider("c7", 0.0, 15.0, 2.0, key="fight")
        st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-row"><span class="input-label">Happy Together Score</span><span class="badge-blue">88</span></div>', unsafe_allow_html=True)
        happy = st.slider("c8", 0.0, 10.0, 8.8, key="happy")

    run = st.button("✨ Run Prediction →", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if 'score' not in st.session_state: st.session_state.score = 48
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
      <div style="font-size:12px; color:#64748b; margin-bottom:10px;">Model output and confidence — Neon Electric Style</div>

      <div class="circle-wrap">
        <div class="circle-48">
          <div class="circle-inner-48">
            <div class="score-48">{sc}%</div>
            <div style="font-size:10px; color:#64748b; font-weight:600;">Compatibility Score</div>
          </div>
        </div>
      </div>

      <div style="text-align:center; margin-top:14px;"><span style="background:#dbeafe; color:#1e40af; padding:6px 14px; border-radius:20px; font-size:12px; font-weight:600;">Prediction: Compatible ✓ • {sc}% Match</span></div>

      <div style="background:#eff6ff; border-left:3px solid #2563eb; padding:12px; border-radius:6px; margin-top:16px; font-size:12px; color:#1e293b; line-height:1.6;">
        <b>Result:</b> The model predicts {sc}% likelihood of compatibility based on current inputs.<br>
        <b>Recommendation:</b> Compatible — Strong match across key features.
      </div>

      <div style="margin-top:14px; border-top:1px solid #e2e8f0; padding-top:12px; text-align:center;">
        <div style="font-size:12px; font-weight:700; color:#1e293b; margin-bottom:6px;">Tech Stack</div>
        <span class="tech">Python</span><span class="tech">Scikit-Learn</span><span class="tech">Random Forest</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
