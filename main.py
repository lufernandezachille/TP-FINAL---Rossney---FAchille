# main

from tienda.producto import Producto
from tienda.inventario import Inventario
from tienda.pedidos import ColaDePedidos
from tienda.historial import HistorialVistos
from tienda.categorias import NodoCategoria

# --------------------------------------------------------------------
# SECCIÓN 1: GESTIÓN DE INVENTARIO 
# --------------------------------------------------------------------
# inventario que guarda los productos usando una tabla hash para busquedas eficientes
# Luego se agregan algunos productos de ejemplo y se muestra el estado completo de la tabla.

print("GESTIÓN DE PRODUCTOS")

inventario = Inventario()

# creación de productos
p1 = Producto("A101", "Batman", 3500, 10, "Cómic clásico de DC Comics")
p2 = Producto("A102", "Spiderman", 3200, 5, "Edición especial Marvel")
p3 = Producto("A103", "Superman", 3300, 8, "Colección especial")

# agrega los productos al inventario
print("--Agregar productos al inventario--")
inventario.agregar_producto(p1)
inventario.agregar_producto(p2)
inventario.agregar_producto(p3)

# mostrar inventario
inventario.mostrar_inventario()

#actualiza el stock de un producto
print("--Actualizar el stock de un producto--")
print(p1)
p1.actualizar_stock(5) #si se obtienen 5 unidades más de un producto
print(p1)

#actualiza el precio de un producto
print("--Actualizar el precio de un producto--")
print(p1)
p1.actualizar_precio(4000)
print(p1)

#buscar un producto en el inventario
print("--Buscar productos en el inventario--")
inventario.buscar_producto("A101")
inventario.buscar_producto("A104")

#eliminar un producto del inventario
p4 = Producto("A104", "Wonder Woman", 3600, 6, "Edición limitada con portada dorada")
inventario.agregar_producto(p4)

print("--Eliminar productos del inventario--")
inventario.eliminar_producto("A104")
inventario.eliminar_producto("A105")
#inventario con el producto eliminado
inventario.mostrar_inventario()

# --------------------------------------------------------------------
# SECCIÓN 2: HISTORIAL DE PRODUCTOS VISTOS 
# --------------------------------------------------------------------
# Representa los últimos productos visitados por el usuario.
# Se guarda un máximo de 5 productos. al agregar uno nuevo, se elimina el más antiguo.

print("HISTORIAL DE ÚLTIMOS PRODUCTOS VISTOS")

historial = HistorialVistos()

# vista de algunos productos
historial.ver_producto(p1)
historial.ver_producto(p2)
historial.ver_producto(p3)

#historial actual (del más reciente al más antiguo)
historial.mostrar_historial()

#si se sobrepasa el límite del historial
p4 = Producto("A104", "Wonder Woman", 3600, 6, "Edición limitada con portada dorada")
p5 = Producto("A105", "Flash", 3100, 9, "Cómic de alta velocidad con arte renovado")
p6 = Producto("A106", "Linterna Verde", 3400, 4, "Volumen especial del Cuerpo de Linternas Verdes")
p7 = Producto("A107", "Aquaman", 3000, 7, "Edición oceánica con portada holográfica")

inventario.agregar_producto(p4)
inventario.agregar_producto(p5)
inventario.agregar_producto(p6)
inventario.agregar_producto(p7)

historial.ver_producto(p4)
historial.ver_producto(p5)
historial.ver_producto(p6)
historial.ver_producto(p7)

historial.mostrar_historial() #solo muestra los 5 más recientes

# --------------------------------------------------------------------
# SECCIÓN 3: PROCESAMIENTO DE PEDIDOS 
# --------------------------------------------------------------------
# Los pedidos se almacenan en una cola (FIFO), para que se procesen en el mismo orden en que fueron recibidos.

print("PROCESAMIENTO DE PEDIDOS")

pedidos = ColaDePedidos()

# mostrar si la cola está vacía
print("--Fijarse si la cola está vacía antes de hacer pedidos--")
pedidos.esta_vacia()

# se agregan pedidos a la cola
print("--Hacer pedidos--")
pedidos.agregar_pedido("Pedido 1 - Batman")
pedidos.agregar_pedido("Pedido 2 - Spiderman")

# mostrar si la cola está vacía
print("--Fijarse si la cola está vacía después de hacer pedidos--")
pedidos.esta_vacia()

# pedidos pendientes
pedidos.mostrar_pedidos()

# primer pedido (el más antiguo)
print("--Procesar pedidos--")
pedidos.procesar_pedido()

# estado de la cola después de procesar un pedido
pedidos.mostrar_pedidos()


# --------------------------------------------------------------------
# SECCIÓN 4: CATEGORIZACIÓN JERÁRQUICA DE PRODUCTOS 
# --------------------------------------------------------------------

print("CATEGORIZACIÓN JERÁRQUICA DE PRODUCTOS")

raiz = NodoCategoria("Cómics")      
dc = NodoCategoria("DC Comics")     
marvel = NodoCategoria("Marvel")     

#Se agregan las subcategorías a la raíz principal
raiz.agregar_subcategoria(dc)
raiz.agregar_subcategoria(marvel)

# asigna productos a cada categoría
dc.agregar_producto(p1)  # Batman
dc.agregar_producto(p3)  # Superman
dc.agregar_producto(p4)  # Wonder Woman
dc.agregar_producto(p5)  # Flash
dc.agregar_producto(p6)  # Linterna Verde
dc.agregar_producto(p7)  # Aquaman
marvel.agregar_producto(p2)  # Spiderman

# Se muestra toda la estructura jerárquica de categorías y sus productos
print("\n----- CATEGORÍAS Y PRODUCTOS -----")
raiz.mostrar()
