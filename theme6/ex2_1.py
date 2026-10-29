def analyze_scores(scores: list[int | float]) -> tuple[float, float, float]:
    return min(scores), max(scores), round(sum(scores) / len(scores), 2)