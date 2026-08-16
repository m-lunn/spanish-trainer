from database import db_attempts, db_review_logs, db_questions, db_cards
from fsrs import Scheduler, Rating
from datetime import datetime, UTC

def get_fsrs_rating(input_func=input):
    while True:
        print()
        print("How difficult was that?")
        print("1. Again")
        print("2. Hard")
        print("3. Good")
        print("4. Easy")

        choice = input_func("Choose 1-4: ").strip()

        if choice in ("1", "2", "3", "4"):
            return Rating(int(choice))

        print("Please enter a number from 1 to 4.")

def run_quiz(connection, input_func=input, questions_func=db_questions.get_daily_questions_random, rating_input=input):
    scheduler = Scheduler()

    questions = questions_func(connection, 10)

    print("Welcome to the Spanish Trainer!")

    for question in questions:

        start = datetime.now(tz=UTC).timestamp()

        print(f"\nEnglish: {question.english}")

        user_answer = input_func(
            "Enter the Spanish translation: "
        )

        stop = datetime.now(tz=UTC).timestamp()
        duration = stop - start

        correct = (
            user_answer.strip().lower()
            == question.spanish.lower()
        )

        if correct:
            print("✓ Correct!")
            db_attempts.record_attempt(connection, question.id, user_answer, 1)

        else:
            print(
                f"✗ The correct answer is: "
                f"{question.spanish}"
            )
            db_attempts.record_attempt(connection, question.id, user_answer, 0)

        rating = get_fsrs_rating(rating_input)

        for verb_instance in question.verb_instances:

#
            if not verb_instance.is_target:
                continue

            verb_id = verb_instance.verb.id
            tense_id = verb_instance.tense.id
            person_id = verb_instance.person.id

            card = db_cards.get_card_by_id(
                connection,
                verb_id,
                tense_id,
                person_id
            )

            if card is None:
                continue

            updated_card, review_log = scheduler.review_card(
                card,
                rating,
                datetime.now(tz=UTC),
                int(duration)
            )

            db_cards.update_card(connection, updated_card)
            db_review_logs.add_review_log(
                connection,
                verb_id,
                tense_id,
                person_id,
                review_log.rating,
                review_log.review_datetime,
                review_log.review_duration
            )

        connection.commit()