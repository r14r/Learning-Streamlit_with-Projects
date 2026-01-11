"""
Step 4: Displaying Data in a DataFrame

In this step, we'll:
- Convert the JSON data to a pandas DataFrame
- Display the data in a table
- Show only the first 20 rows for better performance

Key Concepts:
- pd.DataFrame() to convert JSON to DataFrame
- st.dataframe() for displaying tables
- Limiting displayed rows with .head()
"""

import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="API Dashboard", page_icon="🌐", layout="wide")

st.title("🌐 API Dashboard")
st.write("Fetch and display data from REST APIs")

# API endpoint selection
api_choice = st.selectbox("Select API Endpoint",
    ["Posts", "Users", "Comments", "Todos", "Albums"])

# Base URL for the API
base_url = "https://jsonplaceholder.typicode.com"

# Fetch button
if st.button("Fetch Data", type="primary"):
    with st.spinner("Fetching data..."):
        try:
            endpoint = api_choice.lower()
            response = requests.get(f"{base_url}/{endpoint}")
            response.raise_for_status()
            data = response.json()

            st.success(f"✅ Fetched {len(data)} records")

            # Convert to DataFrame
            df = pd.DataFrame(data)

            # Display the data
            st.subheader("📊 Data Table")
            st.write("Showing first 20 rows:")
            st.dataframe(df.head(20), use_container_width=True)

        except Exception as e:
            st.error(f"Error: {str(e)}")

else:
    st.markdown("""
    ### About this app:
    This dashboard fetches data from the JSONPlaceholder API, which is a free fake API for testing and prototyping.

    **Available endpoints:**
    - **Posts**: Blog posts
    - **Users**: User information
    - **Comments**: Comments on posts
    - **Todos**: Todo items
    - **Albums**: Photo albums

    Click the button above to fetch data!
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
