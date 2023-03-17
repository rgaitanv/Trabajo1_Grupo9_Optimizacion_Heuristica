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
\frac{\partial}{\partial x}=-2(1-x)-400x(y-x^2)
```
```math
\frac{\partial}{\partial y}=200*(y-x^2)
```
- Función de Rosenbrock 3D
```math
F(x_{1},x_{2},x_{3})=(a-x_{1})^2 + b(x_{2}-x_{1}^2)^2 + (a-x_{2})^2 + b(x_{3}-x_{2}^2)^2
```
Derivadas Parciales
```math
\frac{\partial}{\partial x}=-2(1-x) - 400x(y-x^2)
```
```math
\frac{\partial}{\partial y}=200(y-x^2)-400y(z-y^2)-2(1-y)
```
```math
\frac{\partial}{\partial z}=200(z-y^2)
```
- Función de Rastring 2D
```math
F(x,y) = 20 + x^2 - 10\cos(2x\pi)+ y^2 - 10\cos(2y\pi)
```
Derivadas Parciales
```math
\frac{\partial}{\partial x}=2x + 10sin(2x\pi)(2\pi)
```
```math
\frac{\partial}{\partial y}=2y + 10sin(2y\pi)(2\pi)
```
- Función de Rastring 3D
```math
F(x,y,z) = 30 + x^2 - 10\cos(2x\pi)+ y^2 - 10\cos(2y\pi)+ z^2 - 10\cos(2z\pi)
```
-Derivadas Parciales
```math
\frac{\partial}{\partial x}=2x + 10sin(2x\pi)(2\pi)
```
```math
\frac{\partial}{\partial y}=2y + 10sin(2y\pi)(2\pi)
```
```math
\frac{\partial}{\partial z}=2z+10sin(2z\pi)(2\pi)
```
3. Optimice las funciones en dos y tres dimensiones usando: algoritmos evolutivos, optimización de partículas y evolución diferencial

# Rastrigin
 * Algoritmo evolutivo 2D soluciones<br>
    Punto óptimo: [ 0.05214126 -0.06074095]<br>
    Valor óptimo: 0.7950696846817561<br>

 * Algoritmo evolutivo 3D soluciones<br>
    MPunto óptimo:  [-3406.66311433 -3073.54780406  3351.37851544]<br>
    Valor óptimo:  32283839.601949047<br>
    ![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/rastrigin-evolutivo3d.PNG)

 * Optimizacon de particulas 2D soluciones<br>
    Punto óptimo:  [-8.15783695e-07  1.63806771e-06]<br>
    Valor óptimo:  6.643681160767301e-10<br>
    ![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/rastrigin-particulas2d.PNG)

 * Optimizacon de particulas 3D soluciones<br>
    Punto óptimo:  [-1.77528669e-05  7.12565680e-06  9.94956499e-01]<br>
    Valor óptimo:  0.9949591305999235<br>
    ![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/rastrigin-particulas3d.PNG)

 * Evolución diferencial 2D soluciones<br>
    Punto óptimo:  0.0 -0.0<br>
    Valor óptimo:  0.0<br>
    ![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/rastrigin-diferencial2d.PNG)

 * Evolución diferencial 3D soluciones<br>
    Punto óptimo: 0.0 -0.0 0.0<br>
    Valor óptimo: 0.0<br>
    ![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/rastrigin-diferencial3d.PNG)

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

Usando un algoritmo propuesto obtenemos un orden para el recorrido de las ciudades. Dado que este algoritmo busca soluciones pseudo optimas en diferentes corridas es posible que arroje diferentes soluciones por lo que la imagen a continuacion es un ejemplo , mas no es el caso escogido para el analisis entre ambos recorridos, pero sirve para ilustrar un posible recorrido.

![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/10001-1.PNG)

### Algoritmo de colonias de hormigas
El algoritmo de las colonias de hormigas es un método de optimización basado en el comportamiento de las hormigas en busca de alimento. El algoritmo comienza con un conjunto de soluciones potenciales y utiliza un sistema de feromonas para guiar la búsqueda hacia las soluciones óptimas. 

Esto aplicado a nuestro problema busca la solución optima, esto aplicado nos da una ruta entre todas las ciudades sin repetir recorrido ( con excepcion de la ciudad de inicio , ya que el vendedor tiene que volver a la ciudad de inicio)

Usando el codigo propuesto para el algoritmo de las colonias obtenemos un arreglo con numeros , los cuales son asociados a una ciudad , con esto de forma preliminar obtenemos un mapa preliminar de como seria el recorrido.


![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/ciudades.png)

Reusando el codigo para generar el mapa en el algoritmo genetico, obtenemos una mejor visualizacion del recorrido.

![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/hormigas.PNG)

## Elección del recorrido 
Antes de escoger el recorrido definiremos 2 aspectos importantes para el recorrido del vendedor, estos seran el tipo de vehiculo que usara y el tiempo del recorrido. Usando como base los autos mas vendidos en 2022 en colombia , seleccionamos uno de estos , siendo el modelo Chevrolet Onix 2023. El costo del auto no sera considerado , partiendo del supuesto que el vendedor ya lo posee ( pero en caso de no hacerlo , el precio puede ser aproximadamente de 76 Millones de pesos).Este auto consume aproximadamente un rendimiento real de 17 km/l,siendo esto aproximadamente 64.352 km por galon, asi con el kilometraje de los recorridos obtendremos el costo por gasolina. Otra consideracion es que el maximo de litros que soporta este modelo es de 44 , entonces puede almacenar 11.6 galones.

Retomando el segundo aspecto , el cual es el tiempo del viajero para el cual tomaremos los tiempos aproximados entre las distancias entre las ciudades, el costo del tiempo lo asumiremos como la hora del vendedor vale esta  una funcion de 10000 pesos + 10000 pesos adicionales por cada hora recorrida.

Al ser algo volatil el algoritmo genetico, al escoger un pseudo optimo diferentes en diferentes iteraciones , solo tomamos un caso de prueba para la comparacion , en contra parte el recorrido de las hormigas siempre es el mismo, por ende no tendremos problemas con este.

Con esto tendremos dos recorridos , los cuales nos indicaran dos posibles orden para el viaje del vendedor.

Usando informacion del recorrido sabiendo los orden , se pudo extraer la cantidad total de horas de viaje , los km totales recorridos, el numero de pasajes y el total de dinero que se debe gastar en todo el recorrido con los pasajes.

![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/info_del_recorrido.PNG)


### Recorrido Algoritmo de las colonias de hormigas

Para el algoritmo de las colonias el recorrido sera asi partiendo y regresando a pasto.

'Pasto'=> 'Bogota'=> 'Bucaramanga'=> 'Cúcuta'=> 'Valledupar'=> 'Soledad'=> 'Barranquilla'=> 'Cartagena'=> 'Montería'=> 'Medellín'=> 'Manizales'=> 'Pereira'=> 'Armenia'=> 'Tuluá'=> 'Palmira'=> 'Pasto'

El recorrido en total cuenta con 3969.7 km asi que en total el vendedor debera tener aproximadamente 62 galones para todo el recorrido, por lo cual el conductor debera reponer gasolina al menos 6 veces reponiendo 11 galones para un recorrido aproximadamente cada 662 kilometros. para el costo de la gasolina usaremos el precio de venta de la ciudad de partida para el primer llenado del tanque y en las siguientes se usara un promedio del precio de la gasolina redondeado al valor de 1000 pesos mas alto , esto se debe a que hay recorridos entre ciudades que superan los 662 kilometros y es mas complicado determinar exactamente el precio de la  gasolina en el puesto mas cercano cuando esta se esta acabando entre recorridos.

Por ende en pasto iniciamos con un precio por galon de $9.316 y para las siguientes reposiciones se usara un precio de 11000 pesos, por consiguiente el precio de la gasolina en el recorrido es de 707476 pesos.

El recorrido aproximadamente cuenta con 78 horas de viaje, por lo cual el costo por horas es de de 790000 pesos.

El costo por el pago de todos los pasajes es de 629500 pesos.

Por ende para el recorrido de las hormigas es de 2126976 de pesos.

### Recorrido Algoritmo genetico

Para el caso de estudio usando en el algoritmo generico se empieza en Palmira y se termina en esta.

'Palmira'=> 'Tuluá'=> 'Pereira'=> 'Montería'=> 'Barranquilla'=> 'Soledad'=> 'Cartagena'=> 'Valledupar'=> 'Medellín'=> 'Bucaramanga'=> 'Cúcuta'=> 'Bogota'=> 'Manizales'=> 'Armenia'=> 'Pasto'=> 'Palmira'

Usando la misma metodologia usada en el recorrido de las hormigas.

El costo de gasolina, palmira al no ser una ciudad principal , usaremos para todo el analisis el precio de 11000 pesos por galon aproximadamente y el recorrido es de 4912 km por lo que el vendedor debera reponer 77 galones aproximadamente durante todo el recorrido, por lo cual debera reponer 11 galones 7 veces, dando un costo de 847000 pesos por todo el recorrido.

El recorrido aproximadamente dura 95 horas por lo cual el gasto del tiempo de costo es de 960000.

El costo de todos los pasajes es de 748100 pesos.

Por ende el costo por desplazamiento para el algoritmo genetico es de 2555100 pesos.

## Solucion Ganadora
Dado que el algoritmo de las hormigas nos deja ahorrar 400000 pesos, esta es la solucion ganadora.

![](https://github.com/rgaitanv/Trabajo1_Grupo9_Optimizacion_Heuristica/blob/main/Imagenes/Recorridos.gif)

## Referencias
- [ChatGTP](https://chat.openai.com/chat/)
- [Autos Mas vendidos en Colombia 2022](https://www.motor.com.co/industria/Listado-de-los-carros-mas-vendidos-en-2022-20230113-0009.html)
- [Chevrolet Onix 2023](https://noticias.autocosmos.com.mx/2022/08/01/chevrolet-onix-2023-a-prueba-conoce-el-consumo-de-combustible-real-de-este-sedan-hecho-en-china)
- [Precio de la gasolina 2023 Ciudades principales](https://www.canalinstitucional.tv/precio-gasolina-2023-colombia)
- [Precio de la gasolina 2023 Colombia](https://es.globalpetrolprices.com/Colombia/gasoline_prices/)
- [especificaciones del Chevrolet Onix 2023](https://www.chevrolet.com.co/carros/onix-turbo-sedan/especificaciones-versiones)
- [Peajes para el recorridos entre ciudades](https://www.peajesencolombia.com/)
