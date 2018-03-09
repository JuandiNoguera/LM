import json

with open("españa.json") as fichero:
	doc=json.load(fichero)

def mostrar_jugadores(nombre):
	clubes=nombre
	nombres=doc["sheets"]["Players"]
	for i in nombres:
		if clubes==i["club"]:
			print(i["name"])
	return

clubs=input("Dime un club: ")
datos=mostrar_jugadores(clubs)