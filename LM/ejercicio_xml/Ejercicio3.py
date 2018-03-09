from lxml import etree

doc=etree.parse("Libros.xml")

def detalles_libro(nombre):
	var=nombre
	libros=doc.xpath("//title/text()")
	for i in libros:
		if var==i:
			print(i.xpath("//price/text()"))
			print(i.xpath("//author/text()"))
			print(i.xpath("//description/text()"))
			return

libro=input("Dime el nombre del libro: ")
print(detalles_libro(libro))