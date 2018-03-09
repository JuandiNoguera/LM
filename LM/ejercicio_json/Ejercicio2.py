import json

with open("españa.json") as fichero:
	doc=json.load(fichero)

def contar_jugadores():
	nombres=doc["sheets"]["Players"]
	return nombres

l1=[]
cont=0
jugadores=contar_jugadores()
for i in jugadores:
	l1.append(i["name"])
	cont+=1
print(cont)

