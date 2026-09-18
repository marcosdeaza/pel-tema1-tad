"""
Problema 2 - TAD Vector
=======================

Especificacion del TAD
----------------------
Nombre: Vector

Valores: una secuencia de n numeros (coordenadas) en un espacio de n
dimensiones. Las coordenadas se indexan de 0 a n-1.

Operaciones:
    crear(dim)             -> vector de dimension dim con todo a 0.
    dimension()            -> numero de coordenadas (len).
    obtener(i)             -> coordenada i-esima (v[i]).
    modificar(i, valor)    -> cambia la coordenada i-esima (v[i] = valor).
    a_cadena()             -> "(c0,c1,...,cn-1)" (str).
    sumar(otro)            -> nuevo vector con la suma coordenada a coordenada.
                              Los dos vectores deben tener la misma dimension.
    igual(otro)            -> True si tienen la misma dimension y las mismas
                              coordenadas.
    producto_escalar(otro) -> suma de los productos coordenada a coordenada.
    distancia_coseno(otro) -> 1 - cos(angulo) = 1 - (a.b) / (|a| * |b|).
                              No esta definida si alguno de los vectores es
                              el vector cero.
"""

import math


class Vector:

    def __init__(self, dim):
        if dim <= 0:
            raise ValueError("la dimension debe ser mayor que 0")
        self._coords = [0] * dim

    def __len__(self):
        return len(self._coords)

    def __str__(self):
        # "(3,5,0)" sin espacios, como pide el enunciado
        return "(" + ",".join(str(c) for c in self._coords) + ")"

    def __getitem__(self, i):
        return self._coords[i]

    def __setitem__(self, i, new_value):
        self._coords[i] = new_value

    def _comprobar_dimension(self, other):
        if len(self) != len(other):
            raise ValueError("los vectores tienen dimensiones distintas")

    def __add__(self, other):
        self._comprobar_dimension(other)
        resultado = Vector(len(self))
        for i in range(len(self)):
            resultado[i] = self[i] + other[i]
        return resultado

    def __eq__(self, other):
        if not isinstance(other, Vector) or len(self) != len(other):
            return False
        for i in range(len(self)):
            if self[i] != other[i]:
                return False
        return True

    def dot(self, other):
        self._comprobar_dimension(other)
        total = 0
        for i in range(len(self)):
            total += self[i] * other[i]
        return total

    def norm(self):
        # modulo del vector: raiz cuadrada del producto escalar consigo mismo
        return math.sqrt(self.dot(self))

    def cosine_distance(self, other):
        self._comprobar_dimension(other)
        n1 = self.norm()
        n2 = other.norm()
        if n1 == 0 or n2 == 0:
            raise ValueError("la distancia del coseno no esta definida para el vector cero")
        return 1 - self.dot(other) / (n1 * n2)


if __name__ == "__main__":
    a = Vector(3)
    a[0], a[1], a[2] = 3, 5, 0
    b = Vector(3)
    b[0], b[1], b[2] = 1, -2, 4
    print("a =", a, "| len =", len(a))
    print("b =", b)
    print("a + b =", a + b)
    print("a == b ->", a == b)
    print("a.dot(b) =", a.dot(b))
    print("cosine_distance(a, b) =", a.cosine_distance(b))
    print("cosine_distance(a, a) =", a.cosine_distance(a))   # 0 (mismo vector)
