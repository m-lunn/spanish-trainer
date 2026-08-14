class Question:
    def __init__(self, id, english, spanish, verb_id, tense_id):
        self.id = id
        self.english = english
        self.spanish = spanish
        self.verb_id = verb_id
        self.tense_id = tense_id

# question_bank = []
# question_bank = [
#     Question(
#         id=1,
#         english="I eat at home.",
#         spanish="Como en casa.",
#         verb="comer",
#         tense="present"
#     ),

#     Question(
#         id=2,
#         english="I ate dinner yesterday.",
#         spanish="Cené ayer.",
#         verb="cenar",
#         tense="preterite"
#     ),

#     Question(
#         id=3,
#         english="She goes to the beach.",
#         spanish="Ella va a la playa.",
#         verb="ir",
#         tense="present"
#     ),

#     Question(
#         id=4,
#         english="She went to the beach yesterday.",
#         spanish="Ella fue a la playa ayer.",
#         verb="ir",
#         tense="preterite"
#     ),

#     Question(
#         id=5,
#         english="We want to buy a new car.",
#         spanish="Queremos comprar un coche nuevo.",
#         verb="querer",
#         tense="present"
#     ),

#     Question(
#         id=6,
#         english="We wanted to buy a new car.",
#         spanish="Quisimos comprar un coche nuevo.",
#         verb="querer",
#         tense="preterite"
#     ),

#     Question(
#         id=7,
#         english="I need to sleep.",
#         spanish="Necesito dormir.",
#         verb="necesitar",
#         tense="present"
#     ),

#     Question(
#         id=8,
#         english="I needed to sleep.",
#         spanish="Necesité dormir.",
#         verb="necesitar",
#         tense="preterite"
#     ),

#     Question(
#         id=9,
#         english="They can speak Spanish.",
#         spanish="Pueden hablar español.",
#         verb="poder",
#         tense="present"
#     ),

#     Question(
#         id=10,
#         english="They could speak Spanish.",
#         spanish="Pudieron hablar español.",
#         verb="poder",
#         tense="preterite"
#     ),

#     Question(
#         id=11,
#         english="He sees his friends every day.",
#         spanish="Él ve a sus amigos todos los días.",
#         verb="ver",
#         tense="present"
#     ),

#     Question(
#         id=12,
#         english="He saw his friends yesterday.",
#         spanish="Él vio a sus amigos ayer.",
#         verb="ver",
#         tense="preterite"
#     ),

#     Question(
#         id=13,
#         english="I live in Australia.",
#         spanish="Vivo en Australia.",
#         verb="vivir",
#         tense="present"
#     ),

#     Question(
#         id=14,
#         english="I lived in Australia last year.",
#         spanish="Viví en Australia el año pasado.",
#         verb="vivir",
#         tense="preterite"
#     ),

#     Question(
#         id=15,
#         english="She speaks Spanish very well.",
#         spanish="Ella habla español muy bien.",
#         verb="hablar",
#         tense="present"
#     ),

#     Question(
#         id=16,
#         english="She spoke Spanish yesterday.",
#         spanish="Ella habló español ayer.",
#         verb="hablar",
#         tense="preterite"
#     ),

#     Question(
#         id=17,
#         english="We understand the question.",
#         spanish="Entendemos la pregunta.",
#         verb="entender",
#         tense="present"
#     ),

#     Question(
#         id=18,
#         english="We understood the question.",
#         spanish="Entendimos la pregunta.",
#         verb="entender",
#         tense="preterite"
#     ),

#     Question(
#         id=19,
#         english="I think about my family every day.",
#         spanish="Pienso en mi familia todos los días.",
#         verb="pensar",
#         tense="present"
#     ),

#     Question(
#         id=20,
#         english="I thought about my family yesterday.",
#         spanish="Pensé en mi familia ayer.",
#         verb="pensar",
#         tense="preterite"
#     ),

#     Question(
#         id=21,
#         english="He cooks dinner every night.",
#         spanish="Él cocina la cena todas las noches.",
#         verb="cocinar",
#         tense="present"
#     ),

#     Question(
#         id=22,
#         english="He cooked dinner last night.",
#         spanish="Él cocinó la cena anoche.",
#         verb="cocinar",
#         tense="preterite"
#     ),

#     Question(
#         id=23,
#         english="I put the keys on the table.",
#         spanish="Puse las llaves sobre la mesa.",
#         verb="poner",
#         tense="preterite"
#     ),

#     Question(
#         id=24,
#         english="She puts the phone on the table.",
#         spanish="Ella pone el teléfono sobre la mesa.",
#         verb="poner",
#         tense="present"
#     ),

#     Question(
#         id=25,
#         english="We wait for the bus every morning.",
#         spanish="Esperamos el autobús todas las mañanas.",
#         verb="esperar",
#         tense="present"
#     ),

#     Question(
#         id=26,
#         english="We waited for the bus yesterday.",
#         spanish="Esperamos el autobús ayer.",
#         verb="esperar",
#         tense="preterite"
#     ),

#     Question(
#         id=27,
#         english="I prefer coffee.",
#         spanish="Prefiero café.",
#         verb="preferir",
#         tense="present"
#     ),

#     Question(
#         id=28,
#         english="I preferred coffee.",
#         spanish="Preferí café.",
#         verb="preferir",
#         tense="preterite"
#     ),

#     Question(
#         id=29,
#         english="They try to speak Spanish.",
#         spanish="Intentan hablar español.",
#         verb="intentar",
#         tense="present"
#     ),

#     Question(
#         id=30,
#         english="They tried to speak Spanish yesterday.",
#         spanish="Intentaron hablar español ayer.",
#         verb="intentar",
#         tense="preterite"
#     ),

#     Question(
#         id=31,
#         english="I buy food every week.",
#         spanish="Compro comida todas las semanas.",
#         verb="comprar",
#         tense="present"
#     ),

#     Question(
#         id=32,
#         english="I bought food yesterday.",
#         spanish="Compré comida ayer.",
#         verb="comprar",
#         tense="preterite"
#     ),

#     Question(
#         id=33,
#         english="They sell their old car.",
#         spanish="Venden su coche viejo.",
#         verb="vender",
#         tense="present"
#     ),

#     Question(
#         id=34,
#         english="They sold their old car.",
#         spanish="Vendieron su coche viejo.",
#         verb="vender",
#         tense="preterite"
#     ),

#     Question(
#         id=35,
#         english="We change our plans.",
#         spanish="Cambiamos nuestros planes.",
#         verb="cambiar",
#         tense="present"
#     ),

#     Question(
#         id=36,
#         english="We changed our plans yesterday.",
#         spanish="Cambiamos nuestros planes ayer.",
#         verb="cambiar",
#         tense="preterite"
#     ),

#     Question(
#         id=37,
#         english="I take the bus to work.",
#         spanish="Tomo el autobús al trabajo.",
#         verb="tomar",
#         tense="present"
#     ),

#     Question(
#         id=38,
#         english="I took the bus yesterday.",
#         spanish="Tomé el autobús ayer.",
#         verb="tomar",
#         tense="preterite"
#     ),

#     Question(
#         id=39,
#         english="She comes to my house every weekend.",
#         spanish="Ella viene a mi casa todos los fines de semana.",
#         verb="venir",
#         tense="present"
#     ),

#     Question(
#         id=40,
#         english="She came to my house yesterday.",
#         spanish="Ella vino a mi casa ayer.",
#         verb="venir",
#         tense="preterite"
#     ),

#     Question(
#         id=41,
#         english="I lose my keys all the time.",
#         spanish="Pierdo mis llaves todo el tiempo.",
#         verb="perder",
#         tense="present"
#     ),

#     Question(
#         id=42,
#         english="I lost my keys yesterday.",
#         spanish="Perdí mis llaves ayer.",
#         verb="perder",
#         tense="preterite"
#     ),

#     Question(
#         id=43,
#         english="They finish work at five.",
#         spanish="Terminan el trabajo a las cinco.",
#         verb="terminar",
#         tense="present"
#     ),

#     Question(
#         id=44,
#         english="They finished work at five yesterday.",
#         spanish="Terminaron el trabajo a las cinco ayer.",
#         verb="terminar",
#         tense="preterite"
#     ),

#     Question(
#         id=45,
#         english="I believe you.",
#         spanish="Te creo.",
#         verb="creer",
#         tense="present"
#     ),

#     Question(
#         id=46,
#         english="I believed you.",
#         spanish="Te creí.",
#         verb="creer",
#         tense="preterite"
#     ),

#     Question(
#         id=47,
#         english="She creates beautiful things.",
#         spanish="Ella crea cosas bonitas.",
#         verb="crear",
#         tense="present"
#     ),

#     Question(
#         id=48,
#         english="She created something beautiful.",
#         spanish="Ella creó algo bonito.",
#         verb="crear",
#         tense="preterite"
#     ),

#     Question(
#         id=49,
#         english="Open the door, please.",
#         spanish="Abre la puerta, por favor.",
#         verb="abrir",
#         tense="present"
#     ),

#     Question(
#         id=50,
#         english="He opened the door yesterday.",
#         spanish="Él abrió la puerta ayer.",
#         verb="abrir",
#         tense="preterite"
#     ),
# ]

