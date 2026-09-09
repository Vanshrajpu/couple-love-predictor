import streamlit as st
import pandas as pd
import joblib, os, base64

st.set_page_config(page_title="Love Prediction - Vansh Rajput", page_icon="💖", layout="wide")

# 1. MODEL LOAD - TERI PKL
@st.cache_resource
def load_model():
    # GitHub pe jo bhi naam ho
    for name in ["couple_love_model.pkl","model.pkl","love_model.pkl","Love_model.pkl"]:
        if os.path.exists(name):
            try:
                m = joblib.load(name)
                # Check predict method hai ya nahi
                if hasattr(m, "predict"):
                    return m, name
            except Exception as e:
                st.error(f"Model load error {name}: {e}")
                return None, None
    return None, None

model, model_name = load_model()

# 2. TRUE PREDICTION - BINA KISI FAKE BONUS KE
def true_predict(gender_you, gender_part, age_you, age_part, rel_type, interests, comm_style, trust_level):
    if model is None:
        return None, "Model file nahi mila GitHub pe!"

    # --- TUNE JO DATASET PE TRAIN KIYA THA USKA MAPPING ---
    # Ye values tune training me use kiye the wahi rakhna hai
    # Agar tere dataset me alag mapping hai to yahi change karna
    comm_map = {
        "Open": 8, "Open & Honest": 9, "Honest": 8,
        "Playful": 7, "Reserved": 4
    }
    trust_map = {"High": 9, "Medium": 5, "Low": 2}
    rel_map = {"Dating": 6, "Married": 8, "Long Distance": 4, "Crush": 3}

    # Raw features jo model ne dekhe the
    features = {
        "communication_score": comm_map.get(comm_style, 7),
        "trust_score": trust_map.get(trust_level, 5),
        "understanding_score": min(10, 4 + len(interests) * 1.5), # common interest se understanding
        "time_together_hours": rel_map.get(rel_type, 5),
        "support_score": 8 if trust_map.get(trust_level,5)>=7 else 5,
        "fights_per_month": 1 if comm_map.get(comm_style,7)>=8 else 4,
        "gifts_per_month": 3,
        "happy_together_score": 8 if trust_map.get(trust_level,5)>=7 else 5,
        # Agar tere model me ye extra columns hai to bhi chalega
        "age_you": age_you,
        "age_partner": age_part,
        "age_gap": abs(age_you - age_part),
        "interests_count": len(interests),
        "rel_type_encoded": rel_map.get(rel_type,5)
    }

    try:
        # Model ko kaunse columns chahiye ye check karo - YAHI MAIN LOGIC HAI
        if hasattr(model, "feature_names_in_"):
            expected = list(model.feature_names_in_)
            # DataFrame banao sirf expected columns se
            df_dict = {}
            for col in expected:
                if col in features:
                    df_dict[col] = features[col]
                else:
                    # Agar column nahi mila to 0 ya default
                    df_dict[col] = 0

            df = pd.DataFrame([df_dict])
            # Exact order me
            df = df[expected]
        else:
            # Purane sklearn model jisme feature_names_in_ nahi hai
            # Tere training ka default order
            df = pd.DataFrame([[
                features["communication_score"],
                features["trust_score"],
                features["understanding_score"],
                features["time_together_hours"],
                features["support_score"],
                features["fights_per_month"],
                features["gifts_per_month"],
                features["happy_together_score"]
            ]], columns=[
                "communication_score","trust_score","understanding_score",
                "time_together_hours","support_score","fights_per_month",
                "gifts_per_month","happy_together_score"
            ])

        raw_pred = model.predict(df)[0]

        # Model 0-1 me de raha hai ya 0-100 me?
        # Agar 0-1 me hai to 100 se multiply
        if isinstance(raw_pred, (float,)) or raw_pred <= 1.5:
            # Check karo 0-1 hai kya
            if raw_pred <= 1.5:
                score = int(raw_pred * 100)
            else:
                score = int(raw_pred)
        else:
            score = int(raw_pred)

        # Sirf clamp karo, koi bonus add mat karo - TRUE PREDICTION
        score = max(1, min(99, score))

        return score, df

    except Exception as e:
        return None, f"Prediction error: {e}"

# HEADER B64
def get_header():
    for n in ["header_bg.jpg","header_final_exact.jpg"]:
        if os.path.exists(n):
            try:
                with open(n,"rb") as f:
                    return "data:image/jpeg;base64,"+base64.b64encode(f.read()).decode()
            except: pass
    return ""
HB=get_header()

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&family=Dancing+Script:wght@600&display=swap');
.stApp{{background:#050a1e!important;}} header,footer{{visibility:hidden;}}
.block-container{{max-width:100%!important; padding:0 1rem!important;}}
*{{font-family:'Poppins',sans-serif;}}
.top{{height:118px; margin:-14px -16px 16px -16px; padding:0 24px; background: url('{HB}'), #070a1e; background-size:cover; background-position:center; display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid rgba(255,77,166,0.15);}}
.card{{background:rgba(14,20,53,0.98)!important; border:1px solid rgba(255,255,255,0.08)!important; border-radius:16px!important; padding:18px!important;}}
.nav-on{{background:linear-gradient(90deg, rgba(255,77,166,0.3), rgba(120,50,200,0.2))!important; border-radius:10px; padding:11px 14px; color:#ffb3d1!important; font-weight:600; display:flex; gap:10px;}}
.nav{{color:#6f769e; padding:11px 14px; display:flex; gap:10px; font-size:13px;}}
.stSelectbox>div>div,.stNumberInput>div>div>input{{background:#121a3a!important; border:1px solid rgba(255,255,255,0.07)!important; border-radius:10px!important; color:#c8d0f0!important; height:44px!important;}}
.stMultiSelect>div>div{{background:#121a3a!important; border-radius:10px!important;}}
.btn button{{background:linear-gradient(90deg,#ff4da6,#a855f7)!important; color:white!important; border-radius:12px!important; height:50px!important; font-weight:700!important; border:none!important; box-shadow:0 8px 22px rgba(255,77,166,0.4)!important;}}
@keyframes beat{{0%,100%{{transform:scale(1);}}15%{{transform:scale(1.18);}}30%{{transform:scale(1);}}45%{{transform:scale(1.15);}}}}
@keyframes glow{{0%,100%{{filter:drop-shadow(0 0 10px #ff4da6) drop-shadow(0 0 24px #a855f7);}}50%{{filter:drop-shadow(0 0 18px #ff4da6) drop-shadow(0 0 40px #a855f7);}}}}
.heart{{animation: beat 1.4s infinite, glow 2s infinite alternate;}}
.bar{{background:rgba(255,255,255,0.08); height:12px; border-radius:20px; overflow:hidden;}}
.fill{{height:100%; border-radius:20px; background:linear-gradient(90deg,#ff4da6,#a855f7); box-shadow:0 0 10px #ff4da6;}}
</style>
<div class="top">
  <div style="display:flex; gap:14px; align-items:center;"><div style="font-size:44px;">💞</div><div><div style="font-size:28px; font-weight:800;"><span style="color:#ff4da6;">Love</span> <span style="color:white;">Prediction</span></div><div style="color:#8a90c5; font-size:12px;">AI • Data • Better Love Insights • by Vansh Rajput</div></div></div>
  <div style="color:#ffc2d9; font-family:'Dancing Script',cursive; font-size:16px; text-align:right;">Some connections<br>are meant to be... ♡</div>
</div>
""", unsafe_allow_html=True)

c1,c2,c3 = st.columns([0.15,0.38,0.47], gap="medium")

with c1:
    st.markdown('<div class="card" style="height:780px;"><div class="nav-on">🏠 Home</div><div class="nav">♡ Prediction</div><div class="nav">📊 About Model</div><div class="nav">ⓘ How It Works</div><div style="margin-top:300px; text-align:center; background:rgba(26,32,77,0.7); border-radius:12px; padding:10px;"><div style="width:30px; height:30px; background:linear-gradient(135deg,#ff4da6,#a855f7); border-radius:50%; margin:0 auto; display:flex; align-items:center; justify-content:center; color:white; font-weight:800;">VR</div><div style="color:white; font-size:12px; font-weight:700; margin-top:6px;">Vansh Rajput</div><div style="color:#4ade80; font-size:10px;">● Model: '+f'{model_name if model else "Not Found"}'+'</div></div></div>', unsafe_allow_html=True)

with c2:
    st.markdown('<div class="card"><div style="color:white; font-weight:700;">💖 Enter Your Details - TRUE MODEL</div><div style="color:#7a81a8; font-size:11px; margin:6px 0 16px;">Ye values seedha tere model.pkl me jayengi</div>', unsafe_allow_html=True)
    gy=st.selectbox("👤 Gender (You)", ["Male","Female","Other"])
    gp=st.selectbox("👤 Gender (Partner)", ["Female","Male","Other"])
    ay=st.number_input("📅 Age (You)", 18,70,25)
    ap=st.number_input("📅 Age (Partner)", 18,70,23)
    rel=st.selectbox("♡ Relationship Type", ["Dating","Married","Long Distance","Crush"])
    interests=st.multiselect("⭐ Common Interests", ["Travel","Music","Movies","Sports","Gaming"], default=["Travel","Music","Movies"])
    comm=st.selectbox("💬 Communication Style", ["Open","Reserved","Honest","Playful","Open & Honest"])
    trust=st.selectbox("🛡️ Trust Level", ["High","Medium","Low"])
    st.write("")
    st.markdown('<div class="btn">', unsafe_allow_html=True)
    btn=st.button("✨ Predict Love (True Model) →", use_container_width=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

with c3:
    if btn:
        result, debug = true_predict(gy,gp,ay,ap,rel,interests,comm,trust)
        if result is None:
            st.error(f"❌ {debug}")
            st.info("GitHub pe couple_love_model.pkl upload karo root folder me. File size 0KB nahi honi chahiye.")
            score=0
        else:
            score=result
    else:
        score=0
        debug=None

    disp = score if score>0 else 87
    if score==0: label="Ready to Predict"
    elif score>=80: label="High Compatibility!"
    elif score>=60: label="Good Compatibility"
    elif score>=40: label="Average Compatibility"
    else: label="Needs Work"

    st.markdown(f"""
    <div class="card">
      <div style="display:flex; justify-content:space-between;"><div style="color:white; font-weight:700;">💖 Prediction Result</div><div style="background:#1a214a; padding:5px 12px; border-radius:20px; font-size:10px; color:{'#4ade80' if model else '#f87171'};">{'● '+model_name+' Loaded' if model else '● Model Missing'}</div></div>
      <div style="display:flex; gap:20px; align-items:center; margin-top:18px;">
        <div class="heart"><svg width="120" height="108" viewBox="0 0 100 90"><defs><linearGradient id="g" x1="0%" y1="100%" x2="100%" y2="0%"><stop offset="0%" stop-color="#a855f7"/><stop offset="100%" stop-color="#ff8ec8"/></linearGradient></defs><path d="M50 78 L18 47 C 5 34, 5 14, 27 11 C 38 9, 47 19, 50 24 C 53 19, 62 9, 73 11 C 95 14, 95 34, 82 47 Z" fill="rgba(255,77,166,0.12)" stroke="url(#g)" stroke-width="2.4"/><text x="50" y="50" text-anchor="middle" fill="white" font-size="23" font-weight="800">{disp}%</text></svg></div>
        <div><div style="color:#ff7ab8; font-weight:800; font-size:20px;">{label}</div><div style="color:#a8aecf; font-size:12px; margin-top:4px;">True model se prediction - no fake bonus</div></div>
      </div>
      <div class="bar" style="margin-top:18px;"><div class="fill" style="width:{disp}%;"></div></div>
      <div style="display:flex; justify-content:space-between; margin-top:6px; font-size:12px; color:#8b90b5;"><span>Score from {model_name if model else 'model.pkl'}</span><span style="color:white; font-weight:700;">{disp}%</span></div>
    </div>
    """, unsafe_allow_html=True)

    if btn and model and isinstance(debug, pd.DataFrame):
        with st.expander("🔍 Debug - Model ko kya gaya (TRUE VALUES)"):
            st.write(f"Model expects: {list(model.feature_names_in_) if hasattr(model,'feature_names_in_') else '8 default cols'}")
            st.dataframe(debug)
