"""
Problema 3 - TAD Polinomio
==========================

Especificacion del TAD
----------------------
Nombre: Polinomio

Valores: una expresion a0 + a1*x + a2*x^2 + ... + an*x^n. Se representa
con la lista de coeficientes [a0, a1, ..., an]: la posicion de la lista es
el grado del termino.

Operaciones:
    crear(coeficientes)     -> polinomio a partir de la lista [a0, a1, ...].
    grado()                 -> mayor exponente con coeficiente distinto de 0.
                               El polinomio 0 tiene grado 0 por convenio.
    coeficiente(n)          -> coeficiente del termino x^n (0 si n > grado).
    modificar(n, valor)     -> cambia el coeficiente de x^n. Si n es mayor
                               que el grado actual, el polinomio crece
                               rellenando con ceros.
    evaluar(x)              -> valor numerico del polinomio en x.
    sumar(p)                -> nuevo polinomio, suma termino a termino.
    a_cadena()              -> representacion legible, ej. "3x^2 + 4x + 5".
"""


class Polynomial:

    def __init__(self, coefficients):
        # copiamos la lista para que no se modifique desde fuera
        self._coefs = list(coefficients)
        if len(self._coefs) == 0:
            self._coefs = [0]
        self._quitar_ceros_finales()

    def _quitar_ceros_finales(self):
        # [5, 0, 0] representa "5", asi que quitamos los ceros sobrantes
        while len(self._coefs) > 1 and self._coefs[-1] == 0:
            self._coefs.pop()

    def degree(self):
        return len(self._coefs) - 1

    def get_coefficient(self, n):
        if n < 0:
            raise ValueError("el exponente no puede ser negativo")
        if n > self.degree():
            return 0
        return self._coefs[n]

    def set_coefficient(self, n, new_value):
        if n < 0:
            raise ValueError("el exponente no puede ser negativo")
        # si el termino no existe todavia, rellenamos con ceros hasta llegar
        while n > self.degree():
            self._coefs.append(0)
        self._coefs[n] = new_value
        self._quitar_ceros_finales()

    def evaluate(self, x):
        # Q(x) = a0 + a1*x + a2*x^2 + ...
        total = 0
        for exp in range(len(self._coefs)):
            total += self._coefs[exp] * x ** exp
        return total

    def sum(self, p):
        # el resultado tiene tantos terminos como el polinomio mas largo
        n = max(self.degree(), p.degree()) + 1
        nuevos = [0] * n
        for i in range(n):
            nuevos[i] = self.get_coefficient(i) + p.get_coefficient(i)
        return Polynomial(nuevos)

    def __eq__(self, other):
        return isinstance(other, Polynomial) and self._coefs == other._coefs

    def __str__(self):
        if self.degree() == 0:
            return str(self._coefs[0])
        cadena = ""
        for exp in range(self.degree(), -1, -1):
            c = self._coefs[exp]
            if c == 0:
                continue
            # signo: el primer termino lleva "-" pegado, el resto " + " / " - "
            if cadena == "":
                signo = "-" if c < 0 else ""
            else:
                signo = " - " if c < 0 else " + "
            valor = abs(c)
            if exp == 0:
                termino = str(valor)
            else:
                # el coeficiente 1 no se escribe: "x^2" en vez de "1x^2"
                termino = ("" if valor == 1 else str(valor)) + "x"
                if exp > 1:
                    termino += "^{}".format(exp)
            cadena += signo + termino
        return cadena

if __name__ == "__main__":
    q = Polynomial([5, 4, 3])          # 3x^2 + 4x + 5
    p = Polynomial([-3, -2, 4, 1])     # x^3 + 4x^2 - 2x - 3
    print("Q(x) =", q, "| grado:", q.degree())
    print("p(x) =", p, "| grado:", p.degree())
    print("coeficiente de x^2 en Q:", q.get_coefficient(2))
    print("Q(1) =", q.evaluate(1))     # 12
    print("Q + p =", q.sum(p))         # x^3 + 7x^2 + 2x + 2
    q.set_coefficient(4, 2)
    print("Q tras poner 2x^4:", q, "| grado:", q.degree())
