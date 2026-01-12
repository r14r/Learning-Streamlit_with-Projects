"""
Step 3: Adding Basic Metrics

In this step, we'll:
- Add metric cards for key stock statistics
- Calculate current price, high, and low
- Use columns for layout

Key Concepts:
- st.metric() for displaying metrics
- Array indexing (prices[-1] for last element)
- min() and max() for finding extremes
- Column layout for organization
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Stock Price Tracker", page_icon="📈", layout="wide")

st.title("📈 Stock Price Tracker")

stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
selected_stock = st.selectbox("Select Stock", stocks)

# Generate demo data
np.random.seed(hash(selected_stock) % 100)
dates = pd.date_range('2024-01-01', periods=90)
base_price = np.random.randint(100, 300)
prices = base_price + np.cumsum(np.random.randn(90) * 5)

df = pd.DataFrame({'Date': dates, 'Price': prices})

# Display metrics
col1, col2, col3 = st.columns(3)

with col1:
    current_price = prices[-1]
    st.metric("Current Price", f"${current_price:.2f}")

with col2:
    high_price = prices.max()
    st.metric("High", f"${high_price:.2f}")

with col3:
    low_price = prices.min()
    st.metric("Low", f"${low_price:.2f}")

st.divider()

# Display data
st.subheader(f"{selected_stock} Recent Price Data")
st.dataframe(df.tail(10), use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
