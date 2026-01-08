"""
Authentication System - Expert Project 06

User login and session management system.
"""

import streamlit as st
import hashlib

st.set_page_config(page_title="Authentication System", page_icon="🔐", layout="centered")

users_db = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user": hashlib.sha256("user123".encode()).hexdigest()
}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_login(username, password):
    if username in users_db and users_db[username] == hash_password(password):
        return True
    return False

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = None

if not st.session_state.logged_in:
    st.title("🔐 Login")
    
    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login", type="primary")
        
        if submitted:
            if check_login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid credentials")
    
    st.info("Demo credentials: admin/admin123 or user/user123")
else:
    st.title(f"Welcome, {st.session_state.username}! 👋")
    
    st.success("You are logged in!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Session Status", "Active")
    with col2:
        st.metric("User", st.session_state.username)
    with col3:
        st.metric("Access Level", "Full")
    
    st.subheader("Protected Content")
    st.write("This content is only visible to authenticated users.")
    
    if st.button("Logout", type="primary"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

st.divider()
st.caption("Built with Streamlit 🎈")
