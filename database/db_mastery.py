import sqlite3

DATABASE = "spanish.db"

def connect():
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def update_mastery(verb_id, tense_id, mastery_change):
    connection = connect()
    cursor = connection.cursor()

    # Check if a record exists
    cursor.execute("""
        SELECT id, mastery FROM verb_mastery
        WHERE verb_id = ? AND tense_id = ?
    """, (verb_id, tense_id))
    record = cursor.fetchone()

    if record:
        # Update existing record
        new_mastery = max(0, min(5, record[1] + mastery_change))  # Ensure mastery stays between 0 and 5
        cursor.execute("""
            UPDATE verb_mastery
            SET mastery = ?, last_practiced = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (new_mastery, record[0]))
    else:
        # Insert new record
        new_mastery = max(0, mastery_change)  # Ensure mastery doesn't go below 0
        cursor.execute("""
            INSERT INTO verb_mastery (verb_id, tense_id, mastery, last_practiced)
            VALUES (?, ?, ?, CURRENT_TIMESTAMP)
        """, (verb_id, tense_id, new_mastery))

    connection.commit()
    connection.close()