"""
Step 2: Adding Unit Selection with Selectbox
Learning objective: Add dropdowns to select temperature units
"""

import streamlit as st

st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin")

temperature = st.number_input("Enter temperature:", value=0.0, format="%.2f")

# Add unit selection dropdowns
from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])

st.write(f"Converting {temperature} from {from_unit} to {to_unit}")
