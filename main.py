import random
from database import db_attempts
import database.db_debug as db_debug
import database.db_questions as db_questions
import database.db_mastery as db_mastery
import database.db_initialization as db_init
from models.question import Question

def main():
  
    print("Welcome to the Spanish Trainer!")

    questions = db_questions.get_daily_questions_hard(count=10)

    for question in questions:
        print(f"English: {question.english}")
        user_answer = input("Enter the Spanish translation: ")

        correct = user_answer.strip().lower() == question.spanish.lower()

        if correct:
            print("✓ Correct!")
            db_attempts.record_attempt(question.id, user_answer, 1)
            db_mastery.update_mastery(question.verb_id, question.tense_id, 1)
        else:
            print(f"✗ The correct answer is: {question.spanish}")
            db_attempts.record_attempt(question.id, user_answer, 0)
            db_mastery.update_mastery(question.verb_id, question.tense_id, -1)


if __name__ == "__main__":

    db_init.reset_database()

    db_debug.print_database()
    # main()
