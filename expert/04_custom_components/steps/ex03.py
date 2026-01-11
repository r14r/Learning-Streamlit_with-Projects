"""
Step 3: Add Interactive JavaScript Component
- Create component with JavaScript functionality
- Implement click counter
- Demonstrate client-side interactivity
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

# STEP 1: Add JavaScript component section
st.subheader("2. Interactive JavaScript Component")

# STEP 2: Create HTML with embedded JavaScript
# This shows how to add client-side interactivity
js_code = """
<div id="counter-container" style="padding: 20px;
                                   background-color: #f8f9fa;
                                   border-radius: 10px;
                                   text-align: center;">
    <h3>🖱️ Click Counter</h3>
    <button onclick="incrementCounter()"
            style="padding: 10px 20px;
                   font-size: 16px;
                   background-color: #4CAF50;
                   color: white;
                   border: none;
                   border-radius: 5px;
                   cursor: pointer;">
        Click Me!
    </button>
    <p style="font-size: 24px; margin-top: 10px;">
        Count: <span id="count" style="font-weight: bold; color: #4CAF50;">0</span>
    </p>
    <button onclick="resetCounter()"
            style="padding: 5px 15px;
                   font-size: 14px;
                   background-color: #f44336;
                   color: white;
                   border: none;
                   border-radius: 5px;
                   cursor: pointer;">
        Reset
    </button>
</div>

<script>
// STEP 3: JavaScript functionality
let count = 0;

function incrementCounter() {
    count++;
    document.getElementById('count').textContent = count;
}

function resetCounter() {
    count = 0;
    document.getElementById('count').textContent = count;
}
</script>
"""

components.html(js_code, height=220)

# STEP 4: Explain the JavaScript component
st.markdown("""
#### How it works:

The JavaScript component combines HTML and JavaScript:

```html
<button onclick="incrementCounter()">Click Me!</button>
<span id="count">0</span>

<script>
let count = 0;
function incrementCounter() {
    count++;
    document.getElementById('count').textContent = count;
}
</script>
```

**Key features:**
- Client-side interactivity (runs in browser)
- No page refresh needed
- Can use any JavaScript library
- State is maintained within the component

**Limitations:**
- State doesn't sync back to Python automatically
- For Python integration, use bidirectional custom components
""")

st.divider()
st.caption("Built with Streamlit 🎈")
