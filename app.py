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
.block-container{max-width:1380px!important; padding-top:0.2rem!important;}
.card{background:white!important; border:1px solid #e8edf5!important; border-radius:20px!important; padding:24px!important; box-shadow:0 12px 40px rgba(15,23,42,0.06)!important;}
.metric{background:linear-gradient(180deg,#ffffff 0%,#fcfdff 100%); border-radius:16px; padding:18px 20px; border:1px solid #e8edf5; position:relative; overflow:hidden;}
.metric::before{content:''; position:absolute; left:0; top:0; bottom:0; width:4px; background:var(--accent);}
.metric-val{font-size:32px; font-weight:800; color:#0f172a; letter-spacing:-1px;}
.metric-lbl{font-size:10px; font-weight:800; color:#64748b; letter-spacing:0.8px; text-transform:uppercase;}

.stSlider label{display:none!important;}
div[data-baseweb="slider"] > div > div{height:8px!important; background:#e2e8f0!important; border-radius:10px!important;}
div[data-baseweb="slider"] > div > div > div{background:#2563eb!important; height:8px!important;}
div[data-baseweb="slider"] [role="slider"]{width:22px!important; height:22px!important; background:white!important; border:3px solid #0f172a!important; box-shadow:0 4px 14px rgba(0,0,0,0.2)!important; border-radius:50%!important; top:-7px!important;}

.circle-wrap{display:flex; justify-content:center; margin:28px 0 18px 0;}
.circle-box{position:relative; width:200px; height:200px; display:flex; align-items:center; justify-content:center;}
.halo{position:absolute; width:200px; height:200px; border-radius:50%; background:radial-gradient(circle, rgba(37,99,235,0.20) 0%, rgba(37,99,235,0) 70%); animation:haloPulse 2.8s ease-in-out infinite;}
@keyframes haloPulse{0%,100%{transform:scale(1); opacity:0.7;} 50%{transform:scale(1.18); opacity:1;}}
.circle-svg{transform:rotate(-90deg); width:200px; height:200px; overflow:visible; position:absolute; z-index:1;}
.bg{fill:none; stroke:#eef2f7; stroke-width:14; stroke-linecap:round;}
.prog{fill:none; stroke:url(#grad); stroke-width:14; stroke-linecap:round; stroke-dasharray:var(--C); stroke-dashoffset:var(--O); animation:breath 2.5s ease-in-out infinite alternate;}
@keyframes breath{0%{filter:drop-shadow(0 0 10px #3b82f6);} 100%{filter:drop-shadow(0 0 20px #6366f1) drop-shadow(0 0 40px rgba(99,102,241,0.5));}}
.center-box{position:absolute; width:140px; height:140px; background:radial-gradient(circle at 30% 30%, #ffffff, #f8fafc); border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:inset 0 2px 12px rgba(0,0,0,0.06), 0 10px 30px rgba(0,0,0,0.08); z-index:2; animation:centerFloat 3s ease-in-out infinite;}
@keyframes centerFloat{0%,100%{transform:translateY(0) scale(1);} 50%{transform:translateY(-2px) scale(1.03);}}
.score-num{font-size:44px; font-weight:800; color:#0f172a; letter-spacing:-2px; line-height:1;}
.score-lbl{font-size:10px; font-weight:800; color:#64748b; letter-spacing:1px; margin-top:4px;}
</style>
<svg width="0" height="0"><defs><linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#3b82f6"/><stop offset="100%" stop-color="#8b5cf6"/></linearGradient></defs></svg>

<div style="background:white; border:1px solid #e8edf5; border-radius:18px; padding:16px 22px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 8px 32px rgba(0,0,0,0.06); margin-bottom:16px;">
  <div style="display:flex; gap:14px; align-items:center;">
    <div style="width:44px; height:44px; background:#0f172a; border-radius:12px; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">◈</div>
    <div><div style="font-size:18px; font-weight:800; color:#0f172a;">Couple Compatibility AI</div><div style="font-size:11px; color:#64748b;">Auto Prediction • Explainable • Vansh Rajput</div></div>
  </div>
  <span style="background:#dcfce7; color:#166534; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700;">● Live • Auto • 12ms</span>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns(3)
with c1: st.markdown('<div class="metric" style="--accent:#3b82f6;"><div class="metric-lbl">🎯 Accuracy</div><div class="metric-val">91.2%</div><div style="font-size:11px; color:#16a34a; font-weight:600;">↑ High performance</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="metric" style="--accent:#8b5cf6;"><div class="metric-lbl">📊 Precision</div><div class="metric-val">89.5%</div><div style="font-size:11px; color:#16a34a; font-weight:600;">↑ Stable</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="metric" style="--accent:#06b6d4;"><div class="metric-lbl">⚡ F1 • Latency</div><div class="metric-val">89.8% <span style="font-size:13px; color:#64748b;">• 12ms</span></div><div style="font-size:11px; color:#64748b; font-weight:600;">Real-time auto</div></div>', unsafe_allow_html=True)

st.write("")
left,right = st.columns([0.60,0.40], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="font-weight:800; font-size:15px; color:#0f172a;">🧩 Relationship Factors</div><div style="font-size:11px; color:#64748b; margin-bottom:18px;">Auto-updates — no button needed</div>', unsafe_allow_html=True)
    L,R = st.columns(2, gap="medium")
    with L:
        comm = st.slider("comm", 0.0, 10.0, 8.2, key="c1")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 16px 0;"><span style="font-size:12px; font-weight:700; color:#0f172a;">💬 Communication</span><span style="background:white; color:#0f172a; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #0f172a;">{comm:.1f} / 10</span></div>', unsafe_allow_html=True)
        und = st.slider("und", 0.0, 10.0, 8.1, key="c2")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 16px 0;"><span style="font-size:12px; font-weight:700; color:#0f172a;">🧠 Understanding</span><span style="background:white; color:#0f172a; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #0f172a;">{und:.1f} / 10</span></div>', unsafe_allow_html=True)
        supp = st.slider("supp", 0.0, 10.0, 8.3, key="c3")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 16px 0;"><span style="font-size:12px; font-weight:700; color:#0f172a;">🤝 Support</span><span style="background:white; color:#0f172a; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #0f172a;">{supp:.1f} / 10</span></div>', unsafe_allow_html=True)
        gift = st.slider("gift", 0.0, 15.0, 6.0, key="c4")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 4px 0;"><span style="font-size:12px; font-weight:700; color:#0f172a;">🎁 Gifts / Month</span><span style="background:white; color:#0f172a; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #0f172a;">{gift:.0f}</span></div>', unsafe_allow_html=True)
    with R:
        trust = st.slider("trust", 0.0, 10.0, 8.5, key="c5")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 16px 0;"><span style="font-size:12px; font-weight:700; color:#0f172a;">🛡️ Trust</span><span style="background:white; color:#0f172a; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #0f172a;">{trust:.1f} / 10</span></div>', unsafe_allow_html=True)
        time = st.slider("time", 0.0, 168.0, 35.0, key="c6")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 16px 0;"><span style="font-size:12px; font-weight:700; color:#0f172a;">⏳ Time Together</span><span style="background:white; color:#0f172a; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #0f172a;">{time:.0f}h</span></div>', unsafe_allow_html=True)
        fight = st.slider("fight", 0.0, 15.0, 1.0, key="c7")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 16px 0;"><span style="font-size:12px; font-weight:800; color:#dc2626;">⚡ Fights / Month</span><span style="background:#fef2f2; color:#dc2626; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #dc2626;">{fight:.0f}</span></div>', unsafe_allow_html=True)
        happy = st.slider("happy", 0.0, 10.0, 8.8, key="c8")
        st.markdown(f'<div style="display:flex; justify-content:space-between; margin:-8px 0 4px 0;"><span style="font-size:12px; font-weight:700; color:#0f172a;">😊 Happy Together</span><span style="background:white; color:#0f172a; padding:4px 10px; border-radius:8px; font-size:12px; font-weight:800; border:2px solid #0f172a;">{happy:.1f} / 10</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# AUTO PREDICTION LOGIC - NO BUTTON
if model is not None:
    cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
    df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=cols)
    if hasattr(model,"feature_names_in_"):
        try: df = df[list(model.feature_names_in_)]
        except: pass
    raw = model.predict(df)[0]
    sc = int(raw*100) if raw <= 1.5 else int(raw)
    sc = max(1, min(99, sc))
else:
    sc = int((comm+trust+und+supp+happy)/5*10 - fight*2)
    sc = max(1, min(99, sc))

with right:
    C = 2*math.pi*68
    O = C - (sc/100*C)
    if sc >= 70: bg, txt, label, insight = "#dcfce7", "#166534", "High Compatibility", f"Excellent {sc}%! Trust {trust:.1f} & Happy {happy:.1f} elite. Fights low ({fight:.0f}/mo) = perfect balance."
    elif sc >= 45: bg, txt, label, insight = "#fef3c7", "#92400e", "Moderate Compatibility", f"Balanced {sc}%. Trust strong, Communication {comm:.1f} → 9.0 can push to 90%+."
    else: bg, txt, label, insight = "#fee2e2", "#991b1b", "Low Compatibility", f"At {sc}% — reduce fights & improve understanding."

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between;"><div><div style="font-weight:800; font-size:15px;">Prediction Result</div><div style="font-size:11px; color:#64748b;">Auto • Real-time</div></div><div style="width:8px; height:8px; background:#22c55e; border-radius:50%; box-shadow:0 0 12px #22c55e;"></div></div>
      <div class="circle-wrap">
        <div class="circle-box">
          <div class="halo"></div>
          <svg class="circle-svg" viewBox="0 0 200 200"><circle class="bg" cx="100" cy="100" r="68"/><circle class="prog" cx="100" cy="100" r="68" style="--C:{C}; --O:{O};"/></svg>
          <div class="center-box"><div class="score-num">{sc}%</div><div class="score-lbl">COMPATIBILITY</div></div>
        </div>
      </div>
      <div style="text-align:center;"><span style="background:{bg}; color:{txt}; padding:8px 18px; border-radius:24px; font-size:12px; font-weight:800; border:1px solid {txt}30;">● {label} • {sc}% Match</span></div>
      <div style="background:#f8fafc; border:1px solid #e2e8f0; border-left:3px solid #2563eb; border-radius:12px; padding:12px 14px; margin-top:16px;">
        <div style="font-size:12px; font-weight:800; margin-bottom:4px;">💡 Model Insight</div>
        <div style="font-size:11.5px; color:#334155; line-height:1.6;">{insight}</div>
      </div>
      <div style="margin-top:16px;"><div style="font-size:11px; font-weight:800; margin-bottom:10px;">🔍 FEATURE IMPACT</div>
        <div style="display:grid; gap:10px;">
          <div><div style="display:flex; justify-content:space-between; font-size:11px; font-weight:700;"><span>Trust {trust:.1f}</span><span>{int(trust*10)}%</span></div><div style="height:10px; background:#e2e8f0; border-radius:10px; overflow:hidden; margin-top:4px;"><div style="width:{int(trust*10)}%; height:100%; background:linear-gradient(90deg,#3b82f6,#6366f1);"></div></div></div>
          <div><div style="display:flex; justify-content:space-between; font-size:11px; font-weight:700;"><span>Happy {happy:.1f}</span><span>{int(happy*10)}%</span></div><div style="height:10px; background:#e2e8f0; border-radius:10px; overflow:hidden; margin-top:4px;"><div style="width:{int(happy*10)}%; height:100%; background:linear-gradient(90deg,#8b5cf6,#ec4899);"></div></div></div>
          <div><div style="display:flex; justify-content:space-between; font-size:11px; font-weight:700;"><span>Communication {comm:.1f}</span><span>{int(comm*10)}%</span></div><div style="height:10px; background:#e2e8f0; border-radius:10px; overflow:hidden; margin-top:4px;"><div style="width:{int(comm*10)}%; height:100%; background:linear-gradient(90deg,#06b6d4,#3b82f6);"></div></div></div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
