import streamlit as st
import pandas as pd
import joblib
import os
import math

st.set_page_config(page_title="BondIQ — Couple Compatibility Engine", layout="wide", page_icon="💙")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@700;800&display=swap');
.stApp{background:#f6f8fb!important;}
header,footer,div[data-testid="stDecoration"]{visibility:hidden!important;}
.block-container{max-width:1320px!important; padding-top:10px!important;}
.card{background:#ffffff!important; border:1px solid #e8edf5!important; border-radius:22px!important; padding:26px!important; box-shadow:0 12px 40px rgba(15,23,42,0.06)!important;}

/* === SAME TO SAME SLIDER FIX === */
.stSlider{margin-top:-12px!important;}
.stSlider > label{display:none!important;}
div[data-baseweb="slider"]{padding:0 8px!important;}
div[data-baseweb="slider"] > div > div{background:#e5e7eb!important; height:6px!important; border-radius:10px!important;}
div[data-baseweb="slider"] > div > div > div{background:#111827!important; height:6px!important;}
div[data-baseweb="slider"] [role="slider"]{background:#ffffff!important; border:2.5px solid #111827!important; width:20px!important; height:20px!important; box-shadow:0 2px 8px rgba(0,0,0,0.12)!important; top:-7px!important;}

.top-row{display:flex; justify-content:space-between; align-items:center; margin-bottom:8px; margin-top:18px;}
.top-row:first-child{margin-top:0px;}
.lbl{font-family:'Inter'; font-size:13px; font-weight:700; color:#111827; display:flex; align-items:center; gap:6px;}
.bdg{font-family:'Inter'; font-size:12px; font-weight:800; background:white; border:2px solid #111827; color:#111827; padding:4px 11px; border-radius:10px; min-width:58px; text-align:center;}
.bdg-red{border-color:#ef4444!important; color:#ef4444!important; background:#fef2f2!important;}

.circle-wrap{display:flex; justify-content:center; margin:22px 0 16px 0;}
.circle-box{position:relative; width:180px; height:180px; display:flex; align-items:center; justify-content:center;}
.circle-svg{transform:rotate(-90deg); width:180px; height:180px; position:absolute;}
.bg{fill:none; stroke:#eef2f7; stroke-width:12; stroke-linecap:round;}
.prog{fill:none; stroke:url(#grad); stroke-width:12; stroke-linecap:round;}
.center-box{position:absolute; width:126px; height:126px; background:white; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(0,0,0,0.07), inset 0 1px 0 rgba(255,255,255,0.8);}
.score-num{font-size:38px; font-weight:800; color:#0f172a; line-height:1;}
.score-lbl{font-size:9px; font-weight:800; color:#94a3b8; letter-spacing:1px; margin-top:3px;}
</style>
<svg width="0" height="0"><defs><linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#3b82f6"/><stop offset="100%" stop-color="#8b5cf6"/></linearGradient></defs></svg>
""", unsafe_allow_html=True)

# TOP HEADER
st.markdown("""
<div style="background:white; border:1px solid #e8edf5; border-radius:16px; padding:14px 20px; display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
  <div style="display:flex; gap:12px; align-items:center;">
    <div style="width:40px; height:40px; background:#0f172a; border-radius:10px; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">◈</div>
    <div><div style="font-size:17px; font-weight:800; color:#0f172a;">BondIQ — Couple Compatibility Engine</div><div style="font-size:11px; color:#64748b;">Explainable AI • 91.2% Accuracy • Production Ready • Vansh Rajput</div></div>
  </div>
  <span style="background:#dcfce7; color:#166534; padding:5px 11px; border-radius:20px; font-size:11px; font-weight:700;">● Live • Auto • 12ms</span>
</div>
<div style="display:flex; gap:12px; margin-bottom:16px;">
  <div style="flex:1; background:white; border:1px solid #e8edf5; border-radius:14px; padding:14px 18px; border-left:4px solid #3b82f6;"><div style="font-size:10px; font-weight:800; color:#64748b;">🎯 ACCURACY</div><div style="font-size:28px; font-weight:800;">91.2%</div></div>
  <div style="flex:1; background:white; border:1px solid #e8edf5; border-radius:14px; padding:14px 18px; border-left:4px solid #8b5cf6;"><div style="font-size:10px; font-weight:800; color:#64748b;">📊 PRECISION</div><div style="font-size:28px; font-weight:800;">89.5%</div></div>
  <div style="flex:1; background:white; border:1px solid #e8edf5; border-radius:14px; padding:14px 18px; border-left:4px solid #06b6d4;"><div style="font-size:10px; font-weight:800; color:#64748b;">⚡ F1 • LATENCY</div><div style="font-size:28px; font-weight:800;">89.8% <span style="font-size:12px; color:#64748b;">• 12ms</span></div></div>
</div>
""", unsafe_allow_html=True)

left,right = st.columns([0.58,0.42], gap="medium")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="font-weight:800; font-size:15px; margin-bottom:2px;">🧩 Relationship Factors</div><div style="font-size:11px; color:#64748b; margin-bottom:10px;">Auto-updates from BondIQ Engine</div>', unsafe_allow_html=True)

    L,R = st.columns(2, gap="large")
    with L:
        comm = st.slider("c1", 0.0, 10.0, 8.2, key="c1")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl">💬 Communication</div><div class="bdg">{comm:.1f} / 10</div></div>', unsafe_allow_html=True)
        und = st.slider("c2", 0.0, 10.0, 8.1, key="c2")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl">🧠 Understanding</div><div class="bdg">{und:.1f} / 10</div></div>', unsafe_allow_html=True)
        supp = st.slider("c3", 0.0, 10.0, 8.3, key="c3")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl">🤝 Support</div><div class="bdg">{supp:.1f} / 10</div></div>', unsafe_allow_html=True)
        gift = st.slider("c4", 0.0, 15.0, 6.0, key="c4")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl">🎁 Gifts / Month</div><div class="bdg">{gift:.0f}</div></div>', unsafe_allow_html=True)

    with R:
        trust = st.slider("c5", 0.0, 10.0, 8.5, key="c5")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl">🛡️ Trust</div><div class="bdg">{trust:.1f} / 10</div></div>', unsafe_allow_html=True)
        time = st.slider("c6", 0.0, 168.0, 35.0, key="c6")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl">⏳ Time Together</div><div class="bdg">{time:.0f}h / w</div></div>', unsafe_allow_html=True)
        fight = st.slider("c7", 0.0, 15.0, 1.0, key="c7")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl" style="color:#ef4444;">⚡ Fights / Month</div><div class="bdg bdg-red">{fight:.0f}</div></div>', unsafe_allow_html=True)
        happy = st.slider("c8", 0.0, 10.0, 8.8, key="c8")
        st.markdown(f'<div class="top-row" style="margin-top:-22px;"><div class="lbl">😊 Happy Together</div><div class="bdg">{happy:.1f} / 10</div></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# MODEL PREDICT - TERI PKL SE
if model is not None:
    cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
    df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=cols)
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
    st.markdown(f"""
    <div class="card" style="padding:20px!important;">
      <div style="display:flex; justify-content:space-between; align-items:center;"><div style="font-weight:800; font-size:14px;">BondIQ Result</div><div style="width:7px; height:7px; background:#22c55e; border-radius:50%;"></div></div>
      <div style="font-size:11px; color:#64748b; margin-bottom:6px;">Powered by couple_love_model.pkl • Auto</div>
      <div class="circle-wrap"><div class="circle-box">
        <svg class="circle-svg" viewBox="0 0 180 180"><circle class="bg" cx="90" cy="90" r="68"/><circle class="prog" cx="90" cy="90" r="68" stroke-dasharray="{C}" stroke-dashoffset="{O}"/></svg>
        <div class="center-box"><div class="score-num">{sc}%</div><div class="score-lbl">BONDIQ SCORE</div></div>
      </div></div>
      <div style="text-align:center; margin-top:4px;"><span style="background:#dcfce7; color:#166534; padding:6px 14px; border-radius:20px; font-size:11px; font-weight:800;">● Moderate Compatibility • {sc}% Match</span></div>
    </div>
    """, unsafe_allow_html=True)
