Este proyecto implementa un sistema de búsqueda espacial utilizando un Quadtree en 2 dimensiones (2D), donde cada punto representa coordenadas (x, y) en una ciudad.

  Objetivos
- Implementar un Quadtree desde cero  
- Realizar búsqueda por radio (Range Search)  
- Encontrar el vecino más cercano  
- Comparar rendimiento contra fuerza bruta  
- Visualizar los resultados  

  Resultados

Se observó que:

- La fuerza bruta tiene un crecimiento lineal  
- El Quadtree presenta un comportamiento mucho más eficiente al reducir el número de comparaciones  
- Desde conjuntos de datos de aproximadamente **500 - 1000 puntos**, el Quadtree ya supera a la fuerza bruta  
- Para 10,000 puntos, la diferencia de rendimiento es considerable  
