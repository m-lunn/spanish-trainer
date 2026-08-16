import random
import sqlite3
import database.db_attempts as db_attempts
import database.db_debug as db_debug
import database.db_questions as db_questions
import database.db_mastery as db_mastery
import database.db_initialization as db_init

def run_quiz(connection, questions, input_func=input):

    print("Welcome to the Spanish Trainer!")

    for question in questions:

        print(f"English: {question.english}")
        user_answer = input_func("Enter the Spanish translation: ")

        correct = user_answer.strip().lower() == question.spanish.lower()

        if correct:

            print("✓ Correct!")
            db_attempts.record_attempt(connection, question.id, user_answer, 1)

            for verb_instance in question.verb_instances:
                db_mastery.update_mastery(connection, verb_instance.verb.id, verb_instance.tense.id, verb_instance.person.id, 1)

        else:
            print(f"✗ The correct answer is: {question.spanish}")
            db_attempts.record_attempt(connection, question.id, user_answer, 0)

            for verb_instance in question.verb_instances:
                db_mastery.update_mastery(connection, verb_instance.verb.id, verb_instance.tense.id, verb_instance.person.id, -1)

        connection.commit()

def test_question_by_ids(connection, ids):
    questions = db_questions.create_questions_from_ids(connection, ids)
    run_quiz(connection, questions)

def main(connection):
    questions = db_questions.get_daily_questions_hard(connection, count=10)
    run_quiz(connection, questions=questions)

if __name__ == "__main__":

    with sqlite3.connect('spanish.db') as connection:
        db_init.reset_database(connection=connection)

        # test_question_by_ids(connection, [13])

        # db_debug.print_database(connection=connection)
        main(connection=connection)
    
