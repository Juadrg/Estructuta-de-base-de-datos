Problema 1

Descripcion:
Dado un hash, encontrar la secuencia de números que lo genera.

Reglas:

Se usa algoritmo SHA-256
La secuencia esta formada por 10 dígitos concatenados
Cada dígito esta en el rango [0–9]
No se repiten 

Que hace el programa:
Genera todas las permutaciones posibles de los dígitos del 0 al 9.
Para cada combinación:

Forma la secuencia
Calcula su hash SHA-256
Lo compara con el hash objetivo

Cuando encuentra coincidencia, devuelve la secuencia correcta.


Problema 2

Descripcion:
Dado el hash root de un arbol de Merkle, determinar el orden de las transacciones que lo generan.

Reglas:

Se usa SHA-256
Las transacciones son conocidas
Se debe encontrar el orden correcto

Qué hace el programa:
Genera todas las permutaciones posibles de las transacciones.
Para cada orden:

Calcula el hash de cada transaccion
Construye el árbol de Merkle (combinando hashes por pares)
Obtiene el hash root

Luego compara ese resultado con el hash objetivo.
Cuando coinciden, muestra el orden correcto.
