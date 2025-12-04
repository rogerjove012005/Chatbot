import sqlite3
import os

# Crea carpeta db si no existe
os.makedirs("db", exist_ok=True)

con = sqlite3.connect("db/respuestas.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS respuestas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    intent TEXT NOT NULL,
    respuesta TEXT NOT NULL
)
""")

# Datos iniciales
datos = [
    ("saludo", "¡Hola! ¿En qué puedo ayudarte?"),
    ("saludo", "¡Buenas! ¿Qué tal tu día?"),
    ("gracias", "¡De nada!"),
    ("gracias", "Siempre a tu servicio."),
    ("despedida", "¡Hasta luego!"),
    ("despedida", "Nos vemos pronto."),
]

cur.executemany("INSERT INTO respuestas (intent, respuesta) VALUES (?, ?)", datos)

con.commit()
con.close()

print("Base de datos creada en db/respuestas.db")
