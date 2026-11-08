class GestionInventario:
    """Pretende administrar el inventario de productos de una tienda"""
    def __init__(self):
        self.inventario = {}

    def añadir_producto(self, producto, cantidad):
        if producto in self.inventario:
            self.inventario[producto] = self.inventario.get(producto) + cantidad
        else:
            self.inventario[producto] = cantidad

    def eliminar_producto(self, producto):
        if producto in self.inventario:
            self.inventario.pop(producto)

    def consultar_producto(self, producto):
        return self.inventario.get(producto, "Producto no existe en el inventario.")
        

    def mostrar_inventario(self):
        print("--- Inventario ---")
        for key, value in self.inventario.items():
            print("{}: {}".format(key, value))
        print("------------------")

inv = GestionInventario()
inv.añadir_producto("Manzanas", 10)
inv.añadir_producto("Peras", 5)
inv.añadir_producto("Manzanas", 5)
print(f"Consultar Manzanas: {inv.consultar_producto('Manzanas')}")
inv.mostrar_inventario()
inv.eliminar_producto("Peras")
print("Inventario después de eliminar Peras:")
inv.mostrar_inventario()
