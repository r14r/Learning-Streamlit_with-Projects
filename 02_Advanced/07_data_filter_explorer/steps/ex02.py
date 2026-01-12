"""
Step 2: Adding Sidebar for Filters

In this step, we'll:
- Add a sidebar header
- Display information about filters
- Prepare the structure for adding filter widgets

Key Concepts:
- st.sidebar for side panel
- Organizing filter controls
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Data Filter Explorer", page_icon="🔍", layout="wide")

st.title("🔍 Data Filter Explorer")

@st.cache_data
def load_data():
    np.random.seed(42)
    return pd.DataFrame({
        'Name': [f"Person {i}" for i in range(100)],
        'Age': np.random.randint(20, 60, 100),
        'Department': np.random.choice(['IT', 'HR', 'Finance', 'Sales'], 100),
        'Salary': np.random.randint(40000, 120000, 100),
        'City': np.random.choice(['NYC', 'LA', 'Chicago', 'Houston'], 100)
    })

df = load_data()

# Sidebar for filters
st.sidebar.header("Filters")
st.sidebar.info("Use the filters below to explore the data")

# We'll add filter widgets in the next steps

st.subheader("Employee Dataset")
st.write(f"Total records: {len(df)}")
st.dataframe(df, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
