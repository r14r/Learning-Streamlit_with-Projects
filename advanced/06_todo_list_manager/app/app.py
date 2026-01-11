"""
TODO List Manager - Advanced Project 06

Manage tasks with persistent session state.
"""

import streamlit as st
from datetime import datetime

st.set_page_config(page_title="TODO List Manager", page_icon="✅", layout="centered")

st.title("✅ TODO List Manager")

if 'todos' not in st.session_state:
    st.session_state.todos = []

with st.form("add_todo"):
    new_task = st.text_input("New task")
    priority = st.selectbox("Priority", ["Low", "Medium", "High"])
    submitted = st.form_submit_button("Add Task", type="primary")
    
    if submitted and new_task:
        st.session_state.todos.append({
            'task': new_task,
            'priority': priority,
            'completed': False,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        st.success("Task added!")
        st.rerun()

if st.session_state.todos:
    col1, col2, col3 = st.columns(3)
    total = len(st.session_state.todos)
    completed = sum(1 for t in st.session_state.todos if t['completed'])
    
    with col1:
        st.metric("Total Tasks", total)
    with col2:
        st.metric("Completed", completed)
    with col3:
        st.metric("Remaining", total - completed)
    
    st.divider()
    
    for idx, todo in enumerate(st.session_state.todos):
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            task_text = f"~~{todo['task']}~~" if todo['completed'] else todo['task']
            st.write(f"{task_text} ({todo['priority']})")
        
        with col2:
            if st.button("✓", key=f"complete_{idx}"):
                st.session_state.todos[idx]['completed'] = not todo['completed']
                st.rerun()
        
        with col3:
            if st.button("🗑️", key=f"delete_{idx}"):
                st.session_state.todos.pop(idx)
                st.rerun()
else:
    st.info("No tasks yet. Add one above!")

st.divider()
st.caption("Built with Streamlit 🎈")
