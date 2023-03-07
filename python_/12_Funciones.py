
def mi_funcion(num1, num2):
	return num1+num2

resultado_de_suma = mi_funcion(3,4)

print resultado_de_suma

"""
def mi_funcion(cad,v=2,**algomas):
	print cad * v
	
	print algomas['cadenaextra']
	print algomas['cadenademas']

mi_funcion('Python',5,cadenaextra = 'Hola',cadenademas = 'Adios')
"""

"""
def mi_funcion(cad,v=2,*algomas):
	print cad * v
	for cadena in algomas:
		print cadena * v

mi_funcion('Python',5,'Hola','Adios','N','cadenas')
"""

"""
def mi_funcion(cad, v=2):
	print cad * v

mi_funcion('Python',5)
"""

"""
def mi_funcion(num1=0, num2=0):
	print num1+num2

mi_funcion(3)
"""

"""
def mi_funcion(num1, num2):
	print num1+num2

mi_funcion(3,4)
"""
