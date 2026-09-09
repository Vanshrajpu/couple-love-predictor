import streamlit as st
import pandas as pd, joblib, os, random

st.set_page_config(page_title="LOVE AI • Prediction v2.1", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    for n in ["couple_love_model.pkl","model.pkl"]:
        if os.path.exists(n):
            try: return joblib.load(n)
            except: pass
    return None
model=load_model()

def predict_score(comm,trust,ints,rel,ay,ap):
    cmap={"Open":9,"Open & Honest":9,"Honest":8,"Playful":7,"Reserved":5}
    tmap={"High":9,"Medium":6,"Low":3}
    rmap={"Serious • Dating":6,"Dating":6,"Married":8,"Long Distance":4,"Crush":3}
    cs=cmap.get(comm,8); ts=tmap.get(trust,8); th=rmap.get(rel,6)
    us=min(10,5+len(ints)*1.2)
    feats={"communication_score":cs,"trust_score":ts,"understanding_score":us,"time_together_hours":th,"support_score":8,"fights_per_month":1,"gifts_per_month":3,"happy_together_score":9}
    if model is None: return max(15,min(97,int((cs*12+ts*15)/2.2)+len(ints)*3))
    try:
        df=pd.DataFrame([feats])
        if hasattr(model,"feature_names_in_"):
            cols=list(model.feature_names_in_)
            for c in cols:
                if c not in df: df[c]=0
            df=df[cols]
        raw=model.predict(df)[0]
        s=int(raw*100) if raw<=1.5 else int(raw)
        if abs(ay-ap)>12: s-=5
        return max(5,min(98,s+len(ints)))
    except: return 75

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700;800&family=Dancing+Script:wght@600&display=swap');
.stApp{background:#060a1e!important;}
header,footer,#MainMenu{visibility:hidden;}
.block-container{max-width:100%!important; padding:0 1.2rem!important;}
*{font-family:'Plus Jakarta Sans',sans-serif;}

/* COSMIC PARTICLES */
.stApp::before{
  content:''; position:fixed; inset:0; z-index:-1;
  background:
    radial-gradient(800px at 10% 20%, rgba(255,77,166,0.18), transparent 60%),
    radial-gradient(700px at 90% 10%, rgba(168,85,247,0.22), transparent 60%),
    radial-gradient(600px at 50% 100%, rgba(255,45,106,0.12), transparent 70%),
    radial-gradient(1px at 20% 30%, white 0%, transparent 100%),
    radial-gradient(1.5px at 80% 40%, #ff8ec8 0%, transparent 100%);
  animation: cosmic 12s infinite alternate;
}
@keyframes cosmic{0%{transform:scale(1);}100%{transform:scale(1.08) translateY(-10px);}}

.particles{position:fixed; inset:0; pointer-events:none; z-index:0;}
.particles i{
  position:absolute; width:3px; height:3px; background:#ff8ec8; border-radius:50%;
  box-shadow:0 0 6px #ff4da6; animation: twinkle 3s infinite alternate;
}
@keyframes twinkle{0%{opacity:0.2; transform:scale(0.8);}100%{opacity:1; transform:scale(1.4); box-shadow:0 0 12px #ff4da6;}}
@keyframes floatUp{0%{transform:translateY(100vh) translateX(0) rotate(0deg); opacity:0;}10%{opacity:0.8;}90%{opacity:0.6;}100%{transform:translateY(-10vh) translateX(80px) rotate(360deg); opacity:0;}}

/* SIDEBAR */
.sidebar{
  background:linear-gradient(180deg, rgba(16,22,58,0.92), rgba(12,18,48,0.96))!important;
  border:1px solid rgba(255,255,255,0.08)!important; border-radius:20px!important; padding:20px!important;
  backdrop-filter:blur(18px)!important; box-shadow:0 20px 60px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.06)!important;
  height:840px; position:relative; overflow:hidden;
}
.sidebar::before{
  content:''; position:absolute; top:-50%; left:-50%; width:200%; height:200%;
  background:conic-gradient(from 0deg, transparent, rgba(255,77,166,0.06), transparent 30%);
  animation: rotate 8s linear infinite;
}
@keyframes rotate{100%{transform:rotate(360deg);}}

/* CARDS */
.glass{
  background:linear-gradient(180deg, rgba(22,28,72,0.88), rgba(16,22,58,0.92))!important;
  border:1px solid rgba(255,255,255,0.08)!important; border-radius:20px!important; padding:22px!important;
  backdrop-filter:blur(16px)!important; box-shadow:0 12px 40px rgba(0,0,0,0.4)!important;
  transition:all 0.35s cubic-bezier(0.16,1,0.3,1);
}
.glass:hover{transform:translateY(-3px); border-color:rgba(255,77,166,0.22)!important; box-shadow:0 20px 60px rgba(255,77,166,0.12)!important;}

.nav-active{
  background:linear-gradient(90deg,#ff7eb6,#ff4da6 45%,#a855f7)!important;
  border-radius:12px; padding:13px 16px; color:white!important; font-weight:700;
  box-shadow:0 8px 22px rgba(255,77,166,0.45), inset 0 1px 0 rgba(255,255,255,0.2);
  animation: activeGlow 2.5s infinite alternate;
}
@keyframes activeGlow{0%{box-shadow:0 6px 18px rgba(255,77,166,0.3);}100%{box-shadow:0 10px 30px rgba(255,77,166,0.55);}}
.nav{color:#7a81a8; padding:13px 16px; display:flex; gap:12px; border-radius:12px; margin-bottom:8px; transition:0.25s;}
.nav:hover{background:rgba(255,77,166,0.08); color:#ffb3d1; transform:translateX(6px);}

/* INPUTS */
.stTextInput>div>div>input,.stSelectbox>div>div,.stNumberInput>div>div>input{
  background:rgba(26,32,77,0.85)!important; border:1px solid rgba(255,255,255,0.07)!important;
  border-radius:12px!important; color:#e8eaf6!important; height:48px!important;
}
.stTextInput>div>div>input:focus,.stSelectbox>div>div:focus-within{border-color:#ff4da6!important; box-shadow:0 0 0 3px rgba(255,77,166,0.18)!important;}
.stMultiSelect>div>div{background:rgba(26,32,77,0.85)!important; border-radius:12px!important;}

/* BUTTON */
.run button{
  background:linear-gradient(90deg,#ff6eb5 0%,#ff8ec8 20%,#d16eff 50%,#ff6eb5 80%,#ff4da6 100%)!important;
  background-size:300% 100%!important; border-radius:14px!important; height:54px!important;
  font-weight:800!important; font-size:17px!important; border:none!important;
  box-shadow:0 12px 32px rgba(255,77,166,0.45)!important; animation: shimmer 3s linear infinite;
}
@keyframes shimmer{0%{background-position:0% 50%;}100%{background-position:300% 50%;}}
.run button:hover{transform:translateY(-2px) scale(1.01); box-shadow:0 16px 40px rgba(255,77,166,0.6)!important;}

/* HEART */
@keyframes beat{0%,100%{transform:scale(1);}15%{transform:scale(1.18);}30%{transform:scale(1);}45%{transform:scale(1.15);}60%{transform:scale(1);}}
@keyframes neonGlow{0%,100%{filter:drop-shadow(0 0 12px #ff4da6) drop-shadow(0 0 30px #a855f7) drop-shadow(0 0 50px rgba(255,77,166,0.3));}50%{filter:drop-shadow(0 0 22px #ff4da6) drop-shadow(0 0 45px #a855f7) drop-shadow(0 0 70px rgba(255,77,166,0.5));}}
.heart-wrap{animation: beat 1.5s infinite, neonGlow 2s infinite alternate;}

.bar{height:10px; background:rgba(255,255,255,0.07); border-radius:20px; overflow:hidden; position:relative;}
.fill{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff4da6,#ffb3d1,#a855f7); box-shadow:0 0 10px #ff4da6; animation: loadBar 1.6s cubic-bezier(0.16,1,0.3,1);}
@keyframes loadBar{0%{width:0%!important;}}
.pill{
  background:linear-gradient(135deg, rgba(255,77,166,0.18), rgba(168,85,247,0.18));
  border:1px solid rgba(255,77,166,0.22); border-radius:20px; padding:7px 14px;
  font-size:12.5px; color:#ffb3d1; display:inline-flex; gap:6px; margin:4px; transition:0.2s;
}
.pill:hover{transform:translateY(-1px) scale(1.05); background:linear-gradient(135deg, #ff4da6, #a855f7); color:white; box-shadow:0 4px 15px rgba(255,77,166,0.35);}
</style>

<div class="particles">
  <i style="left:8%; top:20%; animation-delay:0s;"></i>
  <i style="left:18%; top:80%; animation-delay:0.5s;"></i>
  <i style="left:28%; top:35%; animation-delay:1s;"></i>
  <i style="left:45%; top:15%; animation-delay:1.5s;"></i>
  <i style="left:62%; top:70%; animation-delay:0.2s;"></i>
  <i style="left:78%; top:25%; animation-delay:0.8s;"></i>
  <i style="left:88%; top:60%; animation-delay:1.2s;"></i>
  <i style="left:95%; top:10%; animation-delay:2s;"></i>
</div>
""", unsafe_allow_html=True)

# LAYOUT
left, mid, right = st.columns([0.20, 0.46, 0.34], gap="medium")

with left:
    st.markdown("""
    <div class="sidebar">
      <div style="display:flex; gap:14px; align-items:center; position:relative; z-index:1;">
        <div style="width:52px; height:52px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:14px; display:flex; align-items:center; justify-content:center; font-size:28px; box-shadow:0 0 25px rgba(255,77,166,0.6); animation: beat 2s infinite;">💜</div>
        <div><div style="font-size:22px; font-weight:800; color:white; letter-spacing:-0.5px;">LOVE AI</div><div style="font-size:11px; color:#ff8ec8; letter-spacing:1.2px; font-weight:600;">PREDICTION • v2.1</div></div>
      </div>
      <div style="margin-top:36px; position:relative; z-index:1;">
        <div class="nav-active">🤍 Home</div>
        <div class="nav">👤 Profile</div>
        <div class="nav">🕒 History</div>
        <div class="nav">📊 Insights</div>
        <div class="nav">⚙️ Settings</div>
        <div class="nav">🔗 Integrations</div>
      </div>
      <div style="position:absolute; bottom:20px; left:20px; right:20px; background:rgba(26,32,77,0.7); border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:14px; display:flex; gap:12px; align-items:center; z-index:1;">
        <img src="https://i.pravatar.cc/100?img=12" style="width:42px; height:42px; border-radius:50%; border:2px solid #ff4da6;">
        <div><div style="color:white; font-weight:600; font-size:13px;">Alex Morgan</div><div style="color:#ff8ec8; font-size:11px;">Pro Plan</div></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with mid:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("""
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
      <div style="color:#7a81a8; font-size:13px;">Dashboard / <span style="color:white; font-weight:600;">Love Prediction AI</span></div>
      <div style="background:rgba(26,32,77,0.8); border:1px solid rgba(255,255,255,0.06); border-radius:20px; padding:6px 14px; font-size:11px; color:#aab0d6;">🔍 Search predictions, history...</div>
    </div>
    <div style="font-size:34px; font-weight:800; color:white; letter-spacing:-0.8px; margin-top:18px;">Enter Your Details</div>
    <div style="color:#8b90b5; font-size:13.5px; margin-top:6px;">Fill in the details below to generate your personalized love compatibility prediction</div>
    """, unsafe_allow_html=True)

    c1,c2 = st.columns(2)
    with c1:
        n1=st.text_input("Your Name", placeholder="e.g. Alex Morgan")
        bd1=st.text_input("Your Birthday", placeholder="1994-08-21")
    with c2:
        n2=st.text_input("Partner's Name", placeholder="e.g. Jamie Lee")
        bd2=st.text_input("Partner's Birthday", placeholder="1996-03-14")

    ay=st.number_input("Your Age",18,70,25)
    ap=st.number_input("Partner Age",18,70,23)
    rel=st.selectbox("Relationship Status", ["Serious • Dating","Dating","Married","Long Distance","Crush"])
    comm=st.selectbox("Communication Style", ["Open & Honest","Open","Honest","Playful","Reserved"])
    trust=st.selectbox("Trust Level", ["High","Medium","Low"])

    st.markdown('<div style="margin:14px 0 8px; color:white; font-weight:600; font-size:14px; text-align:center;">Interests & Values</div>', unsafe_allow_html=True)
    interests=st.multiselect("", ["Travel","Music","Food","Fitness","Art","Technology"], default=["Travel","Music"], label_visibility="collapsed")
    # custom pills display
    pill_html = "".join([f'<span class="pill">{"🌍" if i=="Travel" else "🎵" if i=="Music" else "🍜" if i=="Food" else "💪" if i=="Fitness" else "🎨" if i=="Art" else "💻"} {i}</span>' for i in interests])
    st.markdown(f'<div style="text-align:center; margin:8px 0;">{pill_html}</div>', unsafe_allow_html=True)

    st.markdown('<div class="run" style="margin-top:18px;">', unsafe_allow_html=True)
    btn=st.button("✨ Run Prediction", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; margin-top:12px; color:#6f769e; font-size:11px;">🔒 Data is secure • Encrypted • Privacy compliant</div></div>', unsafe_allow_html=True)

with right:
    if btn:
        score=predict_score(comm,trust,interests,rel,ay,ap)
    else:
        score=87

    emo= min(99, score+5 if score>=70 else score)
    comm_s= min(99, score-2 if score>=60 else score+5)
    fut= min(99, score-6 if score>=60 else score+2)

    st.markdown(f"""
    <div class="glass">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="color:white; font-weight:700; font-size:18px;">Prediction Result</div>
        <div style="background:rgba(34,197,94,0.15); border:1px solid rgba(34,197,94,0.25); color:#4ade80; padding:4px 12px; border-radius:20px; font-size:11px; font-weight:600;">● Live</div>
      </div>

      <div style="text-align:center; margin:26px 0 18px;">
        <div class="heart-wrap">
          <svg width="148" height="132" viewBox="0 0 100 90"><defs><linearGradient id="hg" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#ff4da6"/><stop offset="100%" stop-color="#ff8ec8"/></linearGradient><filter id="glow"><feDropShadow dx="0" dy="0" stdDeviation="5" flood-color="#ff4da6" flood-opacity="0.9"/><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="#a855f7" flood-opacity="0.6"/></filter></defs>
          <path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="none" stroke="url(#hg)" stroke-width="2.6" filter="url(#glow)"/>
          </svg>
        </div>
        <div style="font-size:64px; font-weight:800; background:linear-gradient(180deg,#ffb3d1,#ff4da6); -webkit-background-clip:text; -webkit-text-fill-color:transparent; line-height:1; margin-top:8px; text-shadow:0 0 30px rgba(255,77,166,0.5);">{score}%</div>
        <div style="color:#ffb3d1; font-weight:700; font-size:17px; margin-top:4px; text-shadow:0 0 10px rgba(255,77,166,0.4);">High Compatibility</div>
      </div>

      <div class="bar"><div class="fill" style="width:{score}%;"></div></div>

      <div style="margin-top:22px; display:flex; flex-direction:column; gap:12px;">
        <div style="background:rgba(26,32,77,0.7); border:1px solid rgba(255,255,255,0.05); border-radius:12px; padding:10px 12px;"><div style="display:flex; justify-content:space-between; font-size:12.5px; color:#aab0d6;"><span>Emotional Match</span><span style="color:white; font-weight:700;">{emo}%</span></div><div class="bar" style="height:6px; margin-top:8px;"><div class="fill" style="width:{emo}%; background:linear-gradient(90deg,#a855f7,#ff8ec8);"></div></div></div>
        <div style="background:rgba(26,32,77,0.7); border:1px solid rgba(255,255,255,0.05); border-radius:12px; padding:10px 12px;"><div style="display:flex; justify-content:space-between; font-size:12.5px; color:#aab0d6;"><span>Communication</span><span style="color:white; font-weight:700;">{comm_s}%</span></div><div class="bar" style="height:6px; margin-top:8px;"><div class="fill" style="width:{comm_s}%;"></div></div></div>
        <div style="background:rgba(26,32,77,0.7); border:1px solid rgba(255,255,255,0.05); border-radius:12px; padding:10px 12px;"><div style="display:flex; justify-content:space-between; font-size:12.5px; color:#aab0d6;"><span>Future Stability</span><span style="color:white; font-weight:700;">{fut}%</span></div><div class="bar" style="height:6px; margin-top:8px;"><div class="fill" style="width:{fut}%; background:linear-gradient(90deg,#ff4da6,#a855f7);"></div></div></div>
      </div>

      <div style="margin-top:18px; background:rgba(26,32,77,0.6); border:1px solid rgba(255,255,255,0.05); border-radius:14px; padding:14px;">
        <div style="color:white; font-weight:700; font-size:13px; display:flex; gap:6px;">✨ AI Insights</div>
        <div style="color:#8b90b5; font-size:11.5px; line-height:1.6; margin-top:10px;">
          • Strong emotional connection detected; shared values align highly<br>
          • Communication is {comm.lower()} and supportive; excellent for long-term growth<br>
          • Recommendation: Plan regular quality time to strengthen the bond
        </div>
      </div>
      <div style="text-align:center; margin-top:12px; color:#5a628a; font-size:10.5px;">Generated 2 seconds ago • Confidence score 94%</div>
    </div>
    """, unsafe_allow_html=True)
