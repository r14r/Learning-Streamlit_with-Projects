"""
Step 4: Creating a Grid Layout for Images
Learning objective: Use columns in rows to create a grid layout
"""

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Image Gallery",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Image Gallery")
st.write("Upload and view your images")

uploaded_files = st.file_uploader(
    "Choose images...",
    type=['png', 'jpg', 'jpeg'],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"✅ Uploaded {len(uploaded_files)} image(s)")

    # Display images in a grid (3 columns per row)
    cols_per_row = 3
    # Calculate how many rows we need
    rows = (len(uploaded_files) + cols_per_row - 1) // cols_per_row

    # Create rows
    for row in range(rows):
        # Create columns for this row
        cols = st.columns(cols_per_row)

        # Fill each column in this row
        for col_idx in range(cols_per_row):
            # Calculate which image index this is
            img_idx = row * cols_per_row + col_idx

            # Check if we have an image for this position
            if img_idx < len(uploaded_files):
                uploaded_file = uploaded_files[img_idx]

                with cols[col_idx]:
                    # Open and display image
                    image = Image.open(uploaded_file)
                    st.image(image, caption=uploaded_file.name, use_container_width=True)
else:
    st.info("👆 Upload one or more images to get started")
