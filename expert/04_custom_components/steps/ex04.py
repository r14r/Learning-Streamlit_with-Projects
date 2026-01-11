"""
Step 4: Add Iframe Component (Complete)
- Embed external websites using iframes
- Add user input for URL
- Complete the custom components demo
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
<div id="counter-container" style="padding: 20px; background-color: #f8f9fa;
                                   border-radius: 10px; text-align: center;">
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

# STEP 1: Add iframe component section
st.subheader("3. Iframe Component")

# STEP 2: Add user input for URL
iframe_url = st.text_input(
    "Enter URL to embed",
    "https://streamlit.io",
    help="Enter any website URL to embed it below"
)

# STEP 3: Display iframe if URL is provided
if iframe_url:
    st.write(f"Embedding: `{iframe_url}`")

    # components.iframe() embeds external websites
    components.iframe(iframe_url, height=400, scrolling=True)

# STEP 4: Add explanation and examples
st.markdown("""
#### How it works:

```python
components.iframe(url, height=400, scrolling=True)
```

**Use cases:**
- Embed documentation pages
- Show external dashboards
- Display maps or visualizations
- Integrate third-party tools

**Example URLs to try:**
- `https://streamlit.io` - Streamlit homepage
- `https://plotly.com/python/` - Plotly documentation
- `https://www.openstreetmap.org` - Interactive maps
""")

# STEP 5: Add best practices
with st.expander("📚 Custom Components Best Practices"):
    st.markdown("""
    ### Best Practices

    #### 1. HTML Components
    - Use inline CSS for simplicity
    - Keep components focused and reusable
    - Test across different browsers

    #### 2. JavaScript Components
    - Minimize external dependencies
    - Handle errors gracefully
    - Consider performance impact

    #### 3. Iframe Components
    - Check website allows embedding (some block iframes)
    - Set appropriate height
    - Be aware of security considerations

    #### 4. General Tips
    - Document your custom components
    - Use consistent styling
    - Consider mobile responsiveness
    - Test component lifecycle

    ### Advanced: Building Bidirectional Components

    For components that need to communicate with Python:
    - Use the Streamlit Components API
    - Create a React/Vue component
    - Package as a reusable component
    - See: https://docs.streamlit.io/library/components
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
