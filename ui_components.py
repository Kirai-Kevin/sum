import streamlit as st

def create_ui_components():
    text_input = st.text_area("Enter your text here:", height=200)
    
    summary_length = st.slider("Summary Length (words):", min_value=10, max_value=1000, value=150)
    temperature = st.slider("Temperature:", min_value=0.1, max_value=1.0, value=0.5, step=0.1)
    summary_style = st.selectbox("Summary Style:", ["narrative", "bullet points", "question-answer"])
    
    st.subheader("Optional Features:")
    features = st.multiselect(
        "Select additional features:",
        ["key_points", "vocabulary", "citation", "readability", "study_questions", "topics"],
        default=["key_points"]
    )
    
    return text_input, summary_length, temperature, summary_style, features