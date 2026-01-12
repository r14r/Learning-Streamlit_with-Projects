"""
Step 3: Adding Unit System Selection
Learning objective: Allow users to choose between metric and imperial units
"""

import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)

st.title("⚕️ BMI Calculator")
st.write("Calculate your Body Mass Index and understand your health status")

# Unit selection using radio buttons (horizontal layout)
unit_system = st.radio("Select unit system:", ["Metric (kg, cm)", "Imperial (lbs, inches)"], horizontal=True)

# Input fields based on unit system
if unit_system == "Metric (kg, cm)":
    weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
    height = st.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)

    # Convert height to meters for calculation
    height_m = height / 100
    bmi = weight / (height_m ** 2)
else:
    weight = st.number_input("Weight (lbs)", min_value=1.0, max_value=700.0, value=154.0, step=0.1)
    height = st.number_input("Height (inches)", min_value=20.0, max_value=120.0, value=67.0, step=0.1)

    # Convert to metric for BMI calculation
    weight_kg = weight * 0.453592  # lbs to kg
    height_m = height * 0.0254     # inches to meters
    bmi = weight_kg / (height_m ** 2)

if st.button("Calculate BMI", type="primary"):
    st.write(f"### Your BMI: {bmi:.1f}")
