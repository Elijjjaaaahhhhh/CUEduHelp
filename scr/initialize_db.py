# src/initialize_db.py
import sqlite3

def initialize_db(db_path):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrolled_students (
        id TEXT PRIMARY KEY,
        name TEXT,
        gender TEXT,
        level TEXT,
        college TEXT,
        openness INTEGER,
        conscientiousness INTEGER,
        prediction TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS prospective_students (
        id TEXT PRIMARY KEY,
        name TEXT,
        openness INTEGER,
        conscientiousness INTEGER,
        waec_subject_picked INTEGER,
        waec_subject_selected_1 TEXT,
        waec_subject_selected_2 TEXT,
        waec_subject_selected_3 TEXT,
        waec_subject_selected_4 TEXT,
        waec_subject_selected_5 TEXT,
        waec_subject_selected_6 TEXT,
        waec_subject_selected_7 TEXT,
        waec_subject_selected_8 TEXT,
        waec_subject_selected_9 TEXT,
        jamb_subject_selected_1 TEXT,
        jamb_subject_selected_2 TEXT,
        jamb_subject_selected_3 TEXT,
        jamb_subject_selected_4 TEXT,
        jamb_score INTEGER,
        preferred_course TEXT,
        recommendation_1 TEXT,
        recommendation_2 TEXT,
        recommendation_3 TEXT
    )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    db_path = "c:/Users/elich/Documents/PROJECT/CUEduHelp/database/students.db"
    initialize_db(db_path)
