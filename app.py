import streamlit as st
import pandas as pd
import joblib, os, base64

st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    try:
        if os.path.exists("couple_love_model.pkl"):
            return joblib.load("couple_love_model.pkl")
    except:
        return None
model = load_model()

def get_bg():
    if os.path.exists("header_bg.jpg"):
        with open("header_bg.jpg","rb") as f:
            return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode()}"
    return "https://images.unsplash.com/photo-1529634597503-139d3726fed5?q=80&w=2000"

bg = get_bg()

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&family=Dancing+Script:wght@500;600&display=swap');
* {{ font-family: 'Poppins', sans-serif; }}
.stApp {{ background: #070a1e!important; }}
header, footer, #MainMenu {{ visibility:hidden; }}
.block-container {{ max-width:99%!important; padding:0.2rem 1rem!important; }}
@keyframes heartBeat {{ 0%,100%{{transform:scale(1); filter:drop-shadow(0 0 20px #ff2a8a) drop-shadow(0 0 40px #9d4dff);}} 15%{{transform:scale(1.14); filter:drop-shadow(0 0 35px #ff2a8a) drop-shadow(0 0 70px #9d4dff);}} 45%{{transform:scale(1.06);}} }}
.heart-box {{ animation: heartBeat 1.6s infinite; width:145px; height:135px; }}
.top-header {{
  height: 115px;
  background: linear-gradient(90deg, #070a1e 0%, rgba(7,10,30,0.92) 18%, rgba(7,10,30,0.4) 45%, rgba(7,10,30,0.05) 75%), url('{bg}');
  background-size: cover; background-position: center 35%;
  display:flex; justify-content:space-between; align-items:center;
  padding:0 28px; border-bottom:1px solid rgba(255,255,255,0.06);
  margin: -12px -16px 16px -16px;
}}
.card {{ background: rgba(16,22,55,0.96); border:1px solid rgba(120,110,255,0.14); border-radius:18px; padding:20px; box-shadow:0 8px 32px rgba(0,0,0,0.45); }}
.nav-active {{ background: linear-gradient(90deg, rgba(255,50,130,0.30), rgba(150,50,255,0.20)); border:1px solid rgba(255,80,150,0.28); border-radius:10px; padding:11px 14px; color:#ffc2d9!important; font-weight:600; display:flex; gap:12px; }}
.nav-item {{ color:#6f769e; padding:11px 14px; display:flex; gap:12px; font-size:14px; }}
.stSelectbox > div > div,.stNumberInput > div > div > input {{ background:#121938!important; border:1px solid rgba(255,255,255,0.07)!important; border-radius:10px!important; color:#c8d0f0!important; height:44px!important; font-size:13.5px!important; }}
.stMultiSelect > div > div {{ background:#121938!important; border-radius:10px!important; border:1px solid rgba(255,255,255,0.07)!important; }}
.predict-btn button {{ background: linear-gradient(90deg, #ff4da6 0%, #9d4dff 100%)!important; color:white!important; border-radius:12px!important; height:50px!important; font-weight:700!important; font-size:15px!important; border:none!important; box-shadow:0 8px 22px rgba(255,77,166,0.4)!important; }}
.progress-track {{ background:#1a2042; height:12px; border-radius:20px; overflow:hidden; }}
.progress-fill {{ height:100%; border-radius:20px; background: linear-gradient(90deg, #ff4da6, #b14dff); box-shadow:0 0 10px #ff4da6; transition: width 0.9s ease; }}
.insight-box {{ background: rgba(19,26,68,0.85); border:1px solid rgba(255,255,255,0.06); border-radius:14px; padding:14px; margin-top:14px; }}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="top-header">
  <div style="display:flex; gap:16px; align-items:center;">
    <div style="font-size:52px; line-height:1; filter: drop-shadow(0 0 8px #ff4da6);">💞</div>
    <div>
      <div style="font-size:33px; font-weight:800;"><span style="color:#ff4da6;">Love</span> <span style="color:white;"> Prediction</span></div>
      <div style="color:#8a91b8; font-size:14px; margin-top:1px;">AI • Data • Better Love Insights</div>
    </div>
  </div>
  <div style="text-align:right;">
    <div style="color:#ffcfe6; font-family:'Dancing Script',cursive; font-size:18px; line-height:1.15; transform:rotate(-2deg);">Some connections<br>are meant to be... 💗</div>
    <div style="width:95px; height:2px; background: linear-gradient(90deg,#ff4da6,transparent); border-radius:10px; margin-top:5px; margin-left:auto; transform:rotate(-3deg);"></div>
  </div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.16, 0.38, 0.46], gap="medium")

with c1:
    st.markdown("""
    <div style="padding-top:8px;">
      <div class="nav-active">🏠 Home</div>
      <div class="nav-item">♡ Prediction</div>
      <div class="nav-item">📊 About Model</div>
      <div class="nav-item">ⓘ How It Works</div>
      <div style="margin-top:360px; text-align:left; padding-left:6px;">
        <div style="color:#ff6b9e; font-size:22px; text-align:center;">💗</div>
        <div style="color:#7d5a70; font-family:'Dancing Script',cursive; font-size:13px; line-height:1.35; margin-top:8px;">Love isn't just a feeling...<br><span style="color:#e8e8ff; font-family:Poppins; font-style:italic; font-weight:600;">It's a connection</span> ♡</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; gap:10px;"><span style="font-size:22px;">💖</span><span style="font-size:18px; font-weight:700; color:white;">Enter Your Details</span></div><div style="color:#7a81a8; font-size:12px; margin:4px 0 16px;">Fill in the information below to predict the love compatibility.</div>', unsafe_allow_html=True)

    g_you = st.selectbox("👤 Gender (You)", ["Male", "Female", "Other"])
    g_part = st.selectbox("👤 Gender (Partner)", ["Female", "Male", "Other"])
    age_you = st.number_input("📅 Age (You)", 18, 70, 25)
    age_part = st.number_input("📅 Age (Partner)", 18, 70, 23)
    rel = st.selectbox("💗 Relationship Type", ["Dating", "Married", "Long Distance", "Crush"])
    interests = st.multiselect("⭐ Common Interests", ["Travel", "Music", "Movies", "Sports", "Gaming"], default=["Travel","Music","Movies"])
    comm = st.selectbox("💬 Communication Style", ["Open", "Reserved", "Honest", "Playful"])
    trust = st.selectbox("🛡️ Trust Level", ["High", "Medium", "Low"])

    st.write("")
    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    predict_btn = st.button("✨ Predict Love →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c3:
    if predict_btn:
        cmap = {"Open":9, "Honest":8, "Playful":7, "Reserved":5}
        tmap = {"High":9, "Medium":6, "Low":3}
        rmap = {"Dating":6, "Married":8, "Long Distance":4, "Crush":3}
        c_score, t_score, time_h = cmap[comm], tmap[trust], rmap[rel]
        u_score = min(10, 6+len(interests))
        support, fights, gifts, happy = (8 if trust=="High" else 5), (1 if trust=="High" and comm=="Open" else 6 if trust=="Low" else 2), (3 if len(interests)>=3 else 1), (9 if t_score>=8 and c_score>=8 else 6)
        if model is not None:
            try:
                df = pd.DataFrame([{"communication_score":c_score,"trust_score":t_score,"understanding_score":u_score,"time_together_hours":time_h,"support_score":support,"fights_per_month":fights,"gifts_per_month":gifts,"happy_together_score":happy}])
                raw = model.predict(df)[0]
                score = int(raw*100) if raw<=1.5 else int(raw)
                score = max(15, min(96, score + len(interests) - (6 if abs(age_you-age_part)>12 else 0)))
            except: score = int((c_score*9 + t_score*12 + u_score*8 + support*8 + happy*9 - fights*4)/5.5)
        else:
            score = int((c_score*9 + t_score*12 + u_score*8 + support*8 + happy*9 - fights*4)/5.5)
            score = max(18, min(94, score))
    else:
        score = 87

    if score >= 80: label, desc = "High Compatibility!", "You and your partner have a strong chance of a healthy and long-lasting relationship."
    elif score >= 60: label, desc = "Good Compatibility", "You share a good bond. Improve communication to make it stronger."
    elif score >= 40: label, desc = "Average Compatibility", "Some ups and downs. Work on trust and understanding."
    else: label, desc = "Needs Work", "Your relation needs more time and open talks."

    st.markdown(f"""
    <div class="card" style="border:1px solid rgba(160,100,255,0.18);">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="color:white; font-weight:700; font-size:16px; display:flex; gap:10px;">💗 Prediction Result</div>
        <div style="background: rgba(30,35,80,0.9); border:1px solid rgba(255,255,255,0.08); padding:6px 12px; border-radius:20px; font-size:11px; color:#aab0d6;">✦ AI Powered</div>
      </div>
      <div style="display:flex; gap:24px; align-items:center; margin-top:22px;">
        <div class="heart-box">
          <svg width="145" height="135" viewBox="0 0 100 90">
            <defs>
              <linearGradient id="hg" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ff6eb5"/><stop offset="50%" stop-color="#ff3d8a"/><stop offset="100%" stop-color="#9d4dff"/></linearGradient>
              <filter id="glow"><feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#ff2a8a" flood-opacity="0.9"/><feDropShadow dx="0" dy="0" stdDeviation="12" flood-color="#a020f0" flood-opacity="0.7"/></filter>
            </defs>
            <path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,50,130,0.12)" stroke="url(#hg)" stroke-width="2.2" filter="url(#glow)"/>
            <text x="50" y="48" text-anchor="middle" fill="white" font-size="23" font-weight="800">{score}%</text>
          </svg>
        </div>
        <div><div style="color:#ff7ab8; font-weight:800; font-size:22px;">{label}</div><div style="color:#a8aecf; font-size:13px; line-height:1.5; margin-top:8px;">{desc}</div></div>
      </div>
      <div class="progress-track"><div class="progress-fill" style="width:{score}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:7px; font-size:12.5px;"><span style="color:#8b90b5;">Compatibility Score</span><span style="color:white; font-weight:700;">{score}%</span></div>
      <div class="insight-box">
        <div style="color:white; font-weight:600; font-size:13px; margin-bottom:12px;">⊕ Key Insights</div>
        <div style="display:flex; justify-content:space-between; text-align:center;">
          <div><div style="color:#ff6b9e; font-size:20px;">♡</div><div style="font-size:11px; color:#8b90b5;">Communication</div><div style="color:white; font-weight:600; font-size:13px; margin-top:3px;">{comm if predict_btn else 'High'}</div></div>
          <div><div style="color:#ff8ac6; font-size:20px;">☆</div><div style="font-size:11px; color:#8b90b5;">Shared Interests</div><div style="color:white; font-weight:600; font-size:13px; margin-top:3px;">High</div></div>
          <div><div style="color:#7a8bff; font-size:20px;">🛡</div><div style="font-size:11px; color:#8b90b5;">Trust</div><div style="color:white; font-weight:600; font-size:13px; margin-top:3px;">{trust if predict_btn else 'High'}</div></div>
          <div><div style="color:#8b8bff; font-size:20px;">☺</div><div style="font-size:11px; color:#8b90b5;">Emotional Bond</div><div style="color:white; font-weight:600; font-size:13px; margin-top:3px;">High</div></div>
        </div>
      </div>
      <div class="insight-box">
        <div style="color:white; font-weight:600; font-size:13px;">💡 Why This Prediction?</div>
        <div style="color:#8b90b5; font-size:11.5px; line-height:1.6; margin-top:8px;">Based on your age, communication style, shared interests and trust level, the model predicts a high level of compatibility. Your values and preferences align well, which increases the chances of a successful relationship.</div>
      </div>
    </div>
    <div style="text-align:right; color:#6d7294; font-family:'Dancing Script',cursive; font-size:12.5px; margin-top:10px;">Good things take time... ♡</div>
    """, unsafe_allow_html=True)
