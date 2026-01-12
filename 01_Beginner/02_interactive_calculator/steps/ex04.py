"""
Step 4: Adding Operation Selection
Learning objective: Use selectbox() to let users choose from options
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

# Operation selection using selectbox
# User can choose from a list of operations
operation = st.selectbox(
    "Select operation",
    ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"]
)

st.write(f"You selected: {operation}")
