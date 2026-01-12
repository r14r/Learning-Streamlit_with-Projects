"""
A/B Testing Dashboard - Expert Project 08

Statistical analysis and visualization of A/B tests.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from scipy import stats

st.set_page_config(page_title="A/B Testing Dashboard", page_icon="🧪", layout="wide")

st.title("🧪 A/B Testing Dashboard")

st.sidebar.header("Test Configuration")

visitors_a = st.sidebar.number_input("Group A Visitors", 1000, 100000, 10000)
conversions_a = st.sidebar.number_input("Group A Conversions", 100, visitors_a, 1200)

visitors_b = st.sidebar.number_input("Group B Visitors", 1000, 100000, 10000)
conversions_b = st.sidebar.number_input("Group B Conversions", 100, visitors_b, 1500)

conv_rate_a = conversions_a / visitors_a
conv_rate_b = conversions_b / visitors_b

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Group A Conv. Rate", f"{conv_rate_a:.2%}")

with col2:
    st.metric("Group B Conv. Rate", f"{conv_rate_b:.2%}")

with col3:
    improvement = ((conv_rate_b - conv_rate_a) / conv_rate_a) * 100
    st.metric("Improvement", f"{improvement:+.2f}%")

z_score, p_value = stats.proportions_ztest(
    [conversions_a, conversions_b],
    [visitors_a, visitors_b]
)

st.subheader("📊 Statistical Significance")

col1, col2 = st.columns(2)

with col1:
    st.metric("P-Value", f"{p_value:.4f}")

with col2:
    is_significant = p_value < 0.05
    st.metric("Significant?", "Yes ✅" if is_significant else "No ❌")

if is_significant:
    st.success("The difference is statistically significant!")
else:
    st.warning("The difference is not statistically significant.")

df = pd.DataFrame({
    'Group': ['A', 'A', 'B', 'B'],
    'Type': ['Converted', 'Not Converted'] * 2,
    'Count': [conversions_a, visitors_a - conversions_a, 
              conversions_b, visitors_b - conversions_b]
})

fig = px.bar(df, x='Group', y='Count', color='Type', barmode='group',
             title="Conversion Comparison")
st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
