TRAIT_CONTENT = {
    "Social": {
        "summary": "You are energized by connection, support, and meaningful collaboration with other people.",
        "strengths": [
            "Builds trust quickly and creates supportive relationships",
            "Communicates with empathy and keeps teams aligned",
            "Thrives in roles centered on service, guidance, and collaboration",
        ],
        "weaknesses": [
            "May avoid conflict when direct feedback would help",
            "Can overextend by prioritizing other people too often",
            "May feel drained in highly isolated work environments",
        ],
        "careers": [
            "Customer Success Manager",
            "Academic Advisor",
            "Community Program Coordinator",
        ],
        "growth_plan": [
            "Practice setting boundaries so support stays sustainable",
            "Build confidence with direct but respectful feedback",
            "Take on mentoring or facilitation opportunities to sharpen people leadership",
        ],
    },
    "Investigative": {
        "summary": "You are motivated by solving problems, understanding systems, and making sense of complexity.",
        "strengths": [
            "Thinks analytically and breaks down complex problems well",
            "Learns quickly through research, patterns, and evidence",
            "Brings depth and precision to decision-making",
        ],
        "weaknesses": [
            "May overanalyze before moving into action",
            "Can become disengaged in low-challenge or repetitive work",
            "May need to simplify ideas for non-technical audiences",
        ],
        "careers": [
            "Data Analyst",
            "UX Researcher",
            "Business Intelligence Specialist",
        ],
        "growth_plan": [
            "Set time limits for analysis so decisions turn into action faster",
            "Practice explaining insights in clear, simple language",
            "Build a portfolio of case studies that shows both thinking and execution",
        ],
    },
    "Artistic": {
        "summary": "You are drawn to originality, imagination, and work that allows self-expression and fresh ideas.",
        "strengths": [
            "Generates original ideas and creative solutions",
            "Expresses concepts in memorable and engaging ways",
            "Adapts well when experimentation and innovation are encouraged",
        ],
        "weaknesses": [
            "May struggle in rigid environments with little creative freedom",
            "Can lose momentum if structure and prioritization are weak",
            "May need support translating ideas into repeatable execution",
        ],
        "careers": [
            "Content Strategist",
            "Brand Designer",
            "Creative Producer",
        ],
        "growth_plan": [
            "Use a simple planning system to turn ideas into finished work",
            "Collect feedback early so creative direction stays focused",
            "Strengthen your portfolio with work that shows both originality and delivery",
        ],
    },
    "Enterprising": {
        "summary": "You are energized by leadership, momentum, and turning ideas into practical results.",
        "strengths": [
            "Takes initiative quickly and creates momentum",
            "Influences others with confidence and clarity",
            "Sees opportunities and pushes work toward outcomes",
        ],
        "weaknesses": [
            "May move too fast without enough detail review",
            "Can dominate decisions when more collaboration would help",
            "May become impatient with slow-moving processes",
        ],
        "careers": [
            "Product Manager",
            "Sales Strategist",
            "Operations Lead",
        ],
        "growth_plan": [
            "Add review checkpoints so speed stays matched with quality",
            "Practice active listening to strengthen team buy-in",
            "Deepen expertise in one domain to make your leadership more effective",
        ],
    },
}


def _resolve_scores(report_data):
    if isinstance(report_data, dict) and "scores" in report_data:
        return report_data["scores"]
    return report_data


def _resolve_top_trait(scores, report_data):
    if isinstance(report_data, dict) and report_data.get("top_trait") in scores:
        return report_data["top_trait"]
    return max(scores, key=scores.get)


def _resolve_personality_type(scores, top_trait, report_data):
    if isinstance(report_data, dict) and report_data.get("personality_type"):
        return report_data["personality_type"]

    sorted_traits = sorted(scores, key=scores.get, reverse=True)
    second_trait = sorted_traits[1]
    return f"{top_trait}-{second_trait}"


def _build_header(personality_type, top_trait, lowest_trait):
    return (
        f"""<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px;margin-bottom:28px;">"""
        f"""<div style="background:#eef4ff;border-radius:16px;padding:16px;"><div style="font-size:12px;text-transform:uppercase;letter-spacing:0.08em;color:#64748b;">Personality Type</div><div style="margin-top:6px;font-size:20px;font-weight:700;color:#0f172a;">{personality_type}</div></div>"""
        f"""<div style="background:#ecfdf5;border-radius:16px;padding:16px;"><div style="font-size:12px;text-transform:uppercase;letter-spacing:0.08em;color:#64748b;">Top Trait</div><div style="margin-top:6px;font-size:20px;font-weight:700;color:#0f172a;">{top_trait}</div></div>"""
        f"""<div style="background:#fff7ed;border-radius:16px;padding:16px;"><div style="font-size:12px;text-transform:uppercase;letter-spacing:0.08em;color:#64748b;">Lowest Score</div><div style="margin-top:6px;font-size:20px;font-weight:700;color:#0f172a;">{lowest_trait}</div></div>"""
        """</div>"""
    )


def _build_core_sections(personality_type, top_trait, top_trait_content):
    return (
        f"""<section style="margin-bottom:28px;"><h2 style="margin:0 0 12px;font-size:22px;color:#0f172a;">1. Overview</h2><p style="margin:0;font-size:16px;line-height:1.8;color:#334155;">Your current profile aligns with the <strong>{personality_type}</strong> personality type. This suggests your strongest performance comes when your work reflects how you naturally think, contribute, and stay motivated.</p></section>"""
        f"""<section style="margin-bottom:28px;"><h2 style="margin:0 0 12px;font-size:22px;color:#0f172a;">2. Top Trait Explanation</h2><p style="margin:0;font-size:16px;line-height:1.8;color:#334155;"><strong>{top_trait}</strong> is your highest scoring dimension. {top_trait_content["summary"]}</p></section>"""
    )


def _build_premium_sections(top_trait_content, lowest_trait, lowest_trait_content):
    return (
        f"""<section style="margin-bottom:28px;"><h2 style="margin:0 0 12px;font-size:22px;color:#0f172a;">3. Strengths</h2><ul style="margin:0;padding-left:20px;color:#334155;line-height:1.9;"><li>{top_trait_content["strengths"][0]}</li><li>{top_trait_content["strengths"][1]}</li><li>{top_trait_content["strengths"][2]}</li></ul></section>"""
        f"""<section style="margin-bottom:28px;"><h2 style="margin:0 0 12px;font-size:22px;color:#0f172a;">4. Weaknesses</h2><p style="margin:0 0 12px;font-size:16px;line-height:1.8;color:#334155;">Your lowest score is in <strong>{lowest_trait}</strong>, which points to a potential growth area rather than a fixed limitation.</p><ul style="margin:0;padding-left:20px;color:#334155;line-height:1.9;"><li>{lowest_trait_content["weaknesses"][0]}</li><li>{lowest_trait_content["weaknesses"][1]}</li><li>{lowest_trait_content["weaknesses"][2]}</li></ul></section>"""
        f"""<section style="margin-bottom:28px;"><h2 style="margin:0 0 12px;font-size:22px;color:#0f172a;">5. Career Matches</h2><ul style="margin:0;padding-left:20px;color:#334155;line-height:1.9;"><li>{top_trait_content["careers"][0]}</li><li>{top_trait_content["careers"][1]}</li><li>{top_trait_content["careers"][2]}</li></ul></section>"""
        f"""<section style="margin-bottom:28px;"><h2 style="margin:0 0 12px;font-size:22px;color:#0f172a;">6. Growth Plan</h2><ul style="margin:0;padding-left:20px;color:#334155;line-height:1.9;"><li>{top_trait_content["growth_plan"][0]}</li><li>{top_trait_content["growth_plan"][1]}</li><li>{top_trait_content["growth_plan"][2]}</li></ul></section>"""
    )


def _build_score_snapshot(scores):
    return (
        f"""<section><h2 style="margin:0 0 12px;font-size:22px;color:#0f172a;">Score Snapshot</h2><ul style="margin:0;padding-left:20px;color:#334155;line-height:1.9;"><li>Social: {scores["Social"]}</li><li>Investigative: {scores["Investigative"]}</li><li>Artistic: {scores["Artistic"]}</li><li>Enterprising: {scores["Enterprising"]}</li></ul></section>"""
    )


def _build_report(report_data, include_premium_sections):
    scores = _resolve_scores(report_data)
    top_trait = _resolve_top_trait(scores, report_data)
    personality_type = _resolve_personality_type(scores, top_trait, report_data)
    lowest_trait = min(scores, key=scores.get)

    top_trait_content = TRAIT_CONTENT[top_trait]
    lowest_trait_content = TRAIT_CONTENT[lowest_trait]

    premium_sections = ""
    if include_premium_sections:
        premium_sections = _build_premium_sections(top_trait_content, lowest_trait, lowest_trait_content)

    return (
        f"""<div style="font-family:Arial,sans-serif;padding:32px;background:#f4f7fb;color:#1f2937;"><div style="max-width:860px;margin:0 auto;background:#ffffff;border:1px solid #d9e2ec;border-radius:20px;padding:32px;box-shadow:0 18px 40px rgba(15,23,42,0.08);"><h1 style="margin:0 0 10px;font-size:30px;color:#0f172a;">Career Personality Report</h1><p style="margin:0 0 24px;font-size:16px;line-height:1.8;color:#475569;">A structured view of your strongest tendencies, best-fit roles, and next growth opportunities.</p>"""
        + _build_header(personality_type, top_trait, lowest_trait)
        + _build_core_sections(personality_type, top_trait, top_trait_content)
        + premium_sections
        + _build_score_snapshot(scores)
        + """</div></div>"""
    )


def generate_free_report(scores):
    return _build_report(scores, False)


def generate_full_report(scores):
    return _build_report(scores, True)


def generate_report(report_data):
    return generate_full_report(report_data)
