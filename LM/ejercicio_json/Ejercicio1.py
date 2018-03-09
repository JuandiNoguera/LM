import json

with open("españa.json") as fichero:
	doc=json.load(fichero)

def listar_jugadores():
	nombres=doc["sheets"]["Players"]
	return nombres

jugadores=listar_jugadores()
for i in jugadores:
	print(i["name"])
