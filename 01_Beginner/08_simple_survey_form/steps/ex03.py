"""
Step 3: Adding Feedback Widgets (Slider and Radio)
Learning objective: Use slider() and radio() for user feedback
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

    name = st.text_input("Full Name*", placeholder="John Doe")
    email = st.text_input("Email*", placeholder="john.doe@example.com")
    age = st.number_input("Age", min_value=13, max_value=120, value=25)

    st.subheader("Feedback")

    # Slider for rating (1 to 5)
    rating = st.slider("How would you rate our service?", 1, 5, 3)

    # Radio buttons for satisfaction level
    satisfaction = st.radio(
        "Overall satisfaction:",
        ["Very Satisfied", "Satisfied", "Neutral", "Unsatisfied", "Very Unsatisfied"]
    )

    submitted = st.form_submit_button("Submit Survey", type="primary")

    if submitted:
        st.write(f"**Name**: {name}")
        st.write(f"**Email**: {email}")
        st.write(f"**Age**: {age}")
        st.write(f"**Rating**: {'⭐' * rating}")
        st.write(f"**Satisfaction**: {satisfaction}")
