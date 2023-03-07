nota1 = int (input ("ingresar primera nota: "))
nota2 = int (input ("ingresar segunda nota: "))
nota3 = int (input ("ingresar tercera nota: "))

promedio = (nota1+nota2+nota3)/3

if promedio >= 7:
	print "promocionado"

elif promedio >=4 and promedio < 7:
	print "Regular"
else:
	print "reprobado"
