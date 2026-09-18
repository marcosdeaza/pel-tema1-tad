import unittest

from tad.tarjeta_credito import TarjetaCredito


class TestTarjetaCredito(unittest.TestCase):

    def setUp(self):
        self.t = TarjetaCredito("Marcos", "1234-5678", 1000)

    def test_estado_inicial(self):
        self.assertEqual(self.t.cliente(), "Marcos")
        self.assertEqual(self.t.identificador(), "1234-5678")
        self.assertEqual(self.t.limite(), 1000)
        self.assertEqual(self.t.balance(), 0)

    def test_cargar_dentro_del_limite(self):
        self.assertTrue(self.t.cargar(400))
        self.assertEqual(self.t.balance(), 400)

    def test_cargar_hasta_el_limite_exacto(self):
        self.assertTrue(self.t.cargar(1000))
        self.assertEqual(self.t.balance(), 1000)

    def test_cargar_supera_el_limite(self):
        self.t.cargar(400)
        self.assertFalse(self.t.cargar(700))
        self.assertEqual(self.t.balance(), 400)  # no cambia

    def test_depositar(self):
        self.t.cargar(400)
        self.assertTrue(self.t.depositar(300))
        self.assertEqual(self.t.balance(), 100)

    def test_depositar_mas_que_el_balance(self):
        self.t.cargar(400)
        self.assertFalse(self.t.depositar(500))
        self.assertEqual(self.t.balance(), 400)

    def test_cantidades_no_positivas(self):
        with self.assertRaises(ValueError):
            self.t.cargar(0)
        with self.assertRaises(ValueError):
            self.t.depositar(-5)

    def test_limite_invalido(self):
        with self.assertRaises(ValueError):
            TarjetaCredito("X", "0", 0)


if __name__ == "__main__":
    unittest.main()
