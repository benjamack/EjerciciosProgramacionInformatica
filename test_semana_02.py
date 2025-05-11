import unittest
from semana_02 import invertir_lista, collatz, contar_definiciones, cantidad_de_claves_letra, propagar

class TestInvertirLista(unittest.TestCase):
    # Test típico: invertir una lista de números
    def test_lista_numeros(self):
        self.assertEqual(invertir_lista([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])

    # Test típico: invertir una lista de strings (caso mencionado en clase)
    def test_lista_strings(self):
        ciudades = ["Bogotá", "Rosario", "San Fernando", "San Miguel"]
        esperado = ["San Miguel", "San Fernando", "Rosario", "Bogotá"]
        self.assertEqual(invertir_lista(ciudades), esperado)

    # Test borde: lista vacía
    def test_lista_vacia(self):
        self.assertEqual(invertir_lista([]), [])

    # Test borde: lista con un solo elemento
    def test_lista_un_elemento(self):
        self.assertEqual(invertir_lista([42]), [42])

    # Test error: pasar un tipo no lista debe lanzar TypeError
    def test_no_lista(self):
        with self.assertRaises(TypeError):
            invertir_lista(123)

class TestCollatz(unittest.TestCase):
    # Test base: n=1 debe devolver 0 pasos
    def test_collatz_1(self):
        self.assertEqual(collatz(1), 0)

    # Casos básicos pedidos en clase
    def test_collatz_basicos(self):
        self.assertEqual(collatz(2), 1)
        self.assertEqual(collatz(3), 7)

    # Casos con números grandes mencionados en clase
    def test_collatz_numeros_grandes(self):
        self.assertEqual(collatz(27), 111)
        self.assertEqual(collatz(100), 25)

    # Casos potencias de dos mencionados en clase
    def test_collatz_potencias_de_dos(self):
        self.assertEqual(collatz(16), 4)
        self.assertEqual(collatz(32), 5)
        self.assertEqual(collatz(64), 6)

class TestDiccionario(unittest.TestCase):
    # Test normal: diccionario con definiciones
    def test_contar_definiciones_normal(self):
        d = {"A": ["1", "2"], "B": ["3"]}
        self.assertEqual(contar_definiciones(d), {"A": 2, "B": 1})

    # Test borde: diccionario vacío
    def test_contar_definiciones_vacio(self):
        self.assertEqual(contar_definiciones({}), {})

    # Test típico: claves que empiezan con A
    def test_cantidad_de_claves_letra(self):
        d = {"Ana": [], "Alberto": [], "Beto": []}
        self.assertEqual(cantidad_de_claves_letra(d, "A"), 2)

    # Test borde: ninguna clave coincide
    def test_cantidad_de_claves_letra_none(self):
        d = {"Ana": [], "Alberto": [], "Beto": []}
        self.assertEqual(cantidad_de_claves_letra(d, "Z"), 0)

    # Test adicional: claves en minúsculas (comprobar case-sensitive)
    def test_cantidad_de_claves_letra_minusculas(self):
        d = {"ana": [], "alberto": [], "beto": []}
        self.assertEqual(cantidad_de_claves_letra(d, "a"), 2)

class TestPropagar(unittest.TestCase):
    # Test típico: un fuego al medio
    def test_propagar_simple(self):
        self.assertEqual(propagar([0, 0, 0, 1, 0, 0]), [1, 1, 1, 1, 1, 1])

    # Test con obstáculos: ejemplo visto en clase
    def test_propagar_con_obstaculo(self):
        entrada = [0, 0, 0, -1, 1, 0, 0, 0, -1, 0, 1, 0, 0]
        esperado = [0, 0, 0, -1, 1, 1, 1, 1, -1, 1, 1, 1, 1]
        self.assertEqual(propagar(entrada), esperado)

    # Test borde: todos carbonizados
    def test_propagar_todo_carbonizado(self):
        self.assertEqual(propagar([-1, -1, -1]), [-1, -1, -1])

    # Test borde: sin encendidos
    def test_propagar_sin_encendidos(self):
        self.assertEqual(propagar([0, 0, 0]), [0, 0, 0])

    # Test borde: todos encendidos
    def test_propagar_todo_encendido(self):
        self.assertEqual(propagar([1, 1, 1]), [1, 1, 1])

if __name__ == '__main__':
    unittest.main()
