"""
Step 3: Using Columns for Better Layout
Learning objective: Use columns() to create side-by-side layouts
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
# This makes the inputs appear side by side instead of stacked
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

st.write(f"First number: {num1}")
st.write(f"Second number: {num2}")
