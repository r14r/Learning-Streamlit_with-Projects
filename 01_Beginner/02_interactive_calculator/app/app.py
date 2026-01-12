"""
Interactive Calculator - Beginner Project 02

A simple calculator that performs basic arithmetic operations.
"""

import streamlit as st

st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Interactive Calculator")
st.write("Perform basic arithmetic operations with ease!")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Operation selection
operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Calculate button
if st.button("Calculate", type="primary"):
    result = None
    symbol = ""
    
    if operation == "Addition (+)":
        result = num1 + num2
        symbol = "+"
    elif operation == "Subtraction (-)":
        result = num1 - num2
        symbol = "-"
    elif operation == "Multiplication (×)":
        result = num1 * num2
        symbol = "×"
    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("⚠️ Cannot divide by zero!")
        else:
            result = num1 / num2
            symbol = "÷"
    
    if result is not None:
        st.success(f"**Result**: {num1} {symbol} {num2} = **{result:.2f}**")
        
        # Show additional info
        with st.expander("ℹ️ Calculation Details"):
            st.write(f"- First Number: {num1}")
            st.write(f"- Second Number: {num2}")
            st.write(f"- Operation: {operation}")
            st.write(f"- Result: {result:.2f}")

st.divider()
st.caption("Built with Streamlit 🎈")
