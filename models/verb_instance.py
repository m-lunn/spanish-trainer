class VerbInstance:

    def __init__(self, verb, tense, person, is_target=True):
        self.verb = verb
        self.tense = tense
        self.person = person
        self.is_target = is_target