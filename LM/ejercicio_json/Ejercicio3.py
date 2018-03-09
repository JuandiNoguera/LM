import json

with open("españa.json") as fichero:
	doc=json.load(fichero)

def mostrar_jugadores(nombre):
	jugador=nombre
	nombres=doc["sheets"]["Players"]
	for i in nombres:
		if jugador==i["name"]:
			print(i["club"])
			print(i["position"])
			print(i["date of birth"])
			print(i["bio"])
	return

jugador=input("Dime un Jugador: ")
datos=mostrar_jugadores(jugador)