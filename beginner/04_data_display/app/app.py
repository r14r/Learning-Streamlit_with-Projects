"""
Data Display - Beginner Project 04

Demonstrate various ways to display data in Streamlit.
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Data Display",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Display Examples")
st.write("Learn different ways to display data in Streamlit")

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'London', 'Paris', 'Tokyo'],
    'Salary': [70000, 85000, 92000, 78000, 88000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing']
}

df = pd.DataFrame(data)

# Display metrics
st.subheader("📈 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Employees", len(df))

with col2:
    avg_age = df['Age'].mean()
    st.metric("Average Age", f"{avg_age:.1f}")

with col3:
    avg_salary = df['Salary'].mean()
    st.metric("Avg Salary", f"${avg_salary:,.0f}")

with col4:
    departments = df['Department'].nunique()
    st.metric("Departments", departments)

# DataFrame display
st.subheader("📋 DataFrame Display")
st.write("Using `st.dataframe()` - Interactive table:")
st.dataframe(df, use_container_width=True)

# Static table
st.subheader("📄 Static Table")
st.write("Using `st.table()` - Static display:")
st.table(df.head(3))

# Display specific columns
st.subheader("🔍 Column Selection")
selected_columns = st.multiselect(
    "Select columns to display:",
    df.columns.tolist(),
    default=['Name', 'Age']
)

if selected_columns:
    st.dataframe(df[selected_columns], use_container_width=True)

# JSON display
st.subheader("🗂️ JSON Format")
if st.checkbox("Show data as JSON"):
    st.json(df.to_dict(orient='records'))

# Statistics
with st.expander("📊 Data Statistics"):
    st.write(df.describe())

# Data editor (Streamlit 1.x feature)
st.subheader("✏️ Editable Data")
st.write("Try editing the data below (changes are not saved):")
edited_df = st.data_editor(df, use_container_width=True)

if not df.equals(edited_df):
    st.info("You've made changes to the data!")

st.divider()
st.caption("Built with Streamlit 🎈")
