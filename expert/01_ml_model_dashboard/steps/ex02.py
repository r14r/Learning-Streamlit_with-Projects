"""
Step 2: Generate Training Data
- Import ML libraries
- Create synthetic dataset using sklearn
- Display basic data information
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification

st.set_page_config(page_title="ML Model Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 ML Model Dashboard")

# STEP 1: Generate synthetic classification data
# make_classification creates a random n-class classification problem
# n_samples: number of data points
# n_features: total number of features
# n_informative: number of useful features
# n_redundant: number of redundant features (linear combinations of informative features)
X, y = make_classification(
    n_samples=1000,      # Generate 1000 samples
    n_features=20,       # With 20 total features
    n_informative=15,    # 15 are informative
    n_redundant=5,       # 5 are redundant
    random_state=42      # For reproducibility
)

# STEP 2: Display data information
st.subheader("📊 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Samples", X.shape[0])

with col2:
    st.metric("Features", X.shape[1])

with col3:
    # Count how many samples belong to each class
    st.metric("Classes", len(np.unique(y)))

# STEP 3: Show sample data
st.subheader("Sample Data")
sample_df = pd.DataFrame(X[:10], columns=[f'Feature_{i}' for i in range(X.shape[1])])
sample_df['Target'] = y[:10]
st.dataframe(sample_df, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
