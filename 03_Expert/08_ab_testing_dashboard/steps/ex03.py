"""
Step 3: Add Statistical Significance Testing
- Import scipy for statistical tests
- Perform proportions z-test
- Display p-value and significance
"""

import streamlit as st
import pandas as pd
from scipy import stats

st.set_page_config(page_title="A/B Testing Dashboard", page_icon="🧪", layout="wide")

st.title("🧪 A/B Testing Dashboard")

st.sidebar.header("Test Configuration")

visitors_a = st.sidebar.number_input("Group A Visitors", 1000, 100000, 10000)
conversions_a = st.sidebar.number_input("Group A Conversions", 100, visitors_a, 1200)

visitors_b = st.sidebar.number_input("Group B Visitors", 1000, 100000, 10000)
conversions_b = st.sidebar.number_input("Group B Conversions", 100, visitors_b, 1500)

# Calculate conversion rates
conv_rate_a = conversions_a / visitors_a
conv_rate_b = conversions_b / visitors_b

# Display metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Group A Conv. Rate", f"{conv_rate_a:.2%}")

with col2:
    st.metric("Group B Conv. Rate", f"{conv_rate_b:.2%}")

with col3:
    improvement = ((conv_rate_b - conv_rate_a) / conv_rate_a) * 100
    st.metric("Improvement", f"{improvement:+.2f}%")

st.divider()

# STEP 1: Perform statistical significance test
st.subheader("📊 Statistical Significance")

# STEP 2: Use proportions_ztest from scipy.stats
# This tests if two proportions are significantly different
z_score, p_value = stats.proportions_ztest(
    count=[conversions_a, conversions_b],  # Number of successes
    nobs=[visitors_a, visitors_b]          # Number of trials
)

# STEP 3: Display statistical results
col1, col2 = st.columns(2)

with col1:
    st.metric(
        "P-Value",
        f"{p_value:.4f}",
        help="Probability that the difference is due to chance"
    )

    # STEP 4: Explain p-value interpretation
    if p_value < 0.001:
        st.caption("⭐⭐⭐ Highly significant (p < 0.001)")
    elif p_value < 0.01:
        st.caption("⭐⭐ Very significant (p < 0.01)")
    elif p_value < 0.05:
        st.caption("⭐ Significant (p < 0.05)")
    else:
        st.caption("Not significant (p >= 0.05)")

with col2:
    # STEP 5: Determine if result is significant
    is_significant = p_value < 0.05
    st.metric(
        "Statistically Significant?",
        "Yes ✅" if is_significant else "No ❌",
        help="Using alpha = 0.05 (95% confidence)"
    )

    # Calculate confidence level
    confidence = (1 - p_value) * 100
    st.caption(f"Confidence: {confidence:.1f}%")

# STEP 6: Display interpretation
st.divider()

if is_significant:
    st.success(f"""
    ✅ **The difference IS statistically significant!**

    The improvement of {improvement:+.2f}% is unlikely to be due to chance.
    With p-value = {p_value:.4f}, we can be {(1-p_value)*100:.1f}% confident
    that Group B truly performs better than Group A.

    **Recommendation**: Implement the variant (Group B).
    """)
else:
    st.warning(f"""
    ⚠️ **The difference is NOT statistically significant.**

    While there's an improvement of {improvement:+.2f}%, the p-value of {p_value:.4f}
    suggests this could be due to random chance.

    **Recommendation**: Continue testing with more data or try a different variant.
    """)

# STEP 7: Show z-score for advanced users
with st.expander("🔬 Advanced Statistics"):
    st.markdown(f"""
    ### Statistical Test Details

    **Test Used**: Two-Proportion Z-Test

    **Results:**
    - Z-Score: {z_score:.4f}
    - P-Value: {p_value:.4f}
    - Alpha (Significance Level): 0.05

    ### What is a Z-Test?

    The two-proportion z-test compares two proportions to determine if they're
    significantly different. It calculates how many standard deviations apart
    the two proportions are.

    **Z-Score Interpretation:**
    - |z| > 1.96: Significant at 0.05 level
    - |z| > 2.58: Significant at 0.01 level
    - |z| > 3.29: Significant at 0.001 level

    Current z-score: {z_score:.4f}

    ### P-Value Interpretation

    The p-value represents the probability of observing this difference (or more extreme)
    if there's actually no real difference between the groups.

    - p < 0.001: Very strong evidence against null hypothesis
    - p < 0.01: Strong evidence
    - p < 0.05: Moderate evidence
    - p >= 0.05: Weak evidence

    ### Assumptions

    1. Random sampling
    2. Independent observations
    3. Large enough sample size (np > 5 and n(1-p) > 5)
    4. Binary outcome (success/failure)
    """)

st.divider()
st.caption("Built with Streamlit 🎈")
