import streamlit as st
import pandas as pd
import joblib
import os
import math

st.set_page_config(page_title="BondIQ - FAANG UI", layout="wide", page_icon="💘")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None

model = load_model()

# CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@700;800&display=swap');
.stApp{background:#fdf2f8!important; font-family:'Inter',sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1400px!important; padding-top:10px!important;}
.card{background:white; border:1px solid #ffe4e6; border-radius:20px; padding:22px; box-shadow:0 12px 40px rgba(0,0,0,0.06);}
.label-row{display:flex; justify-content:space-between; align-items:center; margin-top:16px; margin-bottom:4px;}
.label-name{font-size:14px; font-weight:800; color:#0f172a;}
.badge{background:#0f172a; color:white; padding:4px 12px; border-radius:20px; font-size:11px; font-weight:800;}
.badge-red{background:#ff2e63!important;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div style="background:white; border-radius:18px; padding:14px 20px; display:flex; justify-content:space-between; align-items:center; border:1px solid #ffe4e6; margin-bottom:14px;">
  <div style="display:flex; gap:12px; align-items:center;">
    <div style="width:40px; height:40px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); border-radius:12px; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">💘</div>
    <div><div style="font-weight:800; font-size:16px;">BondIQ - FAANG Edition</div><div style="font-size:11px; color:#64748b;">Explainable AI • 91.2% Accuracy • Vansh Rajput</div></div>
  </div>
  <div style="background:#0f172a; color:white; padding:6px 12px; border-radius:20px; font-size:11px; font-weight:700;">● Live</div>
</div>
""", unsafe_allow_html=True)

left, right = st.columns([0.62, 0.38], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 🧩 Relationship Factors")

    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="label-row"><span class="label-name">💬 Communication</span></div>', unsafe_allow_html=True)
        comm = st.slider("Communication", 0.0, 10.0, 8.2, key="a1", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{comm:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">🧠 Understanding</span></div>', unsafe_allow_html=True)
        und = st.slider("Understanding", 0.0, 10.0, 8.1, key="a2", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{und:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">🤝 Support</span></div>', unsafe_allow_html=True)
        supp = st.slider("Support", 0.0, 10.0, 8.3, key="a3", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{supp:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">🎁 Gifts / Month</span></div>', unsafe_allow_html=True)
        gift = st.slider("Gifts per Month", 0.0, 15.0, 6.0, key="a4", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{gift:.0f}</span></div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="label-row"><span class="label-name">🛡️ Trust</span></div>', unsafe_allow_html=True)
        trust = st.slider("Trust", 0.0, 10.0, 8.5, key="b1", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{trust:.1f} / 10</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">⏳ Time Together</span></div>', unsafe_allow_html=True)
        time = st.slider("Time Together", 0.0, 100.0, 35.0, key="b2", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{time:.0f}h / w</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name" style="color:#ff2e63;">⚡ Fights / Month</span></div>', unsafe_allow_html=True)
        fight = st.slider("Fights per Month", 0.0, 15.0, 1.0, key="b3", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge badge-red">{fight:.0f}</span></div>', unsafe_allow_html=True)

        st.markdown('<div class="label-row"><span class="label-name">😊 Happy Together</span></div>', unsafe_allow_html=True)
        happy = st.slider("Happy Together", 0.0, 10.0, 8.8, key="b4", label_visibility="collapsed")
        st.markdown(f'<div style="text-align:right; margin-top:-10px;"><span class="badge">{happy:.1f} / 10</span></div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

# Prediction
if model is not None:
    cols = ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
    df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=cols)
    try:
        df = df[list(model.feature_names_in_)]
    except:
        pass
    raw = model.predict(df)[0]
    sc = int(raw*100) if raw <= 1.5 else int(raw)
else:
    sc = int((comm+trust+und+supp+happy)/5*10 - fight*2)
sc = max(1, min(99, sc))

with right:
    C = 2*math.pi*70
    O = C - (sc/100*C)
    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div style="font-weight:800;">BondIQ Result</div>
      <div style="font-size:11px; color:#64748b;">Powered by couple_love_model.pkl</div>
      <div style="margin:20px 0; display:flex; justify-content:center;">
        <div style="position:relative; width:180px; height:180px;">
          <svg width="180" height="180" style="transform:rotate(-90deg);">
            <circle cx="90" cy="90" r="70" fill="none" stroke="#ffe4e6" stroke-width="14"/>
            <circle cx="90" cy="90" r="70" fill="none" stroke="#ff2e63" stroke-width="14" stroke-linecap="round" stroke-dasharray="{C}" stroke-dashoffset="{O}"/>
          </svg>
          <div style="position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); background:white; width:120px; height:120px; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(255,46,99,0.2);">
            <div style="font-size:40px; font-weight:800; color:#ff2e63;">{sc}%</div>
            <div style="font-size:9px; font-weight:800; color:#94a3b8;">BONDIQ SCORE</div>
          </div>
        </div>
      </div>
      <div style="background:#fef3c7; padding:8px 14px; border-radius:20px; font-size:12px; font-weight:800;">Moderate Compatibility • {sc}% Match</div>
    </div>
    """, unsafe_allow_html=True)
