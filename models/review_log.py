class ReviewLog():
    def __init__(
            self, 
            verb_id,
            tense_id,
            person_id,
            rating,
            review_datetime,
            review_duration=None
    ):
        self.verb_id = verb_id
        self.tense_id = tense_id
        self.person_id = person_id
        self.rating = rating
        self.review_datetime = review_datetime
        self.review_duration = review_duration
