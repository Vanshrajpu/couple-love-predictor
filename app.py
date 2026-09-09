import streamlit as st
import pandas as pd
import joblib
import os

st.set_page_config(page_title="Love Prediction - Vansh Rajput", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    for name in ["couple_love_model.pkl", "model.pkl", "Love_model.pkl"]:
        if os.path.exists(name):
            try:
                m = joblib.load(name)
                if hasattr(m, "predict"):
                    return m, name
            except Exception as e:
                st.error(f"Model load failed: {e}")
                return None, None
    return None, None

model, model_file = load_model()

def true_predict(ay, ap, rel, interests, comm, trust):
    comm_map = {"Open": 8, "Open & Honest": 9, "Honest": 8, "Playful": 7, "Reserved": 4}
    trust_map = {"High": 9, "Medium": 5, "Low": 2}
    rel_map = {"Dating": 6, "Married": 8, "Long Distance": 4, "Crush": 3}

    feats = {
        "communication_score": comm_map.get(comm, 7),
        "trust_score": trust_map.get(trust, 5),
        "understanding_score": min(10, 4 + len(interests) * 1.5),
        "time_together_hours": rel_map.get(rel, 5),
        "support_score": 8 if trust_map.get(trust, 5) >= 7 else 5,
        "fights_per_month": 1 if comm_map.get(comm, 7) >= 8 else 4,
        "gifts_per_month": 3,
        "happy_together_score": 8 if trust_map.get(trust, 5) >= 7 else 5,
        "age_you": ay,
        "age_partner": ap,
        "age_gap": abs(ay - ap),
        "interests_count": len(interests)
    }

    if model is None:
        base = 45 + trust_map.get(trust, 5) * 5 + len(interests) * 4
        if abs(ay - ap) > 12:
            base -= 8
        return max(5, min(97, base))

    try:
        if hasattr(model, "feature_names_in_"):
            cols = list(model.feature_names_in_)
            data = {c: feats.get(c, 0) for c in cols}
            df = pd.DataFrame([data])[cols]
        else:
            df = pd.DataFrame([[
                feats["communication_score"],
                feats["trust_score"],
                feats["understanding_score"],
                feats["time_together_hours"],
                feats["support_score"],
                feats["fights_per_month"],
                feats["gifts_per_month"],
                feats["happy_together_score"]
            ]], columns=[
                "communication_score", "trust_score", "understanding_score",
                "time_together_hours", "support_score", "fights_per_month",
                "gifts_per_month", "happy_together_score"
            ])

        raw = model.predict(df)[0]
        score = int(raw * 100) if raw <= 1.5 else int(raw)
        return max(1, min(99, score))
    except Exception as e:
        st.error(f"Prediction error: {e}")
        return 78

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Dancing+Script:wght@600&display=swap');
.stApp{background:#070a1e!important;}
header,footer,#MainMenu{visibility:hidden;}
.block-container{max-width:100%!important; padding:0 1rem!important;}
*{font-family:'Poppins',sans-serif;}
.top{height:110px; margin:-14px -16px 16px -16px; padding:0 26px; background:linear-gradient(90deg,#070a1e 0%,#1a0a2a 100%), url('bg.jpg'); background-size:cover; background-blend-mode:overlay; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,77,166,0.18);}
.card{background:#10173a!important; border:1px solid rgba(255,255,255,0.07)!important; border-radius:16px!important; padding:18px!important;}
.nav-on{background:linear-gradient(90deg,#ff4da6,#a855f7)!important; border-radius:12px; padding:11px 14px; color:white!important; font-weight:700; display:flex; gap:10px;}
.nav{color:#6f769e; padding:11px 14px; display:flex; gap:10px; font-size:13px;}
.stSelectbox>div>div,.stNumberInput>div>div>input{background:#121b42!important; border-radius:12px!important; color:#c8d0f0!important; height:46px!important;}
.stMultiSelect>div>div{background:#121b42!important; border-radius:12px!important;}
.btn button{background:linear-gradient(90deg,#ff4da6,#a855f7)!important; color:white!important; border-radius:14px!important; height:52px!important; font-weight:800!important; border:none!important; box-shadow:0 10px 25px rgba(255,77,166,0.35)!important;}
@keyframes beat{0%,100%{transform:scale(1);}15%{transform:scale(1.2);}30%{transform:scale(1);}45%{transform:scale(1.15);}}
@keyframes glow{0%,100%{filter:drop-shadow(0 0 10px #ff4da6) drop-shadow(0 0 22px #a855f7);}50%{filter:drop-shadow(0 0 18px #ff4da6) drop-shadow(0 0 38px #a855f7);}}
.heart{animation: beat 1.4s infinite, glow 2s infinite alternate;}
.bar{background:rgba(255,255,255,0.08); height:12px; border-radius:20px; overflow:hidden;}
.fill{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff4da6,#a855f7); box-shadow:0 0 12px #ff4da6;}
</style>
<div class="top">
  <div style="display:flex; gap:14px; align-items:center;">
    <div style="width:44px; height:44px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:12px; display:flex; align-items:center; justify-content:center; font-size:22px;">💞</div>
    <div><div style="font-size:26px; font-weight:800;"><span style="color:#ff4da6;">Love</span> <span style="color:white;">Prediction</span></div><div style="color:#7a81a8; font-size:11px;">AI • Data • Better Love Insights • Vansh Rajput</div></div>
  </div>
  <div style="color:#ffc2d9; font-family:'Dancing Script',cursive;">Some connections<br>are meant to be... ♡</div>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns([0.15, 0.38, 0.47], gap="medium")

with c1:
    st.markdown(f'<div class="card" style="height:760px;"><div class="nav-on">🏠 Home</div><div class="nav">♡ Prediction</div><div class="nav">📊 About Model</div><div class="nav">ⓘ How It Works</div><div style="margin-top:350px; text-align:center;"><div style="background:#151e44; border-radius:12px; padding:10px; display:flex; gap:8px; justify-content:center;"><div style="width:28px; height:28px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:50%; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">VR</div><div style="text-align:left;"><div style="color:white; font-size:11px; font-weight:700;">Vansh Rajput</div><div style="color:#4ade80; font-size:9px;">{model_file if model else "Model Missing"}</div></div></div></div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><div style="color:white; font-weight:700;">💖 Enter Your Details - TRUE MODEL</div>', unsafe_allow_html=True)
    ay = st.number_input("Age (You)", 18, 70, 25)
    ap = st.number_input("Age (Partner)", 18, 70, 23)
    rel = st.selectbox("Relationship Type", ["Dating", "Married", "Long Distance", "Crush"])
    interests = st.multiselect("Common Interests", ["Travel", "Music", "Movies", "Sports", "Gaming"], default=["Travel", "Music", "Movies"])
    comm = st.selectbox("Communication Style", ["Open", "Reserved", "Honest", "Playful", "Open & Honest"])
    trust = st.selectbox("Trust Level", ["High", "Medium", "Low"])
    st.write("")
    st.markdown('<div class="btn">', unsafe_allow_html=True)
    btn = st.button("Predict Love (True Model)", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c3:
    score = true_predict(ay, ap, rel, interests, comm, trust) if btn else 87
    label = "High Compatibility!" if score >= 75 else "Good Compatibility" if score >= 55 else "Average"
    desc = "Strong chance of healthy long-lasting relationship." if score >= 75 else "Good bond - keep nurturing!"
    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between;"><div style="color:white; font-weight:700;">💖 Prediction Result</div><div style="background:#1a214a; padding:6px 12px; border-radius:20px; font-size:10px; color:{'#4ade80' if model else '#f87171'};">{model_file if model else 'Model Missing'}</div></div>
      <div style="display:flex; gap:20px; align-items:center; margin-top:18px;">
        <div class="heart"><svg width="120" height="110" viewBox="0 0 100 90"><defs><linearGradient id="hg" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#ff2d6b"/><stop offset="100%" stop-color="#ff8ec8"/></linearGradient></defs><path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,77,166,0.15)" stroke="url(#hg)" stroke-width="2.5"/><text x="50" y="51" text-anchor="middle" fill="white" font-size="23" font-weight="800">{score}%</text></svg></div>
        <div><div style="color:#ff7ab8; font-weight:800; font-size:20px;">{label}</div><div style="color:#a8aecf; font-size:12px; margin-top:4px;">{desc}</div></div>
      </div>
      <div class="bar" style="margin-top:18px;"><div class="fill" style="width:{score}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:6px; font-size:12px; color:#8b90b5;"><span>Score from {model_file if model else 'model.pkl'}</span><span style="color:white; font-weight:800;">{score}%</span></div>
    </div>
    """, unsafe_allow_html=True)
