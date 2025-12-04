import sqlite3
import random
import re

DB_PATH = "db/respuestas.db"

# Patrones para detectar las intenciones
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

def obtener_respuesta(intent):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT respuesta FROM respuestas WHERE intent = ?", (intent,))
    filas = cur.fetchall()
    con.close()
    
    if filas:
        return random.choice([f[0] for f in filas])
    return None

def responder(texto):
    intent = detectar_intent(texto)
    if intent:
        resp = obtener_respuesta(intent)
        if resp:
            return resp
    
    # Si no hay coincidencia, respuesta genérica
    return "No estoy seguro de cómo responder a eso, pero puedo ayudarte con saludos, despedidas o agradecimientos."

if __name__ == "__main__":
    print("Chatbot con SQLite iniciado. Escribe 'salir' para terminar.")
    while True:
        entrada = input("Tú: ")
        if entrada.strip().lower() in ("salir", "exit", "quit"):
            print("Bot: ¡Adiós!")
            break

        print("Bot:", responder(entrada))
