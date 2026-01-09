"""
Temperature Converter - Beginner Project 05

Convert temperatures between different units.
"""

import streamlit as st

st.set_page_config(
    page_title="Temperature Converter",
    page_icon="🌡️",
    layout="centered"
)

st.title("🌡️ Temperature Converter")
st.write("Convert temperatures between Celsius, Fahrenheit, and Kelvin")

# Input
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("Enter temperature:", value=0.0, format="%.2f")
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])

with col2:
    st.write("")  # Spacing
    st.write("")  # Spacing
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Convert button
if st.button("Convert", type="primary"):
    result = None
    formula = ""
    
    if from_unit == to_unit:
        result = temperature
        st.info(f"Same unit selected: {temperature:.2f}°{from_unit[0]}")
    else:
        # Celsius conversions
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = celsius_to_fahrenheit(temperature)
            formula = "°F = (°C × 9/5) + 32"
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = celsius_to_kelvin(temperature)
            formula = "K = °C + 273.15"
        
        # Fahrenheit conversions
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = fahrenheit_to_celsius(temperature)
            formula = "°C = (°F - 32) × 5/9"
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = fahrenheit_to_kelvin(temperature)
            formula = "K = (°F - 32) × 5/9 + 273.15"
        
        # Kelvin conversions
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = kelvin_to_celsius(temperature)
            formula = "°C = K - 273.15"
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = kelvin_to_fahrenheit(temperature)
            formula = "°F = (K - 273.15) × 9/5 + 32"
        
        if result is not None:
            unit_symbol = "°" if to_unit != "Kelvin" else ""
            st.success(f"### {temperature:.2f}°{from_unit[0]} = {result:.2f}{unit_symbol}{to_unit[0]}")
            st.info(f"**Formula**: {formula}")

# Reference table
with st.expander("📖 Reference Table"):
    st.write("**Common Temperature Conversions:**")
    st.write("- Water freezes: 0°C = 32°F = 273.15K")
    st.write("- Water boils: 100°C = 212°F = 373.15K")
    st.write("- Room temperature: 20°C = 68°F = 293.15K")
    st.write("- Body temperature: 37°C = 98.6°F = 310.15K")

st.divider()
st.caption("Built with Streamlit 🎈")
