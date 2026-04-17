<<<<<<< HEAD
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from scoring import calculate_scores
from report import generate_report

# ✅ ADD THIS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ ADD THIS BLOCK (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Answers(BaseModel):
    answers: List[str]

@app.post("/submit-test")
def submit_test(data: Answers):
    scores = calculate_scores(data.answers)
    report = generate_report(scores)

    return {
        "report": report,
        "scores": scores
    }
=======
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from scoring import calculate_scores
from report import generate_report

# ✅ ADD THIS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ✅ ADD THIS BLOCK (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Answers(BaseModel):
    answers: List[str]

@app.post("/submit-test")
def submit_test(data: Answers):
    scores = calculate_scores(data.answers)
    report = generate_report(scores)

    return {
        "report": report,
        "scores": scores
    }
>>>>>>> b33e1b46d75edb4e95799c8091124c2313c182bf
