# tests/test_database.py

import sqlite3
import pytest

from database import db_initialization
from database import db_language


#############################################
#                   VERBS                   #
#############################################

def test_database_initializes(connection):

    cursor = connection.cursor()

    tables = cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
    """).fetchall()

    table_names = {table[0] for table in tables}

    assert "verbs" in table_names
    assert "tenses" in table_names
    assert "questions" in table_names
    assert "persons" in table_names
    assert "attempts" in table_names
    assert "verb_mastery" in table_names

    connection.close()

def test_verbs_exist(connection):
    cursor = connection.cursor()

    count = cursor.execute("""
        SELECT COUNT(*)
        FROM verbs
    """).fetchone()[0]

    assert count > 0

def test_duplicate_verb_not_allowed(connection):
    cursor = connection.cursor()

    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("""
            INSERT INTO verbs (infinitive, english)
            VALUES (?, ?)
        """, ("haber", "to have"))

#############################################
#                 Questions                 #
#############################################



