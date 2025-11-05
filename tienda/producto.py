#producto

class Producto:
    def __init__(self, codigo, nombre, precio, stock, descripcion=""):
        #datos básicos de cada producto
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion

    def actualizar_stock(self, cantidad):
        #suma o resta unidades del stock según la cantidad indicada
        self.stock += cantidad
        
    def actualizar_precio(self, precio):
        #guarda el valor del nuevo precio
        self.precio = precio

    def mostrar_info(self):
        #devuelve un texto con toda la información del producto
        info = f"Código: {self.codigo} | Nombre: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock}"
        if self.descripcion:
            info += f" | Descripción: {self.descripcion}"
        return info

    def __str__(self):
        return self.mostrar_info()
