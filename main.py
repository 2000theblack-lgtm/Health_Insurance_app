import streamlit as st
from prediction_helper import predict

# Page config
st.set_page_config(page_title="Health Insurance Estimator", layout="centered")

# Custom CSS for modern look
st.markdown("""
    <style>
            
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            background-color: #f5f7fa;
        }

        .main-card {
            background-color: #ffffff;
            padding: 2rem 3rem;
            border-radius: 12px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.05);
            max-width: 800px;
            margin: auto;
        }

        .section-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #333333;
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .result-box {
            background-color: #e0f2f1;
            padding: 1.5rem;
            border-radius: 10px;
            text-align: center;
            font-size: 22px;
            font-weight: 600;
            color: #00695c;
            margin-top: 2rem;
        }

        .predict-btn {
            background-color: #00897b;
            color: white;
            padding: 0.6rem 1.2rem;
            border-radius: 8px;
            border: none;
            font-size: 1rem;
            font-weight: 600;
            margin-top: 1rem;
        }

        .predict-btn:hover {
            background-color: #00796b;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="section-title">🏥 Health Insurance Cost Estimator</div>', unsafe_allow_html=True)

# Main container
with st.container():
    st.markdown('<div class="main-card">', unsafe_allow_html=True)

    # Input columns
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=18, max_value=100, value=30)
        income_lakhs = st.number_input("💰 Income (in Lakhs)", min_value=0, max_value=200, value=10)
        number_of_dependants = st.number_input("👨‍👩‍👧 Dependants", min_value=0, max_value=20, step=1)
        genetical_risk = st.selectbox("🧬 Genetical Risk (0-5)", options=list(range(6)))
        bmi_category = st.selectbox("⚖️ BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])

    with col2:
        gender = st.selectbox("⚧️ Gender", ['Male', 'Female'])
        marital_status = st.selectbox("💍 Marital Status", ['Married', 'Unmarried'])
        smoking_status = st.selectbox("🚬 Smoking Status", ['No Smoking', 'Regular', 'Occasional'])
        employment_status = st.selectbox("💼 Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])
        region = st.selectbox("🌍 Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])

    insurance_plan = st.selectbox("📜 Insurance Plan", ['Bronze', 'Silver', 'Gold'])
    medical_history = st.selectbox("🏥 Medical History", [
        'No Disease', 'Diabetes', 'High Blood Pressure', 'Diabetes & High BP',
        'Thyroid', 'Heart Disease', 'BP & Heart Disease',
        'Diabetes & Thyroid', 'Diabetes & Heart Disease'
    ])

    # Input dictionary
    input_dict = {
        'Age': age,
        'Number of Dependants': number_of_dependants,
        'Income in Lakhs': income_lakhs,
        'Genetical Risk': genetical_risk,
        'Insurance Plan': insurance_plan,
        'Employment Status': employment_status,
        'Gender': gender,
        'Marital Status': marital_status,
        'BMI Category': bmi_category,
        'Smoking Status': smoking_status,
        'Region': region,
        'Medical History': medical_history
    }

    # Prediction
    if st.button("🔍 Predict Insurance Cost", key="predict-btn"):
        prediction = predict(input_dict)
        try:
            formatted = f"{float(prediction):,.2f} ₹"
        except:
            formatted = str(prediction)

        st.markdown(f'<div class="result-box">💰 Estimated Insurance Cost: {formatted}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
