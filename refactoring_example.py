"""Task 2: refactoring example.

--- BEFORE (bad) ---
def f(x, y):
    if y >= 90: return x + " A"
    elif y >= 80: return x + " B"
    elif y >= 70: return x + " C"
    elif y >= 60: return x + " D"
    else: return x + " F"

--- AFTER (clean) is below ---
"""

GRADE_THRESHOLDS = [(90, "A"), (80, "B"), (70, "C"), (60, "D")]
FAILING_GRADE = "F"


def calculate_grade(student_score):
    for minimum_score, grade in GRADE_THRESHOLDS:
        if student_score >= minimum_score:
            return grade
    return FAILING_GRADE


def format_student_result(student_name, student_score):
    return f"{student_name} {calculate_grade(student_score)}"
