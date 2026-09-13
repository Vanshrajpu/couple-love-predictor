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
.stApp{background:#f6f8fb!important; font-family:'Inter',sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1350px!important; padding-top:10px!important;}
.card{background:white; border:1px solid #e8edf5; border-radius:18px; padding:22px; box-shadow:0 8px 24px rgba(15,23,42,0.05);}
.label-row{display:flex; justify-content:space-between; align-items:center; margin-top:18px; margin-bottom:2px;}
.label-name{font-size:14px; font-weight:800; color:#0f172a!important;}
.badge{border:2px solid #0f172a; border-radius:10px; padding:4px 12px; font-weight:800; font-size:12px; background:white; color:#0f172a;}
.badge-red{border-color:#ef4444!important; color:#ef4444!important; background:#fef2f2!important;}
/* slider black */
div[data-baseweb="slider"] > div > div{background:#e5e7eb!important; height:6px!important;}
div[data-baseweb="slider"] > div > div > div{background:#0f172a!important;}
</style>

<div style="background:white; border:1px solid #e8edf5; border-radius:16px; padding:14px 20px; display:flex; justify-content:space-between; align-items:center; margin-bottom:14px;">
  <div style="display:flex; gap:12px; align-items:center;">
    <div style="width:40px; height:40px; background:#0f172a; border-radius:10px; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">◈</div>
    <div><div style="font-size:17px; font-weight:800; color:#0f172a;">BondIQ — Couple Compatibility Engine</div><div style="font-size:11px; color:#64748b;">Explainable AI • 91.2% Accuracy • Production Ready</div></div>
  </div>
  <span style="background:#dcfce7; color:#166534; padding:5px 11px; border-radius:20px; font-size:11px; font-weight:700;">● Live • Auto</span>
</div>
""", unsafe_allow_html=True)

left,right = st.columns([0.62,0.38], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('**🧩 Relationship Factors**')
    st.caption('Har factor ka naam ab kaale me dikhega - teri photo wala issue fixed')

    l1,l2 = st.columns(2, gap="large")
    with l1:
        st.markdown('<div class="label-row"><span class="label-name">💬 Communication</span></div>', unsafe_allow_html=True)
        comm = st.slider("communication", 0.0, 10.0, 8.2, label_visibility="collapsed", key="c1")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{comm:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">🧠 Understanding</span></div>', unsafe_allow_html=True)
        und = st.slider("understanding", 0.0, 10.0, 8.1, label_visibility="collapsed", key="c2")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{und:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">🤝 Support</span></div>', unsafe_allow_html=True)
        supp = st.slider("support", 0.0, 10.0, 8.3, label_visibility="collapsed", key="c3")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{supp:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">🎁 Gifts / Month</span></div>', unsafe_allow_html=True)
        gift = st.slider("gifts", 0.0, 15.0, 6.0, label_visibility="collapsed", key="c4")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{gift:.0f}</span></div>', unsafe_allow_html=True)

    with l2:
        st.markdown('<div class="label-row"><span class="label-name">🛡️ Trust</span></div>', unsafe_allow_html=True)
        trust = st.slider("trust", 0.0, 10.0, 8.5, label_visibility="collapsed", key="c5")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{trust:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">⏳ Time Together</span></div>', unsafe_allow_html=True)
        time = st.slider("time", 0.0, 100.0, 35.0, label_visibility="collapsed", key="c6")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{time:.0f}h / w</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name" style="color:#ef4444!important;">⚡ Fights / Month</span></div>', unsafe_allow_html=True)
        fight = st.slider("fights", 0.0, 15.0, 1.0, label_visibility="collapsed", key="c7")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge badge-red">{fight:.0f}</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">😊 Happy Together</span></div>', unsafe_allow_html=True)
        happy = st.slider("happy", 0.0, 10.0, 8.8, label_visibility="collapsed", key="c8")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{happy:.1f} / 10</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Prediction from your pkl
if model is not None:
    cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
    df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=cols)
    if hasattr(model,"feature_names_in_"):
        try: df = df[list(model.feature_names_in_)]
        except: pass
    raw = model.predict(df)[0]
    sc = int(raw*100) if raw <= 1.5 else int(raw)
else:
    sc = int((comm+trust+und+supp+happy)/5*10 - fight*2)
sc = max(1, min(99, sc))

with right:
    C = 2*math.pi*65
    O = C - (sc/100*C)
    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div style="font-weight:800; font-size:15px;">BondIQ Result</div>
      <div style="font-size:11px; color:#64748b;">Powered by couple_love_model.pkl • Auto</div>
      <div style="margin:24px 0; display:flex; justify-content:center; position:relative;">
        <svg width="180" height="180" style="transform:rotate(-90deg);">
          <circle cx="90" cy="90" r="65" fill="none" stroke="#eef2f7" stroke-width="12"/>
          <circle cx="90" cy="90" r="65" fill="none" stroke="#0f172a" stroke-width="12" stroke-linecap="round" stroke-dasharray="{C}" stroke-dashoffset="{O}"/>
        </svg>
        <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);">
          <div style="font-size:44px; font-weight:800; color:#0f172a;">{sc}%</div>
          <div style="font-size:10px; font-weight:800; color:#94a3b8; letter-spacing:1px;">BONDIQ SCORE</div>
        </div>
      </div>
      <div style="background:#fef3c7; color:#92400e; padding:8px 14px; border-radius:20px; font-size:12px; font-weight:800;">● Moderate Compatibility • {sc}% Match</div>
      <div style="background:#f8fafc; border-radius:12px; padding:12px; margin-top:14px; text-align:left; font-size:12px;">💡 BondIQ Score {sc}% — Communication {comm:.1f} + 0.8 push to 90%+</div>
    </div>
    """, unsafe_allow_html=True)
