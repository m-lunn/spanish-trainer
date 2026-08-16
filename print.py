import database.db_debug as db_debug
import sqlite3

if __name__ == "__main__":
    with sqlite3.connect('spanish.db') as connection:
        db_debug.print_database(connection)
        db_debug.print_table_counts(connection)