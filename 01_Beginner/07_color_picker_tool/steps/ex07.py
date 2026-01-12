"""
Step 7: Adding Copy Values Section
Learning objective: Display all color values in an expander for easy copying
"""

import streamlit as st

st.set_page_config(
    page_title="Color Picker Tool",
    page_icon="🎨",
    layout="centered"
)

st.title("🎨 Color Picker Tool")
st.write("Pick a color and see its values in different formats")

color = st.color_picker("Pick a color", "#3498db")

hex_color = color.lstrip('#')
rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hsl(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2

    if max_c == min_c:
        h = s = 0
    else:
        d = max_c - min_c
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)

        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        h /= 6

    return int(h * 360), int(s * 100), int(l * 100)

hsl = rgb_to_hsl(*rgb)

st.markdown(f"""
<div style="background-color: {color}; padding: 100px; border-radius: 10px; text-align: center; margin: 20px 0;">
    <h2 style="color: {'white' if sum(rgb) < 382 else 'black'};">Color Preview</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("HEX")
    st.code(color.upper())

with col2:
    st.subheader("RGB")
    st.code(f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")

with col3:
    st.subheader("HSL")
    st.code(f"hsl({hsl[0]}°, {hsl[1]}%, {hsl[2]}%)")

st.subheader("🔍 Color Components")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Red", rgb[0])
    st.progress(rgb[0] / 255)

with col2:
    st.metric("Green", rgb[1])
    st.progress(rgb[1] / 255)

with col3:
    st.metric("Blue", rgb[2])
    st.progress(rgb[2] / 255)

# Copy values section in expander
with st.expander("📋 Copy Values"):
    st.code(f"HEX: {color.upper()}")
    st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")
    st.code(f"HSL: hsl({hsl[0]}°, {hsl[1]}%, {hsl[2]}%)")

st.divider()
st.caption("Built with Streamlit 🎈")
