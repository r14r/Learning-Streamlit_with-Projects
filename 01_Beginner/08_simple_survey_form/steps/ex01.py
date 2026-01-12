"""
Step 1: Basic Setup with Form Container
Learning objective: Create a form using st.form() context manager
"""

import streamlit as st

st.set_page_config(
    page_title="Simple Survey Form",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Simple Survey Form")
st.write("We'd love to hear your feedback!")

# Create a form using context manager
# Forms group widgets together and submit all at once
with st.form("survey_form"):
    st.subheader("Personal Information")

    name = st.text_input("Full Name*", placeholder="John Doe")

    # Every form needs a submit button
    submitted = st.form_submit_button("Submit Survey", type="primary")

    if submitted:
        st.write(f"Thank you, {name}!")
