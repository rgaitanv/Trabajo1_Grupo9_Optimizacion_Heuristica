# Trabajo1_Grupo9_Optimizacion_Heuristica

## PUNTO 1:  Optimizacion Nuemerica:
Considere las siguientes funciones de prueba:

* Función de Rosenbrock
* Función de Rastrigin
* Función de Schwefel.
* Función de Griewank
* Función Goldstein-Price
* Función de las seis jorobas de camello ()

1. Escoja dos funciones de prueba
2. Optimice las funciones en dos y tres dimensiones usando un método de descenso por gradiente con condición inicial aleatoria
3. Optimice las funciones en dos y tres dimensiones usando: algoritmos evolutivos, optimización de partículas y evolución diferencial
4. Represente con un gif animado o un video el proceso de optimización de descenso por gradiente y el proceso usando el método heurístico
 
### Solucion

1. Las Funciones escogidas seran la Función de Rosenbrock y la Función de Rastrigin
* La funcion de Rosenbrock esta definida como
```math
F(x)=\sum_{i=1}^{n-1} b(x_{i+1}-x_{i}^2)^2 + (a-x_{i})^2 , \ con \ x={x_{i},\dots,x_{n}}
```
* la funcion de Rastrigin es definidad como 
```math
F(x)=An + \sum_{i=1}^{n}x_{i}^2 -Acos(2x_{i}\pi), \ con \ A=10, \ x_{i} \in [-5.12,5.12]
```
2. Optimice las funciones en dos y tres dimensiones usando un método de descenso por gradiente con condición inicial aleatoria

- Función de Rosenbrock 2D
```math
$$F(x_{1},x_{2})=(a-x_{1})^2 + b(x_{2}-x_{1}^2)^2$$
```
Derivadas Parciales
```math
\frac{\partial ,\partial x}=-2(1-x)-400x(y-x^2)
```
```math
frac{\partial ,\partial y}=200*(y-x^2)
```
- Función de Rosenbrock 3D
```math
F(x_{1},x_{2},x_{3})=(a-x_{1})^2 + b(x_{2}-x_{1}^2)^2 + (a-x_{2})^2 + b(x_{3}-x_{2}^2)^2
```
Derivadas Parciales
```math
frac{\partial ,\partial x}=-2(1-x) - 400x(y-x^2)
```
```math
frac{\partial ,\partial y}=200(y-x^2)-400y(z-y^2)-2(1-y)
```
```math
frac{\partial ,\partial z}=200(z-y^2)
```
- Función de Rastring 2D
```math
F(x,y) = 20 + x^2 - 10\cos(2x\pi)+ y^2 - 10\cos(2y\pi)
```
Derivadas Parciales
```math
frac{\partial ,\partial x}=2x + 10sin(2x\pi)(2\pi)
```
```math
frac{\partial ,\partial y}=2y + 10sin(2y\pi)(2\pi)
```
- Función de Rastring 3D
```math
F(x,y,z) = 30 + x^2 - 10\cos(2x\pi)+ y^2 - 10\cos(2y\pi)+ z^2 - 10\cos(2z\pi)
```
-Derivadas Parciales
```math
frac{\partial ,\partial x}=2x + 10sin(2x\pi)(2\pi)
```
```math
frac{\partial ,\partial y}=2y + 10sin(2y\pi)(2\pi)
```
```math
frac{\partial ,\partial z}=2z+10sin(2z\pi)(2\pi)
```
3. Optimice las funciones en dos y tres dimensiones usando: algoritmos evolutivos, optimización de partículas y evolución diferencial
4. Represente con un gif animado o un video el proceso de optimización de descenso por gradiente y el proceso usando el método heurístico.

## Punto 2

### Introduccion

Nos presentamos ante el siguiente problema, un vendedor que necesita hacer un recorrido entre las siguientes ciudades de colombia.
- Palmira
- Pasto
- Tuluá
- Bogota
- Pereira
- Armenia
- Manizales
- Valledupar
- Montería
- Soledad
- Cartagena
- Barranquilla
- Medellín
- Bucaramanga
- Cúcuta

El vendedor necesita conocer el orden optimo en el cual deberá atravesar esas ciudades , y a partir de ello calcular cuales serian los costos de su viaje ( incluyendo el costo de peajes , el costo de la gasolina gastada en terminos de los kilometros recorridos y el costo al cual el vendedor le pone a su tiempo).

Para esto usaremos tanto el algoritmo de las colonias de hormigas como el algoritmo genetico para establecer 2 posibles alternativas de orden para el recorrido del vendedor


### Algoritmo genetico
El algoritmo genético aplicado al problema del vendedor viajero es un método de optimización que utiliza principios de evolución para encontrar la solución óptima a un problema de rutas. El algoritmo comienza con una población de soluciones potenciales, que se mejoran a través de operaciones de selección, cruce y mutación. Las soluciones se evalúan en función de su aptitud, es decir, la distancia total recorrida por la ruta propuesta. 

Imagen02
![]()

### Algoritmo de colonias de hormigas
El algoritmo de las colonias de hormigas es un método de optimización basado en el comportamiento de las hormigas en busca de alimento. El algoritmo comienza con un conjunto de soluciones potenciales y utiliza un sistema de feromonas para guiar la búsqueda hacia las soluciones óptimas. 

Esto aplicado a nuestro problema busca la solución optima, esto aplicado nos da una ruta entre todas las ciudades sin repetir recorrido ( con excepcion de la ciudad de inicio , ya que el vendedor tiene que volver a la ciudad de inicio)

Usando el codigo propuesto para el algoritmo de las colonias obtenemos un arreglo con numeros , los cuales son asociados a una ciudad , con esto de forma preliminar obtenemos un mapa preliminar de como seria el recorrido.


![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/ciudades.png)

Reusando el codigo para generar el mapa en el algoritmo genetico, obtenemos una mejor visualizacion del recorrido.

![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/hormigas.PNG)

## Referencias
[ChatGTP](https://chat.openai.com/chat/)
