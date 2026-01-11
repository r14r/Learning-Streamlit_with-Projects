"""
Step 4: Add Interactive Predictions
- Add sidebar controls
- Generate predictions on user-specified number of samples
- Display predictions in a table
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

st.set_page_config(page_title="ML Model Dashboard", page_icon="🤖", layout="wide")

st.title("🤖 ML Model Dashboard")

@st.cache_resource
def train_model():
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,
                               n_redundant=5, random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    return model, X_test, y_test

model, X_test, y_test = train_model()

# STEP 1: Add sidebar controls
st.sidebar.header("Model Configuration")
# Slider allows users to select how many predictions to show
n_samples = st.sidebar.slider("Number of predictions", 1, 100, 10)

# Display metrics
col1, col2, col3 = st.columns(3)

with col1:
    accuracy = model.score(X_test, y_test)
    st.metric("Model Accuracy", f"{accuracy:.2%}")

with col2:
    st.metric("Test Samples", len(X_test))

with col3:
    st.metric("Features", X_test.shape[1])

# STEP 2: Generate predictions for the selected number of samples
st.subheader("📊 Predictions")

# predict() returns class labels (0 or 1)
predictions = model.predict(X_test[:n_samples])

# predict_proba() returns probability distributions for each class
probabilities = model.predict_proba(X_test[:n_samples])

# STEP 3: Create a DataFrame to display predictions
pred_df = pd.DataFrame({
    'Sample': range(n_samples),
    'Prediction': predictions,
    # Get the maximum probability (confidence) for each prediction
    'Confidence': probabilities.max(axis=1)
})

# STEP 4: Display the predictions table
st.dataframe(pred_df, use_container_width=True)

# Show some explanation
st.info("""
💡 **Understanding the predictions:**
- **Sample**: Index of the test sample
- **Prediction**: The predicted class (0 or 1)
- **Confidence**: How confident the model is (0.0 to 1.0, higher is more confident)
""")

st.divider()
st.caption("Built with Streamlit 🎈")
