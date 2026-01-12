"""
Step 5: Adding Calculate Button with Basic Logic
Learning objective: Use button() and implement calculation logic with if statements
"""

import streamlit as st

st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered"
)

st.title("🧮 Interactive Calculator")
st.write("Perform basic arithmetic operations with ease!")

col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

# Calculate button
# type="primary" makes it stand out with a different color
if st.button("Calculate", type="primary"):
    result = None
    symbol = ""

    # Perform calculation based on selected operation
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
        result = num1 / num2
        symbol = "÷"

    # Display the result
    if result is not None:
        st.success(f"**Result**: {num1} {symbol} {num2} = **{result:.2f}**")
