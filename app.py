import streamlit as st
import pandas as pd
import joblib
import random

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Love Prediction AI",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# LOAD MODEL
# =========================================================
@st.cache_resource
def load_model():
    try:
        return joblib.load("couple_love_model.pkl")
    except Exception:
        return None

model = load_model()


# =========================================================
# PREMIUM CSS + ANIMATIONS
# =========================================================
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Poppins:wght@300;400;500;600;700;800&display=swap');

/* ---------- GLOBAL ---------- */

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(255, 45, 120, 0.10), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(168, 85, 247, 0.12), transparent 28%),
        radial-gradient(circle at 50% 100%, rgba(255, 45, 120, 0.08), transparent 30%),
        #050816;
    color: white;
}

header, footer, #MainMenu {
    visibility: hidden;
}

.block-container {
    padding: 1rem 3rem 2rem 3rem !important;
    max-width: 1500px !important;
}


/* ---------- FLOATING HEARTS ---------- */

.hearts {
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}

.heart {
    position: absolute;
    bottom: -100px;
    color: #ff4da6;
    font-size: 22px;
    opacity: 0;
    animation: floatHeart linear infinite;
    filter: drop-shadow(0 0 12px rgba(255, 77, 166, 0.8));
}

.h1 { left: 5%; animation-duration: 12s; animation-delay: 1s; }
.h2 { left: 15%; animation-duration: 16s; animation-delay: 4s; font-size: 16px; }
.h3 { left: 27%; animation-duration: 13s; animation-delay: 2s; }
.h4 { left: 39%; animation-duration: 18s; animation-delay: 7s; font-size: 18px; }
.h5 { left: 52%; animation-duration: 14s; animation-delay: 3s; }
.h6 { left: 64%; animation-duration: 17s; animation-delay: 6s; font-size: 17px; }
.h7 { left: 76%; animation-duration: 13s; animation-delay: 5s; }
.h8 { left: 88%; animation-duration: 19s; animation-delay: 1s; font-size: 18px; }

@keyframes floatHeart {
    0% {
        transform: translateY(0) scale(0.5) rotate(0deg);
        opacity: 0;
    }

    15% {
        opacity: 0.7;
    }

    50% {
        transform: translateY(-50vh) scale(1) rotate(15deg);
        opacity: 0.45;
    }

    80% {
        opacity: 0.2;
    }

    100% {
        transform: translateY(-115vh) scale(1.3) rotate(-15deg);
        opacity: 0;
    }
}


/* ---------- TOP NAV ---------- */

.topbar {
    position: relative;
    z-index: 2;
    height: 105px;
    border-radius: 25px;
    padding: 0 30px;

    display: flex;
    align-items: center;
    justify-content: space-between;

    background:
        linear-gradient(
            120deg,
            rgba(255, 45, 120, 0.12),
            rgba(10, 15, 40, 0.92),
            rgba(168, 85, 247, 0.12)
        );

    border: 1px solid rgba(255,255,255,0.09);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.45),
        inset 0 0 40px rgba(255,255,255,0.02);

    overflow: hidden;
}

.topbar::before {
    content: "";
    position: absolute;
    width: 250px;
    height: 250px;
    background: #ff2d78;
    filter: blur(100px);
    opacity: 0.10;
    right: 20%;
    top: -150px;
}

.brand {
    display: flex;
    align-items: center;
    gap: 16px;
    position: relative;
    z-index: 2;
}

.brand-heart {
    font-size: 48px;
    animation: heartbeat 1.4s infinite;
    filter: drop-shadow(0 0 18px #ff2d78);
}

@keyframes heartbeat {
    0%, 100% {
        transform: scale(1);
    }

    15% {
        transform: scale(1.18);
    }

    30% {
        transform: scale(1);
    }

    45% {
        transform: scale(1.12);
    }

    60% {
        transform: scale(1);
    }
}

.title {
    font-size: 29px;
    font-weight: 800;
    letter-spacing: -1px;
}

.title span {
    color: #ff4da6;
    text-shadow: 0 0 20px rgba(255,77,166,0.4);
}

.subtitle {
    color: #9298bd;
    font-size: 12px;
    margin-top: 3px;
}

.quote {
    color: #e8a7c8;
    font-family: 'DM Serif Display', serif;
    font-size: 18px;
    text-align: right;
    line-height: 1.4;
}


/* ---------- MAIN GRID ---------- */

.section-title {
    position: relative;
    z-index: 2;
    color: white;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 12px;
}


/* ---------- CARDS ---------- */

.card {
    position: relative;
    z-index: 2;

    background:
        linear-gradient(
            145deg,
            rgba(22, 29, 65, 0.92),
            rgba(10, 14, 35, 0.92)
        );

    border: 1px solid rgba(255,255,255,0.075);
    border-radius: 22px;

    padding: 24px;

    box-shadow:
        0 20px 60px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.025);

    backdrop-filter: blur(20px);
}

.card:hover {
    border-color: rgba(255,77,166,0.25);
    box-shadow:
        0 25px 70px rgba(0,0,0,0.45),
        0 0 35px rgba(255,77,166,0.07);
}

.card-heading {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 17px;
    font-weight: 700;
    color: white;
}

.card-description {
    color: #858cae;
    font-size: 11.5px;
    margin-top: 5px;
    margin-bottom: 18px;
}


/* ---------- INPUTS ---------- */

.stSelectbox > div > div,
.stNumberInput > div > div > input,
.stMultiSelect > div > div {
    background: #111831 !important;
    color: #e7eaff !important;

    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 13px !important;

    min-height: 45px !important;
}

.stSelectbox label,
.stNumberInput label,
.stMultiSelect label {
    color: #cbd0ea !important;
    font-size: 12px !important;
    font-weight: 500 !important;
}

.stMultiSelect span {
    background: #352348 !important;
    color: white !important;
    border-radius: 8px !important;
}


/* ---------- BUTTON ---------- */

.predict-btn button {
    height: 55px !important;

    border-radius: 15px !important;
    border: 0 !important;

    background:
        linear-gradient(
            100deg,
            #ff2d78,
            #ff4da6,
            #a855f7
        ) !important;

    color: white !important;

    font-size: 15px !important;
    font-weight: 700 !important;

    box-shadow:
        0 10px 30px rgba(255,45,120,0.30),
        0 0 25px rgba(168,85,247,0.15) !important;

    transition: all 0.3s ease !important;
}

.predict-btn button:hover {
    transform: translateY(-3px) scale(1.015);
    box-shadow:
        0 15px 40px rgba(255,45,120,0.45),
        0 0 35px rgba(168,85,247,0.25) !important;
}


/* ---------- RESULT HEART ---------- */

.result-heart-wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 15px 0 25px;
}

.result-heart {
    width: 190px;
    height: 175px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 31px;
    font-weight: 800;

    position: relative;

    color: white;

    background:
        radial-gradient(
            circle,
            rgba(255,90,165,0.95) 0%,
            rgba(255,45,120,0.80) 35%,
            rgba(168,85,247,0.55) 62%,
            transparent 73%
        );

    clip-path: polygon(
        50% 100%,
        8% 55%,
        8% 32%,
        18% 15%,
        35% 14%,
        50% 30%,
        65% 14%,
        82% 15%,
        92% 32%,
        92% 55%
    );

    filter:
        drop-shadow(0 0 15px rgba(255,45,120,0.85))
        drop-shadow(0 0 35px rgba(168,85,247,0.55));

    animation: bigHeartbeat 1.7s infinite;
}

@keyframes bigHeartbeat {
    0%, 100% {
        transform: scale(1);
    }

    10% {
        transform: scale(1.08);
    }

    20% {
        transform: scale(1);
    }

    30% {
        transform: scale(1.05);
    }

    40% {
        transform: scale(1);
    }
}


/* ---------- SCORE ---------- */

.score-label {
    text-align: center;
    color: #ff75b4;
    font-weight: 700;
    font-size: 21px;
}

.score-description {
    text-align: center;
    color: #8e95b7;
    font-size: 12px;
    line-height: 1.6;
    max-width: 450px;
    margin: 8px auto;
}

.progress-container {
    margin-top: 20px;
}

.progress-bg {
    height: 11px;
    width: 100%;
    border-radius: 30px;
    background: #1b2342;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    border-radius: 30px;

    background:
        linear-gradient(
            90deg,
            #ff2d78,
            #ff4da6,
            #a855f7
        );

    box-shadow: 0 0 15px rgba(255,77,166,0.6);

    animation: progressAnimation 1.5s ease-out;
}

@keyframes progressAnimation {
    from {
        width: 0%;
    }
}


/* ---------- INSIGHTS ---------- */

.insights {
    margin-top: 22px;
    padding: 18px;

    background: rgba(15,21,48,0.8);
    border-radius: 17px;

    border: 1px solid rgba(255,255,255,0.055);
}

.insights-title {
    font-size: 13px;
    font-weight: 700;
    margin-bottom: 15px;
}

.insight-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 10px;
}

.insight {
    text-align: center;
    padding: 8px 3px;
}

.insight-icon {
    font-size: 22px;
    margin-bottom: 4px;
}

.insight-name {
    color: #8188aa;
    font-size: 9.5px;
}

.insight-value {
    color: white;
    font-size: 12px;
    font-weight: 700;
    margin-top: 3px;
}


/* ---------- WHY CARD ---------- */

.why-card {
    margin-top: 14px;
    padding: 16px;

    border-radius: 17px;

    background:
        linear-gradient(
            120deg,
            rgba(255,45,120,0.07),
            rgba(168,85,247,0.07)
        );

    border: 1px solid rgba(255,255,255,0.055);
}

.why-title {
    font-size: 13px;
    font-weight: 700;
    color: white;
}

.why-text {
    color: #8d94b5;
    font-size: 11px;
    line-height: 1.7;
    margin-top: 7px;
}


/* ---------- SIDE NAV ---------- */

.side-menu {
    min-height: 650px;
}

.side-item {
    color: #858cac;
    padding: 13px 15px;
    border-radius: 12px;
    margin-bottom: 5px;
    font-size: 12px;
}

.side-active {
    color: white;
    padding: 13px 15px;
    border-radius: 12px;
    margin-bottom: 7px;

    background:
        linear-gradient(
            90deg,
            rgba(255,45,120,0.22),
            rgba(168,85,247,0.10)
        );

    border: 1px solid rgba(255,77,166,0.20);

    font-size: 12px;
    font-weight: 600;

    box-shadow: 0 5px 20px rgba(255,45,120,0.08);
}

.side-bottom {
    margin-top: 280px;
    text-align: center;
}

.side-heart {
    font-size: 30px;
    animation: heartbeat 1.5s infinite;
}


/* ---------- BADGE ---------- */

.ai-badge {
    display: inline-block;
    padding: 6px 12px;

    border-radius: 30px;

    background: rgba(255,255,255,0.045);
    border: 1px solid rgba(255,255,255,0.08);

    color: #b9bfdc;
    font-size: 10px;
}


/* ---------- CELEBRATION ---------- */

.celebrate {
    text-align: center;
    margin-top: 10px;
    font-size: 25px;

    animation: celebrate 1.5s ease infinite;
}

@keyframes celebrate {
    0%,100% {
        transform: translateY(0);
    }

    50% {
        transform: translateY(-7px);
    }
}


/* ---------- MOBILE ---------- */

@media (max-width: 900px) {

    .block-container {
        padding: 0.7rem 1rem !important;
    }

    .topbar {
        height: auto;
        padding: 20px;
    }

    .quote {
        display: none;
    }

    .title {
        font-size: 23px;
    }

    .insight-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

</style>


<!-- FLOATING HEARTS -->
<div class="hearts">
    <div class="heart h1">♡</div>
    <div class="heart h2">♥</div>
    <div class="heart h3">♡</div>
    <div class="heart h4">💗</div>
    <div class="heart h5">♥</div>
    <div class="heart h6">♡</div>
    <div class="heart h7">💖</div>
    <div class="heart h8">♥</div>
</div>

""", unsafe_allow_html=True)


# =========================================================
# TOP BAR
# =========================================================
st.markdown("""
<div class="topbar">

    <div class="brand">

        <div class="brand-heart">💖</div>

        <div>
            <div class="title">
                <span>Love</span> Prediction AI
            </div>

            <div class="subtitle">
                AI • Compatibility • Relationship Insights
            </div>
        </div>

    </div>

    <div class="quote">
        Some connections<br>
        are simply meant to be... ♡
    </div>

</div>
""", unsafe_allow_html=True)

st.write("")


# =========================================================
# THREE COLUMN LAYOUT
# =========================================================
col_nav, col_form, col_result = st.columns(
    [0.18, 0.38, 0.44],
    gap="large"
)


# =========================================================
# LEFT NAVIGATION
# =========================================================
with col_nav:

    st.markdown("""
    <div class="card side-menu">

        <div class="side-active">
            🏠 &nbsp; Home
        </div>

        <div class="side-item">
            💗 &nbsp; Love Prediction
        </div>

        <div class="side-item">
            📊 &nbsp; Compatibility
        </div>

        <div class="side-item">
            🤖 &nbsp; AI Model
        </div>

        <div class="side-item">
            ℹ️ &nbsp; How It Works
        </div>

        <div class="side-bottom">

            <div class="side-heart">💗</div>

            <div style="
                color:#9b7190;
                font-family:'DM Serif Display',serif;
                font-size:14px;
                margin-top:8px;
            ">
                Love isn't just a feeling...
            </div>

            <div style="
                color:white;
                font-family:'DM Serif Display',serif;
                font-size:13px;
                margin-top:3px;
            ">
                It's a connection ♡
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


# =========================================================
# FORM
# =========================================================
with col_form:

    st.markdown("""
    <div class="card">

        <div class="card-heading">
            💕 Enter Your Details
        </div>

        <div class="card-description">
            Tell us a little about your relationship to calculate
            your AI-powered compatibility score.
        </div>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    g_you = st.selectbox(
        "👤 Gender (You)",
        ["Male", "Female", "Other"]
    )

    g_part = st.selectbox(
        "👤 Gender (Partner)",
        ["Female", "Male", "Other"]
    )

    age_you = st.number_input(
        "🎂 Age (You)",
        min_value=18,
        max_value=70,
        value=25
    )

    age_part = st.number_input(
        "🎂 Age (Partner)",
        min_value=18,
        max_value=70,
        value=23
    )

    rel = st.selectbox(
        "💞 Relationship Type",
        [
            "Dating",
            "Married",
            "Crush",
            "Long Distance"
        ]
    )

    interests = st.multiselect(
        "⭐ Common Interests",
        [
            "Travel",
            "Music",
            "Movies",
            "Sports",
            "Food",
            "Gaming"
        ],
        default=["Travel", "Music", "Movies"]
    )

    comm = st.selectbox(
        "💬 Communication Style",
        [
            "Open",
            "Reserved",
            "Honest",
            "Funny"
        ]
    )

    trust = st.selectbox(
        "🛡️ Trust Level",
        [
            "High",
            "Medium",
            "Low"
        ]
    )

    st.write("")

    st.markdown('<div class="predict-btn">', unsafe_allow_html=True)

    predict = st.button(
        "💖  Calculate Love Compatibility",
        use_container_width=True
    )

    st.markdown('</div>', unsafe_allow_html=True)


# =========================================================
# CALCULATE SCORE
# =========================================================

if predict:

    base = 60

    # Communication
    if comm == "Open":
        base += 12

    elif comm == "Honest":
        base += 10

    elif comm == "Funny":
        base += 7

    # Trust
    if trust == "High":
        base += 18

    elif trust == "Medium":
        base += 10

    else:
        base += 2

    # Interests
    base += len(interests) * 3

    # Age compatibility
    if abs(age_you - age_part) <= 3:
        base += 5

    elif abs(age_you - age_part) <= 7:
        base += 2

    # Relationship type
    if rel == "Married":
        base += 4

    elif rel == "Dating":
        base += 2

    # ML MODEL
    if model is not None:

        try:

            df = pd.DataFrame([
                {
                    "communication_score": 8,
                    "trust_score": 9 if trust == "High" else 5,
                    "understanding_score": 8,
                    "time_together_hours": 7,
                    "support_score": 8,
                    "fights_per_month": 1,
                    "gifts_per_month": 3,
                    "happy_together_score": 9
                }
            ])

            model_prediction = float(model.predict(df)[0])

            base = (base + model_prediction) / 2

        except Exception:
            pass

    score = int(max(25, min(97, base)))

else:

    score = 87


# =========================================================
# RESULT PANEL
# =========================================================
with col_result:

    st.markdown("""
    <div class="card">

        <div style="
            display:flex;
            justify-content:space-between;
            align-items:center;
        ">

            <div class="card-heading">
                💗 Prediction Result
            </div>

            <div class="ai-badge">
                ✦ AI POWERED
            </div>

        </div>
    """, unsafe_allow_html=True)

    # HEART
    st.markdown(f"""
    <div class="result-heart-wrapper">

        <div class="result-heart">
            {score}%
        </div>

    </div>
    """, unsafe_allow_html=True)


    # MESSAGE
    if score >= 80:

        result_title = "High Compatibility! 💖"

        result_text = (
            "You and your partner show a strong compatibility pattern. "
            "Your communication, trust and shared interests create a "
            "beautiful foundation for a lasting connection."
        )

    elif score >= 60:

        result_title = "Good Compatibility! 💕"

        result_text = (
            "There is a positive connection between you both. "
            "With better communication and mutual understanding, "
            "your relationship can become even stronger."
        )

    else:

        result_title = "Room to Grow 💜"

        result_text = (
            "Every relationship is unique. More communication, "
            "trust and shared experiences can help strengthen "
            "your connection."
        )


    st.markdown(f"""
    <div class="score-label">
        {result_title}
    </div>

    <div class="score-description">
        {result_text}
    </div>
    """, unsafe_allow_html=True)


    # PROGRESS
    st.markdown(f"""
    <div class="progress-container">

        <div class="progress-bg">

            <div
                class="progress-fill"
                style="width:{score}%"
            ></div>

        </div>

        <div style="
            display:flex;
            justify-content:space-between;
            margin-top:8px;
            font-size:11px;
        ">

            <span style="color:#777f9f;">
                Compatibility Score
            </span>

            <span style="
                color:white;
                font-weight:700;
            ">
                {score}%
            </span>

        </div>

    </div>
    """, unsafe_allow_html=True)


    # INSIGHTS
    communication_value = (
        "Excellent" if comm in ["Open", "Honest"]
        else "Good"
    )

    interest_value = (
        "Excellent" if len(interests) >= 3
        else "Good"
    )

    emotional_value = (
        "Strong" if score >= 75
        else "Growing"
    )

    st.markdown(f"""
    <div class="insights">

        <div class="insights-title">
            ✦ Key Relationship Insights
        </div>

        <div class="insight-grid">

            <div class="insight">
                <div class="insight-icon">💬</div>
                <div class="insight-name">
                    Communication
                </div>
                <div class="insight-value">
                    {communication_value}
                </div>
            </div>


            <div class="insight">
                <div class="insight-icon">⭐</div>
                <div class="insight-name">
                    Shared Interests
                </div>
                <div class="insight-value">
                    {interest_value}
                </div>
            </div>


            <div class="insight">
                <div class="insight-icon">🛡️</div>
                <div class="insight-name">
                    Trust
                </div>
                <div class="insight-value">
                    {trust}
                </div>
            </div>


            <div class="insight">
                <div class="insight-icon">💞</div>
                <div class="insight-name">
                    Emotional Bond
                </div>
                <div class="insight-value">
                    {emotional_value}
                </div>
            </div>

        </div>

    </div>
    """, unsafe_allow_html=True)


    # WHY PREDICTION
    st.markdown(f"""
    <div class="why-card">

        <div class="why-title">
            💡 Why This Prediction?
        </div>

        <div class="why-text">
            Your compatibility score considers relationship factors
            such as communication style, trust level, shared interests,
            age difference and relationship type.
            These signals are combined with the trained ML model
            when available to generate the final compatibility score.
        </div>

    </div>
    """, unsafe_allow_html=True)


    if predict and score >= 80:

        st.markdown("""
        <div class="celebrate">
            💕 ✨ 💖 ✨ 💕
        </div>
        """, unsafe_allow_html=True)


    st.markdown("""
    </div>

    <div style="
        text-align:right;
        color:#666d91;
        font-family:'DM Serif Display',serif;
        font-size:13px;
        margin-top:10px;
    ">
        Good things take time... ♡
    </div>
    """, unsafe_allow_html=True)
