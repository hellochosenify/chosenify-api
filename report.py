from openai import OpenAI
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(scores):
    try:
        prompt = f"""
You are a premium career advisor AI.

Generate a highly structured, visually clean, premium career report.

User Scores:
- Social: {scores.get("Social", 0)}
- Investigative: {scores.get("Investigative", 0)}
- Artistic: {scores.get("Artistic", 0)}
- Enterprising: {scores.get("Enterprising", 0)}

Return the report in this EXACT format:

1. Title: Career Analysis Report

2. Profile Summary:
(Write 3-4 lines describing the user personality and strengths)

3. Top Strengths:
- Strength 1
- Strength 2
- Strength 3

4. Career Matches:
For each career include:
- Career Name
- Why it fits
- Salary range
- Growth outlook

5. Skill Gaps:
- Skill 1
- Skill 2

6. Action Plan:
Step 1:
Step 2:
Step 3:

7. Final Advice:
(Short, powerful closing advice)

IMPORTANT:
- Keep formatting clean
- Use bullet points
- Do not add extra sections
- Do not break structure
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a career guidance expert."},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ ERROR:", str(e))
        return f"Error: {str(e)}"