import google.generativeai as genai
from dotenv import load_dotenv
import os
from google.api_core import exceptions
import textstat

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_summary(text, summary_length, temperature, style):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Summarize the following text in approximately {summary_length} words using a {style} style:\n\n{text}"
    
    try:
        response = model.generate_content(prompt, generation_config=genai.types.GenerationConfig(temperature=temperature))
        return response.text
    except exceptions.ResourceExhausted:
        return "API quota exceeded. Please try again later or check your API usage limits."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def extract_key_points(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Extract 5 key points from the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.split('\n')

def build_vocabulary(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Identify and define 5 complex words or phrases from the following text:\n\n{text}"
    response = model.generate_content(prompt)
    vocab = {}
    for line in response.text.split('\n'):
        if ':' in line:
            word, definition = line.split(':', 1)
            vocab[word.strip()] = definition.strip()
    return vocab

def generate_citation(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Generate an APA citation for the following text, assuming it's from a web page accessed today:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

def calculate_readability(text):
    original_score = textstat.flesch_reading_ease(text)
    summary_score = textstat.flesch_reading_ease(generate_summary(text, 100, 0.5, 'narrative'))
    return {'original': original_score, 'summary': summary_score}

def generate_study_questions(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Generate 3 study questions based on the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.split('\n')

def categorize_topics(text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Identify the main topics or themes in the following text:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.split('\n')

def generate_answer(question, text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Based on the following text, answer this question: {question}\n\nText: {text}"
    response = model.generate_content(prompt)
    return response.text

# Add this to the existing functions in summarizer.py

def generate_answer(question, text):
    model = genai.GenerativeModel('gemini-pro')
    prompt = f"Based on the following text, answer this question: {question}\n\nText: {text}"
    response = model.generate_content(prompt)
    return response.text