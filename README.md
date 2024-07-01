# EduTech Solutions Q&A System

## Overview

This project implements an advanced Question and Answer (Q&A) system using Google Palm LLM and Langchain, designed specifically for EduTech Solutions, an online education platform specializing in data science courses and bootcamps.

### Project Highlights

- Integration of live CSV dataset with frequently asked questions used by EduTech Solutions.
- Implementation of Google Palm LLM-based Q&A system to enhance customer support efficiency.
- Streamlit-based user interface providing instant responses to student queries.
- Key learning components include Langchain integration, Streamlit UI development, Huggingface embeddings, and FAISS for vector database.

## Installation

1. Clone the repository:
git clone https://github.com/edutechsolutions/langchain.git

2. Navigate to the project directory:
cd EduTech-Solutions-Q-A-System

3. Install dependencies:
pip install -r requirements.txt

4. Obtain a Google API key from makersuite.google.com and add it to `.env` file:
GOOGLE_API_KEY="your_api_key_here"


## Usage

- Run the Streamlit app:
streamlit run main.py

- Access the web application in your browser.

- Click on "Create Knowledge Base" to generate a FAQ knowledge base (may take some time).

- Enter your query in the provided box to get instant answers.

## Sample Questions

- Are internships available? Do you offer payment plans?
- Is there a JavaScript course available?
- Should I learn Power BI or Tableau?
- Can Power BI be used on a Mac computer?
- How can I enable Power Pivot if it's not visible?

## Project Structure

- `main.py`: Main script for the Streamlit application.
- `langchain_helper.py`: Contains essential Langchain integration code.
- `requirements.txt`: List of required Python packages.
- `.env`: Configuration file for storing Google API key.

This project aims to optimize the support system at EduTech Solutions, ensuring timely and accurate responses to student queries while enhancing user satisfaction and engagement.
