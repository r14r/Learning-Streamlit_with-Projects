"""
Step 2: Adding Button and Basic Structure

In this step, we'll:
- Add a button to trigger the API fetch
- Create the basic structure for handling the button click
- Display a message when the button is clicked

Key Concepts:
- st.button() for user interaction
- Conditional execution based on button state
- Button styling with type parameter
"""

import streamlit as st

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
    st.info(f"Fetching data from {api_choice} endpoint...")
    # We'll add the actual API call in the next step

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
