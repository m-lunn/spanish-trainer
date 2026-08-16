from database import db_attempts, db_mastery, db_questions, db_language, db_debug, db_initialization

def run_quiz(connection, input_func=input, questions_func=db_questions.get_daily_questions_random):

    questions = questions_func(connection, 10)
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