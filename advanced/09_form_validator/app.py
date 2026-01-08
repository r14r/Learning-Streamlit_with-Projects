"""
Form Validator - Advanced Project 09

Complex form with validation rules.
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
        
        if len(username) < 4:
            errors.append("Username must be at least 4 characters")
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            errors.append("Invalid email format")
        
        if len(password) < 8:
            errors.append("Password must be at least 8 characters")
        
        if password != confirm_password:
            errors.append("Passwords don't match")
        
        if age < 18:
            errors.append("Must be 18 or older")
        
        if not re.match(r"\d{3}-\d{3}-\d{4}", phone):
            errors.append("Invalid phone format (use XXX-XXX-XXXX)")
        
        if errors:
            for error in errors:
                st.error(f"❌ {error}")
        else:
            st.success("✅ Form validated successfully!")
            with st.expander("Submitted Data"):
                st.write(f"Username: {username}")
                st.write(f"Email: {email}")
                st.write(f"Age: {age}")
                st.write(f"Phone: {phone}")

st.divider()
st.caption("Built with Streamlit 🎈")
