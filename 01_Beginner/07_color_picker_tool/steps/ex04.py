"""
Step 4: Displaying Color Values in Columns
Learning objective: Organize color format outputs in columns
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

# Determine text color based on background brightness
# Sum of RGB < 382 means dark background, use white text
text_color = 'white' if sum(rgb) < 382 else 'black'

st.markdown(f"""
<div style="background-color: {color}; padding: 100px; border-radius: 10px; text-align: center; margin: 20px 0;">
    <h2 style="color: {text_color};">Color Preview</h2>
</div>
""", unsafe_allow_html=True)

# Display color values in columns
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("HEX")
    # code() displays text in a monospace font
    st.code(color.upper())

with col2:
    st.subheader("RGB")
    st.code(f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")

with col3:
    st.subheader("HSL")
    st.code("hsl(207°, 70%, 54%)")  # Placeholder for now
