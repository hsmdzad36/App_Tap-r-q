"""Streamlit UI. Run with: streamlit run app.py"""

import streamlit as st

import config
import database
import services


def render_add_student_form():
    st.subheader("Add Student")
    student_name = st.text_input("Student Name")
    student_score = st.number_input(
        "Score", min_value=config.MIN_SCORE, max_value=config.MAX_SCORE, step=1
    )
    if st.button("Add Student"):
        if not student_name.strip():
            st.error("Student name cannot be empty.")
        elif not services.is_valid_score(student_score):
            st.error("Score is out of range.")
        else:
            database.add_student(student_name.strip(), int(student_score))
            st.success(f"{student_name} added.")


def render_statistics(students):
    st.subheader("Statistics")
    stats = services.calculate_statistics(students)
    columns = st.columns(4)
    columns[0].metric("Total Students", stats["total"])
    columns[1].metric("Average Score", stats["average"])
    columns[2].metric("Highest Score", stats["highest"])
    columns[3].metric("Lowest Score", stats["lowest"])


def render_student_table(students):
    st.dataframe(services.add_grades(students), use_container_width=True)


def main():
    st.title("Student Performance Dashboard")
    render_add_student_form()

    search_text = st.text_input("Search Student")
    all_students = database.get_students()
    render_statistics(all_students)

    st.subheader("Students")
    shown_students = database.get_student(search_text) if search_text else all_students
    render_student_table(shown_students)


main()
