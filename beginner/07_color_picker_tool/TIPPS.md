# Color Picker Tool - Tips & Code Sketches

## Step 1: Color Picker Widget

**Key Concept**: `color_picker()` provides a visual color selection interface.

```python
color = st.color_picker(
    "Pick a color",
    "#3498db"  # Default color in HEX format
)

st.write(f"Selected: {color}")
```

**Tip**: Color picker returns hex color codes like "#3498db".

---

## Step 2: HEX to RGB Conversion

**Key Concept**: Parse hex string to extract RGB values.

```python
# Remove '#' from color
hex_color = color.lstrip('#')

# Convert each pair of hex digits to decimal
# Hex format: RRGGBB (each pair is 0-255 in base 16)
rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

st.write(f"**HEX**: {color}")
st.write(f"**RGB**: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")
```

**Tip**: `int(string, 16)` converts hexadecimal to decimal.

---

## Step 3: Color Preview with HTML

**Key Concept**: Use HTML/CSS for custom styling and previews.

```python
# Determine text color based on background brightness
text_color = 'white' if sum(rgb) < 382 else 'black'

st.markdown(f"""
<div style="background-color: {color};
            padding: 100px;
            border-radius: 10px;
            text-align: center;">
    <h2 style="color: {text_color};">Color Preview</h2>
</div>
""", unsafe_allow_html=True)
```

**Tip**: Sum of RGB < 382 indicates a dark color (use white text).

---

## Step 4: Format Display in Columns

**Key Concept**: Organize different color formats in columns.

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("HEX")
    st.code(color.upper())  # Display in monospace

with col2:
    st.subheader("RGB")
    st.code(f"rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")

with col3:
    st.subheader("HSL")
    st.code("hsl(207°, 70%, 54%)")  # Placeholder
```

**Tip**: `st.code()` displays text in monospace font, perfect for color codes.

---

## Step 5: RGB to HSL Conversion

**Key Concept**: Implement the RGB to HSL color space conversion algorithm.

```python
def rgb_to_hsl(r, g, b):
    """Convert RGB (0-255) to HSL (H: 0-360, S: 0-100, L: 0-100)"""
    # Normalize RGB to 0-1
    r, g, b = r/255.0, g/255.0, b/255.0

    max_c = max(r, g, b)
    min_c = min(r, g, b)
    l = (max_c + min_c) / 2  # Lightness

    if max_c == min_c:
        h = s = 0  # Achromatic (gray)
    else:
        d = max_c - min_c
        # Saturation
        s = d / (2 - max_c - min_c) if l > 0.5 else d / (max_c + min_c)

        # Hue
        if max_c == r:
            h = (g - b) / d + (6 if g < b else 0)
        elif max_c == g:
            h = (b - r) / d + 2
        else:
            h = (r - g) / d + 4
        h /= 6

    # Convert to degrees and percentages
    return int(h * 360), int(s * 100), int(l * 100)

hsl = rgb_to_hsl(rgb[0], rgb[1], rgb[2])
st.code(f"hsl({hsl[0]}°, {hsl[1]}%, {hsl[2]}%)")
```

**Tip**: HSL is more intuitive for humans than RGB (Hue, Saturation, Lightness).

---

## Step 6: Component Visualization

**Key Concept**: Use metrics and progress bars to visualize color components.

```python
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Red", rgb[0])
    st.progress(rgb[0] / 255)  # 0.0 to 1.0

with col2:
    st.metric("Green", rgb[1])
    st.progress(rgb[1] / 255)

with col3:
    st.metric("Blue", rgb[2])
    st.progress(rgb[2] / 255)
```

**Tip**: Progress bars visually show the intensity of each color component.

---

## Step 7: Copy Values Section

**Key Concept**: Provide all formats in one place for easy copying.

```python
with st.expander("📋 Copy Values"):
    st.code(f"HEX: {color.upper()}")
    st.code(f"RGB: rgb({rgb[0]}, {rgb[1]}, {rgb[2]})")
    st.code(f"HSL: hsl({hsl[0]}°, {hsl[1]}%, {hsl[2]}%)")
```

**Tip**: `st.code()` allows users to easily select and copy text.

---

## Color Format Reference

```python
# HEX: #RRGGBB (hexadecimal)
"#3498db"

# RGB: Red, Green, Blue (0-255)
"rgb(52, 152, 219)"

# HSL: Hue (0-360°), Saturation (0-100%), Lightness (0-100%)
"hsl(204°, 70%, 53%)"

# Color component ranges
R, G, B: 0-255
H: 0-360 degrees
S, L: 0-100 percent
```

---

## Best Practices

1. **Text Contrast**: Calculate appropriate text color for backgrounds
2. **Format Consistency**: Display all color formats consistently
3. **User Experience**: Make color codes easy to copy
4. **Visual Feedback**: Use progress bars for component values
5. **Code Display**: Use monospace fonts for color codes
6. **Color Preview**: Show large preview area for selected color
7. **Multiple Formats**: Support HEX, RGB, and HSL for flexibility
8. **Default Colors**: Choose visually appealing default colors
