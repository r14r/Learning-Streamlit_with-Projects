"""
Step 4: Adding Email and Password Match Validation

In this step, we'll:
- Add email format validation using regex
- Check if passwords match
- Use re.match() for pattern matching

Key Concepts:
- re.match() for regex validation
- Email regex pattern
- Comparing two values
"""

import streamlit as st
import re

st.set_page_config(page_title="Form Validator", page_icon="✔️", layout="centered")

st.title("✔️ Form Validator")

with st.form("validation_form"):
    st.subheader("User Registration")

    username = st.text_input("Username (min 4 characters)")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    age = st.number_input("Age", min_value=0, max_value=120, value=18)
    phone = st.text_input("Phone (format: XXX-XXX-XXXX)")

    submitted = st.form_submit_button("Submit", type="primary")

    if submitted:
        errors = []

        # Validate username
        if len(username) < 4:
            errors.append("Username must be at least 4 characters")

        # Validate email format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format")

        # Validate password length
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")

        # Check if passwords match
        if password != confirm_password:
            errors.append("Passwords don't match")

        # Display errors or success
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
        else:
            st.success("✅ Great! More validations coming in next step.")

st.divider()
st.caption("Built with Streamlit 🎈")
