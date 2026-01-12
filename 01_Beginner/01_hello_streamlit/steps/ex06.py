"""
Step 6: Adding Status Messages and Dividers
Learning objective: Use info(), success() for notifications and divider() for visual separation
"""

import streamlit as st

st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered"
)

st.title("👋 Hello Streamlit!")
st.header("Welcome to Your First Streamlit App")
st.subheader("Learning Streamlit Basics")
st.write("This is a simple Streamlit application that demonstrates basic text display features.")

st.markdown("""
### What is Streamlit?

Streamlit is an **open-source Python library** that makes it easy to create and share beautiful,
custom web apps for machine learning and data science. In just a few minutes you can build and
deploy powerful data apps.

#### Key Features:
- 🚀 **Simple**: Write apps in pure Python
- 🎨 **Beautiful**: Automatic styling and themes
- 📊 **Interactive**: Widgets update instantly
- 🔧 **Flexible**: Integrate with your favorite libraries
""")

st.subheader("Code Example")
st.write("Here's how simple it is to create text in Streamlit:")

code = '''import streamlit as st

st.title("Hello World")
st.write("Creating apps is this easy!")'''

st.code(code, language='python')

# Info box - displays informational message in blue
st.info("💡 **Tip**: Every time you save your script, Streamlit automatically reruns your app!")

# Success message - displays success message in green
st.success("✅ You've successfully run your first Streamlit app!")

# Divider - creates a horizontal line to separate sections
st.divider()

# Caption - small, faded text for footnotes
st.caption("Built with Streamlit 🎈")
