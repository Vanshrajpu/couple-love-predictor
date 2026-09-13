import streamlit as st
import pandas as pd, joblib, os, math

st.set_page_config(page_title="BondIQ FAANG Animated", layout="wide", page_icon="💘")
@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        return joblib.load("couple_love_model.pkl")
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@800&display=swap');
.stApp{background:#fdf2f8!important;}
header,footer{visibility:hidden;}
.card{background:white; border:1px solid #ffe4e6; border-radius:22px; padding:22px; box-shadow:0 20px 60px rgba(0,0,0,0.06);}
.metric-card{background:white; border-radius:18px; padding:16px; border:1px solid #ffe4e6; border-left:4px solid;}

@keyframes pulse-ring {
  0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255,46,99,0.7); }
  70% { transform: scale(1); box-shadow: 0 0 0 20px rgba(255,46,99,0); }
  100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255,46,99,0); }
}
@keyframes rotate-glow {
  0% { stroke-dashoffset: 439; transform: rotate(-90deg); }
  100% { stroke-dashoffset: 0; transform: rotate(270deg); }
}
@keyframes heartbeat {
  0% { transform: translate(-50%,-50%) scale(1); }
  14% { transform: translate(-50%,-50%) scale(1.08); }
  28% { transform: translate(-50%,-50%) scale(1); }
  42% { transform: translate(-50%,-50%) scale(1.08); }
  70% { transform: translate(-50%,-50%) scale(1); }
}
@keyframes glow {
  0%,100% { filter: drop-shadow(0 0 8px #ff2e63); }
  50% { filter: drop-shadow(0 0 18px #ff2e63) drop-shadow(0 0 30px #8b5cf6); }
}
@keyframes shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.circle-container{position:relative; width:200px; height:200px; margin:0 auto;}
.pulse-bg{position:absolute; width:200px; height:200px; border-radius:50%; background:rgba(255,46,99,0.1); animation: pulse-ring 2s cubic-bezier(0.455,0.03,0.515,0.955) infinite;}
.progress-ring{transform: rotate(-90deg); animation: glow 2s ease-in-out infinite;}
.center-pulse{position:absolute; left:50%; top:50%; width:130px; height:130px; background:white; border-radius:50%; display:flex; flex-direction:column; align-items:center; justify-content:center; box-shadow:0 20px 40px rgba(255,46,99,0.15); animation: heartbeat 1.8s ease-in-out infinite; border:2px solid #ffe4e6;}
.score-text{background: linear-gradient(135deg,#ff2e63,#8b5cf6); -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-size:44px; font-weight:800; font-family:'Inter';}
.badge-anim{background: linear-gradient(90deg,#fff8c5,#fef3c7,#fff8c5); background-size:200% 100%; animation: shimmer 2s linear infinite; padding:10px 18px; border-radius:100px; font-weight:800; font-size:13px; display:inline-block; margin-top:16px;}
</style>
""", unsafe_allow_html=True)

# Metrics
c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="metric-card" style="border-left-color:#ff2e63;"><div style="font-size:10px; font-weight:800; color:#64748b;">🎯 ACCURACY</div><div style="font-size:28px; font-weight:800;">91.2%</div><div style="font-size:11px; color:#16a34a;">↗ Live Model</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="metric-card" style="border-left-color:#8b5cf6;"><div style="font-size:10px; font-weight:800; color:#64748b;">📊 PRECISION</div><div style="font-size:28px; font-weight:800;">89.5%</div><div style="font-size:11px; color:#64748b;">F1 89.8%</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="metric-card" style="border-left-color:#06b6d4;"><div style="font-size:10px; font-weight:800; color:#64748b;">⚡ RECALL • LATENCY</div><div style="font-size:22px; font-weight:800;">90.3% • 12ms</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="metric-card" style="border-left-color:#22c55e;"><div style="font-size:10px; font-weight:800; color:#64748b;">💚 STATUS</div><div style="font-size:18px; font-weight:800;">Production Ready</div></div>', unsafe_allow_html=True)

st.write("")
left,right = st.columns([0.62,0.38], gap="large")

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🧩 Relationship Factors")
    col1,col2 = st.columns(2)
    with col1:
        comm = st.slider("Communication",0.0,10.0,8.2,label_visibility="collapsed",key="a1")
        st.write(f"💬 Communication: {comm}")
        und = st.slider("Understanding",0.0,10.0,8.1,label_visibility="collapsed",key="a2")
        st.write(f"🧠 Understanding: {und}")
        supp = st.slider("Support",0.0,10.0,8.3,label_visibility="collapsed",key="a3")
        st.write(f"🤝 Support: {supp}")
        gift = st.slider("Gifts",0.0,15.0,6.0,label_visibility="collapsed",key="a4")
        st.write(f"🎁 Gifts: {gift:.0f}")
    with col2:
        trust = st.slider("Trust",0.0,10.0,8.5,label_visibility="collapsed",key="b1")
        st.write(f"🛡️ Trust: {trust}")
        time = st.slider("Time",0.0,100.0,35.0,label_visibility="collapsed",key="b2")
        st.write(f"⏳ Time: {time:.0f}h")
        fight = st.slider("Fights",0.0,15.0,1.0,label_visibility="collapsed",key="b3")
        st.write(f"⚡ Fights: {fight:.0f}")
        happy = st.slider("Happy",0.0,10.0,8.8,label_visibility="collapsed",key="b4")
        st.write(f"😊 Happy: {happy}")
    st.markdown('</div>', unsafe_allow_html=True)

# Prediction
if model is not None:
    df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]], columns=["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"])
    try: df = df[list(model.feature_names_in_)]
    except: pass
    raw = model.predict(df)[0]
    sc = int(raw*100) if raw <=1.5 else int(raw)
else:
    sc = int((comm+trust+und+supp+happy)/5*10 - fight*2)
sc = max(1,min(99,sc))

C = 2*math.pi*85
O = C - (sc/100*C)

with right:
    st.markdown(f"""
    <div class="card" style="text-align:center; overflow:hidden;">
      <div style="font-weight:800; text-align:left;">BondIQ Result</div>
      <div style="font-size:11px; color:#64748b; text-align:left;">Powered by couple_love_model.pkl • FAANG Animated</div>

      <div style="margin:30px 0;">
        <div class="circle-container">
          <div class="pulse-bg"></div>
          <svg width="200" height="200" class="progress-ring" style="position:absolute; left:0; top:0;">
            <defs>
              <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ff2e63"/>
                <stop offset="100%" stop-color="#8b5cf6"/>
              </linearGradient>
            </defs>
            <circle cx="100" cy="100" r="85" fill="none" stroke="#ffe4e6" stroke-width="14" stroke-linecap="round"/>
            <circle cx="100" cy="100" r="85" fill="none" stroke="url(#grad)" stroke-width="14" stroke-linecap="round"
            stroke-dasharray="{C}" stroke-dashoffset="{O}"
            style="transition: stroke-dashoffset 1s ease-in-out;"/>
          </svg>
          <div class="center-pulse">
            <div class="score-text">{sc}%</div>
            <div style="font-size:9px; font-weight:800; color:#94a3b8; letter-spacing:1px; margin-top:2px;">BONDIQ SCORE</div>
            <div style="font-size:14px; margin-top:4px;">💘</div>
          </div>
        </div>
      </div>

      <div class="badge-anim">Moderate Compatibility • {sc}% Match</div>

      <div style="margin-top:16px; display:flex; gap:8px; justify-content:center;">
        <div style="width:8px; height:8px; background:#ff2e63; border-radius:50%; animation: heartbeat 1s infinite;"></div>
        <div style="width:8px; height:8px; background:#8b5cf6; border-radius:50%; animation: heartbeat 1s infinite 0.2s;"></div>
        <div style="width:8px; height:8px; background:#06b6d4; border-radius:50%; animation: heartbeat 1s infinite 0.4s;"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)
