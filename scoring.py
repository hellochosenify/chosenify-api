def calculate_scores(answers):
    scores = {
        "Social": 0,
        "Investigative": 0,
        "Artistic": 0,
        "Enterprising": 0
    }

    mapping = [
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Investigative", "Artistic", "Enterprising"
    ]

    for i, answer in enumerate(answers):
        dimension = mapping[i]
        scores[dimension] += answer

    return scores