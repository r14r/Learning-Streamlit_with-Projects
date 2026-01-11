"""
Database Integration - Expert Project 05

CRUD operations with SQLite database.
"""

import streamlit as st
import sqlite3
import pandas as pd

st.set_page_config(page_title="Database Integration", page_icon="🗄️", layout="wide")

st.title("🗄️ Database Integration")

@st.cache_resource
def get_connection():
    conn = sqlite3.connect('app_database.db', check_same_thread=False)
    return conn

conn = get_connection()

def create_table():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER
        )
    ''')
    conn.commit()

create_table()

tab1, tab2, tab3, tab4 = st.tabs(["Create", "Read", "Update", "Delete"])

with tab1:
    st.subheader("➕ Create New User")
    with st.form("create_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        age = st.number_input("Age", min_value=0, max_value=120)
        submitted = st.form_submit_button("Add User")
        
        if submitted:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
                         (name, email, age))
            conn.commit()
            st.success("User added successfully!")

with tab2:
    st.subheader("📋 Read Users")
    df = pd.read_sql_query("SELECT * FROM users", conn)
    st.dataframe(df, use_container_width=True)
    st.metric("Total Users", len(df))

with tab3:
    st.subheader("✏️ Update User")
    user_id = st.number_input("User ID to update", min_value=1, step=1)
    new_name = st.text_input("New Name")
    
    if st.button("Update"):
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name = ? WHERE id = ?", (new_name, user_id))
        conn.commit()
        st.success("User updated!")

with tab4:
    st.subheader("🗑️ Delete User")
    del_id = st.number_input("User ID to delete", min_value=1, step=1)
    
    if st.button("Delete", type="primary"):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (del_id,))
        conn.commit()
        st.success("User deleted!")

st.divider()
st.caption("Built with Streamlit 🎈")
