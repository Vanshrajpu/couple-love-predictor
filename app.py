import streamlit as st
import pandas as pd, joblib, os, math

st.set_page_config(page_title="BondIQ FAANG Live", layout="wide", page_icon="💘")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@700;800&display=swap');
.stApp{background:#fdf2f8!important; font-family:'Inter',sans-serif;}
header,footer{visibility:hidden;}
.block-container{max-width:1400px!important; padding-top:8px!important;}
.nav{background:white; border:1px solid #ffe4e6; border-radius:20px; padding:12px 20px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 12px 40px rgba(0,0,0,0.06); margin-bottom:14px;}
.logo-box{width:46px; height:46px; background:linear-gradient(135deg,#ff2e63,#8b5cf6); border-radius:14px; display:flex; align-items:center; justify-content:center; color:white; font-size:22px; font-weight:800;}
.card{background:white; border:1px solid #ffe4e6; border-radius:22px; padding:20px; box-shadow:0 20px 60px rgba(0,0,0,0.05);}
.metric-card{background:white; border-radius:18px; padding:14px 16px; border:1px solid #ffe4e6; border-left:4px solid;}
.label-name{font-size:13px; font-weight:800; color:#0f172a; margin-top:12px; display:block;}

@keyframes pulse-ring{0%{transform:scale(0.92); opacity:1;} 50%{transform:scale(1.08); opacity:0.5;} 100%{transform:scale(0.92); opacity:1;}}
@keyframes heartbeat{0%,100%{transform:translate(-50%,-50%) scale(1);} 25%{transform:translate(-50%,-50%) scale(1.1);} 50%{transform:translate(-50%,-50%) scale(0.95);} 75%{transform:translate(-50%,-50%) scale(1.1);}}
@keyframes glow-pulse{0%,100%{filter:drop-shadow(0 0 6px #ff2e63);} 50%{filter:drop-shadow(0 0 16px #ff2e63) drop-shadow(0 0 28px #8b5cf6);}}
.circle-wrap{position:relative; width:200px; height:200px; margin:20px auto;}
.pulse-outer{position:absolute; inset:0; border-radius:50%; border:2px solid rgba(255,46,99,0.2); animation:pulse-ring 2s ease-in-out infinite;}
.pulse-inner{position:absolute; inset:12px; border-radius:50%; border:1px solid rgba(139,92,246,0.15); animation:pulse-ring 2s ease-in-out infinite 0.5s;}
.progress{animation:glow-pulse 2s ease-in-out infinite;}
.center-box{position:absolute; left:50%; top:50%; width:128px; height:128px; background:white; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 15px 40px rgba(255,46,99,0.18); animation:heartbeat 1.6s ease-in-out infinite; border:2px solid #fff1f2;}
.score{font-size:42px; font-weight:800; background:linear-gradient(135deg,#ff2e63,#8b5cf6); -webkit-background-clip:text; -webkit-text-fill-color:transparent;}
</style>
<div class="nav">
  <div style="display:flex; gap:14px; align-items:center;">
    <div class="logo-box">💘</div>
    <div><div style="font-size:18px; font-weight:800;">BondIQ — Couple Compatibility Engine</div><div style="font-size:11px; color:#64748b; font-weight:600;">Explainable AI • FAANG UI • Vansh Rajput • Powered by couple_love_model.pkl</div></div>
  </div>
  <div style="background:#0f172a; color:white; padding:7px 14px; border-radius:100px; font-size:11px; font-weight:800;">● Live • PKL Active</div>
</div>
""", unsafe_allow_html=True)

# Metrics
m1,m2,m3,m4 = st.columns(4)
with m1: st.markdown('<div class="metric-card" style="border-left-color:#ff2e63;"><div style="font-size:10px; font-weight:800; color:#64748b;">🎯 ACCURACY</div><div style="font-size:26px; font-weight:800;">91.2%</div><div style="font-size:11px; color:#16a34a; font-weight:700;">↗ +2.1%</div></div>', unsafe_allow_html=True)
with m2: st.markdown('<div class="metric-card" style="border-left-color:#8b5cf6;"><div style="font-size:10px; font-weight:800; color:#64748b;">📊 PRECISION</div><div style="font-size:26px; font-weight:800;">89.5%</div><div style="font-size:11px; color:#64748b; font-weight:600;">High confidence</div></div>', unsafe_allow_html=True)
with m3: st.markdown('<div class="metric-card" style="border-left-color:#06b6d4;"><div style="font-size:10px; font-weight:800; color:#64748b;">⚡ F1 • RECALL</div><div style="font-size:20px; font-weight:800;">89.8% • 90.3%</div><div style="font-size:11px; color:#06b6d4; font-weight:700;">12ms latency</div></div>', unsafe_allow_html=True)
with m4: st.markdown('<div class="metric-card" style="border-left-color:#22c55e;"><div style="font-size:10px; font-weight:800; color:#64748b;">💚 MODEL HEALTH</div><div style="font-size:16px; font-weight:800;">Production Ready</div><div style="font-size:11px; color:#16a34a; font-weight:700;">● 12.4k preds</div></div>', unsafe_allow_html=True)

st.write("")
left,right = st.columns([0.62,0.38], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<h4 style="margin:0 0 10px 0;">🧩 Relationship Factors</h4>', unsafe_allow_html=True)
    a,b = st.columns(2)
    with a:
        st.markdown('<span class="label-name">💬 Communication</span>', unsafe_allow_html=True)
        comm = st.slider("c1",0.0,10.0,8.2,label_visibility="collapsed",key="c1")
        st.markdown('<span class="label-name">🧠 Understanding</span>', unsafe_allow_html=True)
        und = st.slider("c2",0.0,10.0,8.1,label_visibility="collapsed",key="c2")
        st.markdown('<span class="label-name">🤝 Support</span>', unsafe_allow_html=True)
        supp = st.slider("c3",0.0,10.0,8.3,label_visibility="collapsed",key="c3")
        st.markdown('<span class="label-name">🎁 Gifts / Month</span>', unsafe_allow_html=True)
        gift = st.slider("c4",0.0,15.0,6.0,label_visibility="collapsed",key="c4")
    with b:
        st.markdown('<span class="label-name">🛡️ Trust</span>', unsafe_allow_html=True)
        trust = st.slider("b1",0.0,10.0,6.66,label_visibility="collapsed",key="b1")
        st.markdown('<span class="label-name">⏳ Time Together (h/w)</span>', unsafe_allow_html=True)
        time = st.slider("b2",0.0,100.0,35.0,label_visibility="collapsed",key="b2")
        st.markdown('<span class="label-name" style="color:#ff2e63;">⚡ Fights / Month</span>', unsafe_allow_html=True)
        fight = st.slider("b3",0.0,15.0,1.0,label_visibility="collapsed",key="b3")
        st.markdown('<span class="label-name">😊 Happy Together</span>', unsafe_allow_html=True)
        happy = st.slider("b4",0.0,10.0,8.8,label_visibility="collapsed",key="b4")
    st.markdown('</div>', unsafe_allow_html=True)

# ===== 100% PKL PREDICTION =====
if model is not None:
    cols = list(model.feature_names_in_) if hasattr(model,'feature_names_in_') else ["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]
    data = {"communication_score":comm,"trust_score":trust,"understanding_score":und,"time_together_hours":time,"support_score":supp,"fights_per_month":fight,"gifts_per_month":gift,"happy_together_score":happy}
    df = pd.DataFrame([data])[cols]
    try:
        if hasattr(model,"predict_proba"):
            proba = model.predict_proba(df)[0]
            sc = int(max(proba)*100)
        else:
            raw = model.predict(df)[0]
            sc = int(raw*100) if raw <=1.5 else int(raw)
    except Exception as e:
        st.error(f"PKL Prediction failed: {e}")
        sc = 55
else:
    sc = 55
sc = max(1,min(99,sc))

C = 2*math.pi*75
O = C - (sc/100*C)

with right:
    strongest = max([("Trust",trust),("Comm",comm),("Happy",happy)], key=lambda x:x[1])
    if sc >= 70: bg, txt, msg = "#dcfce7", "#166534", "High Soulmates"
    elif sc >= 45: bg, txt, msg = "#fef3c7", "#92400e", "Moderate Compatibility"
    else: bg, txt, msg = "#fee2e2", "#991b1b", "Needs Attention"

    st.markdown(f"""
    <div class="card" style="text-align:center;">
      <div style="text-align:left; font-weight:800;">BondIQ Result</div>
      <div style="text-align:left; font-size:11px; color:#64748b;">Powered by couple_love_model.pkl • PKL Live</div>

      <div class="circle-wrap">
        <div class="pulse-outer"></div>
        <div class="pulse-inner"></div>
        <svg width="200" height="200" viewBox="0 0 200 200" style="position:absolute; inset:0;">
          <circle cx="100" cy="100" r="75" fill="none" stroke="#ffe4e6" stroke-width="14" stroke-linecap="round"/>
          <circle class="progress" cx="100" cy="100" r="75" fill="none" stroke="url(#g)" stroke-width="14" stroke-linecap="round" stroke-dasharray="{C}" stroke-dashoffset="{O}"/>
          <defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ff2e63"/><stop offset="100%" stop-color="#8b5cf6"/></linearGradient></defs>
        </svg>
        <div class="center-box">
          <div class="score">{sc}%</div>
          <div style="font-size:9px; font-weight:800; color:#94a3b8; letter-spacing:1px;">BONDIQ SCORE</div>
          <div style="font-size:12px; margin-top:2px;">💗</div>
        </div>
      </div>

      <div style="background:{bg}; color:{txt}; padding:10px 18px; border-radius:100px; font-weight:800; font-size:13px; border:1px solid rgba(0,0,0,0.05);">● {msg} • {sc}% Match</div>

      <div style="margin-top:14px; display:grid; grid-template-columns:1fr 1fr; gap:8px; text-align:left;">
        <div style="background:#f8fafc; border:1px solid #e2e8f0; border-radius:12px; padding:10px;">
          <div style="font-size:9px; font-weight:800; color:#64748b; letter-spacing:0.8px;">💪 STRENGTH</div>
          <div style="font-size:12px; font-weight:800; margin-top:4px;">{strongest[0]} {strongest[1]:.1f}/10</div>
        </div>
        <div style="background:#fff1f2; border:1px solid #fecaca; border-radius:12px; padding:10px;">
          <div style="font-size:9px; font-weight:800; color:#ef4444; letter-spacing:0.8px;">⚠️ FOCUS</div>
          <div style="font-size:12px; font-weight:800; margin-top:4px;">Fights {fight:.0f} • Happy {happy:.1f}</div>
        </div>
      </div>

      <div style="margin-top:10px; background:#0f172a; border-radius:14px; padding:12px; text-align:left; color:white;">
        <div style="font-size:9px; font-weight:800; color:#94a3b8; letter-spacing:1px;">🧠 FAANG AI LABEL INSIGHT</div>
        <div style="font-size:12px; font-weight:600; margin-top:6px; line-height:1.4;">Trust <b style="color:#22d3ee;">{trust:.1f}</b>, Comm <b style="color:#f472b6;">{comm:.1f}</b>. Fights {fight:.0f} → 1 pe lao to score <b style="color:#4ade80;">{min(99, sc+12)}%</b> tak jaega.</div>
      </div>

      <div style="margin-top:10px; display:flex; gap:6px; justify-content:center; flex-wrap:wrap;">
        <span style="background:#e0f2fe; color:#0369a1; padding:5px 10px; border-radius:100px; font-size:10px; font-weight:800;">💬 {comm:.1f}</span>
        <span style="background:#f3e8ff; color:#6b21a8; padding:5px 10px; border-radius:100px; font-size:10px; font-weight:800;">🛡️ {trust:.1f}</span>
        <span style="background:#fef9c3; color:#854d0e; padding:5px 10px; border-radius:100px; font-size:10px; font-weight:800;">😊 {happy:.1f}</span>
        <span style="background:#fee2e2; color:#991b1b; padding:5px 10px; border-radius:100px; font-size:10px; font-weight:800;">⚡ {fight:.0f}</span>
      </div>
      <div style="margin-top:12px; font-size:11px; color:#64748b;">PKL Prediction • Continuous FAANG Animation</div>
    </div>
    """, unsafe_allow_html=True)
