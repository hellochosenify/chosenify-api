def calculate_scores(answers):
    scores = {
        "Social": 0,
        "Investigative": 0,
        "Artistic": 0,
        "Enterprising": 0
    }

    # Map questions to dimensions
    mapping = [
        "Social", "Investigative", "Artistic", "Enterprising",
        "Social", "Realistic", "Investigative", "Artistic",
        "Enterprising", "Conventional", "Realistic", "Investigative",
        "Artistic", "Enterprising", "Conventional", "Realistic",
        "Investigative", "Artistic", "Enterprising", "Conventional"
    ]

    for i, answer in enumerate(answers):
        dimension = mapping[i]

        if dimension in scores:
            scores[dimension] += int(answer)

    return scores