import questions, vocabulary, random
from database import initialize_database, initialize_tenses, initialize_verbs, initialize_questions, record_attempt, update_mastery, print_database, get_daily_questions_hard

def main():
    print("Welcome to the Spanish Trainer!")

    questions = get_daily_questions_hard(count=10)

    for question in questions:
        print(f"English: {question.english}")
        user_answer = input("Enter the Spanish translation: ")

        correct = user_answer.strip().lower() == question.spanish.lower()

        if correct:
            print("✓ Correct!")
            record_attempt(question.id, user_answer, 1)
            update_mastery(question.verb_id, question.tense_id, 1)
        else:
            print(f"✗ The correct answer is: {question.spanish}")
            record_attempt(question.id, user_answer, 0)
            update_mastery(question.verb_id, question.tense_id, -1)


if __name__ == "__main__":
    initialize_database()

    main()
