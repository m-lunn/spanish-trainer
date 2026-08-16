import random
import sqlite3
import database.db_questions as db_questions
import database.db_initialization as db_init
from tests import test_database
from quiz import run_quiz


if __name__ == "__main__":
    with sqlite3.connect('spanish.db') as connection:
        db_init.reset_database(connection)
    