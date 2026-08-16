from models.tense import Tense
from models.verb import Verb

Tenses = (
    Tense(
        "IND_PAST_PERFECT",
        "indicative",
        "past perfect",
        Verb("haber", "to have (auxiliary)")
    ),
    Tense(
        "IND_PRETERITE",
        "indicative",
        "preterite"
    ),
    Tense(
        "IND_IMPERFECT",
        "indicative",
        "imperfect"
    ),
    Tense(
        "IND_PRESENT_PERFECT",
        "indicative",
        "present perfect",
        Verb("haber", "to have (auxiliary)")
    ),
    Tense(
        "IND_PRESENT",
        "indicative",
        "present"
    ),
    Tense(
        "IND_CONDITIONAL",
        "indicative",
        "conditional",
    ),
    Tense(
        "IND_CONDITIONAL_PERFECT",
        "indicative",
        "conditional perfect",
        Verb("haber", "to have (auxiliary)")
    ),
    Tense(
        "IND_FUTURE",
        "indicative",
        "future"
    ),
    Tense(
        "IND_FUTURE_PERFECT",
        "indicative",
        "future perfect",
        Verb("haber", "to have (auxiliary)")
    ),
    Tense(
        "SUB_PAST_PERFECT",
        "subjunctive",
        "past perfect",
        Verb("haber", "to have (auxiliary)")
    ),
    Tense(
        "SUB_IMPERFECT",
        "subjunctive",
        "imperfect"
    ),
    Tense(
        "SUB_PRESENT_PERFECT",
        "subjunctive",
        "present perfect",
        Verb("haber", "to have (auxiliary)")
    ),
    Tense(
        "SUB_PRESENT",
        "subjunctive",
        "present"
    ),
    Tense(
        "IMP_AFFIRMATIVE",
        "imperative",
        "affirmative"
    ),
    Tense(
        "IMP_NEGATIVE",
        "imperative",
        "negative"
    ),
    Tense(
        "PROG_PAST",
        "progressive",
        "past",
        Verb("estar", "to be (state)")
    ),
    Tense(
        "PROG_PRESENT",
        "progressive",
        "present",
        Verb("estar", "to be (state)"),
    ),
    Tense(
        "PROG_FUTURE",
        "progressive",
        "future",
        Verb("estar", "to be (state)"),
    ),
    Tense(
        "PROG_CONDITIONAL",
        "progressive",
        "conditional",
        Verb("estar", "to be (state)"),
    ),
    Tense(
        "INFINITIVE",
        "infinitive",
        "nil",
    )
)