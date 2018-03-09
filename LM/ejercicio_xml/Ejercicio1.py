from lxml import etree

doc=etree.parse("Libros.xml")

def listar_libro():
	nombres=doc.xpath("//title/text()")
	return nombres

libros=listar_libro()
for elem in libros:
	print(elem)