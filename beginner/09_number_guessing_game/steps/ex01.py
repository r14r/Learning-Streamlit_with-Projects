"""
Step 1: Basic Setup with Random Number
Learning objective: Generate a random number and display game interface
"""

import streamlit as st
import random

st.set_page_config(
    page_title="Number Guessing Game",
    page_icon="🎲",
    layout="centered"
)

st.title("🎲 Number Guessing Game")
st.write("I'm thinking of a number between 1 and 100. Can you guess it?")

# Generate a random number
target_number = random.randint(1, 100)

st.write(f"(Psst... the number is {target_number})") # For testing only!

# Simple guess input
guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, value=50, step=1)
