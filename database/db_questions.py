import sqlite3
from database import db_language
from database import db_debug
from models.question import Question
from models.verb import Verb
from models.tense import Tense
from models.person import Person
from models.verb_instance import VerbInstance

def add_question(connection, question: Question):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT OR IGNORE INTO questions (english, spanish)
        VALUES (?, ?)
    """, (question.english, question.spanish))
    
    question_id = cursor.lastrowid
    
    for verb_instance in question.verb_instances:
        db_language.add_verb_from_verb_object(
            connection,
            verb=verb_instance.verb
        )
        verb_id = db_language.get_verb_id_from_infinitive(
            connection, verb_instance.verb.infinitive
        )
        tense_id = db_language.get_tense_id(
            connection,
            code=verb_instance.tense.code
        )
        person_id = db_language.get_person_id(
            connection,
            code=verb_instance.person.code
        )
        cursor.execute("""
            INSERT OR IGNORE INTO question_verb_instances (question_id, verb_id, tense_id, person_id)
            VALUES (?, ?, ?, ?)
        """, (question_id, verb_id, tense_id, person_id)
            )

def select_hardest_questions(connection, count=10):
    cursor = connection.cursor()

    cursor.execute("""
            SELECT
                q.id
            FROM questions q
    
            INNER JOIN question_verb_instances qvi
                ON q.id = qvi.question_id
    
            LEFT JOIN verb_mastery vm
                ON qvi.verb_id = vm.verb_id
                AND qvi.tense_id = vm.tense_id
                AND qvi.person_id = vm.person_id
    
            GROUP BY q.id
    
            ORDER BY
                MIN(COALESCE(vm.mastery, 0)) ASC,
                RANDOM()
    
            LIMIT ?
        """, (count,))

    return [row[0] for row in cursor.fetchall()]

def select_easiest_questions(connection, count=10):
    cursor = connection.cursor()

    cursor.execute("""
            SELECT
                q.id
            FROM questions q
    
            INNER JOIN question_verb_instances qvi
                ON q.id = qvi.question_id
    
            LEFT JOIN verb_mastery vm
                ON qvi.verb_id = vm.verb_id
                AND qvi.tense_id = vm.tense_id
                AND qvi.person_id = vm.person_id
    
            GROUP BY q.id
    
            ORDER BY
                MAX(COALESCE(vm.mastery, 0)) ASC,
                RANDOM()
    
            LIMIT ?
        """, (count,))

    return [row[0] for row in cursor.fetchall()]

def select_random_questions(connection, count=10):
    cursor = connection.cursor()

    cursor.execute("""
            SELECT
                q.id
            FROM 
                questions q
            ORDER BY
                RANDOM()
            LIMIT ?
        """, (count,))

    return [row[0] for row in cursor.fetchall()]

def get_daily_questions_hard(connection, count=10):
    cursor = connection.cursor()

    question_ids = select_hardest_questions(connection, count)

    if not question_ids:
        return []

    questions = create_questions_from_ids(connection, question_ids=question_ids)

    return questions

def create_questions_from_ids(connection, question_ids):
    cursor = connection.cursor()

    # ---------------------------------------------------------
    # Retrieve questions and all their verb instances
    # ---------------------------------------------------------
    
    placeholders = ",".join("?" for _ in question_ids)

    cursor.execute(f"""
        SELECT
            q.id,
            q.english,
            q.spanish,

            v.id,
            v.infinitive,
            v.english,

            t.id,
            t.code,
            t.mood,
            t.timeframe,
            t.auxiliary_verb_id,

            p.id,
            p.code,
            p.person_number,
            p.plurality

        FROM questions q

        INNER JOIN question_verb_instances qvi
            ON q.id = qvi.question_id

        INNER JOIN verbs v
            ON qvi.verb_id = v.id

        INNER JOIN tenses t
            ON qvi.tense_id = t.id

        LEFT JOIN persons p
            ON qvi.person_id = p.id

        WHERE q.id IN ({placeholders})

        ORDER BY q.id
    """, question_ids)

    rows = cursor.fetchall()

    # ---------------------------------------------------------
    # Build the Python objects
    # ---------------------------------------------------------

    questions = {}

    for row in rows:

        question_id = row[0]

        if question_id not in questions:
            questions[question_id] = Question(
                id=row[0],
                english=row[1],
                spanish=row[2],
                verb_instances=[]
            )

        verb = Verb(
            id=row[3],
            infinitive=row[4],
            english=row[5]
        )

        tense = Tense(
            id=row[6],
            code=row[7],
            mood=row[8],
            timeframe=row[9],
            auxiliary_verb=db_language.get_verb_object_from_id(connection, row[10])
        )

        person = None

        if row[11] is not None:
            person = Person(
                id=row[11],
                code=row[12],
                person_number=row[13],
                plurality=row[14]
            )

        questions[question_id].verb_instances.append(
            VerbInstance(
                verb,
                tense,
                person
            )
        )

    return list(questions.values())

def delete_question(connection, question_id):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM questions WHERE id = ?", (question_id,))

def delete_all_questions(connection):
    cursor = connection.cursor()

    cursor.execute("DELETE FROM questions")