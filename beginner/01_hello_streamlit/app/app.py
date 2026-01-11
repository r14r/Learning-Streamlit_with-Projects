"""
Hello Streamlit - Beginner Project 01

A basic Streamlit application demonstrating text display and formatting features.
"""

import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋",
    layout="centered"
)

# Title
st.title("👋 Hello Streamlit!")

# Header
st.header("Welcome to Your First Streamlit App")

# Subheader
st.subheader("Learning Streamlit Basics")

# Regular text
st.write("This is a simple Streamlit application that demonstrates basic text display features.")

# Markdown
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

# Code snippet
st.subheader("Code Example")
st.write("Here's how simple it is to create text in Streamlit:")

code = '''import streamlit as st

st.title("Hello World")
st.write("Creating apps is this easy!")'''

st.code(code, language='python')

# Info box
st.info("💡 **Tip**: Every time you save your script, Streamlit automatically reruns your app!")

# Success message
st.success("✅ You've successfully run your first Streamlit app!")

# Divider
st.divider()

# Footer
st.caption("Built with Streamlit 🎈")
