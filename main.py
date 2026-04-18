from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi.middleware.cors import CORSMiddleware

from scoring import calculate_scores
from report import generate_free_report, generate_full_report

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
    user_type: str = "free"

@app.get("/")
def root():
    return {"message": "Chosenify API is running"}

@app.post("/submit-test")
def submit_test(data: TestSubmission):
    try:
        scores_data = calculate_scores(data.answers)
        user_type = getattr(data, "user_type", "free")
        if user_type == "free":
            report = generate_free_report(scores_data)
        else:
            report = generate_full_report(scores_data)
        sorted_traits = sorted(scores_data["scores"], key=scores_data["scores"].get, reverse=True)
        personality_type = f"{sorted_traits[0]}-{sorted_traits[1]}"

        return {
            "scores": scores_data["scores"],
            "top_trait": scores_data["top_trait"],
            "personality_type": personality_type,
            "report": report
        }

    except Exception as e:
        return {"error": str(e)}
