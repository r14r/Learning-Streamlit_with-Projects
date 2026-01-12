"""
Step 3: Making the API Request

In this step, we'll:
- Import the requests library
- Make an actual API call
- Handle the response and potential errors
- Display the number of records fetched

Key Concepts:
- requests.get() for making HTTP requests
- response.raise_for_status() for error handling
- response.json() to parse JSON response
- Error handling with try/except
- st.spinner() for loading indicators
"""

import streamlit as st
import requests

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
    # Show a spinner while fetching
    with st.spinner("Fetching data..."):
        try:
            # Convert endpoint name to lowercase for API URL
            endpoint = api_choice.lower()

            # Make the API request
            response = requests.get(f"{base_url}/{endpoint}")

            # Raise an error if the request failed
            response.raise_for_status()

            # Parse JSON response
            data = response.json()

            # Display success message
            st.success(f"✅ Fetched {len(data)} records")

            # We'll display the actual data in the next step
            st.write("Data fetched successfully! Display coming in next step.")

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
