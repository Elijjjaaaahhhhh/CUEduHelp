# src/db_operations.py
import sqlite3

def insert_enrolled_student(student_info):
    connection = sqlite3.connect("c:/Users/elich/Documents/PROJECT/CUEduHelp/database/students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT 1 FROM enrolled_students WHERE id = ?", (student_info['id'],))
    if cursor.fetchone() is not None:
        raise ValueError(f"Student with ID {student_info['id']} already exists in enrolled_students.")

    cursor.execute("""
    INSERT INTO enrolled_students (id, name, gender, level, college, openness, conscientiousness, prediction)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student_info['id'], student_info['name'], student_info['gender'], student_info['level'],
        student_info['college'], student_info['openness'], student_info['conscientiousness'], student_info['prediction']
    ))

    connection.commit()
    connection.close()

def insert_prospective_student(student_info):
    connection = sqlite3.connect("c:/Users/elich/Documents/PROJECT/CUEduHelp/database/students.db")
    cursor = connection.cursor()

    cursor.execute("SELECT 1 FROM prospective_students WHERE id = ?", (student_info['id'],))
    if cursor.fetchone() is not None:
        raise ValueError(f"Student with ID {student_info['id']} already exists in prospective_students.")

    columns = (
        "id", "name", "openness", "conscientiousness", "waec_subject_picked", "waec_subject_selected_1",
        "waec_subject_selected_2", "waec_subject_selected_3", "waec_subject_selected_4", "waec_subject_selected_5",
        "waec_subject_selected_6", "waec_subject_selected_7", "waec_subject_selected_8", "waec_subject_selected_9",
        "jamb_subject_selected_1", "jamb_subject_selected_2", "jamb_subject_selected_3", "jamb_subject_selected_4",
        "jamb_score", "preferred_course", "recommendation_1", "recommendation_2", "recommendation_3"
    )
    
    values = (
        student_info['id'], student_info['name'], student_info['openness'], student_info['conscientiousness'],
        student_info['waec_subject_picked'], student_info['waec_subject_selected_1'], student_info['waec_subject_selected_2'],
        student_info['waec_subject_selected_3'], student_info['waec_subject_selected_4'], student_info['waec_subject_selected_5'],
        student_info['waec_subject_selected_6'], student_info['waec_subject_selected_7'], student_info['waec_subject_selected_8'],
        student_info['waec_subject_selected_9'], student_info['jamb_subject_selected_1'], student_info['jamb_subject_selected_2'],
        student_info['jamb_subject_selected_3'], student_info['jamb_subject_selected_4'], student_info['jamb_score'],
        student_info['preferred_course'], student_info['recommendation_1'], student_info['recommendation_2'],
        student_info['recommendation_3']
    )

    # Print columns and values for debugging
    print("Columns:", columns)
    print("Values:", values)

    cursor.execute("""
    INSERT INTO prospective_students (id, name, openness, conscientiousness, waec_subject_picked,
    waec_subject_selected_1, waec_subject_selected_2, waec_subject_selected_3, waec_subject_selected_4,
    waec_subject_selected_5, waec_subject_selected_6, waec_subject_selected_7, waec_subject_selected_8,
    waec_subject_selected_9, jamb_subject_selected_1, jamb_subject_selected_2, jamb_subject_selected_3,
    jamb_subject_selected_4, jamb_score, preferred_course, recommendation_1, recommendation_2, recommendation_3)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, values)

    connection.commit()
    connection.close()
