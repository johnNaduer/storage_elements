import unittest
from persona import persona

class TestPersona(unittest.TestCase):
    def setUp(self):
        self.nombre1 = persona("yaros")
        self.nombre1.primer_nombre = "naduer"
        self.nombre1.apellido = "espino"
        self.nombre1.edad = 30

    def test_str_method(self):
        expected_output = "[persona] {'nombre': 'john', 'segundo_apellido': 'yaros', 'primer_nombre': 'naduer', 'apellido': 'espino', 'edad': 30}"
        self.assertEqual(str(self.nombre1), expected_output)

if __name__ == '__main__':
    unittest.main()

