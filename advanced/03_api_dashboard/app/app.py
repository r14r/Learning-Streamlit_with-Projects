"""
API Dashboard - Advanced Project 03

Fetch and display data from REST APIs.
"""

import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="API Dashboard", page_icon="🌐", layout="wide")

st.title("🌐 API Dashboard")
st.write("Fetch and display data from REST APIs")

api_choice = st.selectbox("Select API Endpoint", 
    ["Posts", "Users", "Comments", "Todos", "Albums"])

base_url = "https://jsonplaceholder.typicode.com"

if st.button("Fetch Data", type="primary"):
    with st.spinner("Fetching data..."):
        try:
            endpoint = api_choice.lower()
            response = requests.get(f"{base_url}/{endpoint}")
            response.raise_for_status()
            data = response.json()
            
            st.success(f"✅ Fetched {len(data)} records")
            
            df = pd.DataFrame(data)
            
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.subheader("📊 Data Table")
                st.dataframe(df.head(20), use_container_width=True)
            
            with col2:
                st.subheader("📋 Info")
                st.metric("Total Records", len(df))
                st.metric("Columns", len(df.columns))
            
            with st.expander("🗂️ Raw JSON"):
                st.json(data[:3])
                
        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()
st.caption("Built with Streamlit 🎈")
