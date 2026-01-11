"""
Step 3: Adding Headers and Basic Text
Learning objective: Use different text display methods (header, subheader, write)
"""

import streamlit as st

st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered"
)

# Title - largest heading
st.title("👋 Hello Streamlit!")

# Header - medium-sized heading
st.header("Welcome to Your First Streamlit App")

# Subheader - smaller heading
st.subheader("Learning Streamlit Basics")

# Regular text using write()
# write() is versatile and can display many types of content
st.write("This is a simple Streamlit application that demonstrates basic text display features.")
