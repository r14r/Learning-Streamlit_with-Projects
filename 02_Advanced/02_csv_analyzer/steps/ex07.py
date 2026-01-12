"""
Step 7: Adding Correlation Heatmap

In this step, we'll:
- Add a correlation matrix heatmap
- Show relationships between numeric variables
- Use px.imshow() for heatmap visualization

Key Concepts:
- df.corr() for correlation matrix
- px.imshow() for heatmap
- Conditional rendering (only show if multiple numeric columns)
- Color scales in Plotly
"""

import streamlit as st
import pandas as pd
import plotly.express as px

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

        # Overview
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

        # Column information
        st.subheader("📋 Column Information")

        col_info = pd.DataFrame({
            'Column': df.columns,
            'Type': df.dtypes.values,
            'Non-Null': df.count().values,
            'Null': df.isnull().sum().values,
            'Unique': df.nunique().values
        })

        st.dataframe(col_info, use_container_width=True)

        # Statistical summary
        st.subheader("📈 Statistical Summary")
        st.dataframe(df.describe(), use_container_width=True)

        # Visualization
        st.subheader("📊 Data Visualization")

        numeric_cols = df.select_dtypes(include=['number']).columns.tolist()

        if numeric_cols:
            col1, col2 = st.columns(2)

            with col1:
                selected_col = st.selectbox("Select column to visualize", numeric_cols)

            with col2:
                chart_type = st.selectbox("Chart type", ["Histogram", "Box Plot"])

            if chart_type == "Histogram":
                fig = px.histogram(df, x=selected_col, title=f"Distribution of {selected_col}")
            else:
                fig = px.box(df, y=selected_col, title=f"Box Plot of {selected_col}")

            st.plotly_chart(fig, use_container_width=True)

            # Correlation heatmap if multiple numeric columns
            if len(numeric_cols) > 1:
                st.subheader("🔥 Correlation Heatmap")
                corr = df[numeric_cols].corr()
                fig = px.imshow(corr,
                               text_auto=True,
                               aspect="auto",
                               title="Correlation Matrix",
                               color_continuous_scale="RdBu_r")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numeric columns found for visualization")

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
