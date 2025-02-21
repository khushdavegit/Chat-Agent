from fastapi import FastAPI
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import io
import base64
from pydantic import BaseModel

app = FastAPI()

# Load Titanic dataset
df = pd.read_csv("titanic.csv")

# Request model for queries
class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "Titanic Chatbot API is running!"}

@app.post("/query")
def process_query(request: QueryRequest):
    query = request.query.lower()

    if "percentage of passengers were male" in query:
        male_count = df[df["Sex"] == "male"].shape[0]
        total_count = df.shape[0]
        percentage = (male_count / total_count) * 100
        return {"answer": f"{percentage:.2f}% of passengers were male."}

    elif "histogram of passenger ages" in query:
        return generate_histogram()

    elif "average ticket fare" in query:
        avg_fare = df["Fare"].mean()
        return {"answer": f"The average ticket fare was ${avg_fare:.2f}."}

    elif "passengers embarked from each port" in query:
        return generate_port_distribution()

    else:
        return {"answer": "Sorry, I can't process that question yet."}

def generate_histogram():
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Age"].dropna(), bins=20, kde=True)
    plt.xlabel("Age")
    plt.ylabel("Count")
    plt.title("Histogram of Passenger Ages")
    
    return convert_plot_to_base64()

def generate_port_distribution():
    plt.figure(figsize=(8, 5))
    sns.countplot(x=df["Embarked"].dropna())
    plt.xlabel("Port")
    plt.ylabel("Passenger Count")
    plt.title("Passengers Embarked from Each Port")

    return convert_plot_to_base64()

def convert_plot_to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img_str = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return {"image": img_str}
