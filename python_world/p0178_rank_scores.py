def rank_scores(scores: list[float]) -> list[tuple[float, int]]:
    """Return descending scores paired with their dense rank."""
    ranks = {score: rank for rank, score in enumerate(sorted(set(scores), reverse=True), 1)}
    return [(score, ranks[score]) for score in sorted(scores, reverse=True)]

