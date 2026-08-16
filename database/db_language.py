import sqlite3
from models.verb import Verb
from database.exceptions import TenseNotFoundException, PersonNotFoundException

def get_verb_id_from_infinitive(connection, infinitive):
    cursor = connection.cursor()

    cursor.execute("SELECT id FROM verbs WHERE infinitive = ?", (infinitive,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        return None

def get_verb_object_from_id(connection, id):
    cursor = connection.cursor()

    cursor.execute("SELECT id, infinitive, english FROM verbs WHERE id = ?", (id,))
    result = cursor.fetchone()

    if result:
        return Verb(
            result[1], result[2], result[0]
        )
    else:
        return None

def add_verb_from_parts(connection, infinitive, english):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO verbs (infinitive, english)
        VALUES (?, ?)
    """, (infinitive, english))

def get_verb_id_from_verb_object(connection, verb: Verb):
    get_verb_id_from_infinitive(connection, verb.infinitive)

def add_verb_from_verb_object(connection, verb: Verb):
    add_verb_from_parts(connection, verb.infinitive, verb.english)

def get_tense_id(connection, code):

    cursor = connection.cursor()

    cursor.execute("SELECT id FROM tenses WHERE code = ?", (code,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        raise TenseNotFoundException

def get_person_id(connection, code):
    cursor = connection.cursor()
    
    cursor.execute("SELECT id FROM persons WHERE code = ?", (code,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        raise PersonNotFoundException