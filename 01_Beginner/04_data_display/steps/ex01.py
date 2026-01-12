"""
Step 1: Basic Setup and Creating Sample Data
Learning objective: Create a pandas DataFrame from a dictionary
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

# Create sample data using a dictionary
# Each key becomes a column, each list becomes the column values
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'San Francisco', 'London', 'Paris', 'Tokyo'],
    'Salary': [70000, 85000, 92000, 78000, 88000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing']
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
st.write("Here's our sample data:")
st.write(df)
