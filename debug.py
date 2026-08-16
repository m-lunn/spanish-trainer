import random
import sqlite3

from fsrs import Scheduler, Card, Rating

from database import db_questions, db_cards
import database.db_initialization as db_init
from tests import test_database
from quiz import run_quiz
from models.verb_card import VerbCard
from datetime import datetime, timezone


if __name__ == "__main__":
    with sqlite3.connect('spanish.db') as connection:
        run_quiz(connection)
    