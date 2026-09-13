import streamlit as st
import pandas as pd
import pickle


st.set_page_config(
    page_title="Couple Love Prediction",
    page_icon="❤️",
    layout="wide"
)


st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #fff0f5, #f8f0ff);
    }

    .title {
        text-align: center;
        font-size: 45px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #666;
        margin-bottom: 30px;
    }

    .card {
        padding: 25px;
        border-radius: 20px;
        background-color: white;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .result {
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        background-color: white;
        box-shadow: 0px 5px 20px rgba(0,0,0,0.10);
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as file:
        return pickle.load(file)

model = load_model()


st.markdown(
    '<div class="title">❤️ Couple Love Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict relationship happiness using important relationship factors</div>',
    unsafe_allow_html=True
)


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("💑 Enter Relationship Details")

col1, col2 = st.columns(2)

with col1:

    communication = st.slider(
        "💬 Communication Score",
        min_value=1,
        max_value=10,
        value=7
    )

    trust = st.slider(
        "🤝 Trust Score",
        min_value=1,
        max_value=10,
        value=7
    )

    understanding = st.slider(
        "🧠 Understanding Score",
        min_value=1,
        max_value=10,
        value=7
    )

    time_together = st.slider(
        "⏰ Time Together (Hours)",
        min_value=0,
        max_value=24,
        value=5
    )

with col2:

    support = st.slider(
        "❤️ Support Score",
        min_value=1,
        max_value=10,
        value=7
    )

    fights = st.slider(
        "⚡ Fights per Month",
        min_value=0,
        max_value=30,
        value=3
    )

    gifts = st.slider(
        "🎁 Gifts per Month",
        min_value=0,
        max_value=20,
        value=2
    )

    happy_together = st.slider(
        "😊 Happy Together Score",
        min_value=1,
        max_value=10,
        value=8
    )

st.markdown('</div>', unsafe_allow_html=True)


if st.button("❤️ Predict Love Compatibility", use_container_width=True):

 

    input_data = pd.DataFrame({
        "Communication Score": [communication],
        "Trust Score": [trust],
        "Understanding Score": [understanding],
        "Time Together Hours": [time_together],
        "Support Score": [support],
        "Fights per Month": [fights],
        "Gifts per Month": [gifts],
        "Happy Together Score": [happy_together]
    })

    try:

        prediction = model.predict(input_data)[0]

    
        if hasattr(model, "predict_proba"):

            probability = model.predict_proba(input_data)[0]
            confidence = max(probability) * 100

        else:
            confidence = None


        st.markdown('<div class="result">', unsafe_allow_html=True)

        if prediction == 1:

            st.success("❤️ Strong Relationship / Happy Together")

            if confidence is not None:
                st.metric(
                    "Prediction Confidence",
                    f"{confidence:.2f}%"
                )

            st.balloons()

        else:

            st.warning("💔 Relationship May Need Improvement")

            if confidence is not None:
                st.metric(
                    "Prediction Confidence",
                    f"{confidence:.2f}%"
                )

        st.markdown('</div>', unsafe_allow_html=True)

    except Exception as e:

        st.error("Prediction error occurred.")

        st.write(e)


st.markdown("---")

st.caption(
    "⚠️ This is an ML-based prediction project for educational/demo purposes."
)
