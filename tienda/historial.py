# historial
# estructura de datos: pila (stack)

class HistorialVistos:
    def __init__(self, limite=5):
        self.limite = limite
        self.pila = []

    def ver_producto(self, producto):
        # agrega un producto al historial (el último visto)
        if len(self.pila) >= self.limite:
            self.pila.pop(0)  # elimina el más antiguo si se supera el límite
        self.pila.append(producto)
        print(f"Producto visto: {producto.nombre}")

    def mostrar_historial(self):
        print("\n----- ÚLTIMOS PRODUCTOS VISTOS -----")
        if not self.pila:
            print("No hay productos vistos aún.")
        else:
            for p in reversed(self.pila):
                print(" -", p.mostrar_info())
