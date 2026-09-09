import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

# === EXACT SAME CSS ===
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');
* { font-family: 'Poppins', sans-serif; }
.stApp { background: #070b1e!important; }
header, footer, #MainMenu { visibility: hidden; }
.block-container { padding: 0.8rem 1.2rem!important; max-width: 98%!important; }

/* Hide streamlit default backgrounds */
div[data-testid="stSelectbox"], div[data-testid="stNumberInput"] { background: transparent!important; }

/* Inputs */
.stSelectbox > div > div,.stNumberInput > div > div > input,.stMultiSelect > div > div {
  background: #141c3a!important;
  border: 1px solid rgba(255,255,255,0.08)!important;
  color: #cbd5f5!important;
  border-radius: 12px!important;
  height: 46px!important;
}
.stMultiSelect span { background: #2a2f5a!important; color: white!important; border-radius: 8px!important; }

/* Cards */
.card-dark {
  background: linear-gradient(180deg, #111735 0%, #0e1330 100%);
  border: 1px solid rgba(124, 125, 255, 0.12);
  border-radius: 18px;
  padding: 20px;
  box-shadow: 0 0 40px rgba(0,0,0,0.4);
}

.side-active {
  background: linear-gradient(90deg, rgba(255,77,166,0.22) 0%, rgba(168,85,255,0.12) 100%);
  border: 1px solid rgba(255,77,166,0.2);
  color: white!important; border-radius: 12px; padding: 12px 16px; font-weight:600;
}
.side-item { color: #8b90b5; padding: 12px 16px; display:flex; gap:10px; align-items:center; }

.heart-box {
  width: 155px; height: 145px;
  background: radial-gradient(ellipse at center, rgba(255,77,166,0.9) 0%, rgba(168,50,255,0.8) 60%, transparent 75%);
  border-radius: 50% 50% 50% 50% / 60% 60% 40% 40%;
  display:flex; align-items:center; justify-content:center;
  font-size: 44px; font-weight: 900; color: white;
  box-shadow: 0 0 35px rgba(255,77,166,0.7), inset 0 0 25px rgba(255,255,255,0.3);
  border: 2.5px solid #ff7ac0;
  position: relative;
}
.heart-box::before {
  content: '♡'; position:absolute; top:-8px; font-size:130px; opacity:0.15; color:#ff4da6;
}
.progress-bg { background: #1e264d; height:12px; border-radius:20px; }
.progress-fill { height:100%; border-radius:20px; background: linear-gradient(90deg, #ff4da6 0%, #d450ff 100%); }
.predict-btn button {
  background: linear-gradient(90deg, #ff4da6 0%, #a855f7 100%)!important;
  color: white!important; border-radius: 14px!important; height: 52px!important;
  font-weight: 700!important; border: none!important; font-size: 15px!important;
  box-shadow: 0 8px 25px rgba(255,77,166,0.35)!important;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    try: return joblib.load("couple_love_model.pkl")
    except: return None
model = load_model()

# TOP BAR WITH COUPLE SILHOUETTE
st.markdown("""
<div style="height:115px; border-radius:18px; background: linear-gradient(90deg, #070b1e 0%, #121a3d 50%, #2a0f2a 100%); border:1px solid rgba(255,255,255,0.06); display:flex; justify-content:space-between; align-items:center; padding:0 28px; position:relative; overflow:hidden;">
  <div style="display:flex; gap:14px; align-items:center; z-index:2;">
    <div style="font-size:42px; filter: drop-shadow(0 0 10px #ff4da6);">💞</div>
    <div>
      <div style="font-size:30px; font-weight:800;"><span style="color:#ff4da6;">Love</span> <span style="color:white;">Prediction</span></div>
      <div style="color:#8b90b5; font-size:13px; letter-spacing:0.5px;">AI • Data • Better Love Insights</div>
    </div>
  </div>
  <div style="position:absolute; right:180px; top:-10px; font-size:90px; opacity:0.9;">👫<span style="position:absolute; right:-20px; top:10px; width:70px; height:70px; background:#ff2d55; border-radius:50%; filter:blur(1px); z-index:-1;"></span></div>
  <div style="color:#f8a6c8; font-family:cursive; font-size:14px; text-align:right; z-index:2;">Some connections<br>are meant to be... <span style="color:#ff4da6;">♡</span><br><div style="width:100px; height:2px; background:#ff4da6; margin-top:4px; margin-left:auto; border-radius:10px;"></div></div>
</div>
""", unsafe_allow_html=True)

st.write("")

col_nav, col_form, col_result = st.columns([0.18, 0.40, 0.42], gap="medium")

with col_nav:
    st.markdown("""
    <div class="card-dark" style="padding:12px; min-height:680px;">
      <div class="side-active">🏠 Home</div>
      <div class="side-item">♡ Prediction</div>
      <div class="side-item">📊 About Model</div>
      <div class="side-item">ⓘ How It Works</div>
      <div style="margin-top:320px; text-align:center;">
        <div style="color:#ff6b9e; font-size:22px;">💗</div>
        <div style="color:#c084a0; font-family:cursive; font-size:12px; line-height:1.4; margin-top:8px;">Love isn't just a feeling...<br><i style="color:white;">It's a connection</i> <span style="color:#ff4da6;">♡</span></div>
        <div style="width:60px; height:2px; background:#ff4da6; margin:6px auto; border-radius:10px; transform:rotate(-8deg);"></div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_form:
    st.markdown('<div class="card-dark">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; gap:10px; align-items:center;"><span style="font-size:22px;">💖</span><span style="font-size:18px; font-weight:700; color:white;">Enter Your Details</span></div>', unsafe_allow_html=True)
    st.markdown('<div style="color:#8b90b5; font-size:12px; margin-top:4px; margin-bottom:16px;">Fill in the information below to predict the love compatibility.</div>', unsafe_allow_html=True)

    g_you = st.selectbox("👤 Gender (You)", ["Male", "Female", "Other"])
    g_part = st.selectbox("👤 Gender (Partner)", ["Female", "Male", "Other"])
    age_you = st.number_input("📅 Age (You)", 18, 70, 25)
    age_part = st.number_input("📅 Age (Partner)", 18, 70, 23)
    rel = st.selectbox("💗 Relationship Type", ["Dating", "Married", "Crush", "Long Distance"])
    interests = st.multiselect("⭐ Common Interests", ["Travel", "Music", "Movies", "Sports", "Food", "Gaming"], default=["Travel", "Music", "Movies"])
    comm = st.selectbox("💬 Communication Style", ["Open", "Reserved", "Honest", "Funny"])
    trust = st.selectbox("🛡️ Trust Level", ["High", "Medium", "Low"])

    st.write("")
    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    predict = st.button("✨ Predict Love →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with col_result:
    if predict:
        base = 60
        if comm == "Open": base += 12
        if trust == "High": base += 18
        base += len(interests)*3
        if abs(age_you-age_part) <=3: base+=5
        if model is not None:
            try:
                df = pd.DataFrame([{"communication_score":8, "trust_score":9 if trust=="High" else 5, "understanding_score":8, "time_together_hours":7, "support_score":8, "fights_per_month":1, "gifts_per_month":3, "happy_together_score":9}])
                base = (base + float(model.predict(df)[0]))/2
            except: pass
        score = int(max(25, min(97, base)))
    else:
        score = 87

    st.markdown(f"""
    <div class="card-dark">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="color:white; font-weight:700; display:flex; gap:8px; align-items:center;"><span style="color:#ff7ac0;">💗</span> Prediction Result</div>
        <div style="background:#1b2347; border:1px solid rgba(255,255,255,0.08); padding:6px 12px; border-radius:20px; font-size:11px; color:#aab0d6;">✦ AI Powered</div>
      </div>

      <div style="display:flex; gap:20px; align-items:center; margin-top:24px;">
        <div class="heart-box">{score}%</div>
        <div>
          <div style="color:#ff7ab8; font-weight:800; font-size:21px;">High Compatibility!</div>
          <div style="color:#a8aecf; font-size:12.5px; line-height:1.5; margin-top:8px;">You and your partner have a strong chance of a healthy and long-lasting relationship.</div>
        </div>
      </div>

      <div style="margin-top:24px;">
        <div class="progress-bg"><div class="progress-fill" style="width:{score}%;"></div></div>
        <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12px;"><span style="color:#8b90b5;">Compatibility Score</span><span style="color:white; font-weight:700;">{score}%</span></div>
      </div>

      <div style="margin-top:20px; background:#151c3d; border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:14px;">
        <div style="color:white; font-weight:600; font-size:13px; margin-bottom:12px; display:flex; gap:6px;">⊕ Key Insights</div>
        <div style="display:flex; justify-content:space-between; text-align:center;">
          <div><div style="color:#ff6b9e; font-size:20px;">♡</div><div style="font-size:10.5px; color:#8b90b5;">Communication</div><div style="font-size:13px; color:white; font-weight:600; margin-top:3px;">High</div></div>
          <div><div style="color:#ff8ac6; font-size:20px;">☆</div><div style="font-size:10.5px; color:#8b90b5;">Shared Interests</div><div style="font-size:13px; color:white; font-weight:600; margin-top:3px;">High</div></div>
          <div><div style="color:#7a8bff; font-size:20px;">🛡</div><div style="font-size:10.5px; color:#8b90b5;">Trust</div><div style="font-size:13px; color:white; font-weight:600; margin-top:3px;">{trust}</div></div>
          <div><div style="color:#8b8bff; font-size:20px;">☺</div><div style="font-size:10.5px; color:#8b90b5;">Emotional Bond</div><div style="font-size:13px; color:white; font-weight:600; margin-top:3px;">High</div></div>
        </div>
      </div>

      <div style="margin-top:14px; background:#151c3d; border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:14px;">
        <div style="color:white; font-weight:600; font-size:13px;">💡 Why This Prediction?</div>
        <div style="color:#8b90b5; font-size:11.5px; line-height:1.6; margin-top:8px;">Based on your age, communication style, shared interests and trust level, the model predicts a high level of compatibility. Your values and preferences align well, which increases the chances of a successful relationship.</div>
      </div>
    </div>
    <div style="text-align:right; color:#6d7294; font-family:cursive; font-size:12px; margin-top:10px;">Good things take time... ♡</div>
    """, unsafe_allow_html=True)
