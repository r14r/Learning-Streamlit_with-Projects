"""
Data Pipeline Monitor - Expert Project 07

Visualize ETL pipeline status and metrics.
"""

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

st.set_page_config(page_title="Data Pipeline Monitor", page_icon="🔄", layout="wide")

st.title("🔄 Data Pipeline Monitor")

pipelines = {
    "User Data ETL": {"status": "Running", "progress": 75, "records": 15234},
    "Sales Analytics": {"status": "Completed", "progress": 100, "records": 45123},
    "Log Processing": {"status": "Failed", "progress": 45, "records": 8934},
    "Report Generation": {"status": "Running", "progress": 60, "records": 3456}
}

selected_pipeline = st.selectbox("Select Pipeline", list(pipelines.keys()))

pipeline = pipelines[selected_pipeline]

col1, col2, col3, col4 = st.columns(4)

with col1:
    status_color = {"Running": "🟡", "Completed": "🟢", "Failed": "🔴"}
    st.metric("Status", f"{status_color[pipeline['status']]} {pipeline['status']}")

with col2:
    st.metric("Progress", f"{pipeline['progress']}%")

with col3:
    st.metric("Records Processed", f"{pipeline['records']:,}")

with col4:
    st.metric("Runtime", f"{random.randint(10, 60)}min")

st.progress(pipeline['progress'] / 100)

st.subheader("📊 Pipeline Metrics")

dates = pd.date_range(end=datetime.now(), periods=30, freq='D')
records = [random.randint(10000, 50000) for _ in range(30)]

fig = go.Figure()
fig.add_trace(go.Scatter(x=dates, y=records, mode='lines+markers', name='Records'))
fig.update_layout(title="Daily Records Processed", xaxis_title="Date", yaxis_title="Records")

st.plotly_chart(fig, use_container_width=True)

with st.expander("📝 Recent Logs"):
    for i in range(5):
        st.code(f"[{datetime.now().strftime('%H:%M:%S')}] Processing batch {i+1}...")

st.divider()
st.caption("Built with Streamlit 🎈")
