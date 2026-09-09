import streamlit as st
import pandas as pd
import joblib, os

st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

# 1. MODEL LOAD
@st.cache_resource
def load_model():
    # tere repo me jo bhi naam ho usko try karega
    for name in ["couple_love_model.pkl", "love_model.pkl", "model.pkl"]:
        if os.path.exists(name):
            try:
                return joblib.load(name)
            except Exception as e:
                st.error(f"Model load fail: {e}")
    return None

model = load_model()

# 2. TRUE PREDICTION - jo tune train kiya tha usi pe
def model_predict(comm, trust, interests, rel_type, age_you, age_part):
    # ye mapping training ke time wali hai
    comm_map = {"Open": 9, "Open & Honest": 9, "Honest": 8, "Playful": 7, "Reserved": 5}
    trust_map = {"High": 9, "Medium": 6, "Low": 3}
    rel_map = {"Dating": 6, "Married": 8, "Long Distance": 4, "Crush": 3}

    cs = comm_map.get(comm, 8)
    ts = trust_map.get(trust, 8)
    th = rel_map.get(rel_type, 6)
    us = min(10, 5 + len(interests) * 1.2)
    sup = 8 if ts >= 8 else 5
    fights = 1 if (ts >= 8 and cs >= 8) else 6 if ts <= 3 else 2

    features = {
        "communication_score": cs,
        "trust_score": ts,
        "understanding_score": us,
        "time_together_hours": th,
        "support_score": sup,
        "fights_per_month": fights,
        "gifts_per_month": 3,
        "happy_together_score": 9 if ts >= 8 else 6
    }

    if model is None:
        return None

    try:
        # model ke expected columns
        if hasattr(model, "feature_names_in_"):
            cols = list(model.feature_names_in_)
            df = pd.DataFrame([features])
            for c in cols:
                if c not in df.columns:
                    df[c] = 0
            df = df[cols]
        else:
            df = pd.DataFrame([features])

        raw = model.predict(df)[0]
        score = int(raw * 100) if raw <= 1.5 else int(raw)

        # age gap + interest bonus
        if abs(age_you - age_part) > 12:
            score -= 6
        score += len(interests)

        return max(5, min(98, score))
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return None

# CSS - TERI IMAGE JAISE COLOR
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Dancing+Script:wght@600&display=swap');
.stApp{background:#070a1e!important;}
header,footer,#MainMenu{visibility:hidden;}
.block-container{max-width:99%!important; padding:0 1rem!important;}
*{font-family:'Poppins',sans-serif;}
.top{height:92px; margin:-14px -16px 18px -16px; padding:0 24px; background:linear-gradient(90deg,#070a1e 0%,#12112e 60%,#1a0f2e 100%); border-bottom:1px solid rgba(255,77,166,0.12); display:flex; justify-content:space-between; align-items:center;}
.card{background:#10163a!important; border:1px solid rgba(120,110,255,0.13)!important; border-radius:16px!important; padding:18px!important;}
.nav-on{background:linear-gradient(90deg, rgba(255,77,166,0.28), rgba(120,50,200,0.22))!important; border:1px solid rgba(255,77,166,0.18)!important; border-radius:10px; padding:11px 14px; color:#ffb3d1!important; font-weight:600; display:flex; gap:12px;}
.nav{color:#6f769e; padding:11px 14px; display:flex; gap:12px; font-size:14px;}
.stSelectbox>div>div,.stNumberInput>div>div>input{background:#131b42!important; border:1px solid rgba(255,255,255,0.07)!important; border-radius:10px!important; color:#c8d0f0!important; height:44px!important;}
.stMultiSelect>div>div{background:#131b42!important; border-radius:10px!important; border:1px solid rgba(255,255,255,0.07)!important;}
.predict button{background:linear-gradient(90deg,#ff4da6 0%,#a855f7 100%)!important; color:white!important; border-radius:12px!important; height:48px!important; font-weight:600!important; border:none!important; box-shadow:0 8px 22px rgba(255,77,166,0.35)!important;}
@keyframes glow{0%,100%{filter:drop-shadow(0 0 10px #ff4da6) drop-shadow(0 0 22px #a855f7);}50%{filter:drop-shadow(0 0 18px #ff4da6) drop-shadow(0 0 38px #a855f7);}}
.neon{animation:glow 2s infinite;}
.bar{background:rgba(255,255,255,0.08); height:11px; border-radius:20px; overflow:hidden;}
.fill{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff4da6,#d946ef,#a855f7);}
.box{background:rgba(19,27,71,0.9); border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:14px;}
</style>
<div class="top">
  <div style="display:flex; gap:14px; align-items:center;"><div style="width:44px; height:44px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:22px;">💞</div><div><div style="font-size:26px; font-weight:800;"><span style="color:#ff4da6;">Love</span> <span style="color:white;">Prediction</span></div><div style="color:#7a81a8; font-size:11.5px;">AI • Data • Better Love Insights</div></div></div>
  <div style="color:#ffc2d9; font-family:'Dancing Script',cursive; font-size:16px; text-align:right;">Some connections<br>are meant to be... ♡</div>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([0.155,0.38,0.465], gap="medium")

with c1:
    st.markdown('<div class="card" style="height:760px;"><div class="nav-on">🏠 Home</div><div class="nav">♡ Prediction</div><div class="nav">📊 About Model</div><div class="nav">ⓘ How It Works</div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><div style="color:white; font-weight:700; font-size:17px;">💖 Enter Your Details</div><div style="color:#7a81a8; font-size:11.5px; margin:6px 0 16px;">Fill in the information below to predict the love compatibility.</div>', unsafe_allow_html=True)
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
            st.error("❌ couple_love_model.pkl nahi mila GitHub pe! Upload karo.")
            score = 0
    else:
        score = 0

    disp = score if score>0 else 87
    if score==0: label,desc="Ready to Predict?","Model se prediction ke liye Predict dabao"
    elif score>=80: label,desc="High Compatibility!","You and your partner have a strong chance of a healthy and long-lasting relationship."
    elif score>=60: label,desc="Good Compatibility","Good bond, model says improve communication."
    elif score>=40: label,desc="Average Compatibility","Model detected ups & downs."
    else: label,desc="Needs Work","Model says needs more time & understanding."

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center;"><div style="color:white; font-weight:700;">💖 Prediction Result</div><div style="background:#1a214a; padding:5px 12px; border-radius:20px; font-size:10.5px; color:{'#4ade80' if model else '#f87171'};">{'● Model Loaded ✅' if model else '● Model Missing ❌'}</div></div>
      <div style="display:flex; gap:22px; align-items:center; margin-top:20px;">
        <div class="neon"><svg width="124" height="112" viewBox="0 0 100 90"><defs><linearGradient id="hg" x1="0%" y1="100%" x2="0%" y2="0%"><stop offset="0%" stop-color="#a855f7"/><stop offset="100%" stop-color="#ff8ec8"/></linearGradient></defs><path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,77,166,0.10)" stroke="url(#hg)" stroke-width="2.3"/><text x="50" y="49" text-anchor="middle" fill="white" font-size="23" font-weight="800">{disp}%</text></svg></div>
        <div><div style="color:#ff7ab8; font-weight:800; font-size:21px;">{label}</div><div style="color:#a8aecf; font-size:12.5px; margin-top:6px;">{desc}</div></div>
      </div>
      <div class="bar" style="margin-top:18px;"><div class="fill" style="width:{disp}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px;"><span style="color:#8b90b5;">Compatibility Score (Model.pkl)</span><span style="color:white; font-weight:700;">{disp}%</span></div>
      <div class="box" style="margin-top:18px;"><div style="color:white; font-weight:600; font-size:13px; margin-bottom:14px;">⊕ Key Insights</div>
        <div style="display:flex; justify-content:space-between; text-align:center;">
          <div><div style="color:#ff6b9e;">♡</div><div style="font-size:10.5px; color:#8b90b5;">Communication</div><div style="color:white; font-weight:600; font-size:12px;">{comm if btn else 'High'}</div></div>
          <div><div style="color:#ff8ac6;">☆</div><div style="font-size:10.5px; color:#8b90b5;">Shared Interests</div><div style="color:white; font-weight:600; font-size:12px;">{len(interests)}</div></div>
          <div><div style="color:#7a8bff;">🛡</div><div style="font-size:10.5px; color:#8b90b5;">Trust</div><div style="color:white; font-weight:600; font-size:12px;">{trust if btn else 'High'}</div></div>
          <div><div style="color:#8b8bff;">☺</div><div style="font-size:10.5px; color:#8b90b5;">Emotional Bond</div><div style="color:white; font-weight:600; font-size:12px;">{'High' if disp>=60 else 'Low'}</div></div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)
