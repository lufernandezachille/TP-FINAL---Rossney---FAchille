# TP-FINAL---Rossney---FAchille
DESCRIPCIÓN DEL PROYECTO:
El proyecto consiste en el desarrollo de la tienda online de un negocio de cómics en San Telmo llamada “Nadie se salva solo”. Para esto empleamos distintas estructuras de datos dependiendo de cuál fuera la más adecuada para cada función de nuestro proyecto, como lo son la hash table, queue, stack y tree. El objetivo de la tienda online es permitir la gestión del inventario de productos, el procesamiento de los pedidos de los clientes, la visualización de un historial de últimos productos vistos y la organización jerárquica de los productos. 

INSTRUCCIONES DE EJECUCIÓN:
Clonar el repositorio para poder acceder de forma local y ejecutar el archivo main.py.

DECISIONES DE DISEÑO:
GESTIÓN DE PRODUCTOS:
Usamos la estructura de datos denominada hash table ya que para agregar nuevos productos, actualizar la información de productos existentes, buscar un producto específico por su código único y eliminarlo, ya que existe una forma de dirigirse directamente al elemento buscado a través de una función hash. Esto la diferencia de los arrays y las linked lists, en los cuales el tiempo de búsqueda es mayor dado a que se debe comparar cada elemento uno por uno para descubrir si existe. Las hash tables sirven para saber si un elemento está en una colección, guardar elementos únicos y conectar valores a claves.

PROCESAMIENTO DE PEDIDOS:
Usamos la estructura de datos denominada queue ya que permite un uso más eficiente de la memoria y es fácil de comprender e implementar, además, las desventajas que tiene esta estructura de datos no intervienen con el uso que le queremos dar, ya sea que ocupa una parte fija de la memoria, o que puede llegar a ser lenta en el caso de que sea muy larga (lo cual hace que tome mucho tiempo al desplazar cada elemento cuando se quita uno). Los datos en una queue se organizan de una forma llamada FIFO (first in first out), en la cual el primer elemento en entrar es el primero en salir. Las operaciones que se pueden utilizar en una queue facilitan el manejo de los datos en el caso del procesamiento de pedidos, como lo son las siguientes: 
enqueue: agrega un elemento a la cola
dequeue: remueve y devuelve el primer elemento de la cola
peek: devuelve el primer elemento de la cola
isempty: se fija si la cola está vacía
size: devuelve la cantidad de elementos que hay en la cola

HISTORIAL DE ÚLTIMOS PRODUCTOS VISTOS:
Usamos la estructura de datos denominada stack, ya que los datos se organizan de una forma denominada LIFO (last in first out), en la cual el último que se ingresa es el primero en salir. Esto nos permite que al hacer un historial se muestran primero los pedidos que se han visto más recientemente. Las operaciones que se pueden utilizar en un stack facilitan el manejo de los datos en el caso del historial de últimos productos vistos, como lo son las siguientes: 
push: agrega un elemento a la pila
pop: remueve y devuelve el elemento que está más arriba en la pila
peek: devuelve el elemento que está más arriba en la pila
isempty: se fija si la pila está vacía
size: devuelve la cantidad de elementos que hay en la pila

CATEGORIZACIÓN JERÁRQUICA DE PRODUCTOS:
Usamos la estructura de datos denominada tree, ya que permite la organización de los datos de forma jerárquica, o sea, por rangos, y facilita su búsqueda. En el caso del proyecto, estas funciones son fundamentales para la categorización de los productos, organizándolos por distintas categorías, una dentro de otra, es decir, los nodos padres e hijos.

