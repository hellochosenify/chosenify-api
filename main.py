from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from questions import questions
from scoring import calculate_scores
from report import generate_report

# -----------------------------
# Data Models
# -----------------------------
class Answer(BaseModel):
    dimension: str
    value: int

class TestSubmission(BaseModel):
    answers: List[Answer]

# -----------------------------
# App Initialization
# -----------------------------
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# -----------------------------
# Routes
# -----------------------------

# Home route
@app.get("/")
def home():
    return {"message": "API is working"}

# Get questions
@app.get("/questions")
def get_questions():
    return questions

# Submit test → scores + styled report
@app.post("/submit-test")
def submit_test(data: TestSubmission):

    # Convert objects → dictionaries
    answers = [answer.model_dump() for answer in data.answers]

    # Calculate scores
    scores = calculate_scores(answers)

    # Generate AI report
    report = generate_report(scores)

    # Format into premium HTML
    formatted_report = f"""
    <div style="font-family: Arial; max-width: 800px; margin: auto; padding: 20px;">

        <h1 style="text-align:center; color:#2c3e50;">
            Career Analysis Report
        </h1>

        <div style="background:#f8f9fa; padding:15px; border-radius:10px; margin-top:20px;">
            <h2>📊 Your Scores</h2>
            <p><strong>Social:</strong> {scores.get("Social")}</p>
            <p><strong>Investigative:</strong> {scores.get("Investigative")}</p>
            <p><strong>Artistic:</strong> {scores.get("Artistic")}</p>
            <p><strong>Enterprising:</strong> {scores.get("Enterprising")}</p>
        </div>

        <div style="background:#ffffff; padding:15px; border-radius:10px; margin-top:20px; border:1px solid #ddd;">
            <h2>📄 Career Insights</h2>
            <div style="white-space: pre-wrap; line-height:1.6;">
                {report}
            </div>
        </div>

    </div>
    """

    # Return response
    return {
        "scores": scores,
        "report": formatted_report
    }
