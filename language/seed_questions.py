from models.question import Question

questions = [

    # ============================================================
    # INDICATIVE
    # ============================================================

    # 1. Past Perfect
    Question(
        "I had eaten before they arrived.",
        "Había comido antes de que llegaran.",
        14,     # comer
        1,      # indicative past perfect
        1       # yo
    ),

    # 2. Preterite
    Question(
        "We went to the beach yesterday.",
        "Fuimos a la playa ayer.",
        13,     # ir
        2,      # indicative preterite
        4       # nosotros
    ),

    # 3. Imperfect
    Question(
        "She used to speak Spanish every day.",
        "Ella hablaba español todos los días.",
        20,     # hablar
        3,      # indicative imperfect
        3       # ella
    ),

    # 4. Present Perfect
    Question(
        "I have seen that movie before.",
        "He visto esa película antes.",
        12,     # ver
        4,      # indicative present perfect
        1       # yo
    ),

    # 5. Present
    Question(
        "They understand the question.",
        "Entienden la pregunta.",
        24,     # entender
        5,      # indicative present
        6       # ellos
    ),

    # 6. Conditional
    Question(
        "I could help you.",
        "Podría ayudarte.",
        10,     # poder
        6,      # indicative conditional
        1       # yo
    ),

    # 7. Conditional Perfect
    Question(
        "She would have wanted to come.",
        "Ella habría querido venir.",
        8,      # querer
        7,      # indicative conditional perfect
        3       # ella
    ),

    # 8. Future
    Question(
        "I will come tomorrow.",
        "Vendré mañana.",
        18,     # venir
        8,      # indicative future
        1       # yo
    ),

    # 9. Future Perfect
    Question(
        "We will have finished the project by Friday.",
        "Habremos terminado el proyecto para el viernes.",
        38,     # terminar
        9,      # indicative future perfect
        4       # nosotros
    ),


    # ============================================================
    # SUBJUNCTIVE
    # ============================================================

    # 10. Past Perfect Subjunctive
    Question(
        "I wish I had known the answer.",
        "Ojalá hubiera sabido la respuesta.",
        7,      # saber
        10,     # subjunctive past perfect
        1       # yo
    ),

    # 11. Imperfect Subjunctive
    Question(
        "I wanted you to come.",
        "Quería que vinieras.",
        18,     # venir
        11,     # subjunctive imperfect
        2       # tú
    ),

    # 12. Present Perfect Subjunctive
    Question(
        "I am glad that she has arrived.",
        "Me alegra que ella haya llegado.",
        45,     # llegar
        12,     # subjunctive present perfect
        3       # ella
    ),

    # 13. Present Subjunctive
    Question(
        "I hope you can come tomorrow.",
        "Espero que puedas venir mañana.",
        10,     # poder
        13,     # subjunctive present
        2       # tú
    ),


    # ============================================================
    # IMPERATIVE
    # ============================================================

    # 14. Affirmative Imperative
    Question(
        "Open the door!",
        "¡Abre la puerta!",
        42,     # abrir
        14,     # imperative affirmative
        2       # tú
    ),

    # 15. Negative Imperative
    Question(
        "Don't close the door!",
        "¡No cierres la puerta!",
        43,     # cerrar
        15,     # imperative negative
        2       # tú
    ),


    # ============================================================
    # PROGRESSIVE
    # ============================================================

    # 16. Past Progressive
    Question(
        "I was sleeping when you called.",
        "Estaba durmiendo cuando llamaste.",
        19,     # dormir
        16,     # progressive past
        1       # yo
    ),

    # 17. Present Progressive
    Question(
        "We are cooking dinner.",
        "Estamos cocinando la cena.",
        26,     # cocinar
        17,     # progressive present
        4       # nosotros
    ),

    # 18. Future Progressive
    Question(
        "They will be speaking Spanish.",
        "Estarán hablando español.",
        20,     # hablar
        18,     # progressive future
        6       # ellos
    ),

    # 19. Conditional Progressive
    Question(
        "I would be waiting for you.",
        "Estaría esperándote.",
        28,     # esperar
        19,     # progressive conditional
        1       # yo
    ),
]