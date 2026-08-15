import sqlite3

DATABASE = "spanish.db"

def record_attempt(question_id, user_answer, correct):
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO attempts (question_id, user_answer, correct)
        VALUES (?, ?, ?)
    """, (question_id, user_answer, correct))

    connection.commit()
    connection.close()