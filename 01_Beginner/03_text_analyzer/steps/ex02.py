"""
Step 2: Adding Basic Character and Word Count
Learning objective: Calculate basic text statistics using Python string methods
"""

import streamlit as st

st.set_page_config(
    page_title="Text Analyzer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Text Analyzer")
st.write("Enter text to analyze its characteristics")

text = st.text_area("Enter your text here:", height=200,
                    placeholder="Type or paste your text...")

if text:
    # Basic statistics
    # len() gets the total length including spaces
    char_count = len(text)

    # Remove spaces and newlines to count only characters
    char_no_spaces = len(text.replace(" ", "").replace("\n", ""))

    # split() divides text into words, len() counts them
    word_count = len(text.split())

    # Display the statistics
    st.write(f"**Characters (with spaces)**: {char_count}")
    st.write(f"**Characters (without spaces)**: {char_no_spaces}")
    st.write(f"**Words**: {word_count}")
else:
    st.info("👆 Enter some text above to see the analysis")
