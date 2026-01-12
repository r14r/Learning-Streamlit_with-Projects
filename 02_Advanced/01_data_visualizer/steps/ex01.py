"""
Step 1: Basic Setup and Sample Data Generation

In this first step, we'll:
- Set up the basic Streamlit page configuration
- Create a function to generate sample data
- Display the data in a simple table

Key Concepts:
- st.set_page_config() for page setup
- @st.cache_data decorator for performance
- Using pandas and numpy to generate data
"""

import streamlit as st
import pandas as pd
import numpy as np

# Configure the page
st.set_page_config(
    page_title="Data Visualizer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Visualizer")
st.write("Create interactive visualizations with Plotly")

# Generate sample data with caching
@st.cache_data
def generate_sample_data():
    """Generate sample business data for visualization"""
    np.random.seed(42)
    dates = pd.date_range('2024-01-01', periods=100)
    return pd.DataFrame({
        'Date': dates,
        'Sales': np.random.randint(100, 1000, 100),
        'Profit': np.random.randint(50, 500, 100),
        'Customers': np.random.randint(10, 100, 100),
        'Category': np.random.choice(['A', 'B', 'C'], 100),
        'Region': np.random.choice(['North', 'South', 'East', 'West'], 100)
    })

# Load the data
df = generate_sample_data()

# Display the data
st.subheader("📋 Data Table")
st.dataframe(df, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
