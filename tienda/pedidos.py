# pedidos 
# estructura de datos: cola (queue)

from collections import deque

class ColaDePedidos:
    def __init__(self):
        self.cola = deque()

    def agregar_pedido(self, pedido):
        #  agrega un nuevo pedido al final de la cola
        self.cola.append(pedido)
        print(f"Pedido '{pedido}' agregado a la cola.")

    def procesar_pedido(self):
        #procesa el primer pedido en la cola 
        if self.esta_vacia():
            print("No hay pedidos pendientes.")
        else:
            pedido = self.cola.popleft()
            print(f"Pedido '{pedido}' procesado.")
            return pedido

    def esta_vacia(self):
        #si la cola está vacía
        if len(self.cola) == 0 : 
            return print("La cola está vacía.")
        else :
            return print(f"La cola no está vacía, tiene {len(self.cola)} elementos.")

    def mostrar_pedidos(self):
        # todos los pedidos que están en espera dentro de la cola
        print("\n----- PEDIDOS PENDIENTES -----")
        if self.esta_vacia():
            print("No hay pedidos.")
        else:
            for p in self.cola:
                print(" -", p)
