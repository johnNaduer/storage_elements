class Humano:
        def __init__(self,edad):
                self.edad = edad


        def hablar(self,mensaje):
                print self.edad
		print mensaje

pedro = Humano(26)
raul = Humano(21)

print 'Soy Pedro y tengo ', pedro.edad
print 'Soy raul y tengo ', raul.edad

pedro.hablar('Hola')

raul.hablar('Hola,Pedro!')

"""
class iHumano:
	def __init__(self):
		self.edad = 25
		print "soy un nuevo objeto"
	
	def hablar(self,mensaje):
		print mensaje


pedro = Humano()
raul = Humano()

print 'Soy Pedro y tengo ', pedro.edad
print 'Soy raul y tengo ', raul.edad

pedro.hablar('Hola')

raul.hablar('Hola,Pedro!')

"""
