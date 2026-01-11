"""
Step 1: Introduction to Custom Components
- Import components library
- Explain what custom components are
- Set up basic page structure
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Custom Components", page_icon="🎨", layout="wide")

st.title("🎨 Custom Components Demo")

# STEP 1: Explain custom components
st.markdown("""
### What are Custom Components?

Custom components allow you to extend Streamlit with:
- **HTML/CSS**: Custom styling and layouts
- **JavaScript**: Interactive functionality
- **Third-party libraries**: Integrate external tools
- **Iframes**: Embed external websites

### Why Use Custom Components?

1. **Extend functionality**: Add features not available in Streamlit
2. **Custom styling**: Create unique designs beyond Streamlit's defaults
3. **Integration**: Connect with external services and libraries
4. **Interactivity**: Add advanced JavaScript interactions

### Three Main Component Types:

1. **HTML Components**: Render raw HTML with inline CSS/JS
2. **JavaScript Components**: Interactive client-side functionality
3. **Iframe Components**: Embed external websites

Let's explore each type in the following steps!
""")

st.divider()
st.caption("Built with Streamlit 🎈")
