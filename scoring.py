def calculate_scores(answers):
    scores = {
        "Social": 0,
        "Investigative": 0,
        "Artistic": 0,
        "Enterprising": 0
    }

    for answer in answers:
        dimension = answer["dimension"]
        value = answer["value"]

        scores[dimension] += value

    return scores