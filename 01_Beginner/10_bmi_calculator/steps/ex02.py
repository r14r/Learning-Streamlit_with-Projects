"""
Step 2: Calculating BMI
Learning objective: Implement BMI calculation formula
"""

import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)

st.title("⚕️ BMI Calculator")
st.write("Calculate your Body Mass Index and understand your health status")

weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)

# Calculate BMI
# Formula: BMI = weight (kg) / height (m)²
# Convert height from cm to meters
height_m = height / 100
bmi = weight / (height_m ** 2)

# Display BMI
if st.button("Calculate BMI", type="primary"):
    st.write(f"### Your BMI: {bmi:.1f}")
