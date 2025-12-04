import requests
import json
import re
import random

URL_RESPUESTAS = "https://raw.githubusercontent.com/usuario/repositorio/main/respuestas.json"

# descargar respuestas
RESPUESTAS = requests.get(URL_RESPUESTAS).json()

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
    if intent and intent in RESPUESTAS:
        return random.choice(RESPUESTAS[intent])
    return "No entiendo, ¿puedes reformular?"

if __name__ == "__main__":
    while True:
        entrada = input("Tú: ")
        if entrada.strip().lower() in ("salir", "exit", "quit"):
            print("Bot: ¡Adiós!")
            break
        print("Bot:", responder(entrada))
