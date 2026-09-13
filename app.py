import streamlit as st, pandas as pd, joblib, os

st.set_page_config(page_title="Love Prediction - Vansh Rajput", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    if os.path.exists("couple_love_model.pkl"):
        m=joblib.load("couple_love_model.pkl")
        return m
    return None
model = load_model()

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Dancing+Script:wght@600&display=swap');
.stApp{background:#080e2a!important;}
header,footer{visibility:hidden;}
.block-container{padding:0!important; max-width:100%!important;}
*{font-family:'Poppins',sans-serif;}

/* TOP - COUPLE BG */
.top{
  height:110px; padding:16px 28px; display:flex; justify-content:space-between; align-items:center;
  background: linear-gradient(90deg, #0a0f2a 0%, rgba(10,15,42,0.6) 40%, rgba(10,15,42,0.1) 100%),
  radial-gradient(600px at 70% 0%, rgba(255,77,166,0.25), transparent),
  url('https://images.unsplash.com/photo-1516589177381-225540ac6a9c?q=80&w=2000')!important;
  background-size:cover!important; background-position:center 30%!important;
  border-bottom:1px solid rgba(255,77,166,0.15);
}
.logo{width:52px; height:52px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:26px; box-shadow:0 0 24px #ff4da6;}
.card{
  background:linear-gradient(180deg, rgba(16,23,58,0.96), rgba(12,18,48,0.96))!important;
  border:1px solid rgba(255,255,255,0.08)!important; border-radius:18px!important; padding:18px!important;
  box-shadow:0 20px 60px rgba(0,0,0,0.4)!important;
}
.side{ background:rgba(8,12,32,0.9); border-radius:14px; padding:10px; }
.side-item{padding:11px 14px; border-radius:10px; margin:6px 0; color:#8b90b5; font-size:13px; display:flex; gap:10px; align-items:center;}
.side-active{background:linear-gradient(90deg, rgba(255,77,166,0.22), rgba(168,85,247,0.18)); color:white!important; border:1px solid rgba(255,77,166,0.22); box-shadow:0 4px 16px rgba(255,77,166,0.2);}

.stSlider label{color:#cbd5e1!important; font-size:12px!important; font-weight:500!important;}
.stSlider > div > div > div > div{background:linear-gradient(90deg,#ff4da6,#a855f7)!important;}

.btn button{
  background:linear-gradient(90deg,#ff4da6,#a855f7)!important; color:white!important;
  border:none!important; border-radius:12px!important; height:50px!important; font-weight:700!important;
  box-shadow:0 10px 24px rgba(255,77,166,0.4)!important; width:100%!important;
}
.heart{
  width:130px; height:130px; margin:0 auto;
  background: radial-gradient(circle at 30% 30%, rgba(255,77,166,0.35), rgba(168,85,247,0.15));
  border:2.5px solid #ff4da6; border-radius:30% 30% 50% 50% / 30% 30% 70% 70%;
  display:flex; align-items:center; justify-content:center; font-size:36px; font-weight:800; color:white;
  box-shadow:0 0 40px rgba(255,77,166,0.6), inset 0 0 20px rgba(255,77,166,0.3);
  animation: beat 1.2s infinite;
}
@keyframes beat{0%,100%{transform:scale(1);}15%{transform:scale(1.12);}}
.bar{height:10px; background:rgba(255,255,255,0.08); border-radius:20px; overflow:hidden; margin-top:12px;}
.fill{height:100%; background:linear-gradient(90deg,#ff4da6,#a855f7); border-radius:20px;}
.insight{background:rgba(255,255,255,0.05); border-radius:12px; padding:12px; text-align:center; border:1px solid rgba(255,255,255,0.06);}
</style>
.heart{
  animation: beat 1.2s infinite ease-in-out, glow 2s infinite alternate;
}
@keyframes beat{
  0%,100%{transform:scale(1);}
  25%{transform:scale(1.18);}
}
@keyframes glow{
  0%{box-shadow:0 0 20px rgba(255,77,166,0.5);}
  100%{box-shadow:0 0 45px rgba(255,77,166,0.9), 0 0 70px rgba(168,85,247,0.6);}
}
.bar-fill{
  animation: fillBar 2s ease-out forwards;
}
@keyframes fillBar{
  from{width:0%;}
}
<div class="top">
  <div style="display:flex; gap:14px; align-items:center;">
    <div class="logo">💞</div>
    <div><div style="font-size:26px; font-weight:800; color:white;"><span style="color:#ff4da6;">Love</span> Prediction</div><div style="color:#8b90b5; font-size:12px; letter-spacing:0.5px;">AI • Data • Better Love Insights</div></div>
  </div>
  <div style="text-align:right;"><div style="color:#ffb3d1; font-family:'Dancing Script',cursive; font-size:18px;">Some connections<br>are meant to be... ♡</div></div>
</div>
""", unsafe_allow_html=True)

col_nav, col_mid, col_res = st.columns([0.16,0.44,0.40], gap="medium")

with col_nav:
    st.markdown("""
    <div class="side" style="height:780px;">
      <div class="side-item side-active">🏠 Home</div>
      <div class="side-item">♡ Prediction</div>
      <div class="side-item">📊 About Model</div>
      <div class="side-item">ⓘ How It Works</div>
      <div style="margin-top:380px; color:#ff8ec8; font-family:'Dancing Script',cursive; font-size:13px; line-height:1.3; padding:10px;">
        <div style="font-size:18px;">💓</div>
        Love isn't just a feeling...<br><b>It's a connection</b> ♡
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_mid:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 💖 Enter Your Details")
    st.caption("Fill in the 8 factors below to predict your compatibility - True model")

    comm = st.slider("💬 Communication Score", 0.0, 10.0, 7.2)
    trust = st.slider("🛡️ Trust Score", 0.0, 10.0, 8.5)
    und = st.slider("🤝 Understanding Score", 0.0, 10.0, 6.8)
    time = st.slider("⏰ Time Together Hours", 0.0, 168.0, 32.0)
    supp = st.slider("💞 Support Score", 0.0, 10.0, 7.9)
    fight = st.slider("⚡ Fights Per Month", 0.0, 15.0, 2.0)
    gift = st.slider("🎁 Gifts Per Month", 0.0, 15.0, 5.0)
    happy = st.slider("😊 Happy Together Score", 0.0, 10.0, 8.8)

    run = st.button("✨ Predict Love →", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with col_res:
    if 'score' not in st.session_state: st.session_state.score = 87
    if run and model:
        df = pd.DataFrame([[comm,trust,und,time,supp,fight,gift,happy]],
        columns=["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"])
        if hasattr(model,"feature_names_in_"):
            df = df[list(model.feature_names_in_)]
        raw = model.predict(df)[0]
        sc = int(raw*100) if raw<=1.5 else int(raw)
        st.session_state.score = max(1,min(99,sc))

    sc = st.session_state.score
    label = "High Compatibility!" if sc>=75 else "Good Compatibility" if sc>=50 else "Needs Work"
    desc = "You and your partner have a strong chance of a healthy and long-lasting relationship." if sc>=75 else "Decent bond, work on communication."

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="font-weight:700; color:white; display:flex; gap:8px; align-items:center;">💗 Prediction Result</div>
        <div style="background:rgba(255,255,255,0.08); padding:5px 10px; border-radius:20px; font-size:10px; color:#cbd5e1;">✨ AI Powered</div>
      </div>

      <div style="display:flex; gap:18px; align-items:center; margin-top:18px;">
        <div class="heart">{sc}%</div>
        <div><div style="font-size:22px; font-weight:800; color:#ff7ab8;">{label}</div><div style="color:#a8b0d0; font-size:12px; margin-top:6px; line-height:1.4;">{desc}</div></div>
      </div>

      <div class="bar"><div class="fill" style="width:{sc}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:6px; font-size:12px; color:#8b90b5;"><span>Compatibility Score</span><span style="color:white; font-weight:700;">{sc}%</span></div>

      <div style="margin-top:18px; background:rgba(255,255,255,0.04); border-radius:14px; padding:14px; border:1px solid rgba(255,255,255,0.06);">
        <div style="font-weight:600; color:white; font-size:13px; margin-bottom:10px;">⊕ Key Insights</div>
        <div style="display:grid; grid-template-columns:1fr 1fr 1fr 1fr; gap:10px;">
          <div class="insight"><div style="color:#ff4da6;">♡</div><div style="font-size:11px; color:#8b90b5; margin-top:4px;">Communication</div><div style="font-size:12px; color:white; font-weight:700; margin-top:2px;">High</div></div>
          <div class="insight"><div style="color:#ff8ec8;">☆</div><div style="font-size:11px; color:#8b90b5; margin-top:4px;">Trust</div><div style="font-size:12px; color:white; font-weight:700; margin-top:2px;">High</div></div>
          <div class="insight"><div style="color:#60a5fa;">🛡</div><div style="font-size:11px; color:#8b90b5; margin-top:4px;">Support</div><div style="font-size:12px; color:white; font-weight:700; margin-top:2px;">High</div></div>
          <div class="insight"><div style="color:#a78bfa;">☺</div><div style="font-size:11px; color:#8b90b5; margin-top:4px;">Happy</div><div style="font-size:12px; color:white; font-weight:700; margin-top:2px;">{happy}</div></div>
        </div>
      </div>

      <div style="margin-top:14px; background:rgba(255,255,255,0.04); border-radius:14px; padding:14px; border:1px solid rgba(255,255,255,0.06);">
        <div style="font-weight:600; color:white; font-size:13px;">💡 Why This Prediction?</div>
        <div style="color:#8b90b5; font-size:11px; margin-top:6px; line-height:1.5;">Based on your 8 scores (comm, trust, understanding, time, support, fights, gifts, happy), the model predicts {sc}% compatibility. Your values align well, increasing chances of success.</div>
      </div>

      <div style="text-align:right; margin-top:12px; color:#ffb3d1; font-family:'Dancing Script',cursive; font-size:14px;">Good things take time... ♡</div>
    </div>
    """, unsafe_allow_html=True)
