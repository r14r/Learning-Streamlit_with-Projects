# Hello Streamlit - Tips & Code Sketches

## Step 1: Basic Title

**Key Concept**: Every Streamlit app starts with importing the library and displaying content.

```python
import streamlit as st

st.title("👋 Hello Streamlit!")
```

**Tip**: Emojis work great in Streamlit! Use them to make your app more engaging.

---

## Step 2: Page Configuration

**Key Concept**: `st.set_page_config()` must be the FIRST Streamlit command in your script.

```python
st.set_page_config(
    page_title="Your Tab Title",  # Shows in browser tab
    page_icon="👋",                # Favicon
    layout="centered"              # or "wide"
)
```

**Tip**: The page configuration affects the entire app and can only be called once.

---

## Step 3: Text Display Methods

**Key Concept**: Streamlit offers multiple ways to display text with different sizes and styles.

```python
st.title("Largest - Title")
st.header("Medium - Header")
st.subheader("Smaller - Subheader")
st.write("Regular text")
```

**Tip**: `st.write()` is the "Swiss Army knife" - it automatically detects what you're displaying!

---

## Step 4: Markdown Formatting

**Key Concept**: Markdown allows rich text formatting with simple syntax.

```python
st.markdown("""
### This is a heading

This text has **bold** and *italic* formatting.

#### Features:
- Bullet points
- **Bold text**
- *Italic text*
- [Links](https://streamlit.io)
""")
```

**Tip**: Use triple quotes `"""` for multi-line markdown strings.

---

## Step 5: Code Display

**Key Concept**: Display syntax-highlighted code examples in your app.

```python
code = '''import streamlit as st

st.title("Hello World")
st.write("This is easy!")'''

st.code(code, language='python')
```

**Tip**: Store code in a variable (using triple quotes) for better readability.

---

## Step 6: Status Messages & UI Elements

**Key Concept**: Streamlit provides colored message boxes and separators.

```python
# Status messages
st.info("💡 Information message (blue)")
st.success("✅ Success message (green)")
st.warning("⚠️ Warning message (yellow)")
st.error("❌ Error message (red)")

# Visual separation
st.divider()  # Horizontal line

# Small footnote text
st.caption("Small caption text")
```

**Tip**: Use appropriate status messages to guide users and provide feedback.

---

## Best Practices

1. **Import Once**: Always import streamlit at the top of your file
2. **Config First**: `st.set_page_config()` must be the first Streamlit command
3. **Clear Hierarchy**: Use titles, headers, and subheaders to organize content
4. **Visual Feedback**: Use status messages and dividers to guide users
5. **Code Readability**: Use proper indentation and comments in your code