"""
Step 3: Adding Dataset Overview Metrics

In this step, we'll:
- Add metric cards showing dataset statistics
- Display rows, columns, numeric columns, and memory usage
- Use columns for organized layout

Key Concepts:
- df.shape for getting dimensions
- df.select_dtypes() for filtering columns by type
- df.memory_usage() for calculating memory size
- Layout with st.columns()
"""

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="CSV Analyzer",
    page_icon="📁",
    layout="wide"
)

st.title("📁 CSV Analyzer")
st.write("Upload and analyze your CSV files")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    try:
        # Read CSV
        df = pd.read_csv(uploaded_file)

        st.success(f"✅ Successfully loaded: {uploaded_file.name}")

        # Overview metrics
        st.subheader("📊 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Rows", df.shape[0])
        with col2:
            st.metric("Columns", df.shape[1])
        with col3:
            st.metric("Numeric Columns", df.select_dtypes(include=['number']).shape[1])
        with col4:
            st.metric("Memory Usage", f"{df.memory_usage(deep=True).sum() / 1024:.1f} KB")

        # Data preview
        st.subheader("👀 Data Preview")
        st.dataframe(df.head(10), use_container_width=True)

    except Exception as e:
        st.error(f"Error loading file: {str(e)}")

else:
    st.info("👆 Upload a CSV file to get started")

    st.markdown("""
    ### Features:
    - **Data Preview**: View the first rows of your data
    - **Column Analysis**: Understand data types and missing values
    - **Statistics**: Get statistical summaries
    - **Visualizations**: Create histograms and box plots
    - **Correlations**: View relationships between numeric columns
    - **Export**: Download processed data
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
