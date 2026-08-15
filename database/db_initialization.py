import sqlite3
from language import verbs, tenses, persons, seed_questions

DATABASE = "spanish.db"

def connect():
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def create_tables():
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
            mood TEXT NOT NULL,
            timeframe TEXT NOT NULL,
            is_compound INTEGER NOT NULL DEFAULT 0,
            auxiliary_verb_id INTEGER,

            UNIQUE (mood, timeframe, is_compound, auxiliary_verb_id),

            FOREIGN KEY (auxiliary_verb_id) REFERENCES verbs(id)
        )
    """)

    # -------------------------
    # Persons
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            person_number INTEGER NOT NULL,
            plurality TEXT NOT NULL
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
            person_id INTEGER NOT NULL,

            UNIQUE (english, spanish, verb_id, tense_id, person_id),

            FOREIGN KEY (verb_id) REFERENCES verbs(id),
            FOREIGN KEY (tense_id) REFERENCES tenses(id),
            FOREIGN KEY (person_id) REFERENCES persons(id)
        )
    """)

    # -------------------------
    # Verb/Tense/Person mastery
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS verb_mastery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            verb_id INTEGER NOT NULL,
            tense_id INTEGER NOT NULL,
            person_id INTEGER NOT NULL,
            mastery INTEGER NOT NULL DEFAULT 0,
            last_practiced DATETIME,
            next_review DATETIME,

            UNIQUE (verb_id, tense_id, person_id),

            FOREIGN KEY (verb_id) REFERENCES verbs(id),
            FOREIGN KEY (tense_id) REFERENCES tenses(id),
            FOREIGN KEY (person_id) REFERENCES persons(id)
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

    haber_id = get_verb_id("haber")
    estar_id = get_verb_id("estar")

    for tense in tenses.tenses:

        auxiliary_verb_id = None

        if tense.is_compound:
            if tense.auxiliary_verb == "haber":
                auxiliary_verb_id = haber_id
            elif tense.auxiliary_verb == "estar":
                auxiliary_verb_id = estar_id
        
        cursor.execute("""
            INSERT OR IGNORE INTO tenses (mood, timeframe, is_compound, auxiliary_verb_id)
            VALUES (?, ?, ?, ?)
        """, (tense.mood, tense.timeframe, int(tense.is_compound), auxiliary_verb_id))

    connection.commit()
    connection.close()

def initialize_verbs():
    connection = connect()
    cursor = connection.cursor()

    for verb in verbs.verbs:
        cursor.execute("""
            INSERT OR IGNORE INTO verbs (infinitive, english)
            VALUES (?, ?)
        """, (verb.infinitive, verb.english))

    connection.commit()
    connection.close()

def initialize_persons():
    connection = connect()
    cursor = connection.cursor()

    for person in persons.persons:
        cursor.execute("""
            INSERT OR IGNORE INTO persons (name, person_number, plurality)
            VALUES (?, ?, ?)
        """, (person.name, person.person_number, person.plurality))

    connection.commit()
    connection.close()

def initialize_questions():
    connection = connect()
    cursor = connection.cursor()

    for question in seed_questions.questions:
        cursor.execute("""
            INSERT OR IGNORE INTO questions (english, spanish, verb_id, tense_id, person_id)
            VALUES (?, ?, ?, ?, ?)
        """, (question.english, question.spanish, question.verb_id, question.tense_id, question.person_id))

    connection.commit()
    connection.close()
    
    
def drop_table(table_name):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    connection.commit()
    connection.close()

def drop_all_tables():
    connection = connect()
    cursor = connection.cursor()

    tables = ["attempts", "verb_mastery", "questions", "persons", "tenses", "verbs"]

    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")

    connection.commit()
    connection.close()

def reset_database():
    drop_all_tables()
    create_tables()
    initialize_verbs()
    initialize_tenses()
    initialize_persons()
    initialize_questions()

def get_verb_id(infinitive):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM verbs WHERE infinitive = ?", (infinitive,))
    result = cursor.fetchone()

    connection.close()

    if result:
        return result[0]
    else:
        return None