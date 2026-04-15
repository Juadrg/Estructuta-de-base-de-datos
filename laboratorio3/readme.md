Este proyecto implementa un sistema de búsqueda espacial utilizando un Árbol KD en 2 dimensiones (2D), donde cada punto representa coordenadas (x, y) en una ciudad.

Objetivos
Implementar un Árbol KD desde cero
Realizar búsqueda por radio (Range Search)
Encontrar el vecino más cercano
Comparar rendimiento contra fuerza bruta
Visualizar los resultados

Resultados

Se observó que:

La fuerza bruta tiene un crecimiento lineal 
El Árbol KD presenta un comportamiento mucho más eficiente cercano a O(log N)
A partir de conjuntos de datos medianos (1000 - 2000 puntos), el Árbol KD supera a la fuerza bruta
Para 10,000 puntos, la diferencia de rendimiento es considerable
