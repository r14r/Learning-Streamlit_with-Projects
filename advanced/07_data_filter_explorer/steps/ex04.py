"""
Step 4: Adding Department and City Filters

In this step, we'll:
- Add multiselect filters for Department and City
- Combine multiple filters
- Apply all filters to the data

Key Concepts:
- st.sidebar.multiselect() for multiple selection
- df['column'].unique() to get unique values
- Combining multiple filter conditions
- df['column'].isin() for filtering by list of values
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

# Age range filter
age_range = st.sidebar.slider("Age Range", 20, 60, (20, 60))

# Department filter
departments = st.sidebar.multiselect(
    "Department",
    df['Department'].unique(),
    default=df['Department'].unique()
)

# City filter
cities = st.sidebar.multiselect(
    "City",
    df['City'].unique(),
    default=df['City'].unique()
)

# Apply all filters
filtered_df = df[
    (df['Age'] >= age_range[0]) &
    (df['Age'] <= age_range[1]) &
    (df['Department'].isin(departments)) &
    (df['City'].isin(cities))
]

# Display filtered data
st.subheader("Filtered Employee Dataset")
st.write(f"Showing {len(filtered_df)} of {len(df)} records")
st.dataframe(filtered_df, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
