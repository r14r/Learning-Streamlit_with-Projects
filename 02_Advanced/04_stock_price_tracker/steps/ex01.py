"""
Step 1: Basic Stock Selection Setup

In this first step, we'll:
- Set up the page configuration
- Create a stock selector
- Display the selected stock

Key Concepts:
- st.selectbox() for dropdown selection
- Basic page structure
"""

import streamlit as st

st.set_page_config(page_title="Stock Price Tracker", page_icon="📈", layout="wide")

st.title("📈 Stock Price Tracker")

# Define available stocks
stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA"]

# Stock selector
selected_stock = st.selectbox("Select Stock", stocks)

st.info(f"You selected: {selected_stock}")

st.markdown("""
### About this app:
This stock price tracker displays historical price data for popular stocks.

**Note:** This app uses demo/simulated data for educational purposes.

**Available stocks:**
- **AAPL**: Apple Inc.
- **GOOGL**: Alphabet Inc. (Google)
- **MSFT**: Microsoft Corporation
- **AMZN**: Amazon.com Inc.
- **TSLA**: Tesla Inc.
""")

st.divider()
st.caption("Built with Streamlit 🎈")
