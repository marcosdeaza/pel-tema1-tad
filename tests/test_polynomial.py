import unittest

from tad.polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def setUp(self):
        self.q = Polynomial([5, 4, 3])        # 3x^2 + 4x + 5
        self.p = Polynomial([-3, -2, 4, 1])   # x^3 + 4x^2 - 2x - 3

    def test_degree(self):
        self.assertEqual(Polynomial([5]).degree(), 0)
        self.assertEqual(Polynomial([5, 0, 1]).degree(), 2)
        self.assertEqual(self.p.degree(), 3)

    def test_degree_ignora_ceros_finales(self):
        self.assertEqual(Polynomial([5, 0, 0]).degree(), 0)
        self.assertEqual(Polynomial([0, 0, 0]).degree(), 0)

    def test_get_coefficient(self):
        self.assertEqual(self.q.get_coefficient(0), 5)
        self.assertEqual(self.q.get_coefficient(2), 3)
        self.assertEqual(self.q.get_coefficient(7), 0)  # termino que no existe

    def test_set_coefficient(self):
        self.q.set_coefficient(1, 10)
        self.assertEqual(self.q.get_coefficient(1), 10)

    def test_set_coefficient_aumenta_grado(self):
        self.q.set_coefficient(4, 2)
        self.assertEqual(self.q.degree(), 4)
        self.assertEqual(self.q.get_coefficient(3), 0)

    def test_set_coefficient_reduce_grado(self):
        self.q.set_coefficient(2, 0)
        self.assertEqual(self.q.degree(), 1)

    def test_evaluate(self):
        self.assertEqual(self.q.evaluate(1), 12)
        self.assertEqual(self.q.evaluate(0), 5)
        self.assertEqual(self.q.evaluate(2), 25)   # 12 + 8 + 5

    def test_sum(self):
        r = self.q.sum(self.p)
        self.assertEqual(r, Polynomial([2, 2, 7, 1]))   # x^3 + 7x^2 + 2x + 2
        self.assertEqual(r.degree(), 3)

    def test_sum_no_modifica_operandos(self):
        self.q.sum(self.p)
        self.assertEqual(self.q, Polynomial([5, 4, 3]))

    def test_sum_cancela_terminos(self):
        r = Polynomial([1, 0, 2]).sum(Polynomial([1, 0, -2]))
        self.assertEqual(r.degree(), 0)
        self.assertEqual(r.get_coefficient(0), 2)

    def test_str(self):
        self.assertEqual(str(self.q), "3x^2 + 4x + 5")
        self.assertEqual(str(self.p), "x^3 + 4x^2 - 2x - 3")
        self.assertEqual(str(Polynomial([7])), "7")
        self.assertEqual(str(Polynomial([0, -1])), "-x")


if __name__ == "__main__":
    unittest.main()
