def generate_report(scores):

    html = f"""
    <div style="font-family:Arial; padding:20px;">

        <h2>Your Career Report</h2>

        <h3>Scores</h3>
        <ul>
            <li>Social: {scores['Social']}</li>
            <li>Investigative: {scores['Investigative']}</li>
            <li>Artistic: {scores['Artistic']}</li>
            <li>Enterprising: {scores['Enterprising']}</li>
        </ul>

        <h3>Summary</h3>
        <p>
        Based on your responses, you show a mix of personality traits across multiple dimensions.
        Your strongest areas indicate where you are most likely to thrive professionally.
        </p>

        <h3>Top Career Matches</h3>
        <ul>
            <li>Business Analyst</li>
            <li>Creative Strategist</li>
            <li>Project Manager</li>
        </ul>

        <h3>Next Steps</h3>
        <ul>
            <li>Develop skills aligned with your strongest traits</li>
            <li>Explore careers that match your interests</li>
            <li>Gain practical experience through projects</li>
        </ul>

    </div>
    """

    return html