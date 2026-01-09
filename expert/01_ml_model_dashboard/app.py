"""
ML Model Dashboard - Expert Project 01

Deploy and visualize machine learning model predictions.
"""

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import plotly.express as px

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

st.sidebar.header("Model Configuration")
n_samples = st.sidebar.slider("Number of predictions", 1, 100, 10)

col1, col2, col3 = st.columns(3)

with col1:
    accuracy = model.score(X_test, y_test)
    st.metric("Model Accuracy", f"{accuracy:.2%}")

with col2:
    st.metric("Test Samples", len(X_test))

with col3:
    st.metric("Features", X_test.shape[1])

predictions = model.predict(X_test[:n_samples])
probabilities = model.predict_proba(X_test[:n_samples])

st.subheader("📊 Predictions")
pred_df = pd.DataFrame({
    'Sample': range(n_samples),
    'Prediction': predictions,
    'Confidence': probabilities.max(axis=1)
})

st.dataframe(pred_df, use_container_width=True)

fig = px.bar(pred_df, x='Sample', y='Confidence', color='Prediction',
             title="Prediction Confidence")
st.plotly_chart(fig, use_container_width=True)

st.subheader("🎯 Feature Importance")
importance_df = pd.DataFrame({
    'Feature': [f'Feature_{i}' for i in range(X_test.shape[1])],
    'Importance': model.feature_importances_
}).sort_values('Importance', ascending=False).head(10)

fig = px.bar(importance_df, x='Importance', y='Feature', orientation='h',
             title="Top 10 Feature Importance")
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
