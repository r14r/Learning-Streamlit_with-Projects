"""
Step 2: Adding More Personal Information Fields
Learning objective: Add different input types to a form
"""

import streamlit as st

st.set_page_config(
    page_title="Simple Survey Form",
    page_icon="📋",
    layout="centered"
)

st.title("📋 Simple Survey Form")
st.write("We'd love to hear your feedback!")

with st.form("survey_form"):
    st.subheader("Personal Information")

    # Text input for name
    name = st.text_input("Full Name*", placeholder="John Doe")

    # Text input for email
    email = st.text_input("Email*", placeholder="john.doe@example.com")

    # Number input for age with constraints
    age = st.number_input("Age", min_value=13, max_value=120, value=25)

    submitted = st.form_submit_button("Submit Survey", type="primary")

    if submitted:
        st.write(f"**Name**: {name}")
        st.write(f"**Email**: {email}")
        st.write(f"**Age**: {age}")
