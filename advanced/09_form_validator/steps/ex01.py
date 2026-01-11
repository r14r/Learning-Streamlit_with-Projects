"""
Step 1: Basic Form Structure

In this first step, we'll:
- Set up the page configuration
- Create a basic form with a few input fields
- Add a submit button

Key Concepts:
- st.form() for grouping form inputs
- st.text_input() for text entry
- st.form_submit_button() for submission
"""

import streamlit as st

st.set_page_config(page_title="Form Validator", page_icon="✔️", layout="centered")

st.title("✔️ Form Validator")

# Create a form
with st.form("validation_form"):
    st.subheader("User Registration")

    username = st.text_input("Username")
    email = st.text_input("Email")

    submitted = st.form_submit_button("Submit", type="primary")

    if submitted:
        st.info(f"Form submitted with username: {username} and email: {email}")
        st.write("Validation will be added in the next steps")

st.divider()
st.caption("Built with Streamlit 🎈")
