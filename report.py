from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_report(scores):

    prompt = f"""
You are a world-class career psychologist and report generator.

Create a HIGH-QUALITY, PREMIUM career report in clean HTML format.

DO NOT return markdown.
DO NOT explain anything.
RETURN ONLY HTML.

--------------------------------
USER SCORES:
Social: {scores.get("Social", 0)}
Investigative: {scores.get("Investigative", 0)}
Artistic: {scores.get("Artistic", 0)}
Enterprising: {scores.get("Enterprising", 0)}
--------------------------------

STRICT STRUCTURE (FOLLOW EXACTLY):

<h2>🧠 Career Personality Overview</h2>
<p>Deep psychological interpretation of the personality. Avoid generic text.</p>

<h2>📊 Strengths</h2>
<ul>
<li>Specific strength with explanation</li>
<li>Specific strength with explanation</li>
<li>Specific strength with explanation</li>
</ul>

<h2>⚠️ Areas for Improvement</h2>
<ul>
<li>Specific weakness with improvement insight</li>
<li>Specific weakness with improvement insight</li>
<li>Specific weakness with improvement insight</li>
</ul>

<h2>🚀 Top Career Matches</h2>
<ul>
<li><strong>Career 1:</strong> Why it fits</li>
<li><strong>Career 2:</strong> Why it fits</li>
<li><strong>Career 3:</strong> Why it fits</li>
</ul>

<h2>💰 Career Insights</h2>
<ul>
<li>Salary expectations</li>
<li>Growth outlook</li>
<li>Industry demand</li>
</ul>

<h2>📈 Personalized Growth Plan</h2>
<ul>
<li>Step 1: Clear actionable step</li>
<li>Step 2: Clear actionable step</li>
<li>Step 3: Clear actionable step</li>
</ul>

--------------------------------

RULES:
- Make it feel like a $50 premium report
- Avoid generic phrases like "you are good at"
- Be specific, insightful, and professional
- Use clean HTML only (h2, p, ul, li, strong)
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a career report generator."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    report_html = response.choices[0].message.content

    return report_html