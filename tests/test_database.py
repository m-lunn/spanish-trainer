# tests/test_database.py

import sqlite3
import pytest

from database import db_initialization
from database import db_language
from database import db_questions
from quiz import run_quiz
import random


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
    assert "question_verb_instances" in table_names
    assert "verb_cards" in table_names

    connection.close()

#############################################
#                   VERBS                   #
#############################################

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

# def test_mastery_updating(connection):

#     questions = db_questions.create_questions_from_ids(connection, [1])

#     def answer_input_correct(prompt):
#         return questions[0].spanish

#     def answer_input_incorrect(prompt):
#         return ''

#     def questions_func(connection, count):
#         return questions


#     for _ in range(4):
#         run_quiz(connection, answer_input_correct, questions_func)

#     for verb_instance in questions[0].verb_instances:

#         cursor = connection.cursor()
#         cursor.execute("""
#             SELECT mastery
#             FROM verb_mastery
#             WHERE verb_id = ?
#             AND tense_id = ?
#             AND person_id = ?
#         """, (verb_instance.verb.id, verb_instance.tense.id, verb_instance.person.id)),

#         mastery_count = cursor.fetchone()[0]

#         assert mastery_count == 4

#     for _ in range(3):
#         run_quiz(connection, answer_input_correct, questions_func)

#     for verb_instance in questions[0].verb_instances:
    
#             cursor = connection.cursor()
#             cursor.execute("""
#                 SELECT mastery
#                 FROM verb_mastery
#                 WHERE verb_id = ?
#                 AND tense_id = ?
#                 AND person_id = ?
#             """, (verb_instance.verb.id, verb_instance.tense.id, verb_instance.person.id)),
    
#             mastery_count = cursor.fetchone()[0]
    
#             assert mastery_count == 5

#     for _ in range(6):
#             run_quiz(connection, answer_input_incorrect, questions_func)
    
#     for verb_instance in questions[0].verb_instances:
    
#             cursor = connection.cursor()
#             cursor.execute("""
#                 SELECT mastery
#                 FROM verb_mastery
#                 WHERE verb_id = ?
#                 AND tense_id = ?
#                 AND person_id = ?
#             """, (verb_instance.verb.id, verb_instance.tense.id, verb_instance.person.id)),
    
#             mastery_count = cursor.fetchone()[0]
    
#             assert mastery_count == 0


def test_full_quiz(connection):

    questions = db_questions.get_all_questions(connection=connection)
    test_length = len(questions)

    question_iterator = iter(questions)

    def answer_input(prompt):
        question = next(question_iterator)
        return question.spanish

    def questions_func(connection, count):
        return questions

    def rating_input(prompt):
        return str(random.randrange(1, 4))

    run_quiz(connection=connection, input_func=answer_input, questions_func=questions_func, rating_input=rating_input)

    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*) 
        FROM ATTEMPTS
    """)
    assert cursor.fetchone()[0] == test_length

    cursor = connection.cursor()
    cursor.execute("""
        SELECT COUNT(*) 
        FROM attempts
        WHERE correct = 1
    """)
    assert cursor.fetchone()[0] == test_length

