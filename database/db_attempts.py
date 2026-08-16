def record_attempt(connection, question_id, user_answer, correct):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO attempts (question_id, user_answer, correct)
        VALUES (?, ?, ?)
    """, (question_id, user_answer, correct))