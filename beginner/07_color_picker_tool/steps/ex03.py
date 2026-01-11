"""
Step 3: Adding Color Preview with HTML
Learning objective: Use markdown with HTML to display colored elements
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

# Display color preview using HTML
# Create a colored div with the selected color
# unsafe_allow_html=True allows HTML to be rendered
st.markdown(f"""
<div style="background-color: {color}; padding: 100px; border-radius: 10px; text-align: center; margin: 20px 0;">
    <h2 style="color: white;">Color Preview</h2>
</div>
""", unsafe_allow_html=True)

st.write(f"**HEX**: {color}")
st.write(f"**RGB**: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")
