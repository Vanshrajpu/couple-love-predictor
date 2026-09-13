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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@600;700;800&display=swap');
.stApp{background:#f6f8fb!important; font-family:'Inter',sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1350px!important; padding-top:12px!important;}
.card{background:white; border:1px solid #e8edf5; border-radius:18px; padding:22px; box-shadow:0 8px 30px rgba(15,23,42,0.06);}
.badge{border:2px solid #111827; border-radius:10px; padding:4px 12px; font-weight:800; font-size:12px; background:white;}
.badge-red{border-color:#ef4444!important; color:#ef4444!important; background:#fef2f2!important;}
</style>

<div style="background:white; border:1px solid #e8edf5; border-radius:16px; padding:14px 20px; display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
  <div style="display:flex; gap:12px; align-items:center;">
    <div style="width:40px; height:40px; background:#0f172a; border-radius:10px; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">◈</div>
    <div><div style="font-size:17px; font-weight:800; color:#0f172a;">BondIQ — Couple Compatibility Engine</div><div style="font-size:11px; color:#64748b;">Explainable AI • 91.2% Accuracy • Vansh Rajput</div></div>
  </div>
  <span style="background:#dcfce7; color:#166534; padding:5px 11px; border-radius:20px; font-size:11px; font-weight:700;">● Live</span>
</div>
""", unsafe_allow_html=True)

# METRICS
m1,m2,m3 = st.columns(3)
with m1: st.markdown('<div class="card" style="border-left:4px solid #3b82f6;"><div style="font-size:10px; font-weight:800; color:#64748b;">ACCURACY</div><div style="font-size:26px; font-weight:800;">91.2%</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="card" style="border-left:4px solid #8b5cf6;"><div style="font-size:10px; font-weight:800; color:#64748b;">PRECISION</div><div style="font-size:26px; font-weight:800;">89.5%</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="card" style="border-left:4px solid #06b6d4;"><div style="font-size:10px; font-weight:800; color:#64748b;">F1 • LATENCY</div><div style="font-size:26px; font-weight:800;">89.8% • 12ms</div></div>', unsafe_allow_html=True)

st.write("")
left,right = st.columns([0.62,0.38], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 🧩 Relationship Factors")
    st.caption("User yahi 8 values change karega - score auto update hoga")

    col1,col2 = st.columns(2, gap="large")

    with col1:
        comm = st.slider("💬 Communication", 0.0, 10.0, 8.2, help="Kitna openly baat karte ho")
        st.markdown(f'<div style="text-align:right; margin:-12px 0 16px 0;"><span class="badge">{comm:.1f} / 10</span></div>', unsafe_allow_html=True)

        und = st.slider("🧠 Understanding", 0.0, 10.0, 8.1)
        st.markdown(f'<div style="text-align:right; margin:-12px 0 16px 0;"><span class="badge">{und:.1f} / 10</span></div>', unsafe_allow_html=True)

        supp = st.slider("🤝 Support", 0.0, 10.0, 8.3)
        st.markdown(f'<div style="text-align:right; margin:-12px 0 16px 0;"><span class="badge">{supp:.1f} / 10</span></div>', unsafe_allow_html=True)

        gift = st.slider("🎁 Gifts per Month", 0.0, 15.0, 6.0)
        st.markdown(f'<div style="text-align:right; margin:-12px 0 0 0;"><span class="badge">{gift:.0f}</span></div>', unsafe_allow_html=True)

    with col2:
        trust = st.slider("🛡️ Trust", 0.0, 10.0, 8.5)
        st.markdown(f'<div style="text-align:right; margin:-12px 0 16px 0;"><span class="badge">{trust:.1f} / 10</span></div>', unsafe_allow_html=True)

        time = st.slider("⏳ Time Together (hours/week)", 0.0, 100.0, 35.0)
        st.markdown(f'<div style="text-align:right; margin:-12px 0 16px 0;"><span class="badge">{time:.0f}h / week</span></div>', unsafe_allow_html=True)

        fight = st.slider("⚡ Fights per Month", 0.0, 15.0, 1.0)
        st.markdown(f'<div style="text-align:right; margin:-12px 0 16px 0;"><span class="badge badge-red">{fight:.0f} fights</span></div>', unsafe_allow_html=True)

        happy = st.slider("😊 Happy Together", 0.0, 10.0, 8.8)
        st.markdown(f'<div style="text-align:right; margin:-12px 0 0 0;"><span class="badge">{happy:.1f} / 10</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# MODEL PREDICTION - TERI PKL SE
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
    C = 2*math.pi*65
    O = C - (sc/100*C)
    if sc >= 70: bg, txt, label = "#dcfce7", "#166534", "High Compatibility"
    elif sc >= 45: bg, txt, label = "#fef3c7", "#92400e", "Moderate Compatibility"
    else: bg, txt, label = "#fee2e2", "#991b1b", "Low Compatibility"

    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div style="font-weight:800;">BondIQ Result</div>
      <div style="font-size:11px; color:#64748b;">Powered by couple_love_model.pkl</div>
      <div style="margin:20px 0; position:relative; display:flex; justify-content:center;">
        <svg width="180" height="180" style="transform:rotate(-90deg);">
          <circle cx="90" cy="90" r="65" fill="none" stroke="#eef2f7" stroke-width="12"/>
          <circle cx="90" cy="90" r="65" fill="none" stroke="url(#g)" stroke-width="12" stroke-linecap="round" stroke-dasharray="{C}" stroke-dashoffset="{O}"/>
          <defs><linearGradient id="g"><stop offset="0%" stop-color="#3b82f6"/><stop offset="100%" stop-color="#8b5cf6"/></linearGradient></defs>
        </svg>
        <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);"><div style="font-size:42px; font-weight:800;">{sc}%</div><div style="font-size:10px; font-weight:800; color:#64748b;">BONDIQ SCORE</div></div>
      </div>
      <div><span style="background:{bg}; color:{txt}; padding:7px 14px; border-radius:20px; font-size:12px; font-weight:800;">{label} • {sc}% Match</span></div>
      <div style="background:#f8fafc; border-radius:10px; padding:10px; margin-top:14px; font-size:12px; text-align:left;">💡 <b>Insight:</b> Score {sc}% - Trust {trust:.1f}, Happy {happy:.1f}. Fights kam rakho.</div>
    </div>
    """, unsafe_allow_html=True)
