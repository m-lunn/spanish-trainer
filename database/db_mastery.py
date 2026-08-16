import sqlite3

def update_mastery(connection, verb_id, tense_id, person_id, mastery_change):
    cursor = connection.cursor()

    # Check if a record exists
    cursor.execute("""
        SELECT verb_id, tense_id, person_id, mastery FROM verb_mastery
        WHERE verb_id = ? AND tense_id = ? AND person_id = ?
    """, (verb_id, tense_id, person_id))
    record = cursor.fetchone()

    if record:
        # Update existing record
        new_mastery = max(0, min(5, record[3] + mastery_change))  # Ensure mastery stays between 0 and 5
        cursor.execute("""
            UPDATE verb_mastery
            SET mastery = ?, last_practiced = CURRENT_TIMESTAMP
            WHERE verb_id = ? AND tense_id = ? AND person_id = ? 
        """, (new_mastery, record[0], record[1], [record[2]]))
    else:
        # Insert new record
        new_mastery = max(0, mastery_change)  # Ensure mastery doesn't go below 0
        cursor.execute("""
            INSERT INTO verb_mastery (verb_id, tense_id, person_id, mastery, last_practiced)
            VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
        """, (verb_id, tense_id, person_id, new_mastery))