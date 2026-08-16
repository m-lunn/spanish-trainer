from models.verb_card import VerbCard
from datetime import datetime, UTC

def update_card(connection, card):

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE verb_cards
        SET
            state = ?,
            step = ?,
            stability = ?,
            difficulty = ?,
            due = ?,
            last_review = ?
        WHERE
            verb_id = ?
            AND tense_id = ?
            AND person_id = ?
    """, (
        card.state,
        card.step,
        card.stability,
        card.difficulty,
        card.due,
        card.last_review if card.last_review else None,
        card.verb_id,
        card.tense_id,
        card.person_id
    ))
    connection.commit()

def add_card(connection, card):
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO verb_cards (
            verb_id,
            tense_id,
            person_id,
            state,
            step,
            stability,
            difficulty,
            due,
            last_review
            )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        )
    """, (card.verb_id,
          card.tense_id,
          card.person_id,
          card.state,
          card.step,
          card.stability,
          card.difficulty,
          card.due,
          card.last_review))
    connection.commit()

def get_card_by_id(connection, verb_id, tense_id, person_id):
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 
            state,
            step,
            stability,
            difficulty,
            due,
            last_review
         
        FROM verb_cards
        WHERE verb_id = ? AND tense_id = ? AND person_id = ?
    """, (verb_id, tense_id, person_id))

    row = cursor.fetchone()

    return VerbCard.from_database(
        verb_id=verb_id,
        tense_id=tense_id,
        person_id=person_id,
        state=row[0],
        step=row[1],
        stability=row[2],
        difficulty=row[3],
        due=datetime.fromisoformat(row[4]).astimezone(UTC),
        last_review=datetime.fromisoformat(row[5]).astimezone(UTC) if row[5] else None
    )

