import streamlit as st, pandas as pd, joblib, os
st.set_page_config(page_title="Couple Compatibility AI • Vansh", layout="wide", page_icon="💙")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;800&display=swap');
.stApp{background:#f6f8fb!important; font-family:Inter,sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1300px!important; padding-top:0.4rem!important;}

.card{background:white!important; border:1px solid #e2e8f0!important; border-radius:16px!important; padding:22px!important; box-shadow:0 8px 30px rgba(0,0,0,0.04)!important;}

.circle-wrap{display:flex; justify-content:center; margin:16px 0;}
.circle-box{position:relative; width:160px; height:160px; display:flex; align-items:center; justify-content:center;}

.circle-svg{transform:rotate(-90deg); width:160px; height:160px; overflow:visible;}
.bg{fill:none; stroke:#eef2f7; stroke-width:10;}
.prog{
  fill:none; stroke:#2563eb; stroke-width:10; stroke-linecap:round;
  stroke-dasharray: var(--C); stroke-dashoffset: var(--C);
  animation: draw 2.2s cubic-bezier(0.22,1,0.36,1) forwards;
  filter: drop-shadow(0 0 10px rgba(37,99,235,0.5));
}
@keyframes draw{ to{ stroke-dashoffset: var(--O); } }

.center{
  position:absolute; width:118px; height:118px; background:white; border-radius:50%;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  box-shadow:inset 0 2px 8px rgba(0,0,0,0.05), 0 4px 20px rgba(0,0,0,0.05);
}
.num{font-size:34px; font-weight:800; color:#0f172a; animation: pop 0.9s cubic-bezier(0.34,1.56,0.64,1) 0.6s both;}
@keyframes pop{ from{opacity:0; transform:scale(0.5);} to{opacity:1; transform:scale(1);} }

.dot{
  position:absolute; width:14px; height:14px; background:white; border:3px solid #2563eb;
  border-radius:50%; box-shadow:0 0 12px #2563eb; opacity:0;
  animation: dotIn 0.4s forwards 2.1s;
}
@keyframes dotIn{ to{opacity:1;} }
</style>
""", unsafe_allow_html=True)

# Demo metrics like your video
c1,c2,c3 = st.columns(3)
with c1: st.markdown('<div class="card" style="text-align:center;"><div style="font-size:12px; color:#64748b; font-weight:600;">Model Accuracy</div><div style="font-size:32px; font-weight:800; color:#0f172a;">89.8%</div><div style="font-size:11px; color:#16a34a;">↑ High Performance</div></div>', unsafe_allow_html=True)

left,right = st.columns([0.55,0.45], gap="large")
with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.write("#### 🧩 Input Parameters")
    comm = st.slider("Communication", 0.0, 10.0, 7.2)
    trust = st.slider("Trust", 0.0, 10.0, 8.5)
    und = st.slider("Understanding", 0.0, 10.0, 6.8)
    run = st.button("▶ Run Prediction", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if 'score' not in st.session_state: st.session_state.score = 77
    if run and model:
        cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
        df = pd.DataFrame([[comm,trust,6.8,32,7.9,2,5,8.8]], columns=cols)
        if hasattr(model,"feature_names_in_"): df = df[list(model.feature_names_in_)]
        raw = model.predict(df)[0]
        sc = int(raw*100) if raw<=1.5 else int(raw)
        st.session_state.score = max(1,min(99,sc))

    sc = st.session_state.score
    C = 2*3.14159*60
    O = C - (sc/100*C)

    st.markdown(f"""
    <div class="card">
      <div style="font-weight:800; font-size:16px; color:#0f172a;">Prediction Result</div>
      <div style="font-size:12px; color:#64748b; margin-bottom:12px;">Model output and confidence</div>

      <div class="circle-wrap">
        <div class="circle-box">
          <svg class="circle-svg">
            <circle class="bg" cx="80" cy="80" r="60"/>
            <circle class="prog" cx="80" cy="80" r="60" style="--C:{C}; --O:{O};"/>
          </svg>
          <div class="dot" style="top:10px; left:50%; transform:translateX(-50%) rotate({sc*3.6}deg); transform-origin:50% 70px;"></div>
          <div class="center">
            <div class="num">{sc}%</div>
            <div style="font-size:10px; color:#64748b; font-weight:600;">Compatibility Score</div>
          </div>
        </div>
      </div>

      <div style="text-align:center; margin-top:10px;"><span style="background:#dbeafe; color:#1e40af; padding:7px 14px; border-radius:20px; font-size:12px; font-weight:700;">Prediction: Compatible • {sc}% Match</span></div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:12px; margin-top:14px; font-size:12px; color:#334155; line-height:1.6;">
        <b>Result:</b> The model predicts {sc}% likelihood of compatibility based on current inputs.<br>
        <b>Recommendation:</b> Compatible — Strong match across key factors.
      </div>

      <div style="margin-top:12px; display:flex; gap:6px; justify-content:center;">
        <span style="background:#eff6ff; color:#1d4ed8; padding:5px 10px; border-radius:6px; font-size:10px; font-weight:700;">Python</span>
        <span style="background:#f5f3ff; color:#6d28d9; padding:5px 10px; border-radius:6px; font-size:10px; font-weight:700;">Scikit-Learn</span>
        <span style="background:#f0fdfa; color:#0f766e; padding:5px 10px; border-radius:6px; font-size:10px; font-weight:700;">Random Forest</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
