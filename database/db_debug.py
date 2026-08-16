def print_database(connection):
    cursor = connection.cursor()

    # Get all tables in the database
    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """)

    tables = cursor.fetchall()

    for (table_name,) in tables:
        print("\n" + "=" * 60)
        print(f"TABLE: {table_name}")
        print("=" * 60)

        # Get column names
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        column_names = [column[1] for column in columns]

        # Get rows
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()


        # Calculate column widths
        widths = []

        for i, column_name in enumerate(column_names):
            width = len(str(column_name))

            for row in rows:
                width = max(width, len(str(row[i])))

            widths.append(width)

        # Print header
        header = " | ".join(
            str(column_names[i]).ljust(widths[i])
            for i in range(len(column_names))
        )

        print(header)
        print("-" * len(header))

        if not rows:
            print("(empty)")
            continue
        
        # Print rows
        for row in rows:
            print(
                " | ".join(
                    str(row[i]).ljust(widths[i])
                    for i in range(len(row))
                )
            )

def print_table_counts(connection):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM sqlite_master
        WHERE type = 'table'
        AND name NOT LIKE 'sqlite_%'
        ORDER BY name
    """)

    tables = cursor.fetchall()

    print("\nDatabase table counts:")
    print("-" * 35)

    for (table_name,) in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        count = cursor.fetchone()[0]

        print(f"{table_name}: {count}")

    print("-" * 35)
