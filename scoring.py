def calculate_scores(answers):
    """
    Calculate RIASEC scores based on answers (1–5 scale)
    """

    # Map each question to a dimension
    dimensions = [
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising"
    ]

    scores = {
        "Social": 0,
        "Investigative": 0,
        "Artistic": 0,
        "Enterprising": 0
    }

    for i in range(len(answers)):
        value = int(answers[i])  # convert string → int
        dimension = dimensions[i]

        scores[dimension] += value

    return scores