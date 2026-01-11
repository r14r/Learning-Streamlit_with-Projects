"""
Step 5: Adding Settings Page

In this final step, we'll:
- Add content for the Settings page
- Include interactive widgets
- Complete the multi-page app

Key Concepts:
- Complete multi-page navigation
- Different widgets on different pages
- Full app structure
"""

import streamlit as st

st.set_page_config(page_title="Multi-Page App", page_icon="📄", layout="wide")

pages = {
    "Home": "home",
    "About": "about",
    "Dashboard": "dashboard",
    "Settings": "settings"
}

st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Page content
if selection == "Home":
    st.title("🏠 Home Page")
    st.write("Welcome to the multi-page application!")
    st.info("Use the sidebar to navigate between pages.")

elif selection == "About":
    st.title("ℹ️ About Page")
    st.write("This is a demonstration of multi-page navigation in Streamlit.")
    st.markdown("""
    ### Features:
    - Multiple pages
    - Sidebar navigation
    - Different content per page
    """)

elif selection == "Dashboard":
    st.title("📊 Dashboard Page")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Metric 1", "100")
    with col2:
        st.metric("Metric 2", "200")
    with col3:
        st.metric("Metric 3", "300")

elif selection == "Settings":
    st.title("⚙️ Settings Page")
    st.write("Configure your preferences")

    theme = st.selectbox("Theme", ["Light", "Dark"])
    notifications = st.checkbox("Enable notifications")

    if st.button("Save Settings"):
        st.success("Settings saved!")

st.divider()
st.caption("Built with Streamlit 🎈")
