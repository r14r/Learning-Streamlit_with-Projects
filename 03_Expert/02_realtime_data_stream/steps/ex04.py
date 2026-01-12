"""
Step 4: Add Live Metrics Display
- Display current value, average, and count
- Update metrics in real-time
- Use st.empty() placeholder pattern
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

st.set_page_config(page_title="Real-Time Data Stream", page_icon="📡", layout="wide")

st.title("📡 Real-Time Data Stream")

st.sidebar.header("🎛️ Stream Controls")
refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", 1, 10, 2)
auto_refresh = st.sidebar.checkbox("Auto-refresh", value=True)

# STEP 1: Create a placeholder for dynamic content
# st.empty() creates a container that can be updated
placeholder = st.empty()

# Initialize session state
if 'data_history' not in st.session_state:
    st.session_state.data_history = []

# STEP 2: Main loop for auto-refresh
# This loop continues while auto_refresh is True
while auto_refresh:
    # STEP 3: Use placeholder.container() to update content
    with placeholder.container():
        # Generate new data point
        current_time = datetime.now().strftime("%H:%M:%S")
        value = np.random.randint(50, 150)

        # Add to history
        st.session_state.data_history.append({
            'time': current_time,
            'value': value
        })

        # Keep only last 50 points
        if len(st.session_state.data_history) > 50:
            st.session_state.data_history.pop(0)

        # STEP 4: Display real-time metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Current Value", value)

        with col2:
            # Calculate average of all historical values
            avg_value = np.mean([d['value'] for d in st.session_state.data_history])
            st.metric("Average", f"{avg_value:.1f}")

        with col3:
            st.metric("Samples", len(st.session_state.data_history))

        # STEP 5: Show recent data points
        st.subheader("📊 Recent Data")
        recent_data = st.session_state.data_history[-10:]
        for item in recent_data:
            st.write(f"⏱️ {item['time']}: **{item['value']}**")

        # Show last update time
        st.caption(f"Last updated: {current_time}")

    # STEP 6: Wait and then rerun
    time.sleep(refresh_rate)
    st.rerun()  # Triggers script to rerun

# If auto-refresh is off, show static view
if not auto_refresh:
    st.info("Auto-refresh is disabled. Enable it in the sidebar to see live updates!")

    if st.session_state.data_history:
        st.write(f"Total samples collected: {len(st.session_state.data_history)}")

st.divider()
st.caption("Built with Streamlit 🎈")
