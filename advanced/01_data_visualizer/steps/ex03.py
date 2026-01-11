"""
Step 3: Adding First Chart with Plotly

In this step, we'll:
- Import Plotly Express for creating charts
- Create a basic line chart
- Display the chart in the app

Key Concepts:
- plotly.express for quick chart creation
- px.line() for line charts
- st.plotly_chart() to display Plotly charts
"""

import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Data Visualizer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Visualizer")
st.write("Create interactive visualizations with Plotly")

@st.cache_data
def generate_sample_data():
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

df = generate_sample_data()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(df))
with col2:
    st.metric("Total Sales", f"${df['Sales'].sum():,}")
with col3:
    st.metric("Avg Profit", f"${df['Profit'].mean():.0f}")

st.divider()

# Create a line chart
st.subheader("Line Chart")
fig = px.line(df, x='Date', y=['Sales', 'Profit'],
              title="Sales and Profit Over Time")
st.plotly_chart(fig, use_container_width=True)

st.divider()

# Display the data
st.subheader("📋 Data Table")
st.dataframe(df, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
