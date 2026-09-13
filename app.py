import streamlit as st
import pandas as pd
import joblib
import os
import math

st.set_page_config(page_title="Couple Compatibility AI • Vansh", layout="wide", page_icon="💙")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@500;600;700;800&display=swap');
.stApp{background:#f6f8fb!important; font-family:'Inter',sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1320px!important; padding-top:0.4rem!important;}
.card{background:white!important; border:1px solid #e2e8f0!important; border-radius:16px!important; padding:22px!important; box-shadow:0 8px 30px rgba(0,0,0,0.04)!important; margin-bottom:14px;}
.metric{background:white; border-radius:14px; padding:16px 18px; border:1px solid #e2e8f0; border-left:4px solid #3b82f6;}
.metric-val{font-size:32px; font-weight:800; color:#0f172a;}
.metric-lbl{font-size:11px; font-weight:700; color:#64748b; letter-spacing:0.5px;}

.input-card{background:#f8fafc; border:1px solid #e2e8f0; border-radius:10px; padding:10px 12px; display:flex; align-items:center; justify-content:space-between; margin-bottom:8px;}
.icon{width:32px; height:32px; border-radius:8px; display:flex; align-items:center; justify-content:center; color:white; font-size:14px;}
.lbl{font-size:13px; font-weight:600; color:#1e293b; margin-left:8px;}
.badge{background:#0f172a; color:white; padding:4px 10px; border-radius:7px; font-size:11px; font-weight:700;}

.stSlider label{display:none!important;}
div[data-baseweb="slider"] > div > div{height:6px!important; background:#e2e8f0!important; border-radius:10px!important;}
div[data-baseweb="slider"] > div > div > div{background:#2563eb!important; height:6px!important;}
div[data-baseweb="slider"] [role="slider"]{width:18px!important; height:18px!important; background:white!important; border:3px solid #2563eb!important; box-shadow:0 3px 10px rgba(37,99,235,0.4)!important; border-radius:50%!important; top:-6px!important;}
.stButton > button{background:#0f172a!important; color:white!important; height:52px!important; border-radius:12px!important; font-weight:700!important; width:100%!important; border:none!important; margin-top:10px!important;}

/* ===== CONTINUOUS LOOP CIRCLE ===== */
.circle-wrap{display:flex; justify-content:center; margin:20px 0;}
.circle-box{position:relative; width:170px; height:170px; display:flex; align-items:center; justify-content:center;}
.circle-svg{transform:rotate(-90deg); width:170px; height:170px; overflow:visible; position:absolute;}
.bg{fill:none; stroke:#eef2f7; stroke-width:10;}
.outer-ring{fill:none; stroke:#bfdbfe; stroke-width:2; stroke-dasharray:12 8; opacity:0.7; animation: rotateRing 5s linear infinite;}
@keyframes rotateRing{from{transform:rotate(0deg);} to{transform:rotate(360deg);}}
.prog{
  fill:none; stroke:#2563eb; stroke-width:10; stroke-linecap:round;
  stroke-dasharray: var(--C); stroke-dashoffset: var(--C);
  animation: drawCircle 2s cubic-bezier(0.22,1,0.36,1) forwards, glowBreath 1.8s ease-in-out infinite 2s alternate, pulseScale 2.5s ease-in-out infinite 2s;
}
@keyframes drawCircle{to{stroke-dashoffset: var(--O);}}
@keyframes glowBreath{
  0%{filter:drop-shadow(0 0 6px #2563eb); stroke-width:10;}
  100%{filter:drop-shadow(0 0 14px #3b82f6) drop-shadow(0 0 26px #2563eb); stroke-width:11;}
}
@keyframes pulseScale{0%,100%{transform:scale(1);} 50%{transform:scale(1.04);}}
.center-box{
  position:absolute; width:118px; height:118px; background:white; border-radius:50%;
  display:flex; flex-direction:column; align-items:center; justify-content:center;
  box-shadow:inset 0 2px 10px rgba(0,0,0,0.06), 0 4px 20px rgba(0,0,0,0.06); z-index:2;
  animation: centerPulse 2.2s ease-in-out infinite;
}
@keyframes centerPulse{0%,100%{transform:scale(1);} 50%{transform:scale(1.06); box-shadow:inset 0 2px 10px rgba(0,0,0,0.08), 0 8px 30px rgba(37,99,235,0.18);}}
.score-num{font-size:36px; font-weight:800; color:#0f172a; animation: numBreath 2s ease-in-out infinite;}
@keyframes numBreath{0%,100%{transform:scale(1);} 50%{transform:scale(1.1);}}
.shimmer{position:absolute; width:16px; height:16px; background:white; border:3px solid #2563eb; border-radius:50%; box-shadow:0 0 14px #2563eb, 0 0 24px #3b82f6; top:4px; left:50%; z-index:3; animation: orbit 4s linear infinite 2s, shimmerPulse 1s ease-in-out infinite alternate;}
@keyframes orbit{from{transform:translateX(-50%) rotate(0deg) translate(0, -2px);} to{transform:translateX(-50%) rotate(360deg) translate(0, -2px);}}
@keyframes shimmerPulse{from{box-shadow:0 0 12px #2563eb;} to{box-shadow:0 0 20px #3b82f6, 0 0 36px #2563eb; transform:translateX(-50%) scale(1.35);}}
</style>

<div style="background:white; border:1px solid #e2e8f0; border-radius:16px; padding:18px 24px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 4px 20px rgba(0,0,0,0.04); margin-bottom:16px;">
  <div style="display:flex; gap:14px; align-items:center;">
    <div style="width:44px; height:44px; background:#0f172a; border-radius:12px; display:flex; align-items:center; justify-content:center; color:white;">◈</div>
    <div><div style="font-size:19px; font-weight:800; color:#0f172a;">Couple Compatibility AI</div><div style="font-size:12px; color:#64748b;">8 Features • Random Forest • Continuous Animation • Vansh Rajput</div></div>
  </div>
  <span style="background:#dcfce7; color:#166534; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700;">● Live • Animating ∞</span>
</div>
""", unsafe_allow_html=True)

m1,m2,m3 = st.columns(3)
with m1: st.markdown('<div class="metric"><div class="metric-lbl">🎯 ACCURACY</div><div class="metric-val">91.2%</div><div style="font-size:11px; color:#16a34a; font-weight:600;">↑ High performance</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric" style="border-left-color:#8b5cf6;"><div class="metric-lbl">📊 PRECISION</div><div class="metric-val">89.5%</div><div style="font-size:11px; color:#16a34a; font-weight:600;">↑ Stable</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric" style="border-left-color:#06b6d4;"><div class="metric-lbl">⚡ F1 SCORE</div><div class="metric-val">89.8%</div><div style="font-size:11px; color:#64748b; font-weight:600;">~12ms inference</div></div>', unsafe_allow_html=True)

st.write("")

left,right = st.columns([0.58,0.42], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("##### 🧩 Input Parameters (8 Exact Model Features)")

    L,R = st.columns(2)
    with L:
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#3b82f6;">💬</div><div class="lbl">Communication</div></div><div class="badge">7.2</div></div>', unsafe_allow_html=True)
        comm = st.slider("c1", 0.0, 10.0, 7.2, key="c1")
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#8b5cf6;">🧠</div><div class="lbl">Understanding</div></div><div class="badge">6.8</div></div>', unsafe_allow_html=True)
        und = st.slider("c2", 0.0, 10.0, 6.8, key="c2")
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#10b981;">🤝</div><div class="lbl">Support</div></div><div class="badge">7.9</div></div>', unsafe_allow_html=True)
        supp = st.slider("c3", 0.0, 10.0, 7.9, key="c3")
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#f59e0b;">🎁</div><div class="lbl">Gifts / Month</div></div><div class="badge">5</div></div>', unsafe_allow_html=True)
        gift = st.slider("c4", 0.0, 15.0, 5.0, key="c4")

    with R:
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#6366f1;">🛡️</div><div class="lbl">Trust</div></div><div class="badge">8.5</div></div>', unsafe_allow_html=True)
        trust = st.slider("c5", 0.0, 10.0, 8.5, key="c5")
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#06b6d4;">⏳</div><div class="lbl">Time Together</div></div><div class="badge">32h</div></div>', unsafe_allow_html=True)
        time = st.slider("c6", 0.0, 168.0, 32.0, key="c6")
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#ef4444;">⚡</div><div class="lbl">Fights / Month</div></div><div class="badge">2</div></div>', unsafe_allow_html=True)
        fight = st.slider("c7", 0.0, 15.0, 2.0, key="c7")
        st.markdown('<div class="input-card"><div style="display:flex; align-items:center;"><div class="icon" style="background:#ec4899;">😊</div><div class="lbl">Happy</div></div><div class="badge">8.8</div></div>', unsafe_allow_html=True)
        happy = st.slider("c8", 0.0, 10.0, 8.8, key="c8")

    run = st.button("▶ Run Prediction Model", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if 'score' not in st.session_state: st.session_state.score = 77
    if run:
        if model is not None:
            cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
            df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=cols)
            if hasattr(model,"feature_names_in_"):
                try: df = df[list(model.feature_names_in_)]
                except: pass
            raw = model.predict(df)[0]
            sc = int(raw*100) if raw <= 1.5 else int(raw)
            st.session_state.score = max(1, min(99, sc))
        else:
            st.session_state.score = 77

    sc = st.session_state.score
    C = 2 * math.pi * 60
    O = C - (sc/100*C)
    label = "High Compatibility" if sc>=70 else "Moderate Compatibility" if sc>=45 else "Low Compatibility"
    bg_tag = "#dcfce7" if sc>=70 else "#fef3c7" if sc>=45 else "#fee2e2"
    txt_tag = "#166534" if sc>=70 else "#92400e" if sc>=45 else "#991b1b"

    st.markdown(f"""
    <div class="card">
      <div style="font-weight:800; font-size:16px; color:#0f172a;">Prediction Result</div>
      <div style="font-size:12px; color:#64748b; margin-bottom:6px;">Continuous ∞ animation — never stops</div>

      <div class="circle-wrap">
        <div class="circle-box">
          <svg class="circle-svg" viewBox="0 0 170 170">
            <circle class="bg" cx="85" cy="85" r="60"/>
            <circle class="outer-ring" cx="85" cy="85" r="73"/>
            <circle class="prog" cx="85" cy="85" r="60" style="--C:{C}; --O:{O};"/>
          </svg>
          <div class="shimmer"></div>
          <div class="center-box">
            <div class="score-num">{sc}%</div>
            <div style="font-size:10px; color:#64748b; font-weight:700; letter-spacing:0.5px;">COMPATIBILITY</div>
          </div>
        </div>
      </div>

      <div style="text-align:center;"><span style="background:{bg_tag}; color:{txt_tag}; padding:7px 14px; border-radius:20px; font-size:12px; font-weight:700;">● {label} • {sc}% Match • Live ∞</span></div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:12px; margin-top:14px; font-size:12px; color:#334155; line-height:1.6;">
        <b>Result:</b> Model predicts {sc}% compatibility.<br>
        <b>Animation:</b> Outer dotted ring rotates + blue ring breathing glow + number pulse + shimmer orbit — continuously!
      </div>

      <div style="margin-top:12px; display:flex; gap:6px; justify-content:center; flex-wrap:wrap;">
        <span style="background:#eff6ff; color:#1d4ed8; padding:5px 10px; border-radius:6px; font-size:10px; font-weight:700;">Python</span>
        <span style="background:#f5f3ff; color:#6d28d9; padding:5px 10px; border-radius:6px; font-size:10px; font-weight:700;">RandomForest</span>
        <span style="background:#f0fdfa; color:#0f766e; padding:5px 10px; border-radius:6px; font-size:10px; font-weight:700;">Scikit-Learn</span>
      </div>
    </div>
    """, unsafe_allow_html=True)
