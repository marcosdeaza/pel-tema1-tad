import unittest

from tad.vector import Vector


def vec(*coords):
    v = Vector(len(coords))
    for i, c in enumerate(coords):
        v[i] = c
    return v


class TestVector(unittest.TestCase):

    def test_constructor_y_len(self):
        v = Vector(4)
        self.assertEqual(len(v), 4)
        self.assertEqual(str(v), "(0,0,0,0)")

    def test_get_set_item(self):
        v = Vector(3)
        v[1] = 7
        self.assertEqual(v[1], 7)
        self.assertEqual(v[0], 0)

    def test_str(self):
        self.assertEqual(str(vec(3, 5, 0)), "(3,5,0)")
        self.assertEqual(str(vec(0, 1, -1, 3, 2)), "(0,1,-1,3,2)")

    def test_add(self):
        self.assertEqual(vec(3, 5, 0) + vec(1, -2, 4), vec(4, 3, 4))

    def test_add_no_modifica_operandos(self):
        a = vec(1, 2)
        b = vec(3, 4)
        a + b
        self.assertEqual(a, vec(1, 2))
        self.assertEqual(b, vec(3, 4))

    def test_eq(self):
        self.assertTrue(vec(1, 2, 3) == vec(1, 2, 3))
        self.assertFalse(vec(1, 2, 3) == vec(1, 2, 4))
        self.assertFalse(vec(1, 2) == vec(1, 2, 0))  # distinta dimension

    def test_dot(self):
        self.assertEqual(vec(3, 5, 0).dot(vec(1, -2, 4)), -7)
        self.assertEqual(vec(1, 0).dot(vec(0, 1)), 0)

    def test_cosine_distance(self):
        # vectores perpendiculares: cos = 0 -> distancia 1
        self.assertAlmostEqual(vec(1, 0).cosine_distance(vec(0, 1)), 1.0)
        # misma direccion: cos = 1 -> distancia 0
        self.assertAlmostEqual(vec(2, 2).cosine_distance(vec(5, 5)), 0.0)
        # direccion opuesta: cos = -1 -> distancia 2
        self.assertAlmostEqual(vec(1, 0).cosine_distance(vec(-3, 0)), 2.0)

    def test_dimensiones_distintas(self):
        with self.assertRaises(ValueError):
            vec(1, 2) + vec(1, 2, 3)
        with self.assertRaises(ValueError):
            vec(1, 2).dot(vec(1, 2, 3))

    def test_vector_cero_en_coseno(self):
        with self.assertRaises(ValueError):
            Vector(2).cosine_distance(vec(1, 1))


if __name__ == "__main__":
    unittest.main()
