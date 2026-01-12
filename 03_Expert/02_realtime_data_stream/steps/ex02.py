"""
Step 2: Add Sidebar Controls
- Create sidebar with refresh rate slider
- Add auto-refresh toggle
- Explain control parameters
"""

import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Real-Time Data Stream", page_icon="📡", layout="wide")

st.title("📡 Real-Time Data Stream")

# STEP 1: Add sidebar controls
st.sidebar.header("🎛️ Stream Controls")

# Slider for refresh rate (1-10 seconds)
refresh_rate = st.sidebar.slider(
    "Refresh Rate (seconds)",
    min_value=1,
    max_value=10,
    value=2,  # Default 2 seconds
    help="How often the data updates"
)

# Checkbox to enable/disable auto-refresh
auto_refresh = st.sidebar.checkbox(
    "Auto-refresh",
    value=True,
    help="Enable automatic data updates"
)

# STEP 2: Display current settings
st.subheader("⚙️ Current Configuration")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Refresh Rate", f"{refresh_rate}s")

with col2:
    st.metric("Auto-refresh", "ON ✅" if auto_refresh else "OFF ❌")

with col3:
    current_time = datetime.now().strftime("%H:%M:%S")
    st.metric("Current Time", current_time)

# STEP 3: Explain the controls
st.info("""
💡 **Control Panel:**
- **Refresh Rate**: Controls how frequently data updates
- **Auto-refresh**: Turn streaming on/off
- When enabled, the page will automatically update!
""")

st.divider()
st.caption("Built with Streamlit 🎈")
