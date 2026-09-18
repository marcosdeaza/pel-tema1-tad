"""
Problema 1 - TAD Tarjeta de credito
====================================

Especificacion del TAD
----------------------
Nombre: TarjetaCredito

Valores: una tarjeta queda definida por el nombre del cliente, un
identificador, un limite mensual y el balance (dinero gastado).

Operaciones:
    crear(cliente, identificador, limite)
        Crea una tarjeta con balance 0. El limite debe ser > 0.
    cliente()        -> devuelve el nombre del cliente.
    identificador()  -> devuelve el identificador de la tarjeta.
    limite()         -> devuelve el limite mensual.
    balance()        -> devuelve el dinero gastado hasta el momento.
    cargar(cantidad) -> incrementa el balance en `cantidad`. Si el nuevo
                        balance supera el limite, no se hace nada y se
                        devuelve False. Si se ha podido cargar, True.
    depositar(cantidad) -> disminuye el balance en `cantidad`. El deposito
                        no puede ser mayor que el balance actual; en ese
                        caso no se hace nada y se devuelve False.

Nota: el enunciado dice que sigamos las especificaciones tal cual, asi que
no se han anadido cosas como intereses, fecha de caducidad, etc.
"""


class TarjetaCredito:

    def __init__(self, cliente, identificador, limite):
        if limite <= 0:
            raise ValueError("el limite debe ser mayor que 0")
        self._cliente = cliente
        self._identificador = identificador
        self._limite = limite
        self._balance = 0

    # --- consultas ---------------------------------------------------------

    def cliente(self):
        return self._cliente

    def identificador(self):
        return self._identificador

    def limite(self):
        return self._limite

    def balance(self):
        return self._balance

    # --- operaciones que modifican la tarjeta -------------------------------

    def cargar(self, cantidad):
        """Suma `cantidad` al balance si no se pasa del limite."""
        if cantidad <= 0:
            raise ValueError("la cantidad a cargar debe ser positiva")
        if self._balance + cantidad > self._limite:
            return False
        self._balance += cantidad
        return True

    def depositar(self, cantidad):
        """Resta `cantidad` al balance. No puede superar el balance actual."""
        if cantidad <= 0:
            raise ValueError("la cantidad a depositar debe ser positiva")
        if cantidad > self._balance:
            return False
        self._balance -= cantidad
        return True

    def __str__(self):
        return "Tarjeta {} de {}: balance {} / limite {}".format(
            self._identificador, self._cliente, self._balance, self._limite)


if __name__ == "__main__":
    # Pequena prueba manual
    t = TarjetaCredito("Marcos", "1234-5678", 1000)
    print(t)
    print("cargar 400  ->", t.cargar(400), "| balance:", t.balance())
    print("cargar 700  ->", t.cargar(700), "| balance:", t.balance())   # se pasa del limite
    print("depositar 500 ->", t.depositar(500), "| balance:", t.balance())  # mas que el balance
    print("depositar 300 ->", t.depositar(300), "| balance:", t.balance())
    print(t)
