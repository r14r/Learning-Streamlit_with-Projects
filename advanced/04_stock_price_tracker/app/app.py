"""
Stock Price Tracker - Advanced Project 04

Display stock price data and charts (demo data).
"""

import streamlit as st
import plotly.graph_objects as go
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

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Price", f"${prices[-1]:.2f}", 
              f"{((prices[-1] - prices[-2]) / prices[-2] * 100):.2f}%")
with col2:
    st.metric("High", f"${prices.max():.2f}")
with col3:
    st.metric("Low", f"${prices.min():.2f}")

fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Price'], mode='lines', name=selected_stock))
fig.update_layout(title=f"{selected_stock} Price Chart", xaxis_title="Date", yaxis_title="Price ($)")

st.plotly_chart(fig, use_container_width=True)

st.dataframe(df.tail(10), use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
