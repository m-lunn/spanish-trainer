import sqlite3
import pytest
import database.db_initialization as db_init

@pytest.fixture
def connection():
    connection = sqlite3.connect(":memory:")
    connection.execute("PRAGMA foreign_keys = ON")

    db_init.initialize_database(connection)

    yield connection

    connection.close()