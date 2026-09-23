import os
import joblib
import numpy as np
import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------
# Custom CSS Styling
# ----------------------------
st.markdown("""
    <style>
        .main {
            background-color: #f9fafb;
        }
        .stApp {
            font-family: 'Segoe UI', sans-serif;
        }
        h1 {
            color: #b91c1c;
            font-weight: 800;
        }
        .subtitle {
            color: #4b5563;
            font-size: 1.05rem;
            margin-bottom: 1.5rem;
        }
        div.stButton > button {
            background-color: #dc2626;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            padding: 0.6rem 1.5rem;
            border: none;
            width: 100%;
            transition: 0.2s;
        }
        div.stButton > button:hover {
            background-color: #991b1b;
            color: white;
        }
        .result-box {
            padding: 1.2rem;
            border-radius: 12px;
            font-size: 1.1rem;
            font-weight: 600;
            text-align: center;
            margin-top: 1rem;
        }
        .risk {
            background-color: #fee2e2;
            color: #991b1b;
            border: 1px solid #fca5a5;
        }
        .safe {
            background-color: #dcfce7;
            color: #166534;
            border: 1px solid #86efac;
        }
        section[data-testid="stSidebar"] {
            background-color: #111827;
        }
        section[data-testid="stSidebar"] * {
            color: #f3f4f6 !important;
        }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Load Model
# ----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'heart_disease_model.pkl')
model = joblib.load(model_path)

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    st.markdown("## ❤️ About")
    st.write(
        "This tool uses a Machine Learning model trained on clinical data "
        "to estimate the likelihood of heart disease based on patient health metrics."
    )
    st.markdown("---")
    st.markdown("### How to use")
    st.write(
        "1. Fill in the patient details.\n"
        "2. Click **Predict**.\n"
        "3. View the result instantly."
    )
    st.markdown("---")
    st.caption("⚠️ For educational purposes only. Not a substitute for professional medical advice.")

# ----------------------------
# Header
# ----------------------------
st.title("❤️ Heart Disease Risk Predictor")
st.markdown('<p class="subtitle">Enter the patient\'s health information below to get an instant ML-based prediction.</p>', unsafe_allow_html=True)
st.markdown("---")

# ----------------------------
# Input Form
# ----------------------------
with st.form("prediction_form"):
    st.subheader("🧍 Patient Information")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", min_value=1, max_value=120, value=45, step=1)
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=220, value=120, step=1)
        thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150, step=1)
        slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[0, 1, 2],
                              format_func=lambda x: {0: "Upsloping", 1: "Flat", 2: "Downsloping"}[x])

    with col2:
        sex = st.selectbox("Sex", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")
        chol = st.number_input("Serum Cholesterol (mg/dl)", min_value=100, max_value=600, value=200, step=1)
        exang = st.selectbox("Exercise Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        ca = st.selectbox("Number of Major Vessels Colored (0–3)", options=[0, 1, 2, 3])

    with col3:
        cp = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3],
                           format_func=lambda x: {0: "Typical Angina", 1: "Atypical Angina",
                                                   2: "Non-anginal Pain", 3: "Asymptomatic"}[x])
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
        restecg = st.selectbox("Resting ECG Results", options=[0, 1, 2],
                                format_func=lambda x: {0: "Normal", 1: "ST-T Abnormality", 2: "LV Hypertrophy"}[x])
        thal = st.selectbox("Thalassemia", options=[0, 1, 2],
                             format_func=lambda x: {0: "Normal", 1: "Fixed Defect", 2: "Reversible Defect"}[x])

    oldpeak = st.slider("ST Depression Induced by Exercise", min_value=0.0, max_value=6.0, value=1.0, step=0.1)

    st.markdown("")
    submitted = st.form_submit_button("🔍 Predict")

# ----------------------------
# Prediction
# ----------------------------
if submitted:
    user_input = [age, sex, cp, trestbps, chol, fbs, restecg,
                  thalach, exang, oldpeak, slope, ca, thal]

    prediction = model.predict([user_input])[0]

    try:
        proba = model.predict_proba([user_input])[0][int(prediction)] * 100
    except AttributeError:
        proba = None

    if prediction == 1:
        confidence_text = f" (confidence: {proba:.1f}%)" if proba else ""
        st.markdown(
            f'<div class="result-box risk">⚠️ High Risk: The patient is likely to have heart disease{confidence_text}.</div>',
            unsafe_allow_html=True
        )
    else:
        confidence_text = f" (confidence: {proba:.1f}%)" if proba else ""
        st.markdown(
            f'<div class="result-box safe">✅ Low Risk: The patient is unlikely to have heart disease{confidence_text}.</div>',
            unsafe_allow_html=True
        )