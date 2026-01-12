"""
Step 4: Adding Column Selection
Learning objective: Use multiselect() to filter DataFrame columns
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Display",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Display Examples")
st.write("Learn different ways to display data in Streamlit")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'London', 'Paris', 'Tokyo'],
    'Salary': [70000, 85000, 92000, 78000, 88000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing']
}

df = pd.DataFrame(data)

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

st.subheader("📋 DataFrame Display")
st.write("Using `st.dataframe()` - Interactive table:")
st.dataframe(df, use_container_width=True)

st.subheader("📄 Static Table")
st.write("Using `st.table()` - Static display:")
st.table(df.head(3))

# Column selection feature
st.subheader("🔍 Column Selection")
# multiselect allows selecting multiple columns
# df.columns.tolist() gets all column names
# default specifies which columns are selected initially
selected_columns = st.multiselect(
    "Select columns to display:",
    df.columns.tolist(),
    default=['Name', 'Age']
)

if selected_columns:
    # Display only selected columns using df[column_list]
    st.dataframe(df[selected_columns], use_container_width=True)
