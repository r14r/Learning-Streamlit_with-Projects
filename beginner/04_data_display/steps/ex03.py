"""
Step 3: Using Different Display Methods (dataframe vs table)
Learning objective: Learn the difference between dataframe() and table()
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

# DataFrame display - interactive, scrollable, sortable
st.subheader("📋 DataFrame Display")
st.write("Using `st.dataframe()` - Interactive table:")
# use_container_width makes it fill the available width
st.dataframe(df, use_container_width=True)

# Static table - simple, non-interactive
st.subheader("📄 Static Table")
st.write("Using `st.table()` - Static display:")
# head(3) shows only first 3 rows
st.table(df.head(3))
