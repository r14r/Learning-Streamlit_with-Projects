"""
Step 3: Train ML Model with Caching
- Split data into train/test sets
- Train a Random Forest classifier
- Use @st.cache_resource to avoid retraining on every rerun
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="ML Model Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 ML Model Dashboard")

# STEP 1: Create cached function for model training
# @st.cache_resource ensures the model is only trained once
# and reused across reruns - critical for performance!
@st.cache_resource
def train_model():
    """Train a Random Forest model and return model + test data"""
    # Generate data
    X, y = make_classification(
        n_samples=1000,
        n_features=20,
        n_informative=15,
        n_redundant=5,
        random_state=42
    )

    # STEP 2: Split into training and testing sets
    # 80% for training, 20% for testing
    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=0.2,      # 20% for testing
        random_state=42
    )

    # STEP 3: Create and train the model
    # Random Forest is an ensemble of decision trees
    model = RandomForestClassifier(
        n_estimators=100,   # Use 100 trees
        random_state=42
    )
    model.fit(X_train, y_train)

    return model, X_test, y_test

# STEP 4: Train the model (or load from cache)
with st.spinner("Training model..."):
    model, X_test, y_test = train_model()

st.success("✅ Model trained successfully!")

# STEP 5: Display model accuracy
accuracy = model.score(X_test, y_test)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Model Accuracy", f"{accuracy:.2%}")

with col2:
    st.metric("Test Samples", len(X_test))

with col3:
    st.metric("Features", X_test.shape[1])

st.info("💡 The model is cached using @st.cache_resource, so it won't retrain on every page refresh!")

st.divider()
st.caption("Built with Streamlit 🎈")
