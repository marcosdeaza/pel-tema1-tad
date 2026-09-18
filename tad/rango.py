"""
Problema 4 - TAD Rango
======================

Especificacion del TAD
----------------------
Nombre: Rango

Valores: una secuencia de enteros start, start+step, start+2*step, ...
que no llega a alcanzar end (end queda fuera). step no puede ser 0.

Operaciones:
    crear(start, end, step=1) -> construye la secuencia. Error si step == 0.
    tamano()                  -> numero de elementos (len).
    elemento(i)               -> i-esimo elemento, con 0 <= i < tamano (r[i]).
    a_cadena()                -> elementos separados por comas: "2,4,6,8".
    suma()                    -> suma de todos los elementos.

Restriccion del enunciado: no se puede usar la funcion range de Python.
"""


class Range:

    def __init__(self, start, end, step=1):
        if step == 0:
            raise ValueError("step no puede ser 0")
        self._start = start
        self._end = end
        self._step = step

    def __len__(self):
        # Numero de saltos de tamano step que caben entre start y end.
        # Division entera redondeando hacia arriba: (a + b - 1) // b
        if self._step > 0:
            if self._start >= self._end:
                return 0
            return (self._end - self._start + self._step - 1) // self._step
        else:
            if self._start <= self._end:
                return 0
            paso = -self._step
            return (self._start - self._end + paso - 1) // paso

    def __getitem__(self, i):
        if i < 0 or i >= len(self):
            raise IndexError("indice fuera del rango")
        return self._start + i * self._step

    def __iter__(self):
        # Recorrido con un bucle while para no usar range()
        i = 0
        n = len(self)
        while i < n:
            yield self._start + i * self._step
            i += 1

    def __str__(self):
        return ",".join(str(x) for x in self)

    def sum(self):
        total = 0
        for x in self:
            total += x
        return total


if __name__ == "__main__":
    r = Range(2, 10, 2)
    print("Range(2, 10, 2)")
    print("  len   =", len(r))                 # 4
    print("  r[0..3] =", r[0], r[1], r[2], r[3])   # 2 4 6 8
    print("  str   =", str(r))                 # 2,4,6,8
    print("  sum   =", r.sum(), "/ sum(r) =", sum(r))   # 20
    print("Range(5) ->", str(Range(0, 5)))
    print("Range(10, 0, -3) ->", str(Range(10, 0, -3)))  # 10,7,4,1
    print("Range(5, 2) vacio ->", len(Range(5, 2)))
