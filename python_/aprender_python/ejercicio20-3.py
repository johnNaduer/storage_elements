# -*- coding: utf-8 -*-

# Solicitamos al usuario que ingrese la fecha
dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

# Verificamos si la fecha corresponde al primer trimestre
if mes == 1 or mes == 2 or mes == 3:
    print ("La fecha corresponde al primer trimestre del año.")
else:
    print ("La fecha no corresponde al primer trimestre del año.")
