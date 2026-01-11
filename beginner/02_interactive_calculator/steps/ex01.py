"""
Step 1: Basic Setup with Title
Learning objective: Set up a calculator app with basic configuration
"""

import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Interactive Calculator",
    page_icon="🧮",
    layout="centered"
)

# Add title and description
st.title("🧮 Interactive Calculator")
st.write("Perform basic arithmetic operations with ease!")
