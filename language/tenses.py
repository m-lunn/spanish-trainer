from models.tense import tense

tenses = [
    tense("indicative", "past perfect", is_compound=True, auxiliary_verb="haber"),
    tense("indicative", "preterite"),
    tense("indicative", "imperfect"),
    tense("indicative", "present perfect", is_compound=True, auxiliary_verb="haber" ),
    tense("indicative", "present"),
    tense("indicative", "conditional"),
    tense("indicative", "conditional perfect", is_compound=True, auxiliary_verb="haber"),
    tense("indicative", "future"),
    tense("indicative", "future perfect", is_compound=True, auxiliary_verb="haber"),
    tense("subjunctive", "past perfect", is_compound=True, auxiliary_verb="haber"),
    tense("subjunctive", "imperfect"),
    tense("subjunctive", "present perfect", is_compound=True, auxiliary_verb="haber"),
    tense("subjunctive", "present"),
    tense("imperative", "affirmative"),
    tense("imperative", "negative"),
    tense("progressive", "past", is_compound=True, auxiliary_verb="estar"),
    tense("progressive", "present", is_compound=True, auxiliary_verb="estar"),
    tense("progressive", "future", is_compound=True, auxiliary_verb="estar"),
    tense("progressive", "conditional", is_compound=True, auxiliary_verb="estar")
]