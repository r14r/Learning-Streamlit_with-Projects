"""
Step 2: Reading and Displaying CSV Data

In this step, we'll:
- Read the uploaded CSV file using pandas
- Add error handling with try/except
- Display a preview of the data
- Show basic dataset information

Key Concepts:
- pd.read_csv() to read CSV files
- try/except blocks for error handling
- st.error() for displaying errors
- st.dataframe() for displaying data
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

        # Data preview
        st.subheader("👀 Data Preview")
        st.write(f"Showing first 10 rows of {len(df)} total rows")
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
