def calculate_scores(answers):
    scores = {
        "Social": 0,
        "Investigative": 0,
        "Artistic": 0,
        "Enterprising": 0
    }

    mapping = [
        "Social",
        "Investigative",
        "Artistic",
        "Enterprising"
    ]

    for i, answer in enumerate(answers):
        if i < len(mapping):
            dimension = mapping[i]
            try:
                scores[dimension] += int(answer)
            except:
                scores[dimension] += 0

    top_trait = max(scores, key=scores.get)

    return {
        "scores": scores,
        "top_trait": top_trait
    }
