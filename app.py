import streamlit as st
import pandas as pd
import joblib, os

st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    for name in ["couple_love_model.pkl","model.pkl","love_model.pkl"]:
        if os.path.exists(name):
            try: return joblib.load(name)
            except: pass
    return None
model = load_model()

def model_predict(comm, trust, interests, rel, ay, ap):
    cmap={"Open":9,"Open & Honest":9,"Honest":8,"Playful":7,"Reserved":5}
    tmap={"High":9,"Medium":6,"Low":3}
    rmap={"Dating":6,"Married":8,"Long Distance":4,"Crush":3}
    cs=cmap.get(comm,8); ts=tmap.get(trust,8); th=rmap.get(rel,6)
    us=min(10,5+len(interests)*1.2)
    feats={"communication_score":cs,"trust_score":ts,"understanding_score":us,"time_together_hours":th,"support_score":8,"fights_per_month":1,"gifts_per_month":3,"happy_together_score":9 if ts>=8 else 6}
    if model is None: return None
    try:
        df=pd.DataFrame([feats])
        if hasattr(model,"feature_names_in_"):
            cols=list(model.feature_names_in_)
            for c in cols:
                if c not in df: df[c]=0
            df=df[cols]
        raw=model.predict(df)[0]
        score=int(raw*100) if raw<=1.5 else int(raw)
        if abs(ay-ap)>12: score-=6
        score+=len(interests)
        return max(5,min(98,score))
    except: return None

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Dancing+Script:wght@600&display=swap');
.stApp{background:#050a1e!important; overflow:hidden;}
header,footer,#MainMenu{visibility:hidden;}
.block-container{max-width:99%!important; padding:0 1rem!important;}
*{font-family:'Poppins',sans-serif;}

/* ANIMATED BG GRADIENT */
.stApp::before{
  content:''; position:fixed; inset:0; z-index:-1;
  background: radial-gradient(600px at 15% 20%, rgba(255,77,166,0.18), transparent),
              radial-gradient(800px at 85% 80%, rgba(168,85,247,0.18), transparent),
              radial-gradient(500px at 50% 0%, rgba(255,45,106,0.12), transparent);
  animation: bgMove 10s infinite alternate;
}
@keyframes bgMove{0%{transform:scale(1) translate(0,0);}100%{transform:scale(1.1) translate(-20px,20px);}}

/* FLOATING HEARTS */
.hearts{position:fixed; inset:0; pointer-events:none; z-index:0; overflow:hidden;}
.hearts span{
  position:absolute; bottom:-20px; font-size:18px; color:#ff4da6; opacity:0.6;
  animation: floatUp linear infinite;
}
@keyframes floatUp{
  0%{transform:translateY(0) translateX(0) rotate(0deg) scale(0.8); opacity:0;}
  10%{opacity:0.7;}
  90%{opacity:0.5;}
  100%{transform:translateY(-110vh) translateX(100px) rotate(360deg) scale(1.4); opacity:0;}
}

.top{
  height:96px; margin:-14px -16px 18px -16px; padding:0 28px;
  background:linear-gradient(90deg, rgba(7,10,30,0.9) 0%, rgba(25,15,50,0.8) 100%);
  border-bottom:1px solid rgba(255,77,166,0.18);
  backdrop-filter:blur(12px);
  display:flex; justify-content:space-between; align-items:center;
  position:relative; z-index:2;
  box-shadow:0 4px 30px rgba(255,77,166,0.15);
  animation: topGlow 3s infinite alternate;
}
@keyframes topGlow{0%{box-shadow:0 4px 20px rgba(255,77,166,0.1);}100%{box-shadow:0 4px 35px rgba(168,85,247,0.25);}}

.logo-box{
  width:48px; height:48px; background:linear-gradient(135deg,#ff4da6,#a855f7);
  border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:24px;
  box-shadow:0 0 20px rgba(255,77,166,0.6); animation: logoPulse 2s infinite;
}
@keyframes logoPulse{0%,100%{transform:scale(1); box-shadow:0 0 15px #ff4da6;}50%{transform:scale(1.08); box-shadow:0 0 30px #ff4da6, 0 0 45px #a855f7;}}

.card{
  background:rgba(16,22,58,0.85)!important; backdrop-filter:blur(14px)!important;
  border:1px solid rgba(255,77,166,0.14)!important; border-radius:18px!important; padding:20px!important;
  box-shadow:0 8px 32px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05)!important;
  position:relative; z-index:1; transition:0.3s;
}
.card:hover{border-color:rgba(255,77,166,0.3)!important; box-shadow:0 12px 40px rgba(255,77,166,0.18)!important; transform:translateY(-2px);}

.nav-on{
  background:linear-gradient(90deg, rgba(255,77,166,0.32), rgba(168,85,247,0.28))!important;
  border:1px solid rgba(255,77,166,0.3)!important; border-radius:12px; padding:12px 16px;
  color:white!important; font-weight:700; display:flex; gap:12px; box-shadow:0 0 20px rgba(255,77,166,0.35);
  animation: navGlow 2.5s infinite alternate;
}
@keyframes navGlow{0%{box-shadow:0 0 10px rgba(255,77,166,0.2);}100%{box-shadow:0 0 22px rgba(255,77,166,0.45);}}
.nav{color:#6f769e; padding:12px 16px; display:flex; gap:12px; font-size:14px; border-radius:12px; background:rgba(19,27,71,0.6); margin-bottom:10px; border:1px solid rgba(255,255,255,0.04); transition:0.2s;}
.nav:hover{background:rgba(255,77,166,0.08); color:#ffb3d1; transform:translateX(4px);}

.stSelectbox>div>div,.stNumberInput>div>div>input{background:rgba(19,27,71,0.9)!important; border:1px solid rgba(255,255,255,0.08)!important; border-radius:12px!important; color:#c8d0f0!important; height:46px!important; transition:0.2s;}
.stSelectbox>div>div:focus-within{border-color:#ff4da6!important; box-shadow:0 0 0 3px rgba(255,77,166,0.2)!important;}
.stMultiSelect>div>div{background:rgba(19,27,71,0.9)!important; border-radius:12px!important; border:1px solid rgba(255,255,255,0.08)!important;}

/* PREDICT BUTTON WITH SHIMMER */
.predict button{
  background:linear-gradient(90deg,#ff4da6 0%,#ff7ab8 25%,#a855f7 50%,#ff4da6 75%)!important;
  background-size:300% 100%!important;
  color:white!important; border-radius:14px!important; height:52px!important; font-weight:700!important; font-size:16px!important; border:none!important;
  box-shadow:0 8px 25px rgba(255,77,166,0.45)!important; animation: shimmer 3s infinite linear;
  position:relative; overflow:hidden;
}
@keyframes shimmer{0%{background-position:0% 50%;}100%{background-position:300% 50%;}}
.predict button:hover{transform:scale(1.02); box-shadow:0 12px 35px rgba(255,77,166,0.6)!important;}

/* NEON HEART */
@keyframes heartBeat{0%,100%{transform:scale(1);}14%{transform:scale(1.18);}28%{transform:scale(1);}42%{transform:scale(1.18);}70%{transform:scale(1);}}
@keyframes heartGlow{0%,100%{filter:drop-shadow(0 0 12px #ff4da6) drop-shadow(0 0 28px #a855f7) drop-shadow(0 0 45px rgba(255,77,166,0.4));}50%{filter:drop-shadow(0 0 20px #ff4da6) drop-shadow(0 0 40px #a855f7) drop-shadow(0 0 60px rgba(255,77,166,0.6));}}
.neon-heart{animation: heartBeat 1.6s infinite, heartGlow 2s infinite alternate;}

/* PROGRESS BAR ANIMATION */
.bar{background:rgba(255,255,255,0.07); height:12px; border-radius:20px; overflow:hidden; position:relative;}
.fill{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff4da6,#ff8ec8,#a855f7); box-shadow:0 0 12px #ff4da6; animation: fillAnim 1.8s ease-out;}
@keyframes fillAnim{0%{width:0%!important;}}

/* INSIGHT CARDS ANIM */
.insight{animation: fadeInUp 0.6s ease-out forwards; opacity:0;}
@keyframes fadeInUp{0%{transform:translateY(15px); opacity:0;}100%{transform:translateY(0); opacity:1;}}
.box{background:rgba(19,27,71,0.85); border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:14px; transition:0.3s;}
.box:hover{border-color:rgba(255,77,166,0.2); transform:translateY(-1px);}
</style>

<!-- FLOATING HEARTS BACKGROUND -->
<div class="hearts">
  <span style="left:5%; animation-duration:12s; animation-delay:0s;">💗</span>
  <span style="left:15%; animation-duration:14s; animation-delay:1s; font-size:14px;">💖</span>
  <span style="left:25%; animation-duration:10s; animation-delay:2s;">💜</span>
  <span style="left:35%; animation-duration:13s; animation-delay:0.5s; font-size:22px;">💕</span>
  <span style="left:50%; animation-duration:11s; animation-delay:1.5s;">💗</span>
  <span style="left:65%; animation-duration:15s; animation-delay:0s; font-size:16px;">💖</span>
  <span style="left:75%; animation-duration:12s; animation-delay:2.5s;">💜</span>
  <span style="left:85%; animation-duration:10s; animation-delay:1s; font-size:20px;">💕</span>
  <span style="left:92%; animation-duration:13s; animation-delay:0.8s;">💗</span>
</div>

<div class="top">
  <div style="display:flex; gap:14px; align-items:center; z-index:2;">
    <div class="logo-box">💞</div>
    <div><div style="font-size:27px; font-weight:800;"><span style="color:#ff4da6; text-shadow:0 0 12px #ff4da6;">Love</span> <span style="color:white;">Prediction</span></div><div style="color:#7a81a8; font-size:11.5px; letter-spacing:0.5px;">AI • Data • Better Love Insights</div></div>
  </div>
  <div style="color:#ffc2d9; font-family:'Dancing Script',cursive; font-size:17px; text-align:right; line-height:1.2; z-index:2; text-shadow:0 0 10px #ff4da6;">Some connections<br>are meant to be... ♡</div>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([0.155,0.38,0.465], gap="medium")

with c1:
    st.markdown("""
    <div class="card" style="height:780px;">
      <div class="nav-on">🏠 Home</div>
      <div class="nav">♡ Prediction</div>
      <div class="nav">📊 About Model</div>
      <div class="nav">ⓘ How It Works</div>
      <div style="margin-top:380px; text-align:center; animation: fadeInUp 1s ease-out 0.5s forwards; opacity:0;">
        <div style="color:#ff6b9e; font-size:22px; animation: heartBeat 2s infinite;">💗</div>
        <div style="color:#8a4a6a; font-family:'Dancing Script',cursive; font-size:13.5px; line-height:1.35; margin-top:6px;">Love isn't just a feeling...<br><span style="color:#ffb3d1; font-weight:700; font-family:Poppins; font-style:italic; text-shadow:0 0 8px #ff4da6;">It's a connection</span> ♡</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; gap:10px; align-items:center; color:white; font-weight:700; font-size:18px;"><span style="color:#ff7ab8; text-shadow:0 0 10px #ff4da6; animation: heartBeat 1.5s infinite;">💖</span> Enter Your Details</div><div style="color:#7a81a8; font-size:11.5px; margin:6px 0 18px;">Fill in the information below to predict the love compatibility.</div>', unsafe_allow_html=True)
    gy=st.selectbox("👤 Gender (You)", ["Male","Female","Other"])
    gp=st.selectbox("👤 Gender (Partner)", ["Female","Male","Other"])
    ay=st.number_input("📅 Age (You)", 18,70,25)
    ap=st.number_input("📅 Age (Partner)", 18,70,23)
    rel=st.selectbox("♡ Relationship Type", ["Dating","Married","Long Distance","Crush"])
    interests=st.multiselect("⭐ Common Interests", ["Travel","Music","Movies","Sports","Gaming"], default=["Travel","Music","Movies"])
    comm=st.selectbox("💬 Communication Style", ["Open","Reserved","Honest","Playful","Open & Honest"])
    trust=st.selectbox("🛡️ Trust Level", ["High","Medium","Low"])
    st.write("")
    st.markdown('<div class="predict">', unsafe_allow_html=True)
    btn=st.button("✨ Predict Love →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c3:
    if btn:
        score = model_predict(comm, trust, interests, rel, ay, ap)
        if score is None:
            st.error("❌ model.pkl nahi mila! GitHub pe couple_love_model.pkl daalo")
            score = 0
    else:
        score = 0

    disp = score if score>0 else 87
    if score==0: label,desc="Ready? ✨","Press Predict for real AI magic!", "#a78bfa"
    elif score>=80: label,desc="High Compatibility! 🔥","Model says strong long-lasting relationship - true soulmates!", "#ff7ab8"
    elif score>=60: label,desc="Good Compatibility 💫","Good bond detected by AI - keep nurturing it!", "#a78bfa"
    elif score>=40: label,desc="Average Compatibility 💭","Model detected ups & downs - work on trust!", "#ffb86c"
    else: label,desc="Needs Work 💔","Model says needs more time & understanding.", "#f87171"

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="color:white; font-weight:700; font-size:16px; display:flex; gap:10px; align-items:center;"><span style="width:32px; height:32px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:10px; display:flex; align-items:center; justify-content:center; box-shadow:0 0 15px #ff4da6; animation: logoPulse 2s infinite;">💖</span> Prediction Result</div>
        <div style="background:rgba(26,33,74,0.9); border:1px solid rgba(255,77,166,0.18); padding:6px 14px; border-radius:20px; font-size:10.5px; color:#ffb3d1; animation: navGlow 2s infinite alternate;">✨ AI Powered</div>
      </div>
      <div style="display:flex; gap:22px; align-items:center; margin-top:22px;">
        <div class="neon-heart"><svg width="128" height="116" viewBox="0 0 100 90"><defs><linearGradient id="hg" x1="0%" y1="100%" x2="0%" y2="0%"><stop offset="0%" stop-color="#a855f7"/><stop offset="50%" stop-color="#ff4da6"/><stop offset="100%" stop-color="#ff8ec8"/></linearGradient></defs><path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,77,166,0.12)" stroke="url(#hg)" stroke-width="2.4"/><text x="50" y="50" text-anchor="middle" fill="white" font-size="24" font-weight="800" style="text-shadow:0 0 12px white;">{disp}%</text></svg></div>
        <div><div style="color:#ff7ab8; font-weight:800; font-size:21px; text-shadow:0 0 12px rgba(255,77,166,0.6);">{label}</div><div style="color:#a8aecf; font-size:12.5px; line-height:1.5; margin-top:6px;">{desc}</div></div>
      </div>
      <div class="bar" style="margin-top:20px;"><div class="fill" style="width:{disp}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px;"><span style="color:#8b90b5;">Compatibility Score</span><span style="color:white; font-weight:700; text-shadow:0 0 8px #ff4da6;">{disp}%</span></div>
      <div class="box" style="margin-top:18px;">
        <div style="color:white; font-weight:600; font-size:13px; margin-bottom:14px; display:flex; gap:8px;">⊕ Key Insights</div>
        <div style="display:flex; justify-content:space-between; text-align:center; gap:8px;">
          <div class="insight" style="animation-delay:0.1s; flex:1;"><div style="font-size:18px; animation: heartBeat 2s infinite;">♡</div><div style="font-size:10.5px; color:#8b90b5; margin-top:4px;">Communication</div><div style="color:white; font-weight:600; font-size:12px; margin-top:3px;">High</div></div>
          <div class="insight" style="animation-delay:0.2s; flex:1;"><div style="font-size:18px; animation: heartBeat 2s infinite 0.3s;">☆</div><div style="font-size:10.5px; color:#8b90b5; margin-top:4px;">Interests</div><div style="color:white; font-weight:600; font-size:12px; margin-top:3px;">High</div></div>
          <div class="insight" style="animation-delay:0.3s; flex:1;"><div style="font-size:18px; animation: heartBeat 2s infinite 0.6s;">🛡</div><div style="font-size:10.5px; color:#8b90b5; margin-top:4px;">Trust</div><div style="color:white; font-weight:600; font-size:12px; margin-top:3px;">{trust if btn else 'High'}</div></div>
          <div class="insight" style="animation-delay:0.4s; flex:1;"><div style="font-size:18px; animation: heartBeat 2s infinite 0.9s;">☺</div><div style="font-size:10.5px; color:#8b90b5; margin-top:4px;">Bond</div><div style="color:white; font-weight:600; font-size:12px; margin-top:3px;">High</div></div>
        </div>
      </div>
      <div class="box" style="margin-top:12px; animation: fadeInUp 0.8s ease-out 0.6s forwards; opacity:0;">
        <div style="color:white; font-weight:600; font-size:13px;">💡 Why This Prediction?</div>
        <div style="color:#8b90b5; font-size:11px; line-height:1.6; margin-top:8px;">Based on your age, communication style, shared interests and trust level, the model predicts a high level of compatibility. Your values and preferences align well, which increases the chances of a successful relationship.</div>
      </div>
      <div style="text-align:right; margin-top:12px; color:#ff8ec8; font-family:'Dancing Script',cursive; font-size:13px; text-shadow:0 0 8px #ff4da6; animation: floatUp 4s infinite;">Good things take time... ♡</div>
    </div>
    """, unsafe_allow_html=True)
