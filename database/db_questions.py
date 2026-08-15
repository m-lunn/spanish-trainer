import sqlite3
from models.question import Question

DATABASE = "spanish.db"

def connect():
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection

def add_question(english, spanish, verb_infinitive, tense_name):
    connection = connect()
    cursor = connection.cursor()

    # Get verb_id
    cursor.execute("SELECT id FROM verbs WHERE infinitive = ?", (verb_infinitive,))
    verb_id = cursor.fetchone()
    if verb_id is None:
        raise ValueError(f"Verb '{verb_infinitive}' not found in database.")
    verb_id = verb_id[0]

    # Get tense_id
    cursor.execute("SELECT id FROM tenses WHERE name = ?", (tense_name,))
    tense_id = cursor.fetchone()
    if tense_id is None:
        raise ValueError(f"Tense '{tense_name}' not found in database.")
    tense_id = tense_id[0]

    # Insert question
    cursor.execute("""
        INSERT OR IGNORE INTO questions (english, spanish, verb_id, tense_id)
        VALUES (?, ?, ?, ?)
    """, (english, spanish, verb_id, tense_id))

    connection.commit()
    connection.close()

def add_questions_from_list(questions):
    for question in questions:
        add_question(question.english, question.spanish, question.infinitive, question.tense)

def get_daily_questions_hard(count=10):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            q.id,
            q.english,
            q.spanish,
            q.verb_id,
            q.tense_id,
            COALESCE(vm.mastery, 0)
        FROM questions q
        LEFT JOIN verb_mastery vm
            ON q.verb_id = vm.verb_id
            AND q.tense_id = vm.tense_id
        ORDER BY
            COALESCE(vm.mastery, 0) ASC,
            RANDOM()
        LIMIT ?
    """, (count,))

    rows = cursor.fetchall()

    connection.close()

    return [
        Question(
            id=row[0],
            english=row[1],
            spanish=row[2],
            verb_id=row[3],
            tense_id=row[4]
        )
        for row in rows
    ]

def get_daily_questions_random(count=10):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            q.id,
            q.english,
            q.spanish,
            q.verb_id,
            q.tense_id
        FROM questions q
        ORDER BY RANDOM()
        LIMIT ?
    """, (count,))

    rows = cursor.fetchall()

    connection.close()

    return [
        Question(
            id=row[0],
            english=row[1],
            spanish=row[2],
            verb_id=row[3],
            tense_id=row[4]
        )
        for row in rows
    ]

def delete_question(question_id):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))

    connection.commit()
    connection.close()

def delete_all_questions():
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM questions")

    connection.commit()
    connection.close()