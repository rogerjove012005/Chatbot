import nltk
nltk.download('punkt')
nltk.download('stopwords')

import re

RESPUESTAS = {
    "saludo": ["Hola 😄 ¿en qué puedo ayudarte?", "¡Hola! ¿Qué quieres aprender hoy?"],
    "despedida": ["Adiós 👋", "Hasta luego, ¡que tengas un buen día!"],
    "gracias": ["De nada 😊", "Con gusto."],
}

PATRONES = {
    "saludo": [r"\b(hola|buenas|buenas tardes|buenos días)\b"],
    "despedida": [r"\b(adiós|chao|hasta luego|nos vemos)\b"],
    "gracias": [r"\b(gracias|muchas gracias)\b"],
}

def detectar_intent(texto):
    texto = texto.lower()
    for intent, patrones in PATRONES.items():
        for pat in patrones:
            if re.search(pat, texto):
                return intent
    return None

def responder(texto):
    intent = detectar_intent(texto)
    if intent:
        # selecciona una respuesta aleatoria entre las definidas
        import random
        return random.choice(RESPUESTAS[intent])
    return "Lo siento, no entiendo. ¿Puedes reformular?"

if __name__ == "__main__":
    while True:
        entrada = input("Tú: ")
        if entrada.strip().lower() in ("salir", "exit", "quit"):
            print("Bot: ¡Adiós!")
            break
        print("Bot:", responder(entrada))