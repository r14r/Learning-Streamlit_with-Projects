"""
Step 4: Add Column Selection (Complete)
- Allow users to select which columns to display
- Reduce data transfer and rendering
- Complete the performance optimizer
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Performance Optimizer", page_icon="⚡", layout="wide")

st.title("⚡ Performance Optimizer")

st.markdown("""
### Optimization Techniques Demonstrated:
1. **Caching** - Cache expensive computations
2. **Lazy Loading** - Load data on demand
3. **Pagination** - Display data in chunks
4. **Column Selection** ⚡ - Reduce memory usage
""")

@st.cache_data
def generate_large_dataset(n_rows):
    time.sleep(1)
    return pd.DataFrame(
        np.random.randn(n_rows, 10),
        columns=[f'Col_{i}' for i in range(10)]
    )

# 1. Caching
st.subheader("1. Data Caching")

if st.button("Generate Dataset (Cached)"):
    start = time.time()
    df = generate_large_dataset(10000)
    elapsed = time.time() - start
    st.success(f"Generated in {elapsed:.2f}s (subsequent runs will be instant)")
    st.dataframe(df.head(), use_container_width=True)

st.divider()

# 2. Pagination
st.subheader("2. Pagination")

total_rows = 10000
df_large = generate_large_dataset(total_rows)

page_size = st.slider("Rows per page", 10, 100, 50)
page_number = st.number_input("Page", 1, total_rows // page_size, 1)

start_idx = (page_number - 1) * page_size
end_idx = start_idx + page_size

st.dataframe(df_large.iloc[start_idx:end_idx], use_container_width=True)
st.caption(f"Showing rows {start_idx + 1} to {min(end_idx, total_rows)} of {total_rows}")

st.divider()

# STEP 1: Add column selection section
st.subheader("3. Column Selection ⚡")

st.markdown("""
**Problem**: Displaying many columns uses memory and slows rendering.

**Solution**: Let users select only the columns they need.
""")

# STEP 2: Add multiselect for column selection
selected_cols = st.multiselect(
    "Select columns to display",
    options=df_large.columns.tolist(),
    default=df_large.columns[:3].tolist(),  # Default to first 3 columns
    help="Choose which columns to display. Fewer columns = better performance"
)

# STEP 3: Display only selected columns
if selected_cols:
    # Filter DataFrame to show only selected columns
    filtered_df = df_large[selected_cols]

    # Show memory usage comparison
    col1, col2, col3 = st.columns(3)

    with col1:
        all_cols_size = df_large.memory_usage(deep=True).sum() / 1024 / 1024
        st.metric("All Columns Size", f"{all_cols_size:.2f} MB")

    with col2:
        selected_size = filtered_df.memory_usage(deep=True).sum() / 1024 / 1024
        st.metric("Selected Columns Size", f"{selected_size:.2f} MB")

    with col3:
        savings = ((all_cols_size - selected_size) / all_cols_size) * 100
        st.metric("Memory Saved", f"{savings:.1f}%", delta=f"-{savings:.1f}%")

    # Display filtered data
    st.dataframe(filtered_df.head(20), use_container_width=True)

else:
    st.warning("Please select at least one column to display.")

# STEP 4: Show performance comparison
st.divider()

st.subheader("📊 Column Selection Performance Impact")

col1, col2 = st.columns(2)

with col1:
    st.write("**All Columns (10 columns):**")
    st.code("""
# Load all columns
df = load_data()  # 10 columns

# Problems:
# - Higher memory usage
# - Slower rendering
# - Information overload
# - Horizontal scrolling
    """)
    st.error("Memory: 100 MB | Render: 2s")

with col2:
    st.write("**Selected Columns (3 columns):**")
    st.code("""
# Load only needed columns
df = load_data()[selected_cols]

# Benefits:
# - 70% less memory
# - Faster rendering
# - Focused view
# - Better UX
    """)
    st.success("Memory: 30 MB | Render: 0.5s")

# STEP 5: Add comprehensive best practices
with st.expander("💡 Performance Optimization Summary"):
    st.markdown("""
    ### Complete Optimization Strategy

    #### 1. Caching ⚡
    **When**: Expensive computations, data loading
    ```python
    @st.cache_data
    def load_data():
        return pd.read_csv('large_file.csv')
    ```
    **Impact**: 10-1000x speedup for repeated operations

    #### 2. Pagination ⚡
    **When**: Displaying > 100 rows
    ```python
    page_size = 50
    start = (page - 1) * page_size
    df_page = df[start:start + page_size]
    ```
    **Impact**: 5-10x faster rendering

    #### 3. Column Selection ⚡
    **When**: DataFrames with many columns
    ```python
    selected_cols = st.multiselect("Columns", df.columns)
    df_filtered = df[selected_cols]
    ```
    **Impact**: 30-70% memory reduction

    #### 4. Lazy Loading ⚡
    **When**: Large datasets, conditional displays
    ```python
    if st.button("Load Data"):
        data = load_large_dataset()
    ```
    **Impact**: Faster initial load

    ### Combined Example

    ```python
    @st.cache_data
    def load_data():
        return pd.read_csv('huge_file.csv')

    # Load once (cached)
    df = load_data()

    # Select columns
    cols = st.multiselect("Columns", df.columns)
    df_filtered = df[cols]

    # Paginate
    page = st.number_input("Page", 1, len(df) // 50)
    start = (page - 1) * 50
    st.dataframe(df_filtered[start:start + 50])
    ```

    ### Performance Checklist

    ✅ Cache expensive operations
    ✅ Use pagination for large datasets
    ✅ Allow column selection
    ✅ Lazy load when possible
    ✅ Optimize queries at database level
    ✅ Use appropriate data types
    ✅ Avoid unnecessary reruns
    ✅ Monitor memory usage
    ✅ Profile slow functions
    ✅ Test with production-size data

    ### Advanced Techniques

    1. **Chunked Processing**: Process data in batches
    2. **Async Operations**: Use async for I/O
    3. **Data Compression**: Compress stored data
    4. **Index Optimization**: Use proper DataFrame indices
    5. **Query Optimization**: Push filters to database
    6. **Connection Pooling**: Reuse database connections
    7. **CDN for Static Files**: Serve assets from CDN
    8. **Code Splitting**: Load modules on demand

    ### Monitoring Performance

    ```python
    import time

    start = time.time()
    # Your operation
    elapsed = time.time() - start
    st.metric("Time", f"{elapsed:.2f}s")
    ```

    ### Memory Profiling

    ```python
    import sys

    size = sys.getsizeof(df) / 1024 / 1024
    st.metric("Memory", f"{size:.2f} MB")
    ```
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
