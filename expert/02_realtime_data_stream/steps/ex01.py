"""
Step 1: Basic Setup for Real-Time Dashboard
- Configure page layout
- Add title and introduction
- Explain the real-time concept
"""

import streamlit as st

# STEP 1: Configure page for real-time data display
st.set_page_config(page_title="Real-Time Data Stream", page_icon="📡", layout="wide")

# STEP 2: Add title
st.title("📡 Real-Time Data Stream")

# STEP 3: Explain what we'll build
st.markdown("""
### What is Real-Time Data Streaming?

Real-time data streaming means displaying data that updates continuously without manual refresh.

**Key Concepts:**
- **Auto-refresh**: Page updates automatically
- **st.rerun()**: Forces Streamlit to rerun the script
- **Session state**: Preserves data across reruns
- **Placeholders**: Update specific sections without full reload

In the next steps, we'll build a live data dashboard!
""")

st.divider()
st.caption("Built with Streamlit 🎈")
