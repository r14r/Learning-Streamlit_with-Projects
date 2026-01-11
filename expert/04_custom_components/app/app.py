"""
Custom Components - Expert Project 04

Demonstrate custom Streamlit component patterns.
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Custom Components", page_icon="🎨", layout="wide")

st.title("🎨 Custom Components Demo")

st.subheader("1. Custom HTML Component")

html_code = """
<div style="background: linear-gradient(45deg, #667eea 0%, #764ba2 100%); 
            padding: 30px; border-radius: 10px; color: white; text-align: center;">
    <h2>Custom HTML Component</h2>
    <p>This is rendered from raw HTML!</p>
</div>
"""

components.html(html_code, height=150)

st.subheader("2. Interactive JavaScript Component")

js_code = """
<div id="counter-container">
    <h3>Click Counter</h3>
    <button onclick="incrementCounter()" style="padding: 10px 20px; font-size: 16px;">
        Click Me!
    </button>
    <p>Count: <span id="count">0</span></p>
</div>

<script>
let count = 0;
function incrementCounter() {
    count++;
    document.getElementById('count').textContent = count;
}
</script>
"""

components.html(js_code, height=200)

st.subheader("3. Iframe Component")

iframe_url = st.text_input("Enter URL", "https://streamlit.io")
if iframe_url:
    components.iframe(iframe_url, height=400)

st.divider()
st.caption("Built with Streamlit 🎈")
