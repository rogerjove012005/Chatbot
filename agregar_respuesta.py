import sqlite3

intent = input("Intent: ")
respuesta = input("Respuesta: ")

con = sqlite3.connect("db/respuestas.db")
cur = con.cursor()

cur.execute("INSERT INTO respuestas (intent, respuesta) VALUES (?, ?)", (intent, respuesta))
con.commit()
con.close()

print("Respuesta agregada correctamente.")
