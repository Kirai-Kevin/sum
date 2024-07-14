
# Advanced Text Summarizer for Students

## Overview

The Advanced Text Summarizer for Students is a powerful tool designed to help students quickly understand and analyze complex texts. This Streamlit-based application leverages Google's Generative AI to provide comprehensive summaries, key points, vocabulary building, and various other features to enhance the learning experience.

## Current Features

- Text summarization with adjustable length and style
- Extraction of key points
- Vocabulary building with definitions
- Citation generation (APA format)
- Readability analysis (Flesch Reading Ease score)
- Study question generation with answer checking
- Topic categorization
- Customizable summary settings (length, temperature, style)

## Future Features

- Support for multiple document formats (PDF, DOCX, etc.)
- Integration with academic databases for broader research capabilities
- Collaborative study sessions with real-time sharing
- Personalized learning paths based on user interaction history
- Multi-language support for international students

## Technologies Used

- Python
- Streamlit
- Google Generative AI (Gemini Pro model)
- textstat (for readability analysis)
- python-dotenv (for environment variable management)

## Getting Started

To run the Advanced Text Summarizer for Students on your local machine, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/Kirai-Kevin/sum.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Google Generative AI API key:
   - Create a `.env` file in the project root
   - Add your API key: `GEMINI_API_KEY=your_api_key_here`

4. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

5. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`)

6. Enter your text in the provided text area, adjust the summary settings, and select additional features as needed.

7. Click on "Generate Summary and Features" to process the text and view the results.