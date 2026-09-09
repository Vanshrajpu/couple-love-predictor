import streamlit as st
import pandas as pd
import joblib
import base64, os

st.set_page_config(page_title="Love Prediction", page_icon="💖", layout="wide")

# Load header image if exists
def get_header_bg():
    if os.path.exists("header_bg.jpg"):
        with open("header_bg.jpg","rb") as f:
            b64 = base64.b64encode(f.read()).decode()
            return f"data:image/jpeg;base64,{b64}"
    # fallback - online romantic couple
    return "https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=2000"

bg_url = get_header_bg()

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&display=swap');
* {{ font-family: 'Poppins', sans-serif; }}
.stApp {{ background: #070b1e!important; }}
header, footer {{ visibility: hidden; }}
.block-container {{ padding-top: 0.5rem!important; max-width: 98%!important; }}

@keyframes heartbeat {{
  0%,100% {{ transform: scale(1); }}
  15% {{ transform: scale(1.18); }}
  30% {{ transform: scale(1); }}
  45% {{ transform: scale(1.1); }}
}}
@keyframes glowPulse {{
  0% {{ filter: drop-shadow(0 0 20px #ff4da6) drop-shadow(0 0 40px #a855f7); }}
  100% {{ filter: drop-shadow(0 0 35px #ff4da6) drop-shadow(0 0 70px #a855f7); }}
}}

.card {{
  background: linear-gradient(180deg, rgba(19,26,62,0.95) 0%, rgba(12,17,42,0.98) 100%);
  border: 1px solid rgba(120,110,255,0.12);
  border-radius: 20px; padding: 22px;
}}
.top-bar {{
  height: 135px;
  background: linear-gradient(90deg, #070b1e 0%, rgba(7,11,30,0.85) 25%, rgba(7,11,30,0.15) 60%, rgba(255,0,80,0.15) 100%),
              url('{bg_url}');
  background-size: cover;
  background-position: center 30%;
  border-radius: 20px;
  border: 1px solid rgba(255,255,255,0.08);
  display:flex; justify-content:space-between; align-items:center;
  padding: 0 30px; position:relative; overflow:hidden;
}}
.heart-svg-wrap {{
  width: 155px; height: 140px;
  animation: heartbeat 1.6s infinite, glowPulse 1.6s infinite alternate;
}}

.side-active {{
  background: linear-gradient(90deg, rgba(255,77,166,0.26), rgba(168,85,255,0.14));
  border: 1px solid rgba(255,77,166,0.28); color:white!important;
  border-radius:12px; padding:13px 16px; font-weight:700; display:flex; gap:12px;
}}
.side-item {{ color:#7a81a8; padding:13px 16px; display:flex; gap:12px; font-size:14px; }}
.stSelectbox > div > div,.stNumberInput > div > div > input {{
  background:#131b3d!important; border:1px solid rgba(255,255,255,0.07)!important;
  border-radius:12px!important; color:#dbe2ff!important; height:48px!important;
}}
.stMultiSelect > div > div {{ background:#131b3d!important; border-radius:12px!important; border:1px solid rgba(255,255,255,0.07)!important; }}
.predict-btn button {{
  background: linear-gradient(90deg, #ff4da6 0%, #a855f7 100%)!important;
  color:white!important; border-radius:14px!important; height:54px!important;
  font-weight:800!important; border:none!important;
  box-shadow: 0 8px 28px rgba(255,77,166,0.45)!important;
}}
</style>
""", unsafe_allow_html=True)

# HEADER WITH COUPLE IMAGE
st.markdown("""
<div class="top-bar">
  <div style="display:flex; gap:16px; align-items:center; z-index:2;">
    <div style="font-size:48px; line-height:1; filter:drop-shadow(0 0 10px #ff4da6);">💞</div>
    <div>
      <div style="font-size:32px; font-weight:800;"><span style="color:#ff4da6;">Love</span> <span style="color:white;"> Prediction</span></div>
      <div style="color:#8b90b5; font-size:14px; letter-spacing:0.6px;">AI • Data • Better Love Insights</div>
    </div>
  </div>
  <div style="z-index:2; text-align:right; color:#ffd1e6; font-family:cursive; font-size:15px; line-height:1.3; text-shadow:0 2px 10px rgba(0,0,0,0.8);">
    Some connections<br>are meant to be... 💗
    <div style="width:110px; height:2px; background:#ff4da6; border-radius:10px; margin-top:6px; margin-left:auto; box-shadow:0 0 10px #ff4da6;"></div>
  </div>
</div>
""", unsafe_allow_html=True)

col_nav, col_form, col_res = st.columns([0.19, 0.40, 0.41], gap="medium")

with col_nav:
    st.markdown("""
    <div class="card" style="min-height:700px; padding:14px;">
      <div class="side-active">🏠 Home</div>
      <div class="side-item">♡ Prediction</div>
      <div class="side-item">📊 About Model</div>
      <div class="side-item">ⓘ How It Works</div>
      <div style="margin-top:380px; text-align:center;">
        <div style="color:#ff6b9e; font-size:26px;">💗</div>
        <div style="color:#a87a90; font-family:cursive; font-size:12px;">Love isn't just a feeling...<br><i style="color:white;">It's a connection</i> ♡</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

with col_form:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div style="display:flex; gap:10px;"><span style="font-size:24px;">💖</span><span style="font-size:19px; font-weight:700; color:white;">Enter Your Details</span></div><div style="color:#7a81a8; font-size:12px; margin:6px 0 18px;">Fill in the information below to predict the love compatibility.</div>', unsafe_allow_html=True)
    g_you = st.selectbox("👤 Gender (You)", ["Male", "Female", "Other"])
    g_part = st.selectbox("👤 Gender (Partner)", ["Female", "Male", "Other"])
    age_you = st.number_input("📅 Age (You)", 18, 70, 25)
    age_part = st.number_input("📅 Age (Partner)", 18, 70, 23)
    rel = st.selectbox("💗 Relationship Type", ["Dating", "Married", "Crush", "Long Distance"])
    interests = st.multiselect("⭐ Common Interests", ["Travel", "Music", "Movies"], default=["Travel","Music","Movies"])
    comm = st.selectbox("💬 Communication Style", ["Open", "Reserved", "Honest"])
    trust = st.selectbox("🛡️ Trust Level", ["High", "Medium", "Low"])
    st.write("")
    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)
    predict = st.button("✨ Predict Love →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with col_res:
    score = 87 if not predict else 85
    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between; align-items:center;">
        <div style="color:white; font-weight:700; display:flex; gap:8px; font-size:16px;">💗 Prediction Result</div>
        <div style="background:#1b2347; border:1px solid rgba(255,255,255,0.08); padding:6px 12px; border-radius:20px; font-size:11px; color:#aab0d6;">✦ AI Powered</div>
      </div>
      <div style="display:flex; gap:22px; align-items:center; margin-top:26px;">
        <div class="heart-svg-wrap">
          <svg width="155" height="140" viewBox="0 0 100 90" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="hg" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#ff9ac8"/><stop offset="30%" stop-color="#ff4da6"/><stop offset="70%" stop-color="#c44dff"/><stop offset="100%" stop-color="#7a2bff"/>
              </linearGradient>
              <filter id="glow"><feDropShadow dx="0" dy="0" stdDeviation="8" flood-color="#ff4da6" flood-opacity="0.9"/><feDropShadow dx="0" dy="0" stdDeviation="18" flood-color="#a855f7" flood-opacity="0.6"/></filter>
            </defs>
            <path d="M50 82 L16 48 C 3 35, 3 12, 26 9 C 38 7, 48 18, 50 22 C 52 18, 62 7, 74 9 C 97 12, 97 35, 84 48 Z" fill="url(#hg)" stroke="#ff8ac6" stroke-width="1.4" filter="url(#glow)"/>
            <text x="50" y="47" text-anchor="middle" dominant-baseline="middle" fill="white" font-size="22" font-weight="900" style="font-family:Poppins;">{score}%</text>
          </svg>
        </div>
        <div>
          <div style="color:#ff7ab8; font-weight:800; font-size:22px;">High Compatibility!</div>
          <div style="color:#a8aecf; font-size:13px; line-height:1.5; margin-top:8px;">You and your partner have a strong chance of a healthy and long-lasting relationship.</div>
        </div>
      </div>
      <div style="margin-top:26px;">
        <div style="background:#1e264d; height:14px; border-radius:20px; overflow:hidden;"><div style="height:100%; width:{score}%; border-radius:20px; background: linear-gradient(90deg, #ff4da6, #d450ff);"></div></div>
        <div style="display:flex; justify-content:space-between; margin-top:8px; font-size:12.5px;"><span style="color:#8b90b5;">Compatibility Score</span><span style="color:white; font-weight:700;">{score}%</span></div>
      </div>
      <div style="margin-top:20px; background:#151c3d; border:1px solid rgba(255,255,255,0.06); border-radius:16px; padding:16px;">
        <div style="color:white; font-weight:600; font-size:14px; margin-bottom:12px;">⊕ Key Insights</div>
        <div style="display:flex; justify-content:space-between; text-align:center;">
          <div><div style="color:#ff6b9e; font-size:22px;">♡</div><div style="font-size:11px; color:#8b90b5;">Communication</div><div style="color:white; font-weight:700; margin-top:4px;">High</div></div>
          <div><div style="color:#ff8ac6; font-size:22px;">☆</div><div style="font-size:11px; color:#8b90b5;">Shared</div><div style="color:white; font-weight:700; margin-top:4px;">High</div></div>
          <div><div style="color:#7a8bff; font-size:22px;">🛡</div><div style="font-size:11px; color:#8b90b5;">Trust</div><div style="color:white; font-weight:700; margin-top:4px;">High</div></div>
          <div><div style="color:#8b8bff; font-size:22px;">☺</div><div style="font-size:11px; color:#8b90b5;">Bond</div><div style="color:white; font-weight:700; margin-top:4px;">High</div></div>
        </div>
      </div>
    </div>
    <div style="text-align:right; color:#6d7294; font-family:cursive; font-size:12px; margin-top:10px;">Good things take time... ♡</div>
    """, unsafe_allow_html=True)
