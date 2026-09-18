import unittest

from tad.rango import Range


class TestRange(unittest.TestCase):

    def setUp(self):
        self.r = Range(2, 10, 2)   # [2, 4, 6, 8]

    def test_len(self):
        self.assertEqual(len(self.r), 4)
        self.assertEqual(len(Range(0, 5)), 5)
        self.assertEqual(len(Range(0, 7, 3)), 3)   # 0, 3, 6
        self.assertEqual(len(Range(0, 6, 3)), 2)   # 0, 3

    def test_len_rango_vacio(self):
        self.assertEqual(len(Range(5, 2)), 0)
        self.assertEqual(len(Range(3, 3)), 0)

    def test_getitem(self):
        self.assertEqual(self.r[0], 2)
        self.assertEqual(self.r[1], 4)
        self.assertEqual(self.r[2], 6)
        self.assertEqual(self.r[3], 8)

    def test_getitem_fuera_de_rango(self):
        with self.assertRaises(IndexError):
            self.r[4]
        with self.assertRaises(IndexError):
            self.r[-1]

    def test_str(self):
        self.assertEqual(str(self.r), "2,4,6,8")
        self.assertEqual(str(Range(0, 5)), "0,1,2,3,4")
        self.assertEqual(str(Range(5, 2)), "")

    def test_sum(self):
        self.assertEqual(self.r.sum(), 20)
        self.assertEqual(sum(self.r), 20)
        self.assertEqual(Range(5, 2).sum(), 0)

    def test_step_negativo(self):
        r = Range(10, 0, -3)
        self.assertEqual(len(r), 4)
        self.assertEqual(str(r), "10,7,4,1")
        self.assertEqual(r.sum(), 22)

    def test_step_cero(self):
        with self.assertRaises(ValueError):
            Range(0, 10, 0)

    def test_coincide_con_range_de_python(self):
        # comprobacion cruzada con el range real en varios casos
        casos = [(0, 10, 1), (2, 10, 2), (0, 7, 3), (10, 0, -3), (5, 2, 1),
                 (-5, 5, 4), (3, -9, -4)]
        for start, end, step in casos:
            esperado = list(range(start, end, step))
            r = Range(start, end, step)
            self.assertEqual(len(r), len(esperado), (start, end, step))
            self.assertEqual(list(r), esperado, (start, end, step))


if __name__ == "__main__":
    unittest.main()
