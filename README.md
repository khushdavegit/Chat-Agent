# Chat-Agent
Build a friendly chatbot that can analyze the famous Titanic dataset. Users should be able to  ask questions in plain English and get both text answers and visual insights about the  passengers.  

**FastAPI Backend – Handles dataset queries and responses.
**LangChain Integration – Processes natural language queries.
**Streamlit Frontend – Provides a user-friendly interface.
**Data Processing & Visualization – Generates text responses and visual insights.

STEPS TO APPLY AND RUN THIS Chat Bot---
**Set Up Your Environment
Install necessary dependencies 
[pip install fastapi uvicorn pandas matplotlib seaborn streamlit langchain openai]

**Prepare the Titanic Dataset
titanic.csv

**Backend (FastAPI)
This FastAPI service will load the dataset and process queries.

Create backend.py

**Frontend (Streamlit)
This will communicate with the FastAPI backend and display responses.

Create app.py

**Running the App
start the FastAPI server
uvicorn backend:app --reload
--------------------------------------------------------------------------------
