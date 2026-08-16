from models.verb_instance import VerbInstance

class Question:

    def __init__(self, english, spanish, verb_instances: list[VerbInstance], id=None):
        self.id = id
        self.english = english
        self.spanish = spanish
        self.verb_instances = verb_instances
        self.id = id

    def __str__(self):
        return (f"English: {self.english} | Spanish: {self.spanish}")

