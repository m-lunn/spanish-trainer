import random
import sqlite3
import database.db_questions as db_questions
import database.db_initialization as db_init
from quiz import run_quiz


def main():
    with sqlite3.connect('spanish.db') as connection:
        db_init.reset_database(connection=connection)
        run_quiz(connection)

if __name__ == "__main__":
     main()
    
