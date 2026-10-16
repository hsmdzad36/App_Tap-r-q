"""Business logic: grading and statistics (no UI, no SQL)."""

import config


def calculate_grade(score):
    if score >= config.GRADE_A_MIN:
        return "A"
    if score >= config.GRADE_B_MIN:
        return "B"
    if score >= config.GRADE_C_MIN:
        return "C"
    if score >= config.GRADE_D_MIN:
        return "D"
    return "F"


def is_valid_score(score):
    return config.MIN_SCORE <= score <= config.MAX_SCORE


def add_grades(students):
    """Convert (name, score) pairs into dicts that include the grade."""
    return [
        {"Name": name, "Score": score, "Grade": calculate_grade(score)}
        for name, score in students
    ]


def calculate_statistics(students):
    scores = [score for _, score in students]
    if not scores:
        return {"total": 0, "average": 0, "highest": 0, "lowest": 0}
    return {
        "total": len(scores),
        "average": round(sum(scores) / len(scores), 1),
        "highest": max(scores),
        "lowest": min(scores),
    }
