"""
Step 1: Understanding the Performance Problem
- Create an expensive computation without caching
- Demonstrate the performance issue
- Time the execution
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Advanced Caching", page_icon="⚡", layout="wide")

st.title("⚡ Advanced Caching Demo")

# STEP 1: Create an expensive function WITHOUT caching
def expensive_computation(n):
    """Simulates an expensive computation that takes time"""
    # Sleep for 2 seconds to simulate heavy processing
    time.sleep(2)
    # Generate random data
    return pd.DataFrame(np.random.randn(n, 5), columns=list('ABCDE'))

# STEP 2: Add controls
st.sidebar.header("Configuration")
n_rows = st.sidebar.slider("Number of rows", 100, 10000, 1000, step=100)

# STEP 3: Run computation and time it
if st.button("Run Computation", type="primary"):
    # Measure execution time
    start_time = time.time()

    with st.spinner("Processing... (this will take 2 seconds)"):
        df = expensive_computation(n_rows)

    end_time = time.time()
    elapsed = end_time - start_time

    # Display results
    col1, col2 = st.columns(2)

    with col1:
        st.metric("Execution Time", f"{elapsed:.2f}s")

    with col2:
        st.metric("Rows Generated", n_rows)

    st.dataframe(df.head(10), use_container_width=True)

    # STEP 4: Show the problem
    st.warning("⚠️ **Problem**: Every button click takes 2+ seconds, even with the same parameters!")

# STEP 5: Explain the issue
st.info("""
💡 **The Performance Problem:**
- The computation takes 2 seconds every time
- Even if you use the same parameters, it recalculates
- This wastes time and resources
- Solution: **Caching!**
""")

st.divider()
st.caption("Built with Streamlit 🎈")
