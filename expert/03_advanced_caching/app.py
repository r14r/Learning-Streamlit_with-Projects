"""
Advanced Caching - Expert Project 03

Demonstrate caching strategies for performance.
"""

import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(page_title="Advanced Caching", page_icon="⚡", layout="wide")

st.title("⚡ Advanced Caching Demo")

@st.cache_data
def expensive_computation_cached(n):
    time.sleep(2)
    return pd.DataFrame(np.random.randn(n, 5), columns=list('ABCDE'))

def expensive_computation_uncached(n):
    time.sleep(2)
    return pd.DataFrame(np.random.randn(n, 5), columns=list('ABCDE'))

st.sidebar.header("Configuration")
use_cache = st.sidebar.checkbox("Use Caching", value=True)
n_rows = st.sidebar.slider("Number of rows", 100, 10000, 1000, step=100)

if st.button("Run Computation", type="primary"):
    start_time = time.time()
    
    with st.spinner("Processing..."):
        if use_cache:
            df = expensive_computation_cached(n_rows)
        else:
            df = expensive_computation_uncached(n_rows)
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Execution Time", f"{elapsed:.2f}s")
    with col2:
        st.metric("Rows Generated", n_rows)
    
    st.dataframe(df.head(10), use_container_width=True)
    
    if use_cache:
        st.success("✅ Used cached result (subsequent runs will be faster)")
    else:
        st.warning("⚠️ No caching (every run takes full time)")

with st.expander("ℹ️ About Caching"):
    st.markdown("""
    ### Streamlit Caching
    
    **@st.cache_data**: Cache data computations
    - Use for expensive data processing
    - Automatic invalidation on parameter change
    - Returns new copy each time
    
    **@st.cache_resource**: Cache global resources
    - Use for ML models, database connections
    - Returns same object each time
    - Manually manage lifecycle
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
