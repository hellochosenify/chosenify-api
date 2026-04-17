from openai import OpenAI
import os
from dotenv import load_dotenv
import markdown

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(scores):
    """
    Generate a structured career report based on user scores
    """

    prompt = f"""
You are a professional career assessment expert.

User psychometric scores:
{scores}

Generate a HIGH-QUALITY structured career report.

Follow this EXACT format:

## Personality Summary
Write 3-4 insightful lines explaining the user's personality based on scores.

## Top Traits
- Trait 1 (short explanation)
- Trait 2 (short explanation)
- Trait 3 (short explanation)

## Career Matches
- Career Option 1 (why it fits)
- Career Option 2 (why it fits)
- Career Option 3 (why it fits)

## Strengths
- Strength 1
- Strength 2
- Strength 3

## Areas to Improve
- Weakness 1
- Weakness 2

## Action Plan
- Step 1
- Step 2
- Step 3

Make it personalized, practical, and easy to read.
Avoid generic advice.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a career coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    report_text = response.choices[0].message.content

    # Convert markdown → HTML
    report_html = markdown.markdown(report_text)

    return report_html
