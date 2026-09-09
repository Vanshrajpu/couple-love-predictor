import streamlit as st, pandas as pd, joblib, os
st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    try:
        if os.path.exists("couple_love_model.pkl"):
            return joblib.load("couple_love_model.pkl")
    except: return None
model = load_model()

BG = "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=2000"

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Dancing+Script:wght@600&display=swap');
*{{font-family:'Poppins',sans-serif;}}.stApp{{background:#070a1e!important;}} header,footer{{visibility:hidden;}}
.block-container{{max-width:99%!important; padding:0.3rem 1rem!important;}}
@keyframes beat{{0%,100%{{transform:scale(1)}}15%{{transform:scale(1.14)}}}}
.heart{{animation:beat 1.4s infinite; filter:drop-shadow(0 0 18px #ff4da6) drop-shadow(0 0 32px #9d4dff);}}
.top{{height:108px; background:linear-gradient(90deg,#070a1e 0% 20%,rgba(7,10,30,0.92) 32%,rgba(7,10,30,0.25) 62%),url('{BG}'); background-size:cover; background-position:center 35%; display:flex; justify-content:space-between; align-items:center; padding:0 26px; margin:-12px -16px 14px -16px; border-bottom:1px solid rgba(255,255,255,0.06);}}
.card{{background:#101638!important; border:1px solid rgba(120,110,255,0.14)!important; border-radius:18px!important; padding:18px!important;}}
.nav-on{{background:linear-gradient(90deg,rgba(255,50,130,0.32),rgba(150,50,255,0.18))!important; border:1px solid rgba(255,80,150,0.28)!important; border-radius:10px; padding:10px 14px; color:#ffc2d9!important; font-weight:700; display:flex; gap:10px;}}
.nav{{color:#6f769e; padding:10px 14px; display:flex; gap:10px; font-size:14px;}}
.stSelectbox>div>div,.stNumberInput>div>div>input{{background:#121938!important; border:1px solid rgba(255,255,255,0.07)!important; border-radius:10px!important; color:#c8d0f0!important; height:42px!important;}}
.stMultiSelect>div>div{{background:#121938!important; border-radius:10px!important; border:1px solid rgba(255,255,255,0.07)!important;}}
.predict-btn button{{background:linear-gradient(90deg,#ff4da6 0%,#9d4dff 100%)!important; color:white!important; border-radius:12px!important; height:48px!important; font-weight:700!important; border:none!important; box-shadow:0 8px 22px rgba(255,77,166,0.45)!important;}}
.bar{{background:#1a2042; height:10px; border-radius:20px; overflow:hidden; margin-top:14px;}}
.fill{{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff4da6,#b14dff);}}
.box{{background:#141c42; border:1px solid rgba(255,255,255,0.06); border-radius:12px; padding:12px; margin-top:12px;}}
</style>
<div class="top">
  <div style="display:flex; gap:14px; align-items:center;"><div style="font-size:42px;">💞</div><div><div style="font-size:28px; font-weight:800;"><span style="color:#ff4da6;">Love</span> <span style="color:white;"> Prediction</span></div><div style="color:#8a91b8; font-size:12px;">AI • Data • Better Love Insights</div></div></div>
  <div style="color:#ffcfe6; font-family:'Dancing Script',cursive; font-size:16px; text-align:right; transform:rotate(-2deg);">Some connections<br>are meant to be... 💗</div>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([0.15,0.40,0.45], gap="medium")
with c1:
    st.markdown("""<div><div class="nav-on">🏠 Home</div><div class="nav">♡ Prediction</div><div class="nav">📊 About Model</div><div class="nav">ⓘ How It Works</div><div style="margin-top:360px; text-align:center;"><div style="color:#ff6b9e; font-size:22px;">💗</div><div style="color:#7d5a70; font-family:'Dancing Script',cursive; font-size:13px;">Love isn't just a feeling...<br><span style="color:#e8e8ff; font-weight:600;">It's a connection</span> ♡</div></div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="font-weight:700; color:white;">💖 Enter Your Details</div><div style="color:#7a81a8; font-size:11px; margin:4px 0 12px;">Fill in the information below to predict the love compatibility.</div>', unsafe_allow_html=True)
    gy=st.selectbox("👤 Gender (You)",["Male","Female","Other"]); gp=st.selectbox("👤 Gender (Partner)",["Female","Male","Other"])
    ay=st.number_input("📅 Age (You)",18,70,25); ap=st.number_input("📅 Age (Partner)",18,70,23)
    rel=st.selectbox("💗 Relationship Type",["Dating","Married","Long Distance","Crush"])
    interests=st.multiselect("⭐ Common Interests",["Travel","Music","Movies","Sports","Gaming"],default=["Travel","Music","Movies"])
    comm=st.selectbox("💬 Communication Style",["Open","Reserved","Honest","Playful"]); trust=st.selectbox("🛡️ Trust Level",["High","Medium","Low"])
    st.write(""); st.markdown('<div class="predict-btn">', unsafe_allow_html=True); btn=st.button("✨ Predict Love →",use_container_width=True); st.markdown('</div></div>', unsafe_allow_html=True)
with c3:
    if btn:
        cmap={"Open":9,"Honest":8,"Playful":7,"Reserved":5}; tmap={"High":9,"Medium":6,"Low":3}; rmap={"Dating":6,"Married":8,"Long Distance":4,"Crush":3}
        cs,ts,th=cmap[comm],tmap[trust],rmap[rel]; us=min(10,6+len(interests)); sup=8 if trust=="High" else 5; fights=1 if trust=="High" and comm=="Open" else 6 if trust=="Low" else 2
        if model is not None:
            try: df=pd.DataFrame([{"communication_score":cs,"trust_score":ts,"understanding_score":us,"time_together_hours":th,"support_score":sup,"fights_per_month":fights,"gifts_per_month":3,"happy_together_score":9 if ts>=8 else 6}]); raw=model.predict(df)[0]; score=int(raw*100) if raw<=1.5 else int(raw); score=max(15,min(96,score+len(interests)))
            except: score=70
        else: score=int((cs*9+ts*12+us*8+sup*8)/4.5); score=max(18,min(94,score))
    else: score=87
    if score>=80: label,desc,col="High Compatibility!","You and your partner have a strong chance of a healthy and long-lasting relationship.","#ff7ab8"
    elif score>=60: label,desc,col="Good Compatibility","You share a good bond.","#a78bfa"
    elif score>=40: label,desc,col="Average Compatibility","Some ups and downs. Work on trust and understanding.","#ffb86c"
    else: label,desc,col="Needs Work","Needs more time.","#f87171"
    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between;"><div style="color:white; font-weight:600; font-size:14px;">💗 Prediction Result</div><div style="background:#1e264d; padding:4px 10px; border-radius:20px; font-size:10px; color:#aab0d6;">✦ AI Powered</div></div>
      <div style="display:flex; gap:20px; align-items:center; margin-top:18px;">
        <div class="heart"><svg width="110" height="100" viewBox="0 0 100 90"><defs><linearGradient id="hg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ff6eb5"/><stop offset="100%" stop-color="#9d4dff"/></linearGradient></defs><path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,50,130,0.18)" stroke="url(#hg)" stroke-width="2.2"/><text x="50" y="48" text-anchor="middle" fill="white" font-size="20" font-weight="800">{score}%</text></svg></div>
        <div><div style="color:{col}; font-weight:800; font-size:18px;">{label}</div><div style="color:#a8aecf; font-size:12px; margin-top:6px;">{desc}</div></div>
      </div>
      <div class="bar"><div class="fill" style="width:{score}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:6px; font-size:11px;"><span style="color:#8b90b5;">Compatibility Score</span><span style="color:white; font-weight:700;">{score}%</span></div>
      <div class="box"><div style="color:white; font-weight:600; font-size:12px; margin-bottom:10px;">⊕ Key Insights</div><div style="display:flex; justify-content:space-between; text-align:center; font-size:11px;"><div><div style="color:#ff6b9e;">♡</div><div style="color:#8b90b5; font-size:10px;">Communication</div><div style="color:white; font-weight:600;">{comm if btn else 'High'}</div></div><div><div style="color:#ff8ac6;">☆</div><div style="color:#8b90b5; font-size:10px;">Shared Interests</div><div style="color:white; font-weight:600;">High</div></div><div><div style="color:#7a8bff;">🛡</div><div style="color:#8b90b5; font-size:10px;">Trust</div><div style="color:white; font-weight:600;">{trust if btn else 'High'}</div></div><div><div style="color:#8b8bff;">☺</div><div style="color:#8b90b5; font-size:10px;">Emotional Bond</div><div style="color:white; font-weight:600;">High</div></div></div></div>
    </div>
    """, unsafe_allow_html=True)
