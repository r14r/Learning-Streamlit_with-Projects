"""
Step 2: Demonstrate Data Caching
- Create expensive computation
- Compare cached vs uncached
- Measure performance improvement
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Performance Optimizer", page_icon="⚡", layout="wide")

st.title("⚡ Performance Optimizer")

st.markdown("""
### Optimization Techniques Demonstrated:
1. **Caching** ⚡ - Cache expensive computations
2. Lazy Loading (coming next)
3. Pagination (coming next)
4. Column Selection (coming next)
""")

st.divider()

# STEP 1: Create cached function
@st.cache_data
def generate_large_dataset(n_rows):
    """Generate a large dataset with artificial delay"""
    # Simulate expensive computation
    time.sleep(1)

    # Generate random data
    return pd.DataFrame(
        np.random.randn(n_rows, 10),
        columns=[f'Col_{i}' for i in range(10)]
    )

# STEP 2: Add caching demonstration
st.subheader("1. Data Caching ⚡")

st.markdown("""
**Problem**: Generating large datasets takes time.

**Solution**: Cache the result so it only runs once per parameter set.
""")

# STEP 3: Add button to trigger generation
if st.button("Generate Dataset (Cached)", type="primary"):
    # Measure time
    start = time.time()

    # Generate data (will use cache if available)
    with st.spinner("Generating data..."):
        df = generate_large_dataset(10000)

    elapsed = time.time() - start

    # STEP 4: Display results and timing
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Generation Time", f"{elapsed:.2f}s")

    with col2:
        st.metric("Rows Generated", "10,000")

    # Show sample data
    st.dataframe(df.head(), use_container_width=True)

    # STEP 5: Explain caching benefit
    if elapsed < 0.1:  # If very fast, it used cache
        st.success("""
        ✅ **Used cache!** The data was retrieved instantly because it was
        already generated before. Try clicking again - same result!
        """)
    else:
        st.info("""
        ⏳ **First run took ~1 second** due to generation time.
        Click again to see caching in action - it will be instant!
        """)

# STEP 6: Add comparison visualization
st.divider()

st.subheader("📊 Caching Performance Impact")

col1, col2 = st.columns(2)

with col1:
    st.write("**Without Caching:**")
    st.code("""
def generate_data(n):
    time.sleep(1)  # Expensive operation
    return data

# Every call takes 1+ second
generate_data(1000)  # 1s
generate_data(1000)  # 1s (again!)
generate_data(1000)  # 1s (again!)
    """)
    st.error("Total: 3+ seconds for same data")

with col2:
    st.write("**With Caching:**")
    st.code("""
@st.cache_data
def generate_data(n):
    time.sleep(1)  # Expensive operation
    return data

# Only first call takes time
generate_data(1000)  # 1s
generate_data(1000)  # instant! ⚡
generate_data(1000)  # instant! ⚡
    """)
    st.success("Total: ~1 second (2s saved!)")

# STEP 7: Explain when caching helps
with st.expander("💡 When to Use Caching"):
    st.markdown("""
    ### Ideal for Caching

    ✅ **Good candidates:**
    - Database queries
    - API calls
    - File loading
    - Data transformations
    - ML model predictions
    - Complex calculations

    ❌ **Avoid caching:**
    - Random number generation (needs to change)
    - Current time/date
    - User-specific data (unless keyed properly)
    - Functions with side effects

    ### Cache Invalidation

    Cache automatically clears when:
    - Function parameters change
    - Function code changes
    - Manually cleared with `st.cache_data.clear()`

    ### Best Practices

    1. **Cache aggressively**: Cache anything taking > 0.1s
    2. **Watch memory**: Cached data stays in RAM
    3. **Use TTL**: Set time-to-live for time-sensitive data
    4. **Monitor size**: Check cache size regularly

    ### Example with TTL

    ```python
    @st.cache_data(ttl=3600)  # Cache for 1 hour
    def fetch_stock_prices():
        return api.get_prices()
    ```
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
