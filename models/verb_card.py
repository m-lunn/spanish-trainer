from fsrs import Card

class VerbCard(Card):

    def __init__(self, verb_id, tense_id, person_id):
        super().__init__()

        self.verb_id = verb_id
        self.tense_id = tense_id
        self.person_id = person_id

    @classmethod
    def from_database(
        cls,
        verb_id,
        tense_id,
        person_id,
        state,
        step,
        stability,
        difficulty,
        due,
        last_review
    ):
        card = cls(
            verb_id,
            tense_id,
            person_id
        )

        card.state = state
        card.step = step
        card.stability = stability
        card.difficulty = difficulty
        card.due = due
        card.last_review = last_review

        return card