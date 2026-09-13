import streamlit as st
import pandas as pd
import joblib, os

st.set_page_config(page_title="Love Prediction - True Model", page_icon="💖", layout="wide")

@st.cache_resource
def load_model():
    path = "couple_love_model.pkl"
    if os.path.exists(path):
        m = joblib.load(path)
        # Check karo 8 features ka naam kya hai pkl me
        if hasattr(m, "feature_names_in_"):
            st.sidebar.success(f"Model expects: {list(m.feature_names_in_)}")
        return m
    return None

model = load_model()

# ---- UI (Teri screenshot jaisa hi dark theme) ----
st.markdown("""
<style>
.stApp{background:#070a1e!important; color:white;}
header,footer{visibility:hidden;}
.card{background:#10173a; border:1px solid #ffffff12; border-radius:18px; padding:20px; margin-bottom:15px;}
</style>
""", unsafe_allow_html=True)

st.markdown("## 💖 Enter Your Details - True model prediction")

if model is None:
    st.error("couple_love_model.pkl nahi mila! Root me daal de.")
    st.stop()

# ---- 8 EXACT INPUTS FROM YOUR PKL ----
c1,c2 = st.columns(2)
with c1:
    comm = st.slider("Communication Score", 0.0, 10.0, 7.2)
    trust = st.slider("Trust Score", 0.0, 10.0, 8.5)
    und = st.slider("Understanding Score", 0.0, 10.0, 6.8)
    time = st.slider("Time Together Hours", 0.0, 168.0, 32.0)
with c2:
    supp = st.slider("Support Score", 0.0, 10.0, 9.0)
    fight = st.slider("Fights Per Month", 0.0, 20.0, 2.0)
    gift = st.slider("Gifts Per Month", 0.0, 20.0, 5.0)
    happy = st.slider("Happy Together Score", 0.0, 10.0, 8.1)

if st.button("✨ Run Prediction →", use_container_width=True, type="primary"):
    # EXACT 8 columns in same order as pkl trained
    data = {
        "communication_score": comm,
        "trust_score": trust,
        "understanding_score": und,
        "time_together_hours": time,
        "support_score": supp,
        "fights_per_month": fight,
        "gifts_per_month": gift,
        "happy_together_score": happy
    }
    df = pd.DataFrame([data])

    # Agar model ne order alag save kiya ho to auto-fix
    if hasattr(model, "feature_names_in_"):
        df = df[list(model.feature_names_in_)]

    raw = model.predict(df)[0]
    score = int(raw*100) if raw <= 1.5 else int(raw)
    score = max(1, min(99, score))

    st.success(f"### Predicted Compatibility: {score}%")
    st.progress(score)
    if score >= 75:
        st.markdown("### 🔥 High Compatibility!")
    elif score >= 50:
        st.markdown("### 💫 Good Compatibility")
    else:
        st.markdown("### 💭 Needs Work")

    st.info(f"True prediction from your pkl - Input: {data}")
