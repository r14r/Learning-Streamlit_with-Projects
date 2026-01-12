"""
Step 1: Basic Setup with Weight and Height Inputs
Learning objective: Create basic BMI calculator interface
"""

import streamlit as st

st.set_page_config(
    page_title="BMI Calculator",
    page_icon="⚕️",
    layout="centered"
)

st.title("⚕️ BMI Calculator")
st.write("Calculate your Body Mass Index and understand your health status")

# Simple inputs for weight and height
weight = st.number_input("Weight (kg)", min_value=1.0, max_value=300.0, value=70.0, step=0.1)
height = st.number_input("Height (cm)", min_value=50.0, max_value=300.0, value=170.0, step=0.1)

st.write(f"Weight: {weight} kg")
st.write(f"Height: {height} cm")
