from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from scoring import calculate_scores
from report import generate_report

app = FastAPI()

# ✅ CORS (VERY IMPORTANT for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Request model (FIXED TYPE)
class TestSubmission(BaseModel):
    answers: List[int]

@app.get("/")
def root():
    return {"message": "Chosenify API is running"}

@app.post("/submit-test")
def submit_test(data: TestSubmission):
    try:
        scores = calculate_scores(data.answers)
        report = generate_report(scores)

        return {
            "scores": scores,
            "report": report
        }

    except Exception as e:
        return {"error": str(e)}