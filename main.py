from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from scoring import calculate_scores
from report import generate_report

app = FastAPI()

class Answers(BaseModel):
    answers: List[str]

@app.post("/submit-test")
def submit_test(data: Answers):
    # Calculate scores
    scores = calculate_scores(data.answers)

    # Generate report
    report = generate_report(scores)

    # Return BOTH report + scores
    return {
        "report": report,
        "scores": scores
    }
