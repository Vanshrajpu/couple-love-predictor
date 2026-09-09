import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Love Prediction - Vansh Rajput", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    for name in ["couple_love_model.pkl", "model.pkl"]:
        if os.path.exists(name):
            try:
                m = joblib.load(name)
                if hasattr(m, "predict"):
                    return m, name
            except:
                pass
    return None, None

model, model_name = load_model()

def predict_true(ay, ap, rel, interests, comm, trust):
    cmap = {"Open": 8, "Open & Honest": 9, "Honest": 8, "Playful": 7, "Reserved": 4}
    tmap = {"High": 9, "Medium": 5, "Low": 2}
    rmap = {"Dating": 6, "Married": 8, "Long Distance": 4, "Crush": 3}
    feats = {
        "communication_score": cmap.get(comm, 7),
        "trust_score": tmap.get(trust, 5),
        "understanding_score": min(10, 4 + len(interests) * 1.5),
        "time_together_hours": rmap.get(rel, 5),
        "support_score": 8,
        "fights_per_month": 1,
        "gifts_per_month": 3,
        "happy_together_score": 8,
        "age_gap": abs(ay - ap),
        "interests_count": len(interests)
    }
    if model is None:
        base = 40 + tmap.get(trust, 5) * 5 + len(interests) * 4
        return max(5, min(98, base))
    try:
        if hasattr(model, "feature_names_in_"):
            cols = list(model.feature_names_in_)
            df = pd.DataFrame([{c: feats.get(c, 0) for c in cols}])[cols]
        else:
            df = pd.DataFrame([[
                feats["communication_score"], feats["trust_score"],
                feats["understanding_score"], feats["time_together_hours"],
                feats["support_score"], feats["fights_per_month"],
                feats["gifts_per_month"], feats["happy_together_score"]
            ]], columns=[
                "communication_score", "trust_score", "understanding_score",
                "time_together_hours", "support_score", "fights_per_month",
                "gifts_per_month", "happy_together_score"
            ])
        raw = model.predict(df)[0]
        score = int(raw * 100) if raw <= 1.5 else int(raw)
        return max(1, min(99, score))
    except:
        return 75

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Dancing+Script:wght@600&display=swap');
.stApp{background:#070a1e!important;}
header,footer,#MainMenu{visibility:hidden;}
.block-container{max-width:100%!important; padding:0 1rem!important;}
*{font-family:'Poppins',sans-serif;}

.stApp::before{
  content:''; position:fixed; inset:0; z-index:-2;
  background: radial-gradient(800px at 15% 20%, rgba(255,45,107,0.18), transparent 60%), radial-gradient(700px at 85% 15%, rgba(168,85,247,0.20), transparent 60%);
}
.hearts{position:fixed; inset:0; pointer-events:none; z-index:-1;}
.hearts span{position:absolute; bottom:-30px; color:#ff4da6; text-shadow:0 0 12px #ff4da6; animation: up linear infinite; opacity:0.6;}
@keyframes up{0%{transform:translateY(0) rotate(0deg); opacity:0;}10%{opacity:0.8;}100%{transform:translateY(-115vh) translateX(80px) rotate(360deg); opacity:0;}}

.top{
  height:115px; margin:-14px -16px 18px -16px; padding:0 26px;
  background: linear-gradient(90deg, rgba(7,10,30,0.96) 0%, rgba(26,10,42,0.6) 100%), url('bg.jpg');
  background-size:cover; background-position:center 35%;
  display:flex; justify-content:space-between; align-items:center;
  border-bottom:1px solid rgba(255,77,166,0.18);
}
.logo{width:48px; height:48px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:23px; box-shadow:0 0 22px #ff4da6; animation: logoBeat 2s infinite;}
@keyframes logoBeat{0%,100%{transform:scale(1);}50%{transform:scale(1.12);}}

.card{
  background:linear-gradient(180deg, rgba(18,24,65,0.98) 0%, rgba(14,20,53,0.98) 100%)!important;
  border:1px solid rgba(120,110,255,0.14)!important;
  border-radius:20px!important; padding:20px!important;
}
.nav-on{background:linear-gradient(90deg,#ff4da6,#a855f7)!important; border-radius:12px; padding:12px 14px; color:white!important; font-weight:700; display:flex; gap:10px;}
.nav{color:#6f769e; padding:12px 14px; display:flex; gap:10px; font-size:13.5px; border-radius:12px;}

.stSelectbox>div>div,.stNumberInput>div>div>input{background:#121b42!important; border-radius:12px!important; color:#e2e6ff!important; height:48px!important;}
.stMultiSelect>div>div{background:#121b42!important; border-radius:12px!important;}

.btn button{
  background:linear-gradient(90deg,#ff2d6b 0%,#ff4da6 20%,#ff8ec8 40%,#a855f7 60%,#ff4da6 80%,#ff2d6b 100%)!important;
  background-size:400% 100%!important;
  color:white!important; border-radius:14px!important; height:56px!important; font-weight:800!important; font-size:16px!important; border:none!important;
  box-shadow:0 14px 34px rgba(255,77,166,0.48)!important;
  animation: shimmer 3s linear infinite;
}
@keyframes shimmer{0%{background-position:0% 50%;}100%{background-position:400% 50%;}}

@keyframes beat{0%,100%{transform:scale(1);}12%{transform:scale(1.28);}24%{transform:scale(1);}36%{transform:scale(1.24);}}
@keyframes neon{0%,100%{filter:drop-shadow(0 0 14px #ff4da6) drop-shadow(0 0 32px #a855f7);}50%{filter:drop-shadow(0 0 22px #ff4da6) drop-shadow(0 0 50px #a855f7);}}
.heart{animation: beat 1.25s infinite, neon 2s infinite alternate;}

/* ===== PREDICTED LOVE LINE - SPECIAL ANIMATION ===== */
.predicted-line{
  font-weight:800;
  font-size:22px;
  background: linear-gradient(90deg, #ff2d6b, #ff7ab8, #ff8ec8, #a855f7, #ff2d6b);
  background-size: 300% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: gradientMove 3s linear infinite, bounceIn 0.8s cubic-bezier(0.16,1,0.3,1), textGlowPulse 2s infinite alternate, floatText 3s ease-in-out infinite;
  display:inline-block;
  position:relative;
  letter-spacing:0.5px;
}
@keyframes gradientMove{
  0%{background-position:0% 50%;}
  100%{background-position:300% 50%;}
}
@keyframes bounceIn{
  0%{transform:scale(0.5) translateY(20px); opacity:0;}
  60%{transform:scale(1.15) translateY(-5px); opacity:1;}
  80%{transform:scale(0.95) translateY(2px);}
  100%{transform:scale(1) translateY(0);}
}
@keyframes textGlowPulse{
  0%{filter:drop-shadow(0 0 8px #ff4da6) drop-shadow(0 0 15px #a855f7); text-shadow:0 0 10px rgba(255,77,166,0.5);}
  100%{filter:drop-shadow(0 0 16px #ff4da6) drop-shadow(0 0 30px #a855f7) drop-shadow(0 0 45px #ff4da6); text-shadow:0 0 20px rgba(255,77,166,0.8);}
}
@keyframes floatText{
  0%,100%{transform:translateY(0);}
  50%{transform:translateY(-4px);}
}
.predicted-line::after{
  content:'';
  position:absolute;
  bottom:-4px;
  left:0;
  width:100%;
  height:3px;
  background:linear-gradient(90deg, #ff2d6b, #ff8ec8, #a855f7);
  background-size:200% 100%;
  border-radius:10px;
  animation: lineShine 2s linear infinite;
  box-shadow:0 0 10px #ff4da6;
}
@keyframes lineShine{
  0%{background-position:-100% 0;}
  100%{background-position:200% 0;}
}
.score-anim{
  animation: countPop 1s cubic-bezier(0.16,1,0.3,1) both;
  display:inline-block;
}
@keyframes countPop{
  0%{transform:scale(0) rotate(-10deg); opacity:0;}
  60%{transform:scale(1.3) rotate(5deg); opacity:1;}
  100%{transform:scale(1) rotate(0);}
}

.bar{background:rgba(255,255,255,0.07); height:14px; border-radius:20px; overflow:hidden;}
.fill{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff2d6b,#ff8ec8,#a855f7); box-shadow:0 0 16px #ff4da6; animation: loadBar 1.8s cubic-bezier(0.16,1,0.3,1); position:relative;}
.fill::after{content:''; position:absolute; inset:0; background:linear-gradient(90deg, transparent, rgba(255,255,255,0.55), transparent); animation: shine 1.8s infinite;}
@keyframes loadBar{0%{width:0%!important;}}
@keyframes shine{0%{transform:translateX(-100%);}100%{transform:translateX(250%);}}
</style>

<div class="hearts">
  <span style="left:8%; animation-duration:12s;">💗</span>
  <span style="left:25%; animation-duration:11s; animation-delay:0.5s; font-size:20px;">💖</span>
  <span style="left:55%; animation-duration:10s;">💕</span>
  <span style="left:82%; animation-duration:13s; font-size:22px;">💜</span>
</div>

<div class="top">
  <div style="display:flex; gap:14px; align-items:center;">
    <div class="logo">💞</div>
    <div><div style="font-size:27px; font-weight:800;"><span style="color:#ff4da6; text-shadow:0 0 12px #ff4da6;">Love</span> <span style="color:white;">Prediction</span></div><div style="color:#7a81a8; font-size:11px;">AI • Data • Better Love Insights • Vansh Rajput</div></div>
  </div>
  <div style="text-align:right;"><div style="color:#ffc2d9; font-family:'Dancing Script',cursive; font-size:16px; text-shadow:0 0 12px #ff4da6;">Some connections<br>are meant to be... ♡</div></div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.15, 0.38, 0.47], gap="medium")

with c1:
    st.markdown(f'<div class="card" style="height:780px;"><div class="nav-on">🏠 Home</div><div class="nav">♡ Prediction</div><div class="nav">📊 About Model</div><div class="nav">ⓘ How It Works</div><div style="margin-top:350px; text-align:center;"><div style="background:rgba(21,30,68,0.9); border-radius:14px; padding:12px; display:flex; gap:10px; justify-content:center;"><div style="width:32px; height:32px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">VR</div><div style="text-align:left;"><div style="color:white; font-weight:700; font-size:12px;">Vansh Rajput</div><div style="color:#4ade80; font-size:9px;">{model_name if model else "Upload pkl"}</div></div></div></div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><div style="color:white; font-weight:700;">💖 Enter Your Details</div><div style="color:#7a81a8; font-size:11px; margin:8px 0 18px;">True model prediction</div>', unsafe_allow_html=True)
    ay = st.number_input("Age (You)", 18, 70, 25)
    ap = st.number_input("Age (Partner)", 18, 70, 23)
    rel = st.selectbox("Relationship Type", ["Dating", "Married", "Long Distance", "Crush"])
    interests = st.multiselect("Common Interests", ["Travel", "Music", "Movies", "Sports", "Gaming"], default=["Travel", "Music", "Movies"])
    comm = st.selectbox("Communication Style", ["Open", "Reserved", "Honest", "Playful", "Open & Honest"])
    trust = st.selectbox("Trust Level", ["High", "Medium", "Low"])
    st.write("")
    st.markdown('<div class="btn">', unsafe_allow_html=True)
    btn = st.button("✨ Predict Love →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c3:
    score = predict_true(ay, ap, rel, interests, comm, trust) if btn else 87
    if score >= 75:
        lab = "High Compatibility! 🔥"
        desc = "You and your partner have a strong chance of a healthy and long-lasting relationship."
    elif score >= 55:
        lab = "Good Compatibility 💫"
        desc = "Good bond detected - keep nurturing your connection!"
    else:
        lab = "Needs Attention 💭"
        desc = "Model detects ups & downs - work on trust and communication."

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="color:white; font-weight:700; display:flex; gap:10px;"><div style="width:32px; height:32px; background:linear-gradient(135deg,#ff8ec8,#a855f7); border-radius:10px; display:flex; align-items:center; justify-content:center;">💖</div> Prediction Result</div>
        <div style="background:rgba(26,32,77,0.9); padding:6px 12px; border-radius:20px; font-size:10px; color:#ffb3d1;">✨ AI Powered</div>
      </div>
      <div style="display:flex; gap:24px; align-items:center; margin-top:22px;">
        <div class="heart"><svg width="128" height="118" viewBox="0 0 100 90"><defs><linearGradient id="hg" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#ff2d6b"/><stop offset="100%" stop-color="#ff8ec8"/></linearGradient></defs><path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,77,166,0.16)" stroke="url(#hg)" stroke-width="2.6"/><text x="50" y="51" text-anchor="middle" fill="white" font-size="24" font-weight="800" class="score-anim">{score}%</text></svg></div>
        <div>
          <div class="predicted-line">{lab}</div>
          <div style="color:#a8aecf; font-size:12px; margin-top:14px; line-height:1.5;">{desc}</div>
        </div>
      </div>
      <div class="bar" style="margin-top:20px;"><div class="fill" style="width:{score}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px;"><span style="color:#8b90b5;">Compatibility Score • True Model</span><span style="color:white; font-weight:800;">{score}%</span></div>
    </div>
    """, unsafe_allow_html=True)
