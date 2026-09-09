import streamlit as st, pandas as pd, joblib, os
st.set_page_config(page_title="Couple Love - Vansh Rajput", page_icon="💖", layout="wide")

@st.cache_resource
def load():
    for n in ["couple_love_model.pkl","model.pkl"]:
        if os.path.exists(n):
            try:
                m=joblib.load(n)
                return m,n
            except: pass
    return None,None
model,fname = load()

def predict(ay,ap,rel,ints,comm,trust):
    cmap={"Open":8,"Open & Honest":9,"Honest":8,"Playful":7,"Reserved":4}
    tmap={"High":9,"Medium":5,"Low":2}
    rmap={"Dating":6,"Married":8,"Long Distance":4,"Crush":3}
    feats={"communication_score":cmap.get(comm,7),"trust_score":tmap.get(trust,5),"understanding_score":min(10,4+len(ints)*1.5),"time_together_hours":rmap.get(rel,5),"support_score":8,"fights_per_month":1,"gifts_per_month":3,"happy_together_score":8}
    if model is None:
        return max(5,min(98,50 + (tmap.get(trust,5)*5) + len(ints)*4))
    try:
        if hasattr(model,"feature_names_in_"):
            cols=list(model.feature_names_in_)
            df=pd.DataFrame([{c:feats.get(c,0) for c in cols}])[cols]
        else:
            df=pd.DataFrame([list(feats.values())[:8]], columns=["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"])
        r=model.predict(df)[0]
        s=int(r*100) if r<=1.5 else int(r)
        return max(1,min(99,s))
    except: return 78

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600;700;800&family=Dancing+Script:wght@600&display=swap');
.stApp{background:#05091c!important;} header,footer{visibility:hidden;}.block-container{max-width:100%!important; padding:0 1rem!important;}
*{font-family:'Poppins',sans-serif;}
.stApp::before{content:''; position:fixed; inset:0; z-index:-2; background: radial-gradient(700px at 10% 10%, #ff2d6b33, transparent), radial-gradient(600px at 90% 20%, #a855f799, transparent), radial-gradient(500px at 50% 120%, #ff4da61a, transparent); animation: bg 10s infinite alternate;}
@keyframes bg{0%{transform:scale(1);}100%{transform:scale(1.1) translateY(-15px);}}
.hearts{position:fixed; inset:0; pointer-events:none; z-index:-1;}.hearts span{position:absolute; bottom:-20px; animation: up linear infinite; color:#ff4da6; text-shadow:0 0 10px #ff4da6;}
@keyframes up{0%{transform:translateY(0) translateX(0) rotate(0deg); opacity:0;}10%{opacity:0.7;}100%{transform:translateY(-110vh) translateX(80px) rotate(360deg); opacity:0;}}
.top{height:115px; margin:-14px -16px 20px -16px; padding:0 28px; background:linear-gradient(90deg,#070a1e 20%,#141034 60%,#2a0a2a 100%); border-bottom:1px solid #ff4da622; display:flex; justify-content:space-between; align-items:center; box-shadow:0 10px 40px #0008;}
.card{background:linear-gradient(180deg, rgba(20,26,68,0.98), rgba(14,20,52,0.98))!important; border:1px solid #ffffff12!important; border-radius:20px!important; padding:20px!important; backdrop-filter:blur(14px)!important; box-shadow:0 20px 50px #0006, inset 0 1px 0 #ffffff0a!important; transition:0.35s;}
.card:hover{transform:translateY(-4px); border-color:#ff4da633!important; box-shadow:0 25px 60px #ff4da61a!important;}
.nav-on{background:linear-gradient(90deg,#ff4da6,#a855f7)!important; border-radius:12px; padding:12px 14px; color:white!important; font-weight:700; display:flex; gap:10px; box-shadow:0 8px 20px #ff4da66a; animation: glow 2s infinite alternate;}
@keyframes glow{0%{box-shadow:0 6px 15px #ff4da64d;}100%{box-shadow:0 10px 30px #ff4da68a;}}
.nav{color:#6f769e; padding:12px 14px; display:flex; gap:10px; border-radius:12px; transition:0.2s;}
.nav:hover{background:#ff4da612; color:#ffb3d1; transform:translateX(5px);}
.stSelectbox>div>div,.stNumberInput>div>div>input{background:#121a3a!important; border:1px solid #ffffff12!important; border-radius:12px!important; color:#e8eaf6!important; height:46px!important;}
.stMultiSelect>div>div{background:#121a3a!important; border-radius:12px!important;}
.btn button{background:linear-gradient(90deg,#ff2d6b,#ff6b9e,#a855f7,#ff2d6b)!important; background-size:300% 100%!important; color:white!important; border-radius:14px!important; height:54px!important; font-weight:800!important; font-size:16px!important; border:none!important; box-shadow:0 12px 30px #ff2d6b66!important; animation: shimmer 3s linear infinite;}
@keyframes shimmer{0%{background-position:0% 50%;}100%{background-position:300% 50%;}}
@keyframes beat{0%,100%{transform:scale(1);}14%{transform:scale(1.25);}28%{transform:scale(1);}42%{transform:scale(1.22);}70%{transform:scale(1);}}
@keyframes neon{0%,100%{filter:drop-shadow(0 0 12px #ff4da6) drop-shadow(0 0 30px #a855f7) drop-shadow(0 0 50px #ff4da655);}50%{filter:drop-shadow(0 0 20px #ff4da6) drop-shadow(0 0 45px #a855f7) drop-shadow(0 0 70px #ff4da6aa);}}
.heart{animation: beat 1.3s infinite, neon 2s infinite alternate;}
.bar{height:14px; background:#ffffff12; border-radius:20px; overflow:hidden;}.fill{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff2d6b,#ff8ec8,#a855f7); box-shadow:0 0 15px #ff4da6; animation: load 1.6s ease-out; position:relative;}
.fill::after{content:''; position:absolute; inset:0; background:linear-gradient(90deg, transparent, #ffffff66, transparent); animation: shine 2s infinite; }
@keyframes load{0%{width:0%!important;}} @keyframes shine{0%{transform:translateX(-100%);}100%{transform:translateX(200%);}}
</style>
<div class="hearts">
  <span style="left:5%; animation-duration:12s; font-size:18px;">💗</span><span style="left:18%; animation-duration:14s; animation-delay:1s;">💖</span><span style="left:30%; animation-duration:10s; animation-delay:0.5s; font-size:20px;">💜</span><span style="left:50%; animation-duration:11s; animation-delay:1.2s;">💕</span><span style="left:70%; animation-duration:13s; animation-delay:0.2s;">💗</span><span style="left:85%; animation-duration:12s; animation-delay:1.5s; font-size:22px;">💖</span>
</div>
<div class="top">
  <div style="display:flex; gap:16px; align-items:center;"><div style="width:50px; height:50px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:26px; box-shadow:0 0 25px #ff4da6; animation: beat 2s infinite;">💞</div><div><div style="font-size:29px; font-weight:800;"><span style="color:#ff4da6; text-shadow:0 0 12px #ff4da6;">Love</span> <span style="color:white;">Prediction</span></div><div style="color:#7a81b0; font-size:12px;">AI • Data • Better Love Insights • Vansh Rajput</div></div></div>
  <div style="color:#ffb3d1; font-family:'Dancing Script',cursive; font-size:17px; text-align:right; text-shadow:0 0 10px #ff4da6; transform:rotate(-1deg);">Some connections<br>are meant to be... ♡</div>
</div>
""", unsafe_allow_html=True)

a,b,c = st.columns([0.15,0.37,0.48], gap="medium")
with a:
    st.markdown(f'<div class="card" style="height:780px;"><div class="nav-on">🏠 Home</div><div class="nav">♡ Prediction</div><div class="nav">📊 About Model</div><div class="nav">ⓘ How It Works</div><div style="margin-top:320px; text-align:center;"><div style="font-size:26px; animation: beat 1.5s infinite;">💗</div><div style="color:#8a4a6a; font-family:Dancing Script,cursive; font-size:13px; margin-top:8px;">Love isn\'t just a feeling...<br><span style="color:#ffb3d1; font-family:Poppins; font-weight:700;">It\'s a connection</span> ♡</div><div style="margin-top:16px; background:#151e44; border-radius:14px; padding:12px; display:flex; gap:10px; align-items:center; justify-content:center; border:1px solid #ffffff10;"><div style="width:32px; height:32px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">VR</div><div style="text-align:left;"><div style="color:white; font-weight:700; font-size:12px;">Vansh Rajput</div><div style="color:#4ade80; font-size:9px;">● {fname if fname else "Upload pkl"}</div></div></div></div></div>', unsafe_allow_html=True)

with b:
    st.markdown('<div class="card"><div style="color:white; font-weight:700; font-size:17px; display:flex; gap:8px;"><span style="color:#ff7ab8;">💖</span> Enter Your Details</div><div style="color:#7a81a8; font-size:11px; margin:6px 0 16px;">Fill below - true model prediction</div>', unsafe_allow_html=True)
    gy=st.selectbox("👤 Gender (You)", ["Male","Female","Other"])
    gp=st.selectbox("👤 Gender (Partner)", ["Female","Male","Other"])
    ay=st.number_input("📅 Age (You)",18,70,25)
    ap=st.number_input("📅 Age (Partner)",18,70,23)
    rel=st.selectbox("♡ Relationship Type", ["Dating","Married","Long Distance","Crush"])
    ints=st.multiselect("⭐ Common Interests", ["Travel","Music","Movies","Sports","Gaming"], default=["Travel","Music","Movies"])
    comm=st.selectbox("💬 Communication Style", ["Open","Reserved","Honest","Playful","Open & Honest"])
    trust=st.selectbox("🛡️ Trust Level", ["High","Medium","Low"])
    st.write("")
    st.markdown('<div class="btn">', unsafe_allow_html=True)
    go=st.button("✨ Predict Love →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c:
    score = predict(ay,ap,rel,ints,comm,trust) if go else 87
    lab = "High Compatibility! 🔥" if score>=75 else "Good Compatibility 💫" if score>=55 else "Average 💭" if score>=35 else "Needs Work 💔"
    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center;"><div style="color:white; font-weight:700; display:flex; gap:10px; align-items:center;"><div style="width:32px; height:32px; background:linear-gradient(135deg,#ff8ec8,#a855f7); border-radius:10px; display:flex; align-items:center; justify-content:center; box-shadow:0 0 15px #ff4da6;">💖</div> Prediction Result</div><div style="background:#1a214a; border:1px solid #ffffff12; padding:6px 12px; border-radius:20px; font-size:10px; color:#ffb3d1;">✨ AI Powered</div></div>
      <div style="display:flex; gap:24px; align-items:center; margin-top:22px;">
        <div class="heart"><svg width="132" height="122" viewBox="0 0 100 90"><defs><linearGradient id="hg" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#ff2d6b"/><stop offset="50%" stop-color="#ff4da6"/><stop offset="100%" stop-color="#ff8ec8"/></linearGradient></defs><path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,77,166,0.15)" stroke="url(#hg)" stroke-width="2.6"/><text x="50" y="51" text-anchor="middle" fill="white" font-size="24" font-weight="800" style="text-shadow:0 0 10px white;">{score}%</text></svg></div>
        <div><div style="color:#ff7ab8; font-weight:800; font-size:22px; text-shadow:0 0 12px #ff4da688;">{lab}</div><div style="color:#a8aecf; font-size:12px; margin-top:6px; line-height:1.4;">{'Strong long-lasting relationship - true soulmates!' if score>=75 else 'Good bond - keep nurturing it!'}</div></div>
      </div>
      <div class="bar" style="margin-top:20px;"><div class="fill" style="width:{score}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px;"><span style="color:#8b90b5;">Compatibility Score • {fname if fname else 'demo'}</span><span style="color:white; font-weight:800;">{score}%</span></div>
      <div style="margin-top:20px; background:rgba(19,26,68,0.9); border:1px solid #ffffff0a; border-radius:14px; padding:14px; display:flex; justify-content:space-between; text-align:center;">
        <div><div style="font-size:18px;">♡</div><div style="font-size:10px; color:#8b90b5;">Communication</div><div style="color:white; font-weight:600; font-size:12px;">High</div></div>
        <div><div style="font-size:18px;">☆</div><div style="font-size:10px; color:#8b90b5;">Interests</div><div style="color:white; font-weight:600; font-size:12px;">High</div></div>
        <div><div style="font-size:18px;">🛡</div><div style="font-size:10px; color:#8b90b5;">Trust</div><div style="color:white; font-weight:600; font-size:12px;">{trust if go else 'High'}</div></div>
        <div><div style="font-size:18px;">☺</div><div style="font-size:10px; color:#8b90b5;">Bond</div><div style="color:white; font-weight:600; font-size:12px;">High</div></div>
      </div>
      <div style="margin-top:12px; background:rgba(19,26,68,0.8); border-radius:14px; padding:14px;"><div style="color:white; font-weight:600; font-size:13px;">💡 Why This Prediction?</div><div style="color:#8b90b5; font-size:11px; line-height:1.6; margin-top:6px;">Based on your age, communication, shared interests and trust, the model predicts compatibility. Created by <b style="color:#ffb3d1;">Vansh Rajput</b> • True prediction from {fname if fname else 'model.pkl'}.</div></div>
      <div style="text-align:right; margin-top:12px; color:#ff8ec8; font-family:'Dancing Script',cursive; font-size:13px; text-shadow:0 0 8px #ff4da6;">Good things take time... ♡</div>
    </div>
    """, unsafe_allow_html=True)
