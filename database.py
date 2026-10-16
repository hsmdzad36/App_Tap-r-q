"""Database layer: all SQL Server access lives here."""

import pyodbc

import config


def create_connection():
    connection_string = (
        f"DRIVER={{{config.DB_DRIVER}}};"
        f"SERVER={config.DB_SERVER};"
        f"DATABASE={config.DB_NAME};"
        f"Trusted_Connection={config.DB_TRUSTED_CONNECTION};"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(connection_string)


def add_student(student_name, student_score):
    with create_connection() as connection:
        connection.execute(
            "INSERT INTO Students (Name, Score) VALUES (?, ?)",
            student_name,
            student_score,
        )


def get_students():
    with create_connection() as connection:
        rows = connection.execute(
            "SELECT Name, Score FROM Students ORDER BY Id"
        ).fetchall()
    return [(row.Name, row.Score) for row in rows]


def get_student(student_name):
    """Return students whose name contains the given text."""
    with create_connection() as connection:
        rows = connection.execute(
            "SELECT Name, Score FROM Students WHERE Name LIKE ? ORDER BY Id",
            f"%{student_name}%",
        ).fetchall()
    return [(row.Name, row.Score) for row in rows]
