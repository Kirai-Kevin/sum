import streamlit as st
from summarizer import generate_summary, extract_key_points, build_vocabulary, generate_citation, calculate_readability, generate_study_questions, categorize_topics, generate_answer
from ui_components import create_ui_components

def main():
    st.title("Advanced Text Summarizer for Students")
    
    if 'questions' not in st.session_state:
        st.session_state.questions = []
    if 'answers' not in st.session_state:
        st.session_state.answers = []
    if 'show_answers' not in st.session_state:
        st.session_state.show_answers = []
    
    text_input, summary_length, temperature, summary_style, features = create_ui_components()
    
    if st.button("Generate Summary and Features"):
        if text_input:
            summary = generate_summary(text_input, summary_length, temperature, summary_style)
            
            if summary.startswith("API quota exceeded") or summary.startswith("An error occurred"):
                st.error(summary)
            else:
                st.subheader("Summary:")
                st.write(summary)
                
                if "key_points" in features:
                    key_points = extract_key_points(text_input)
                    st.subheader("Key Points:")
                    for point in key_points:
                        st.write(f"• {point}")
                
                if "vocabulary" in features:
                    vocab = build_vocabulary(text_input)
                    st.subheader("Vocabulary:")
                    for word, definition in vocab.items():
                        st.write(f"**{word}**: {definition}")
                
                if "citation" in features:
                    citation = generate_citation(text_input)
                    st.subheader("Citation:")
                    st.write(citation)
                
                if "readability" in features:
                    readability = calculate_readability(text_input)
                    st.subheader("Readability:")
                    st.write(f"Original text score: {readability['original']}")
                    st.write(f"Summary score: {readability['summary']}")
                
                if "study_questions" in features:
                    st.session_state.questions = generate_study_questions(text_input)
                    st.session_state.answers = [generate_answer(q, text_input) for q in st.session_state.questions]
                    st.session_state.show_answers = [False] * len(st.session_state.questions)
                
                if "topics" in features:
                    topics = categorize_topics(text_input)
                    st.subheader("Main Topics:")
                    for topic in topics:
                        st.write(f"• {topic}")
        else:
            st.warning("Please enter text to summarize.")

    if st.session_state.questions:
        st.subheader("Study Questions:")
        for i, (question, answer) in enumerate(zip(st.session_state.questions, st.session_state.answers)):
            st.write(f"Q{i+1}: {question}")
            user_answer = st.text_area(f"Your answer for Q{i+1}:", key=f"answer_{i}")
            if st.button(f"Show Answer {i+1}", key=f"show_answer_{i}"):
                st.session_state.show_answers[i] = True
            if st.session_state.show_answers[i]:
                st.write(f"Generated Answer: {answer}")

if __name__ == "__main__":
    main()