"""
Step 5: Adding Salary Filter and Summary Metrics

In this final step, we'll:
- Add a minimum salary filter
- Display summary metrics for filtered data
- Complete the data filter explorer

Key Concepts:
- st.sidebar.number_input() for numeric input
- Calculating aggregate statistics
- st.metric() for displaying summary stats
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

# Sidebar filters
st.sidebar.header("Filters")

age_range = st.sidebar.slider("Age Range", 20, 60, (20, 60))

departments = st.sidebar.multiselect(
    "Department",
    df['Department'].unique(),
    default=df['Department'].unique()
)

cities = st.sidebar.multiselect(
    "City",
    df['City'].unique(),
    default=df['City'].unique()
)

# Salary filter
salary_min = st.sidebar.number_input("Min Salary", 40000, 120000, 40000)

# Apply all filters
filtered_df = df[
    (df['Age'] >= age_range[0]) &
    (df['Age'] <= age_range[1]) &
    (df['Department'].isin(departments)) &
    (df['City'].isin(cities)) &
    (df['Salary'] >= salary_min)
]

# Summary metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Filtered Records", len(filtered_df))
with col2:
    st.metric("Avg Salary", f"${filtered_df['Salary'].mean():,.0f}")
with col3:
    st.metric("Avg Age", f"{filtered_df['Age'].mean():.1f}")

# Display filtered data
st.dataframe(filtered_df, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
