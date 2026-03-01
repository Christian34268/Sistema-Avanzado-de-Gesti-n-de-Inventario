# Módulo que define la clase Producto
# Representa cada ítem del inventario con sus atributos principales

class Producto:
    # Constructor de la clase
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Métodos Captadores (Getters)
    def get_id(self):
        return self.__id_producto

    def get_nombre(self):
        return self.__nombre

    def get_cantidad(self):
        return self.__cantidad

    def get_precio(self):
        return self.__precio

    # Métodos Definidores (Setters)
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            print(":-( La cantidad ingresada no puede ser negativa.")

    def set_precio(self, precio):
        if precio >= 0:
            self.__precio = precio
        else:
            print(":-( El precio no puede ser negativo.")

    # Representación en texto del objeto Producto
    def __str__(self):
        return (
            f"[{self.__id_producto}] "
            f"{self.__nombre:25} | "
            f"Cant: {self.__cantidad:4} | "
            f"${self.__precio:8.2f}"
        )

    # Retorna los datos como tupla (útil para guardar en archivo)
    def to_tuple(self):
        return (self.__id_producto, self.__nombre, self.__cantidad, self.__precio)