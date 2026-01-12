"""
Step 3: Organizing Inputs with Columns
Learning objective: Use columns for better layout of input fields
"""

import streamlit as st

st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin")

# Create two columns for better organization
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("Enter temperature:", value=0.0, format="%.2f")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])

with col2:
    # Add spacing to align with left column
    st.write("")
    st.write("")
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])

st.write(f"Converting {temperature} from {from_unit} to {to_unit}")
