# inventario
# estructura de datos: hash table

from tienda.producto import Producto

class Inventario:
    def __init__(self, tamaño=10):
        # tabla hash vacía (lista de tamaño fijo)
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    def funcion_hash(self, codigo):
        # convierte un código de producto string en un índice numérico.
        suma = 0
        for caracter in codigo:
            suma += ord(caracter)
        return suma % self.tamaño

    def agregar_producto(self, producto):
        # agrega o actualiza un producto en la tabla
        indice = self.funcion_hash(producto.codigo)
        inicio = indice

        while self.tabla[indice] is not None:
            # si el producto ya existe, se actualiza
            if self.tabla[indice].codigo == producto.codigo:
                self.tabla[indice] = producto
                print(f"Producto '{producto.nombre}' actualizado (índice {indice}).")
                return
            # si hay colisión, se avanza a la siguiente posicion
            indice = (indice + 1) % self.tamaño
            if indice == inicio:
                print("No se puede agregar el producto.")
                return

        # insertar el producto
        self.tabla[indice] = producto
        print(f"Producto '{producto.nombre}' agregado (índice {indice}).")

    def buscar_producto(self, codigo):
        # busca un producto por su código
        indice = self.funcion_hash(codigo)
        inicio = indice

        while self.tabla[indice] is not None:
            if self.tabla[indice].codigo == codigo:
                return print(f"El producto {codigo} está en el inventario.")
            indice = (indice + 1) % self.tamaño
            if indice == inicio:
                break
        return print(f"El producto {codigo} no está en el inventario.")

    def eliminar_producto(self, codigo):
        # elimina un producto
        indice = self.funcion_hash(codigo)
        inicio = indice

        while self.tabla[indice] is not None:
            if self.tabla[indice].codigo == codigo:
                print(f"Producto '{self.tabla[indice].nombre}' eliminado.")
                self.tabla[indice] = None
                return
            indice = (indice + 1) % self.tamaño
            if indice == inicio:
                break
        print("Producto no encontrado.")

    def mostrar_inventario(self):
        # muestra el contenido del inventario
        print("\n----- INVENTARIO ACTUAL -----")
        for i, producto in enumerate(self.tabla):
            if producto is None:
                print(f"[{i}] → vacío")
            else:
                print(f"[{i}] → {producto.mostrar_info()}")
