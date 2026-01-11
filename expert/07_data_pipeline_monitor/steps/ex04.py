"""
Step 4: Add Historical Trends Chart (Complete)
- Generate historical data
- Create time-series visualization with Plotly
- Add log viewer
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

# Metrics Dashboard
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

st.divider()

# STEP 1: Add historical trends section
st.subheader("📈 Pipeline Metrics - Last 30 Days")

# STEP 2: Generate historical data
# Create dates for last 30 days
dates = pd.date_range(end=datetime.now(), periods=30, freq='D')

# Generate random records counts (simulating daily pipeline runs)
records = [random.randint(10000, 50000) for _ in range(30)]

# STEP 3: Create Plotly line chart
fig = go.Figure()

# Add line trace
fig.add_trace(go.Scatter(
    x=dates,
    y=records,
    mode='lines+markers',
    name='Records Processed',
    line=dict(color='#1f77b4', width=2),
    marker=dict(size=6)
))

# STEP 4: Customize chart layout
fig.update_layout(
    title="Daily Records Processed",
    xaxis_title="Date",
    yaxis_title="Records",
    hovermode='x unified',
    template='plotly_white',
    height=400
)

# Display chart
st.plotly_chart(fig, use_container_width=True)

# STEP 5: Add statistics summary
st.subheader("📊 30-Day Statistics")

stat_col1, stat_col2, stat_col3, stat_col4 = st.columns(4)

with stat_col1:
    st.metric("Average Daily Records", f"{int(sum(records)/len(records)):,}")

with stat_col2:
    st.metric("Peak Day", f"{max(records):,}")

with stat_col3:
    st.metric("Total Records", f"{sum(records):,}")

with stat_col4:
    success_rate = 95 if pipeline['status'] != "Failed" else 85
    st.metric("Success Rate", f"{success_rate}%")

st.divider()

# STEP 6: Add log viewer
st.subheader("📝 Recent Pipeline Logs")

with st.expander("View Logs"):
    # STEP 7: Generate sample log entries
    log_entries = []

    if pipeline['status'] == "Running":
        log_entries = [
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Processing batch 5/10",
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Processed 10,000 records",
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Transform stage completed",
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Starting load stage",
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Pipeline running smoothly",
        ]
    elif pipeline['status'] == "Failed":
        log_entries = [
            f"[{datetime.now().strftime('%H:%M:%S')}] ERROR: Database connection timeout",
            f"[{datetime.now().strftime('%H:%M:%S')}] ERROR: Retrying connection (1/3)",
            f"[{datetime.now().strftime('%H:%M:%S')}] ERROR: Retrying connection (2/3)",
            f"[{datetime.now().strftime('%H:%M:%S')}] ERROR: Max retries exceeded",
            f"[{datetime.now().strftime('%H:%M:%S')}] ERROR: Pipeline failed at transform stage",
        ]
    else:  # Completed
        log_entries = [
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Pipeline completed successfully",
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Total records processed: {pipeline['records']:,}",
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Data quality checks passed",
            f"[{datetime.now().strftime('%H:%M:%S')}] INFO: Loading data to destination",
            f"[{datetime.now().strftime('%H:%M:%S')}] SUCCESS: All stages completed",
        ]

    # Display logs
    for entry in log_entries:
        if "ERROR" in entry:
            st.code(entry, language=None)
            st.error("Error detected in logs")
        else:
            st.code(entry, language=None)

# STEP 8: Add pipeline documentation
with st.expander("📚 Pipeline Monitoring Best Practices"):
    st.markdown("""
    ### Monitoring Data Pipelines

    #### Key Metrics to Track

    1. **Status**: Current state (running, completed, failed)
    2. **Progress**: Completion percentage
    3. **Throughput**: Records processed per time unit
    4. **Runtime**: Total execution time
    5. **Error Rate**: Percentage of failed runs
    6. **Data Quality**: Validation and quality checks

    #### Alert Conditions

    Set up alerts for:
    - Pipeline failures
    - Runtime exceeds threshold
    - Data quality issues
    - Missing or delayed runs
    - Resource constraints

    #### Visualization Tips

    - **Time-series charts**: Track trends over time
    - **Status dashboards**: Quick overview of all pipelines
    - **Progress bars**: Visual completion indicators
    - **Log viewers**: Detailed troubleshooting

    #### Production Considerations

    1. **Real-time updates**: Use auto-refresh or websockets
    2. **Historical data**: Store pipeline metrics in database
    3. **Alerting**: Integrate with notification systems
    4. **Access control**: Restrict sensitive pipeline info
    5. **Performance**: Optimize queries for large datasets
    6. **Scalability**: Design for multiple concurrent pipelines
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
