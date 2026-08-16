class Tense:

    def __init__(self, code, mood, timeframe, auxiliary_verb=None, id=None):
        self.code = code
        self.mood = mood
        self.timeframe = timeframe
        self.auxiliary_verb = auxiliary_verb
        self.id = id

    @property
    def is_compound(self):
        return self.auxiliary_verb is not None