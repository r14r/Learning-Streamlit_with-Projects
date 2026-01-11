"""
Step 4: Adding Submit and Score Calculation

In this step, we'll:
- Add a submit button
- Calculate the score after submission
- Display the score
- Show different states (quiz vs results)

Key Concepts:
- Conditional rendering based on submission state
- Score calculation by comparing answers
- st.rerun() to refresh the app
"""

import streamlit as st

st.set_page_config(page_title="Quiz Application", page_icon="🎯", layout="centered")

st.title("🎯 Quiz Application")

questions = [
    {"q": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"q": "What is the capital of France?", "options": ["London", "Paris", "Berlin"], "answer": "Paris"},
    {"q": "What is 10 * 5?", "options": ["50", "55", "45"], "answer": "50"}
]

# Initialize session state
if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Quiz mode vs Results mode
if not st.session_state.submitted:
    # Display questions
    for idx, q in enumerate(questions):
        st.subheader(f"Question {idx + 1}")
        st.write(q['q'])
        answer = st.radio(f"Select answer:", q['options'], key=f"q{idx}")
        st.session_state.answers[idx] = answer

    # Submit button
    if st.button("Submit Quiz", type="primary"):
        st.session_state.submitted = True
        st.rerun()

else:
    # Calculate score
    score = 0
    for idx, q in enumerate(questions):
        if st.session_state.answers.get(idx) == q['answer']:
            score += 1

    # Display score
    st.success(f"🎉 Your Score: {score}/{len(questions)}")

    # Restart button (will be enhanced in next step)
    if st.button("Restart Quiz"):
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()

st.divider()
st.caption("Built with Streamlit 🎈")
