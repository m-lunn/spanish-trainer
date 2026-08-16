from models.question import Question
from models.verb_instance import VerbInstance
from models.verb import Verb
from language.tenses import Tenses
from language.persons import Persons

indicative_past_perfect = Tenses[0]
indicative_preterite = Tenses[1]
indicative_imperfect = Tenses[2] 
indicative_present_perfect = Tenses[3]
indicative_present = Tenses[4]
indicative_conditional = Tenses[5]
indicative_conditional_perfect = Tenses[6]
indicative_future = Tenses[7]
indicative_future_perfect = Tenses[8]
subjunctive_past_perfect = Tenses[9]
subjunctive_imperfect = Tenses[10]
subjunctive_present_perfect = Tenses[11]
subjunctive_present = Tenses[12]
imperative_postive = Tenses[13]
imperative_negative = Tenses[14]
progressive_past = Tenses[15]
progressive_present = Tenses[16]
progressive_future = Tenses[17]
progressive_conditional = Tenses[18]
infinitive = Tenses[19]

first_singular = Persons[0]
second_singular = Persons[1]
third_singular = Persons[2]
first_plural = Persons[3]
second_plural = Persons[4]
third_plural = Persons[5]
nil_person = Persons[6]

questions = [

    # ============================================================
    # INDICATIVE
    # ============================================================

    # 1. Past Perfect
    Question(
        "I had eaten before they arrived.",
        "Había comido antes de que llegaran.",
        [
            VerbInstance(
                Verb("comer", "to eat"),
                indicative_past_perfect,
                first_singular
            ),
            VerbInstance(
                Verb("llegar", "to arrive"),
                indicative_preterite,
                third_plural
            )
        ]
    ),

    # 2. Preterite
    Question(
        "We went to the beach yesterday.",
        "Fuimos a la playa ayer.",
        [
            VerbInstance(
                Verb("ir", "to go"),
                indicative_preterite,
                first_plural
            )
        ]
    ),

    # 3. Imperfect
    Question(
        "She used to speak Spanish every day.",
        "Ella hablaba español todos los días.",
        [
            VerbInstance(
                Verb("hablar","to speak"),
                indicative_imperfect,
                third_singular
            ),
        ]
    ),

    # 4. Present Perfect
    Question(
        "I have seen that movie before.",
        "He visto esa película antes.",
        [
            VerbInstance(
                Verb("ver", "to see"),
                indicative_present_perfect,
                first_singular
            )
        ]
    ),

    # 5. Present
    Question(
        "They understand the question.",
        "Entienden la pregunta.",
        [
            VerbInstance(
                Verb("entender", "to understand"),
                indicative_present,
                third_plural
            )
        ]
    ),

    # 6. Conditional
    Question(
        "I could help you.",
        "Podría ayudarte.",
        [
            VerbInstance(
                Verb("poder", "to be able to"),
                indicative_conditional,
                first_singular
            ),
            VerbInstance(
                Verb("ayudar", "to help"),
                infinitive,
                nil_person
            )
        ]
    ),

    # 7. Conditional Perfect
    Question(
        "She would have wanted to come.",
        "Ella habría querido venir.",
        [
            VerbInstance(
                Verb("querer", "to want"),
                indicative_conditional_perfect,
                third_singular
            ),
            VerbInstance(
                Verb("venir", "to come"),
                infinitive,
                nil_person
            )
        ]
    ),

    # 8. Future
    Question(
        "I will come tomorrow.",
        "Vendré mañana.",
        [
            VerbInstance(
                Verb("venir", "to come"),
                indicative_future,
                first_singular
            )
        ]
    ),

    # 9. Future Perfect
    Question(
        "We will have finished the project by Friday.",
        "Habremos terminado el proyecto para el viernes.",
        [
            VerbInstance(
                Verb("terminar", "to finish"),
                indicative_future_perfect,
                first_plural
            )
        ]
    ),


    # ============================================================
    # SUBJUNCTIVE
    # ============================================================

    # 10. Past Perfect Subjunctive
    Question(
        "If I had known the answer.",
        "Sí hubiera sabido la respuesta.",
        [
            VerbInstance(
                Verb("saber", "to know"),
                subjunctive_past_perfect,
                first_singular)
        ]
    ),

    # 11. Imperfect Subjunctive
    Question(
        "I wanted you to come.",
        "Quería que vinieras.",
        [
            VerbInstance(
                Verb("querer", "to want"),
                indicative_imperfect,
                first_singular
            ),
            VerbInstance(
                Verb("venir", "to come"),
                subjunctive_imperfect,
                second_singular
            )
        ]
    ),

    # 12. Present Perfect Subjunctive
    Question(
        "I am glad that she has arrived.",
        "Me alegra que ella haya llegado.",
        [
            VerbInstance(
                Verb("alegrar", "to gladden"),
                indicative_present,
                first_singular
            ),
            VerbInstance(
                Verb("llegar", "to arrive"),
                subjunctive_present_perfect,
                third_singular
            )
        ]
    ),

    # 13. Present Subjunctive
    Question(
        "I hope you can come tomorrow.",
        "Espero que puedas venir mañana.",
        [
            VerbInstance(
                Verb("esperar", "to hope"),
                indicative_present,
                first_singular
            ),
            VerbInstance(
                Verb("poder", "to be able to"),
                subjunctive_present,
                second_singular
            ),
            VerbInstance(
                Verb("venir", "to come"),
                infinitive,
                nil_person
            )
        ]
    ),


    # ============================================================
    # IMPERATIVE
    # ============================================================

    # 14. Affirmative Imperative
    Question(
        "Open the door!",
        "¡Abre la puerta!",
        [
            VerbInstance(
                Verb("abrir", "to open"),
                imperative_postive,
                second_singular
            )
        ]
    ),

    # 15. Negative Imperative
    Question(
        "Don't close the door!",
        "¡No cierres la puerta!",
        [
            VerbInstance(
                Verb("cerrar", "to close"),
                imperative_negative,
                second_singular
            )
        ]
    ),


    # ============================================================
    # PROGRESSIVE
    # ============================================================

    # 16. Past Progressive
    Question(
        "I was sleeping when you called.",
        "Estaba durmiendo cuando llamaste.",
        [
            VerbInstance(
                Verb("dormir", "to sleep"),
                progressive_past,
                first_singular
            )
        ]
    ),

    # 17. Present Progressive
    Question(
        "We are cooking dinner.",
        "Estamos cocinando la cena.",
        [
            VerbInstance(
                Verb("cocinar", "to cook"),
                progressive_present,
                first_plural
            )
        ]
    ),

    # 18. Future Progressive
    Question(
        "They will be speaking Spanish.",
        "Estarán hablando español.",
        [
            VerbInstance(
                Verb("hablar", "to speak"),
                progressive_future,
                third_plural
            )
        ]
    ),

    # 19. Conditional Progressive
    Question(
        "I would be waiting for you.",
        "Estaría esperándote.",
        [
            VerbInstance(
                Verb("esperar", "to wait/hope"),
                progressive_conditional,
                first_singular
            )
        ]
    ),
]