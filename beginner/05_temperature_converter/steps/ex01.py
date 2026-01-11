"""
Step 1: Basic Setup with Input Fields
Learning objective: Create input fields for temperature conversion
"""

import streamlit as st

st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin")

# Simple temperature input
temperature = st.number_input("Enter temperature:", value=0.0, format="%.2f")

# Display what was entered
st.write(f"You entered: {temperature}")
