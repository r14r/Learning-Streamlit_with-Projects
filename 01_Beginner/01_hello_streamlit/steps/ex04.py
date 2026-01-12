"""
Step 4: Adding Markdown for Rich Text Formatting
Learning objective: Use markdown() for formatted text with bold, italic, lists, etc.
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

# Markdown allows rich text formatting
# You can use bold (**text**), italic (*text*), lists, links, etc.
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
