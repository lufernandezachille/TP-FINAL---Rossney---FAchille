# categorías
# estructura de datos: árbol (tree)

class NodoCategoria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.subcategorias = []
        self.productos = []

    #agrega subcategoria a la categoria actual
    def agregar_subcategoria(self, subcategoria):
        self.subcategorias.append(subcategoria)

    #agrerga producto en la categoría actual
    def agregar_producto(self, producto):
        self.productos.append(producto)

    #muestra la jerarquía completa de categorías y productos
    def mostrar(self, nivel=0):
        print("  " * nivel + f"{self.nombre.upper()}")
        for p in self.productos:
            print("  " * (nivel + 1) + f"- {p.nombre}")
        for sub in self.subcategorias:
            sub.mostrar(nivel + 1)
