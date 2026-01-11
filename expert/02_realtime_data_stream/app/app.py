"""
Real-Time Data Stream - Expert Project 02

Display live updating data with auto-refresh.
"""

import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

st.set_page_config(page_title="Real-Time Data Stream", page_icon="📡", layout="wide")

st.title("📡 Real-Time Data Stream")

refresh_rate = st.sidebar.slider("Refresh Rate (seconds)", 1, 10, 2)
auto_refresh = st.sidebar.checkbox("Auto-refresh", value=True)

placeholder = st.empty()

if 'data_history' not in st.session_state:
    st.session_state.data_history = []

while auto_refresh:
    with placeholder.container():
        current_time = datetime.now().strftime("%H:%M:%S")
        value = np.random.randint(50, 150)
        
        st.session_state.data_history.append({
            'time': current_time,
            'value': value
        })
        
        if len(st.session_state.data_history) > 50:
            st.session_state.data_history.pop(0)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Current Value", value)
        with col2:
            avg_value = np.mean([d['value'] for d in st.session_state.data_history])
            st.metric("Average", f"{avg_value:.1f}")
        with col3:
            st.metric("Samples", len(st.session_state.data_history))
        
        df = pd.DataFrame(st.session_state.data_history)
        st.line_chart(df.set_index('time'))
        
        st.caption(f"Last updated: {current_time}")
    
    time.sleep(refresh_rate)
    st.rerun()

st.divider()
st.caption("Built with Streamlit 🎈")
