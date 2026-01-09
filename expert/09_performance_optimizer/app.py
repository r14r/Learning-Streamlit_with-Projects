"""
Performance Optimizer - Expert Project 09

Demonstrate app optimization techniques.
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
4. **Column Selection** - Reduce memory usage
""")

@st.cache_data
def generate_large_dataset(n_rows):
    time.sleep(1)
    return pd.DataFrame(
        np.random.randn(n_rows, 10),
        columns=[f'Col_{i}' for i in range(10)]
    )

st.subheader("1. Data Caching")

if st.button("Generate Dataset (Cached)"):
    start = time.time()
    df = generate_large_dataset(10000)
    elapsed = time.time() - start
    st.success(f"Generated in {elapsed:.2f}s (subsequent runs will be instant)")
    st.dataframe(df.head(), use_container_width=True)

st.subheader("2. Pagination")

total_rows = 10000
page_size = st.slider("Rows per page", 10, 100, 50)
page_number = st.number_input("Page", 1, total_rows // page_size, 1)

df_large = generate_large_dataset(total_rows)
start_idx = (page_number - 1) * page_size
end_idx = start_idx + page_size

st.dataframe(df_large.iloc[start_idx:end_idx], use_container_width=True)
st.caption(f"Showing rows {start_idx + 1} to {min(end_idx, total_rows)} of {total_rows}")

st.subheader("3. Column Selection")

selected_cols = st.multiselect(
    "Select columns to display",
    df_large.columns.tolist(),
    default=df_large.columns[:3].tolist()
)

if selected_cols:
    st.dataframe(df_large[selected_cols].head(20), use_container_width=True)

st.divider()
st.caption("Built with Streamlit 🎈")
