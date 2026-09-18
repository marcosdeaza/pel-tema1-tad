# PEL - Tema 1: Tipos Abstractos de Datos

Hoja de problemas del Tema 1 de **Programación con Estructuras Lineales**
(2º de Ingeniería Informática, Universidad Europea de Valencia).

Cuatro TADs especificados e implementados en Python, cada uno con su
batería de pruebas.

| Problema | TAD | Módulo | Clase |
|---|---|---|---|
| 1 | Tarjeta de crédito | `tad/tarjeta_credito.py` | `TarjetaCredito` |
| 2 | Vector | `tad/vector.py` | `Vector` |
| 3 | Polinomio | `tad/polynomial.py` | `Polynomial` |
| 4 | Rango | `tad/rango.py` | `Range` |

## Cómo ejecutarlo

Solo hace falta Python 3 (sin dependencias externas).

Cada módulo tiene una pequeña demo al final que se lanza ejecutándolo
directamente:

```bash
python3 tad/rango.py
```

Los tests están hechos con `unittest` (librería estándar):

```bash
python3 -m unittest -v
```

## Estructura del proyecto

```
tad/
  tarjeta_credito.py   Problema 1
  vector.py            Problema 2
  polynomial.py        Problema 3
  rango.py             Problema 4
tests/
  test_tarjeta_credito.py
  test_vector.py
  test_polynomial.py
  test_rango.py
```

La especificación formal de cada TAD (nombre, valores y operaciones con
lo que reciben y devuelven) está en el docstring de cabecera de cada
módulo, tal y como pide la hoja: primero se especifica el TAD y después
se implementa la clase.

## Resumen de cada problema

### 1. Tarjeta de crédito

Atributos: cliente, identificador, límite y balance (empieza a 0).

- `cargar(cantidad)`: suma al balance. Si el resultado supera el límite
  no se hace el cargo y devuelve `False`.
- `depositar(cantidad)`: resta al balance. Si la cantidad es mayor que el
  balance actual no se hace nada y devuelve `False`.

Decisión de diseño: las operaciones devuelven un booleano en vez de lanzar
una excepción, porque que un cargo no se admita es un resultado normal del
TAD, no un error del programa. Las cantidades no positivas sí lanzan
`ValueError` porque eso ya es un mal uso.

### 2. Vector

Vector de dimensión `n` guardado como lista de coordenadas. Se implementan
los métodos especiales que pide el enunciado (`__len__`, `__str__`,
`__getitem__`, `__setitem__`, `__add__`, `__eq__`) más `dot` y
`cosine_distance`.

- `str(v)` devuelve `"(3,5,0)"`, sin espacios.
- `dot`: suma de los productos coordenada a coordenada.
- `cosine_distance`: `1 - (a·b) / (|a|·|b|)`. Vale 0 si apuntan en la
  misma dirección, 1 si son perpendiculares y 2 si son opuestos. No está
  definida para el vector cero (se lanza `ValueError`).

Operar con vectores de distinta dimensión lanza `ValueError`.

### 3. Polinomio

Se representa con una lista de coeficientes donde el índice es el grado
del término: `[5, 4, 3]` es `3x^2 + 4x + 5`.

- `degree()`: `len(coeficientes) - 1`. Para que esto funcione, el
  constructor y `set_coefficient` eliminan los ceros del final de la
  lista (`[5, 0, 0]` es el polinomio `5`, de grado 0).
- `get_coefficient(n)`: devuelve 0 si `n` es mayor que el grado, así
  `sum` puede recorrer los dos polinomios sin preocuparse de cuál es más
  largo.
- `set_coefficient(n, valor)`: si `n` supera el grado actual se rellena
  con ceros hasta llegar a él.
- `evaluate(x)`: suma de `a_i * x^i`.
- `sum(p)`: devuelve un polinomio nuevo, no modifica los operandos.

`__str__` no lo pedía el enunciado pero ayuda mucho a depurar
(`x^3 + 4x^2 - 2x - 3`).

### 4. Rango

Réplica de `range` sin usar `range`. Solo se guardan `start`, `end` y
`step`; los elementos se calculan como `start + i * step`.

- `len(r)`: número de saltos que caben entre `start` y `end`, con división
  entera redondeando hacia arriba: `(end - start + step - 1) // step`.
  Si `step` es negativo se hace lo mismo con los signos cambiados.
- `r[i]`: `start + i * step`, comprobando `0 <= i < len(r)`.
- `str(r)`: `"2,4,6,8"`.
- `r.sum()`: suma de los elementos. También funciona `sum(r)` porque la
  clase define `__iter__` con un bucle `while`.

Uno de los tests compara `Range` con el `range` real de Python en varios
casos (pasos positivos, negativos, rangos vacíos) para asegurar que se
comporta igual.

## Uso de inteligencia artificial

Siguiendo la normativa de la asignatura, declaro el uso de IA en este
trabajo:

- El código de los cuatro problemas lo he escrito yo siguiendo los
  apuntes y la hoja de problemas. He usado IA como apoyo para revisar y
  depurar (por ejemplo, la fórmula del tamaño del rango con `step`
  negativo y el formato de `__str__` del polinomio).
- Este README lo he redactado con ayuda de IA a partir de mis notas,
  principalmente para darle formato Markdown.
