"""
Step 2: Adding Page Configuration
Learning objective: Configure page settings like title, icon, and layout
"""

import streamlit as st

# Set page configuration
# This must be the first Streamlit command in your script
# page_title: appears in browser tab
# page_icon: emoji or image that appears in browser tab
# layout: can be "centered" or "wide"
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered"
)

# Title
st.title("👋 Hello Streamlit!")
