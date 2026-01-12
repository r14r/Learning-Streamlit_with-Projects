"""
Step 6: Adding Score History
Learning objective: Track best scores across multiple games
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

if 'target_number' not in st.session_state:
    st.session_state.target_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.guesses = []  # List to store winning attempts
    st.session_state.game_over = False

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Attempts", st.session_state.attempts)

with col2:
    # Show best score if available
    best = min(st.session_state.guesses) if st.session_state.guesses else "-"
    st.metric("Best Score", best)

with col3:
    remaining = max(0, 10 - st.session_state.attempts)
    st.metric("Remaining", remaining)

if not st.session_state.game_over and st.session_state.attempts < 10:
    guess = st.number_input("Enter your guess (1-100):", min_value=1, max_value=100, value=50, step=1)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Submit Guess", type="primary", use_container_width=True):
            st.session_state.attempts += 1

            if guess == st.session_state.target_number:
                st.session_state.game_over = True
                # Add to score history
                st.session_state.guesses.append(st.session_state.attempts)
                st.balloons()
                st.success(f"🎉 Congratulations! You guessed it in {st.session_state.attempts} attempts!")
            elif guess < st.session_state.target_number:
                st.info("📈 Too low! Try a higher number.")
            else:
                st.info("📉 Too high! Try a lower number.")

            if st.session_state.attempts >= 10 and not st.session_state.game_over:
                st.session_state.game_over = True
                st.error(f"😔 Game Over! The number was {st.session_state.target_number}")

    with col2:
        if st.button("Give Up", use_container_width=True):
            st.session_state.game_over = True
            st.warning(f"The number was {st.session_state.target_number}")

elif st.session_state.game_over:
    if st.session_state.attempts <= 10 and guess == st.session_state.target_number:
        st.success(f"🎉 You won in {st.session_state.attempts} attempts!")
    else:
        st.error(f"😔 Game Over! The number was {st.session_state.target_number}")

    if st.button("Play Again", type="primary"):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.attempts = 0
        st.session_state.game_over = False
        st.rerun()

# Game history
if st.session_state.guesses:
    with st.expander("🏆 Your Best Scores"):
        sorted_scores = sorted(st.session_state.guesses)
        for i, score in enumerate(sorted_scores[:5], 1):
            st.write(f"{i}. {score} attempts")
