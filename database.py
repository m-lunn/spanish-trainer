import sqlite3
import vocabulary
from questions import Question

DATABASE = "spanish.db"


def connect():
    return sqlite3.connect(DATABASE)


import sqlite3

DATABASE = "spanish.db"


def connect():
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def initialize_database():
    connection = connect()
    cursor = connection.cursor()

    # -------------------------
    # Verbs
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS verbs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            infinitive TEXT NOT NULL UNIQUE,
            english TEXT NOT NULL
        )
    """)

    # -------------------------
    # Tenses
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    """)

    # -------------------------
    # Questions
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            english TEXT NOT NULL,
            spanish TEXT NOT NULL,
            verb_id INTEGER NOT NULL,
            tense_id INTEGER NOT NULL,

            UNIQUE (english, spanish, verb_id, tense_id),

            FOREIGN KEY (verb_id) REFERENCES verbs(id),
            FOREIGN KEY (tense_id) REFERENCES tenses(id)
        )
    """)

    # -------------------------
    # Verb/Tense mastery
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS verb_mastery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            verb_id INTEGER NOT NULL,
            tense_id INTEGER NOT NULL,
            mastery INTEGER NOT NULL DEFAULT 0,
            last_practiced DATETIME,
            next_review DATETIME,

            UNIQUE (verb_id, tense_id),

            FOREIGN KEY (verb_id) REFERENCES verbs(id),
            FOREIGN KEY (tense_id) REFERENCES tenses(id)
        )
    """)

    # -------------------------
    # Attempts
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_id INTEGER NOT NULL,
            user_answer TEXT NOT NULL,
            correct INTEGER NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,

            FOREIGN KEY (question_id) REFERENCES questions(id)
        )
    """)

    connection.commit()
    connection.close()

def initialize_tenses():
    connection = connect()
    cursor = connection.cursor()

    tenses = [
        "present",
        "preterite",
        "imperfect",
        "future"
    ]

    for tense in tenses:
        cursor.execute("""
            INSERT OR IGNORE INTO tenses (name)
            VALUES (?)
        """, (tense,))

    connection.commit()
    connection.close()

def initialize_verbs():
    connection = connect()
    cursor = connection.cursor()

    for infinitive, english in vocabulary.verbs.items():
        cursor.execute("""
            INSERT OR IGNORE INTO verbs (infinitive, english)
            VALUES (?, ?)
        """, (infinitive, english))

    connection.commit()
    connection.close()

def initialize_questions(questions):
    connection = connect()
    cursor = connection.cursor()

    for question in questions:

        # Get the ID of the verb
        cursor.execute("""
            SELECT id
            FROM verbs
            WHERE infinitive = ?
        """, (question.verb,))

        verb_result = cursor.fetchone()

        if verb_result is None:
            raise ValueError(
                f"Verb '{question.verb}' does not exist in the database."
            )

        verb_id = verb_result[0]

        # Get the ID of the tense
        cursor.execute("""
            SELECT id
            FROM tenses
            WHERE name = ?
        """, (question.tense,))

        tense_result = cursor.fetchone()

        if tense_result is None:
            raise ValueError(
                f"Tense '{question.tense}' does not exist in the database."
            )

        tense_id = tense_result[0]

        # Add the question
        cursor.execute("""
            INSERT OR IGNORE INTO questions (
                english,
                spanish,
                verb_id,
                tense_id
            )
            VALUES (?, ?, ?, ?)
        """, (
            question.english,
            question.spanish,
            verb_id,
            tense_id
        ))

    connection.commit()
    connection.close()

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
        INSERT INTO questions (english, spanish, verb_id, tense_id)
        VALUES (?, ?, ?, ?)
    """, (english, spanish, verb_id, tense_id))

    connection.commit()
    connection.close()

def add_questions_from_list(questions):
    for question in questions:
        add_question(question.english, question.spanish, question.verb, question.tense)

def record_attempt(question_id, user_answer, correct):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO attempts (question_id, user_answer, correct)
        VALUES (?, ?, ?)
    """, (question_id, user_answer, correct))

    connection.commit()
    connection.close()

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


def print_database():
    connection = connect()
    cursor = connection.cursor()

    # Get all tables in the database
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """)

    tables = cursor.fetchall()

    for (table_name,) in tables:
        print("\n" + "=" * 60)
        print(f"TABLE: {table_name}")
        print("=" * 60)

        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        column_names = [column[1] for column in columns]

        # Get rows
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()

        if not rows:
            print("(empty)")
            continue

        # Calculate column widths
        widths = []

        for i, column_name in enumerate(column_names):
            width = len(str(column_name))

            for row in rows:
                width = max(width, len(str(row[i])))

            widths.append(width)

        # Print header
        header = " | ".join(
            str(column_names[i]).ljust(widths[i])
            for i in range(len(column_names))
        )

        print(header)
        print("-" * len(header))

        # Print rows
        for row in rows:
            print(
                " | ".join(
                    str(row[i]).ljust(widths[i])
                    for i in range(len(row))
                )
            )

    connection.close()

