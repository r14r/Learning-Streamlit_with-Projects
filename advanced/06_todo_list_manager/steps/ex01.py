"""
Step 1: Basic Session State Setup

In this first step, we'll:
- Set up the page configuration
- Initialize session state for storing todos
- Understand how session state works

Key Concepts:
- st.session_state for persistent data across reruns
- Checking if a key exists in session_state
- Initializing session state variables
"""

import streamlit as st

st.set_page_config(page_title="TODO List Manager", page_icon="✅", layout="centered")

st.title("✅ TODO List Manager")

# Initialize session state for todos
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Display current state
st.write(f"Current number of todos: {len(st.session_state.todos)}")

st.info("""
### About Session State:
Session state allows us to store data that persists across app reruns.
This is essential for building interactive apps like a TODO list.

We've initialized an empty list to store our todos.
""")

st.divider()
st.caption("Built with Streamlit 🎈")
