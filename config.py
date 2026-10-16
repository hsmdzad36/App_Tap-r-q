"""Application configuration: connection settings and grading rules."""

DB_DRIVER = "ODBC Driver 17 for SQL Server"
DB_SERVER = "localhost"
DB_NAME = "UniversityDB"
DB_TRUSTED_CONNECTION = "yes"  # Windows authentication

MIN_SCORE = 0
MAX_SCORE = 100

# Grade thresholds (minimum score for each grade)
GRADE_A_MIN = 90
GRADE_B_MIN = 80
GRADE_C_MIN = 70
GRADE_D_MIN = 60
