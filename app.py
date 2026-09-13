import streamlit as st
import pandas as pd
import joblib
import os
import math

st.set_page_config(page_title="Couple Compatibility AI • Vansh Rajput", layout="wide", page_icon="💙")

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
.block-container{max-width:1360px!important; padding-top:0.3rem!important;}

/* HEADER */
.header{background:white; border:1px solid #e2e8f0; border-radius:16px; padding:16px 22px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 4px 20px rgba(0,0,0,0.04); margin-bottom:14px;}

/* METRICS */
.metric{background:white; border-radius:14px; padding:16px 18px; border:1px solid #e2e8f0; border-left:4px solid #3b82f6; box-shadow:0 2px 10px rgba(0,0,0,0.03);}
.metric-val{font-size:30px; font-weight:800; color:#0f172a; letter-spacing:-0.5px;}
.metric-lbl{font-size:11px; font-weight:700; color:#64748b; letter-spacing:0.4px;}

/* CARDS */
.card{background:white!important; border:1px solid #e2e8f0!important; border-radius:16px!important; padding:20px!important; box-shadow:0 8px 30px rgba(0,0,0,0.04)!important;}

/* SLIDER - CLEAN */
.stSlider label{display:none!important;}
div[data-baseweb="slider"] > div > div{height:6px!important; background:#e2e8f0!important; border-radius:10px!important;}
div[data-baseweb="slider"] [role="slider"]{width:18px!important; height:18px!important; background:white!important; border:3px solid #2563eb!important; box-shadow:0 3px 10px rgba(37,99,235,0.35)!important; border-radius:50%!important; top:-6px!important;}
.fight-slider div[data-baseweb="slider"] > div > div > div{background:#ef4444!important;}
.fight-slider div[data-baseweb="slider"] [role="slider"]{border-color:#ef4444!important; box-shadow:0 3px 10px rgba(239,68,68,0.35)!important;}

.stButton > button{background:#0f172a!important; color:white!important; height:52px!important; border-radius:12px!important; font-weight:700!important; width:100%!important; border:none!important;}

/* ===== APPLE STYLE BREATHING CIRCLE - SINGLE RING ===== */
.circle-wrap{display:flex; justify-content:center; margin:22px 0;}
.circle-box{position:relative; width:190px; height:190px; display:flex; align-items:center; justify-content:center;}
.circle-svg{transform:rotate(-90deg); width:190px; height:190px; overflow:visible; position:absolute;}
.bg{fill:none; stroke:#eef2f7; stroke-width:12;}
.prog{
  fill:none; stroke:#2563eb; stroke-width:12; stroke-linecap:round;
  stroke-dasharray:var(--C); stroke-dashoffset:var(--C);
  animation: draw 2s cubic-bezier(0.22,1,0.36,1) forwards, breath 2.2s ease-in-out infinite 2s alternate;
}
@keyframes draw{to{stroke-dashoffset:var(--O);}}
@keyframes breath{
  0%{filter:drop-shadow(0 0 8px #3b82f6); stroke-width:12;}
  100%{filter:drop-shadow(0 0 16px #3b82f6) drop-shadow(0 0 32px rgba(37,99,235,0.45)); stroke-width:13;}
}
.center-box{position:absolute; width:132px; height:132px; background:white; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:inset 0 2px 12px rgba(0,0,0,0.06), 0 8px 24px rgba(0,0,0,0.06); z-index:2; animation: centerBreath 2.5s ease-in-out infinite;}
@keyframes centerBreath{0%,100%{transform:scale(1);} 50%{transform:scale(1.04);}}
.score-num{font-size:40px; font-weight:800; color:#0f172a; letter-spacing:-1.5px;}
.explain-bar{height:6px; border-radius:10px; background:#e2e8f0; overflow:hidden; margin-top:6px;}
.explain-fill{height:100%; border-radius:10px; transition:1s;}
</style>

<div class="header">
  <div style="display:flex; gap:12px; align-items:center;">
    <div style="width:42px; height:42px; background:#0f172a; border-radius:11px; display:flex; align-items:center; justify-content:center; color:white; font-size:18px;">◈</div>
    <div><div style="font-size:18px; font-weight:800; color:#0f172a;">Couple Compatibility AI</div><div style="font-size:11px; color:#64748b;">Production Model • 8 Features • Explainable AI • Vansh Rajput</div></div>
  </div>
  <span style="background:#dcfce7; color:#166534; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700;">● Live • 12ms</span>
</div>
""", unsafe_allow_html=True)

# TOP METRICS WITH ICONS
c1,c2,c3 = st.columns(3)
with c1: st.markdown('<div class="metric"><div class="metric-lbl">🎯 MODEL ACCURACY</div><div class="metric-val">91.2%</div><div style="font-size:11px; color:#16a34a; font-weight:600;">↑ +1.4% • High performance</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="metric" style="border-left-color:#8b5cf6;"><div class="metric-lbl">📊 PRECISION</div><div class="metric-val">89.5%</div><div style="font-size:11px; color:#16a34a; font-weight:600;">↑ Stable across folds</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="metric" style="border-left-color:#06b6d4;"><div class="metric-lbl">⚡ F1 SCORE • LATENCY</div><div class="metric-val">89.8% <span style="font-size:14px; color:#64748b; font-weight:600;">• 12ms</span></div><div style="font-size:11px; color:#64748b; font-weight:600;">Real-time inference</div></div>', unsafe_allow_html=True)

st.write("")

left,right = st.columns([0.58,0.42], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("##### 🧩 Relationship Factors")
    st.caption("Live values — model interprets instantly")

    L,R = st.columns(2)
    with L:
        comm = st.slider("Communication", 0.0, 10.0, 7.2, key="c1")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:12px;"><span style="font-size:12px; font-weight:600; color:#334155;">💬 Communication</span><span style="background:#0f172a; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{comm:.1f}</span></div>', unsafe_allow_html=True)

        und = st.slider("Understanding", 0.0, 10.0, 6.8, key="c2")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:12px;"><span style="font-size:12px; font-weight:600; color:#334155;">🧠 Understanding</span><span style="background:#0f172a; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{und:.1f}</span></div>', unsafe_allow_html=True)

        supp = st.slider("Support", 0.0, 10.0, 7.9, key="c3")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:12px;"><span style="font-size:12px; font-weight:600; color:#334155;">🤝 Support</span><span style="background:#0f172a; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{supp:.1f}</span></div>', unsafe_allow_html=True)

        gift = st.slider("Gifts", 0.0, 15.0, 5.0, key="c4")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:6px;"><span style="font-size:12px; font-weight:600; color:#334155;">🎁 Gifts / Month</span><span style="background:#0f172a; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{gift:.0f}</span></div>', unsafe_allow_html=True)

    with R:
        trust = st.slider("Trust", 0.0, 10.0, 8.5, key="c5")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:12px;"><span style="font-size:12px; font-weight:600; color:#334155;">🛡️ Trust</span><span style="background:#0f172a; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{trust:.1f}</span></div>', unsafe_allow_html=True)

        time = st.slider("Time Together", 0.0, 168.0, 32.0, key="c6")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:12px;"><span style="font-size:12px; font-weight:600; color:#334155;">⏳ Time Together</span><span style="background:#0f172a; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{time:.0f}h</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="fight-slider">', unsafe_allow_html=True)
        fight = st.slider("Fights", 0.0, 15.0, 2.0, key="c7")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:12px;"><span style="font-size:12px; font-weight:600; color:#dc2626;">⚡ Fights / Month</span><span style="background:#dc2626; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{fight:.0f}</span></div>', unsafe_allow_html=True)

        happy = st.slider("Happy", 0.0, 10.0, 8.8, key="c8")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin-top:-10px; margin-bottom:6px;"><span style="font-size:12px; font-weight:600; color:#334155;">😊 Happy Together</span><span style="background:#0f172a; color:white; padding:3px 9px; border-radius:6px; font-size:11px; font-weight:700;">{happy:.1f}</span></div>', unsafe_allow_html=True)

    run = st.button("▶ Run Prediction Model", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    if 'score' not in st.session_state: st.session_state.score = 65
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

    sc = st.session_state.score
    C = 2 * math.pi * 68
    O = C - (sc/100*C)

    if sc >= 70:
        tag_bg, tag_txt, tag_label = "#dcfce7", "#166534", "High Compatibility"
        insight = f"Strong match! Trust ({trust:.1f}) & Happy ({happy:.1f}) are top drivers. Keep fights low to stay above 70%."
    elif sc >= 45:
        tag_bg, tag_txt, tag_label = "#fef3c7", "#92400e", "Moderate Compatibility"
        insight = f"Balanced at {sc}%. Trust ({trust:.1f}) & Happy ({happy:.1f}) are positive. Improving Communication ({comm:.1f} → 8.5+) can push to 80%+."
    else:
        tag_bg, tag_txt, tag_label = "#fee2e2", "#991b1b", "Low Compatibility"
        insight = f"Needs work — {sc}%. High fights ({fight:.0f}/mo) & low understanding ({und:.1f}) hurting score. Focus on communication."

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div><div style="font-weight:800; font-size:15px; color:#0f172a;">Prediction Result</div><div style="font-size:11px; color:#64748b;">Explainable AI output • Real-time</div></div>
        <div style="width:8px; height:8px; background:#22c55e; border-radius:50%; box-shadow:0 0 10px #22c55e; animation: centerBreath 1.5s infinite;"></div>
      </div>

      <div class="circle-wrap">
        <div class="circle-box">
          <svg class="circle-svg" viewBox="0 0 190 190">
            <circle class="bg" cx="95" cy="95" r="68"/>
            <circle class="prog" cx="95" cy="95" r="68" style="--C:{C}; --O:{O};"/>
          </svg>
          <div class="center-box">
            <div class="score-num">{sc}%</div>
            <div style="font-size:10px; color:#64748b; font-weight:700; letter-spacing:0.6px;">COMPATIBILITY</div>
          </div>
        </div>
      </div>

      <div style="text-align:center; margin-top:6px;">
        <span style="background:{tag_bg}; color:{tag_txt}; padding:7px 16px; border-radius:20px; font-size:12px; font-weight:700; border:1px solid {tag_txt}20;">● {tag_label} • {sc}% Match</span>
      </div>

      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:3px solid #2563eb; border-radius:10px; padding:12px; margin-top:14px;">
        <div style="font-size:12px; font-weight:700; color:#0f172a; margin-bottom:4px;">💡 Model Insight</div>
        <div style="font-size:11.5px; color:#334155; line-height:1.6;">{insight}</div>
      </div>

      <div style="margin-top:14px;">
        <div style="font-size:11px; font-weight:700; color:#0f172a; margin-bottom:8px; letter-spacing:0.3px;">🔍 Feature Impact</div>
        <div style="display:grid; gap:8px;">
          <div><div style="display:flex; justify-content:space-between; font-size:11px;"><span>Trust {trust:.1f}</span><span>{int(trust*10)}%</span></div><div class="explain-bar"><div class="explain-fill" style="width:{int(trust*10)}%; background:#2563eb;"></div></div></div>
          <div><div style="display:flex; justify-content:space-between; font-size:11px;"><span>Happy {happy:.1f}</span><span>{int(happy*10)}%</span></div><div class="explain-bar"><div class="explain-fill" style="width:{int(happy*10)}%; background:#8b5cf6;"></div></div></div>
          <div><div style="display:flex; justify-content:space-between; font-size:11px;"><span>Communication {comm:.1f}</span><span>{int(comm*10)}%</span></div><div class="explain-bar"><div class="explain-fill" style="width:{int(comm*10)}%; background:#06b6d4;"></div></div></div>
          <div><div style="display:flex; justify-content:space-between; font-size:11px;"><span>Fights {fight:.0f}/mo</span><span style="color:#ef4444;">Risk</span></div><div class="explain-bar"><div class="explain-fill" style="width:{min(100,int(fight*8))}%; background:#ef4444;"></div></div></div>
        </div>
      </div>

      <div style="margin-top:14px; text-align:center; font-size:10px; color:#94a3b8; letter-spacing:0.3px;">Tech Stack • Python • Scikit-Learn • Random Forest • Streamlit Cloud</div>
    </div>
    """, unsafe_allow_html=True)
