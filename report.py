<<<<<<< HEAD
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_report(scores):
    """
    Generate a premium HTML career report
    """

    prompt = f"""
You are a premium career assessment expert.

User scores:
{scores}

Generate a BEAUTIFULLY FORMATTED HTML career report.

STRICT RULES:
- ONLY return HTML (NO markdown)
- Use clean structure
- Use <h2> for section titles
- Use <ul><li> for lists
- Keep paragraphs short
- Add spacing using <br>

STRUCTURE EXACTLY LIKE THIS:

<h2>🧠 Personality Summary</h2>
<p>...</p>

<h2>💡 Key Traits</h2>
<ul>
<li>...</li>
<li>...</li>
</ul>

<h2>🚀 Career Matches</h2>
<ul>
<li>...</li>
<li>...</li>
</ul>

<h2>✅ Strengths</h2>
<ul>
<li>...</li>
</ul>

<h2>⚠️ Areas to Improve</h2>
<ul>
<li>...</li>
</ul>

<h2>📈 Action Plan</h2>
<ul>
<li>...</li>
</ul>

Make it specific, structured, and premium.
Avoid generic wording.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a career coach."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    report_html = response.choices[0].message.content

    return report_html
=======
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
>>>>>>> b33e1b46d75edb4e95799c8091124c2313c182bf
