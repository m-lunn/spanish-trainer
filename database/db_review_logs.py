from models.review_log import ReviewLog

def get_review_logs_for_card(connection, verb_id, tense_id, person_id):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
           rating,
           review_datetime,
           review_duration
        FROM review_logs
        WHERE verb_id = ? AND tense_id = ? AND person_id = ? 
    """, (verb_id, tense_id, person_id))

    rows = cursor.fetchall()
    review_logs = []

    for row in rows:
        review_logs.append(
            ReviewLog(
                verb_id, tense_id, person_id, row[0], row[1], row[2]
            )
        )

def add_review_log(connection, verb_id, tense_id, person_id, rating, review_datetime, review_duration=None):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO review_logs (
            verb_id,
            tense_id,
            person_id,
            rating,
            review_datetime,
            review_duration
        )
        VALUES (?, ?, ?, ?, ?, ?)
""", (verb_id, tense_id, person_id, rating, review_datetime, review_duration))

    connection.commit()