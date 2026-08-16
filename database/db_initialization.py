import sqlite3
from database import db_questions, db_language
from language import verbs, tenses, persons, seed_questions
from database.exceptions import AuxiliaryVerbIsMissingException

DATABASE = "spanish.db"

def initialize_database(connection):
    create_tables(connection)
    initialize_verbs(connection)
    initialize_tenses(connection)
    initialize_persons(connection)
    initialize_questions(connection)

def create_tables(connection):
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
            code TEXT NOT NULL UNIQUE,
            mood TEXT NOT NULL,
            timeframe TEXT NOT NULL,
            auxiliary_verb_id INTEGER,

            UNIQUE (code, mood, timeframe, auxiliary_verb_id),

            FOREIGN KEY (auxiliary_verb_id) REFERENCES verbs(id)
        )
    """)

    # -------------------------
    # Persons
    # -------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            code TEXT NOT NULL UNIQUE,
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

            UNIQUE (english, spanish)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS question_verb_instances (
            question_id INTEGER NOT NULL,
            verb_id INTEGER NOT NULL,
            tense_id INTEGER NOT NULL,
            person_id INTEGER NOT NULL,
            
            PRIMARY KEY (question_id, verb_id, tense_id, person_id),
            
            FOREIGN KEY (question_id) REFERENCES questions(id),
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
            verb_id INTEGER NOT NULL,
            tense_id INTEGER NOT NULL,
            person_id INTEGER NOT NULL,
            mastery INTEGER NOT NULL DEFAULT 0,
            last_practiced DATETIME,
            next_review DATETIME,

            PRIMARY KEY (verb_id, tense_id, person_id),

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

def initialize_verbs(connection):
    cursor = connection.cursor()

    for verb in verbs.verbs:
        cursor.execute("""
            INSERT OR IGNORE INTO verbs (infinitive, english)
            VALUES (?, ?)
        """, (verb.infinitive, verb.english))

def initialize_tenses(connection):
    cursor = connection.cursor()

    haber_id = db_language.get_verb_id_from_infinitive(connection, "haber") 
    estar_id = db_language.get_verb_id_from_infinitive(connection, "estar")

    if not haber_id or not estar_id:
        raise AuxiliaryVerbIsMissingException

    for tense in tenses.Tenses:

        auxiliary_verb_id = None

        if tense.is_compound:
            if tense.auxiliary_verb.infinitive == "haber":
                auxiliary_verb_id = haber_id
            elif tense.auxiliary_verb.infinitive == "estar":
                auxiliary_verb_id = estar_id
        
        cursor.execute("""
            INSERT OR IGNORE INTO tenses (code, mood, timeframe, auxiliary_verb_id)
            VALUES (?, ?, ?, ?)
        """, (tense.code, tense.mood, tense.timeframe, auxiliary_verb_id))


def initialize_persons(connection):
    cursor = connection.cursor()

    for person in persons.Persons:
        cursor.execute("""
            INSERT OR IGNORE INTO persons (code, person_number, plurality)
            VALUES (?, ?, ?)
        """, (person.code, person.person_number, person.plurality))


def initialize_questions(connection):
    cursor = connection.cursor()

    for question in seed_questions.questions:
        db_questions.add_question(connection, question)


def drop_table(connection, table_name):
    cursor = connection.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

def drop_all_tables(connection):
    cursor = connection.cursor()

    tables = ["attempts", "verb_mastery", "questions", "persons", "tenses", "verbs"]

    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")

def reset_database(connection):
    drop_all_tables(connection)
    create_tables(connection)
    initialize_verbs(connection)
    initialize_tenses(connection)
    initialize_persons(connection)
    initialize_questions(connection)
    connection.commit()