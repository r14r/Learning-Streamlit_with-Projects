"""
Step 2: Generating Demo Stock Data

In this step, we'll:
- Import necessary libraries (numpy, pandas)
- Generate random stock price data
- Display the data in a table

Key Concepts:
- Using numpy for random number generation
- Creating date ranges with pandas
- np.random.seed() for reproducible randomness
- Cumulative sum for realistic price trends
"""

import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Stock Price Tracker", page_icon="📈", layout="wide")

st.title("📈 Stock Price Tracker")

stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]
selected_stock = st.selectbox("Select Stock", stocks)

# Generate demo data based on selected stock
# Use hash to create different but consistent data for each stock
np.random.seed(hash(selected_stock) % 100)

# Generate 90 days of price data
dates = pd.date_range('2024-01-01', periods=90)
base_price = np.random.randint(100, 300)

# Create price changes using cumulative sum for realistic trends
price_changes = np.random.randn(90) * 5
prices = base_price + np.cumsum(price_changes)

# Create DataFrame
df = pd.DataFrame({
    'Date': dates,
    'Price': prices
})

st.subheader(f"{selected_stock} Price Data")
st.dataframe(df.tail(10), use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
