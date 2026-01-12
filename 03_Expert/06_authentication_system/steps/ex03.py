"""
Step 3: Implement Session State and Login Form
- Initialize session state for login status
- Create login form
- Handle login logic
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

# STEP 1: Initialize session state for authentication
# Session state persists across reruns, perfect for login status
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'username' not in st.session_state:
    st.session_state.username = None

# STEP 2: Create login form
st.title("🔐 Login")

# STEP 3: Use st.form to prevent re-running on every keystroke
with st.form("login_form"):
    username = st.text_input(
        "Username",
        placeholder="Enter your username",
        help="Demo users: admin or user"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password",
        help="Demo passwords: admin123 or user123"
    )

    # STEP 4: Add submit button
    submitted = st.form_submit_button("Login", type="primary", use_container_width=True)

    # STEP 5: Process login
    if submitted:
        if check_login(username, password):
            # Set session state on successful login
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("✅ Login successful!")
            st.balloons()  # Celebrate!

            # Show rerun message
            st.info("Redirecting to dashboard...")
            st.rerun()  # Refresh to show logged-in view
        else:
            st.error("❌ Invalid credentials. Please try again.")

# STEP 6: Show demo credentials
st.info("""
📋 **Demo Credentials:**
- Username: `admin` / Password: `admin123`
- Username: `user` / Password: `user123`
""")

# STEP 7: Show current session state for debugging
with st.expander("🔍 Debug: Session State"):
    st.write("Logged in:", st.session_state.logged_in)
    st.write("Username:", st.session_state.username)
    st.caption("Session state maintains login status across page reruns")

# STEP 8: Explain session state
with st.expander("💡 About Session State"):
    st.markdown("""
    ### Streamlit Session State

    Session state is a way to store information across reruns:

    ```python
    # Initialize
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    # Set value
    st.session_state.logged_in = True

    # Read value
    if st.session_state.logged_in:
        print("User is logged in")
    ```

    **Why it's essential for authentication:**
    - Preserves login status across page interactions
    - Stores current user information
    - Maintains state without cookies/backend
    - Works seamlessly with Streamlit's rerun model
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
