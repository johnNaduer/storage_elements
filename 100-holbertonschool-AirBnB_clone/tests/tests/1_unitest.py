import unittest
from test.persona import Persona

class TestPersona(unittest.TestCase):

    def test_persona_str(self):
        p = Persona("yaros")
        p.primer_nombre = "naduer"
        p.apellido = "espino"
        p.edad = 30
        self.assertEqual(str(p), "[Persona] {'nombre': 'john', 'segundo_apellido': 'yaros', 'primer_nombre': 'naduer', 'apellido': 'espino', 'edad': 30}")

