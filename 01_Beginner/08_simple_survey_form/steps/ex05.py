"""
Step 5: Adding Form Validation
Learning objective: Validate form inputs before processing
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

    rating = st.slider("How would you rate our service?", 1, 5, 3)

    satisfaction = st.radio(
        "Overall satisfaction:",
        ["Very Satisfied", "Satisfied", "Neutral", "Unsatisfied", "Very Unsatisfied"]
    )

    interests = st.multiselect(
        "Areas of interest:",
        ["Technology", "Science", "Arts", "Sports", "Music", "Travel"]
    )

    comments = st.text_area("Additional comments", placeholder="Tell us more...")

    # Checkbox for newsletter
    newsletter = st.checkbox("Subscribe to newsletter")

    submitted = st.form_submit_button("Submit Survey", type="primary")

    if submitted:
        # Validate required fields
        if not name or not email:
            st.error("⚠️ Please fill in all required fields (marked with *)")
        elif "@" not in email:
            st.error("⚠️ Please enter a valid email address")
        else:
            # Form is valid
            st.success("✅ Thank you for your feedback!")
            st.write(f"**Name**: {name}")
            st.write(f"**Email**: {email}")
            st.write(f"**Age**: {age}")
            st.write(f"**Rating**: {'⭐' * rating}")
            st.write(f"**Satisfaction**: {satisfaction}")
            if interests:
                st.write(f"**Interests**: {', '.join(interests)}")
            if comments:
                st.write(f"**Comments**: {comments}")
            st.write(f"**Newsletter**: {'Yes' if newsletter else 'No'}")
