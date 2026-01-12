"""
Quiz Application - Advanced Project 10

Interactive quiz with scoring system.
"""

import streamlit as st

st.set_page_config(page_title="Quiz Application", page_icon="🎯", layout="centered")

st.title("🎯 Quiz Application")

questions = [
    {"q": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"q": "What is the capital of France?", "options": ["London", "Paris", "Berlin"], "answer": "Paris"},
    {"q": "What is 10 * 5?", "options": ["50", "55", "45"], "answer": "50"}
]

if 'answers' not in st.session_state:
    st.session_state.answers = {}
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

if not st.session_state.submitted:
    for idx, q in enumerate(questions):
        st.subheader(f"Question {idx + 1}")
        st.write(q['q'])
        answer = st.radio(f"Select answer:", q['options'], key=f"q{idx}")
        st.session_state.answers[idx] = answer
    
    if st.button("Submit Quiz", type="primary"):
        st.session_state.submitted = True
        st.rerun()
else:
    score = 0
    for idx, q in enumerate(questions):
        if st.session_state.answers.get(idx) == q['answer']:
            score += 1
    
    st.success(f"🎉 Your Score: {score}/{len(questions)}")
    
    percentage = (score / len(questions)) * 100
    if percentage == 100:
        st.balloons()
        st.write("Perfect score! 🌟")
    elif percentage >= 60:
        st.write("Good job! 👍")
    else:
        st.write("Keep practicing! 📚")
    
    if st.button("Restart Quiz"):
        st.session_state.answers = {}
        st.session_state.submitted = False
        st.rerun()

st.divider()
st.caption("Built with Streamlit 🎈")
