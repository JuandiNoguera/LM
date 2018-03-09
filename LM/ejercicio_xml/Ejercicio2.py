from lxml import etree

doc=etree.parse("Libros.xml")

def contar_libros():
	nombres=int(doc.xpath("count(//title)"))
	return nombres

libros=contar_libros()
print(libros)