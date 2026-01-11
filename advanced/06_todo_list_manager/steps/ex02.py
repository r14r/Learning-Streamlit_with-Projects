"""
Step 2: Adding Input Form

In this step, we'll:
- Create a form for adding new tasks
- Add text input and selectbox for priority
- Handle form submission

Key Concepts:
- st.form() for grouping inputs
- st.text_input() for text entry
- st.selectbox() for dropdown selection
- st.form_submit_button() for form submission
"""

import streamlit as st

st.set_page_config(page_title="TODO List Manager", page_icon="✅", layout="centered")

st.title("✅ TODO List Manager")

# Initialize session state
if 'todos' not in st.session_state:
    st.session_state.todos = []

# Add task form
with st.form("add_todo"):
    st.subheader("Add New Task")
    new_task = st.text_input("Task description")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Task", type="primary")

    if submitted:
        if new_task:
            st.success(f"Task '{new_task}' with priority '{priority}' will be added!")
            # We'll actually add it to the list in the next step
        else:
            st.warning("Please enter a task description")

# Display current todos
st.write(f"Current number of todos: {len(st.session_state.todos)}")

st.divider()
st.caption("Built with Streamlit 🎈")
