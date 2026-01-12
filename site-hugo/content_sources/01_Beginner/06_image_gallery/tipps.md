# Image Gallery - Tips & Code Sketches

## Step 1: File Uploader

**Key Concept**: `file_uploader()` handles file uploads with type filtering.

```python
uploaded_files = st.file_uploader(
    "Choose images...",
    type=['png', 'jpg', 'jpeg'],      # Allowed extensions
    accept_multiple_files=True         # Allow multiple files
)

if uploaded_files:
    st.success(f"✅ Uploaded {len(uploaded_files)} image(s)")
else:
    st.info("👆 Upload images to get started")
```

**Tip**: Use `accept_multiple_files=True` for gallery applications.

---

## Step 2: Display Single Image

**Key Concept**: Use PIL to open uploaded files and st.image() to display.

```python
from PIL import Image

if uploaded_files:
    # Get first file
    uploaded_file = uploaded_files[0]

    # Open with PIL
    image = Image.open(uploaded_file)

    # Display
    st.image(
        image,
        caption=uploaded_file.name,      # Show filename
        use_container_width=True         # Responsive width
    )
```

**Tip**: `use_container_width=True` makes images responsive to screen size.

---

## Step 3: Loop Through Images

**Key Concept**: Iterate over all uploaded files to display them.

```python
for uploaded_file in uploaded_files:
    image = Image.open(uploaded_file)
    st.image(image, caption=uploaded_file.name, use_container_width=True)
```

**Tip**: Simple loops work well for vertical list layouts.

---

## Step 4: Grid Layout

**Key Concept**: Calculate rows and use nested loops for grid display.

```python
cols_per_row = 3
rows = (len(uploaded_files) + cols_per_row - 1) // cols_per_row

for row in range(rows):
    cols = st.columns(cols_per_row)

    for col_idx in range(cols_per_row):
        # Calculate which image this is
        img_idx = row * cols_per_row + col_idx

        # Check if we have an image for this position
        if img_idx < len(uploaded_files):
            uploaded_file = uploaded_files[img_idx]

            with cols[col_idx]:
                image = Image.open(uploaded_file)
                st.image(image, caption=uploaded_file.name, use_container_width=True)
```

**Tip**: Use `//` (floor division) to calculate rows needed.

---

## Step 5: Extract Image Metadata

**Key Concept**: Access file and image properties for metadata.

```python
# File information
filename = uploaded_file.name
file_size = uploaded_file.size / 1024  # Convert bytes to KB

# Image information
image = Image.open(uploaded_file)
width, height = image.size
image_format = image.format

# Display
st.write(f"**Filename**: {filename}")
st.write(f"**Size**: {file_size:.2f} KB")
st.write(f"**Dimensions**: {width} x {height} pixels")
st.write(f"**Format**: {image_format}")
```

**Tip**: PIL images have `size` (tuple of width, height) and `format` properties.

---

## Step 6: Expandable Information

**Key Concept**: Hide detailed info in expanders to save space.

```python
with st.expander("ℹ️ Image Info"):
    st.write(f"**Filename**: {uploaded_file.name}")
    st.write(f"**Size**: {uploaded_file.size / 1024:.2f} KB")
    st.write(f"**Dimensions**: {image.size[0]} x {image.size[1]} pixels")
    st.write(f"**Format**: {image.format}")
    st.write(f"**Mode**: {image.mode}")  # RGB, RGBA, etc.
```

**Tip**: Expanders keep the gallery clean while providing detailed info on demand.

---

## PIL Image Attributes

```python
image = Image.open(file)

image.size       # (width, height) tuple
image.width      # Width in pixels
image.height     # Height in pixels
image.format     # 'PNG', 'JPEG', etc.
image.mode       # 'RGB', 'RGBA', 'L', etc.
image.info       # Dictionary of image metadata
```

---

## Grid Layout Math

```python
# Calculate rows needed
total_items = len(uploaded_files)
cols_per_row = 3
rows = (total_items + cols_per_row - 1) // cols_per_row

# Calculate item index from row and column
item_index = row * cols_per_row + col_idx

# Check if index is valid
if item_index < total_items:
    # Process item
```

---

## Best Practices

1. **File Validation**: Specify allowed file types in uploader
2. **Responsive Images**: Use `use_container_width=True`
3. **Grid Consistency**: Calculate rows properly to avoid empty cells
4. **Memory Management**: Don't load all images at once for large galleries
5. **User Feedback**: Show upload status and image count
6. **Error Handling**: Check if files exist before processing
7. **Metadata Display**: Use expanders to keep UI clean
8. **File Size**: Display file sizes in KB or MB for readability