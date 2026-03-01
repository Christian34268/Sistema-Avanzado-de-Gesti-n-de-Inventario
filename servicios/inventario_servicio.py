# Módulo que gestiona las operaciones del inventario
# Usa un DICCIONARIO como colección principal para búsqueda rápida por ID

from modelos.producto import Producto

ARCHIVO_INVENTARIO = "inventario.txt"

class InventarioServicio:
    """Gestiona las operaciones relacionadas al inventario"""

    # ============================================
    # 🏗️  CONSTRUCTOR
    # ============================================
    def __init__(self):
        self.productos = {}
        self.__ids_registrados = set()
        self.__cargar_desde_archivo()

    # ============================================
    # 📂 MANEJO DE ARCHIVOS
    # ============================================
    def __cargar_desde_archivo(self):
        """Lee inventario.txt y reconstruye el diccionario de productos"""
        try:
            with open(ARCHIVO_INVENTARIO, "r") as archivo:
                lineas = archivo.readlines()

        except FileNotFoundError:
            print("📂 El archivo de inventario no existe. Se creará uno nuevo al guardar.")
            with open(ARCHIVO_INVENTARIO, "w") as archivo:
                pass
            return

        except PermissionError:
            print("🔒 No posee la autoridad necesaria para leer el archivo de inventario.")
            return

        else:
            for linea in lineas:
                linea = linea.strip()
                if linea:
                    partes = linea.split("|")
                    id_producto, nombre, cantidad, precio = tuple(partes)
                    producto = Producto(int(id_producto), nombre, int(cantidad), float(precio))
                    self.productos[int(id_producto)] = producto
                    self.__ids_registrados.add(int(id_producto))

    def __guardar_en_archivo(self):
        """Guarda el inventario actual en el archivo de texto"""
        try:
            with open(ARCHIVO_INVENTARIO, "w") as archivo:
                for producto in self.productos.values():
                    datos = producto.to_tuple()
                    linea = f"{datos[0]}|{datos[1]}|{datos[2]}|{datos[3]}\n"
                    archivo.write(linea)

        except PermissionError:
            print("🔒 No posee la autoridad necesaria para escribir en el archivo de inventario.")

    # ============================================
    # ➕ AGREGAR PRODUCTO
    # ============================================
    def agregar_producto(self, id_producto, nombre, cantidad, precio):
        """Añade un nuevo producto al diccionario del inventario"""
        if id_producto in self.__ids_registrados:
            return False, "❌ El ID del producto ya existe dentro del inventario"
        if cantidad < 0:
            return False, "⚠️  La cantidad no puede ser negativa"
        if precio < 0:
            return False, "⚠️  El precio no puede ser negativo"

        nuevo = Producto(id_producto, nombre, cantidad, precio)
        self.productos[id_producto] = nuevo
        self.__ids_registrados.add(id_producto)
        self.__guardar_en_archivo()
        return True, "✅ Producto agregado exitosamente"

    # ============================================
    # 📋 LISTAR PRODUCTOS
    # ============================================
    def listar_productos(self):
        """Muestra todos los productos del inventario"""
        if not self.productos:
            print("📭 El inventario se encuentra vacío.")
            return

        print("\n📦 Inventario:")
        print("=" * 60)
        for producto in self.productos.values():
            print(producto)
        print("=" * 60)

    # ============================================
    # 🔍 BUSCAR POR NOMBRE
    # ============================================
    def buscar_por_nombre(self, texto):
        """Busca productos por nombre"""
        resultados = []
        texto = texto.lower()
        for producto in self.productos.values():
            if texto in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados

    # ============================================
    # 🔎 BUSCAR POR ID
    # ============================================
    def buscar_por_id(self, id_producto):
        """Busca y retorna un producto por su ID en el diccionario"""
        if id_producto in self.productos:
            return self.productos[id_producto]
        return None

    # ============================================
    # ✏️  ACTUALIZAR PRODUCTO
    # ============================================
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza cantidad o precio de un producto por ID"""
        if id_producto not in self.productos:
            return False, "❌ Producto no encontrado"

        producto = self.productos[id_producto]
        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)
        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        self.__guardar_en_archivo()
        return True, "✅ Producto actualizado"

    # ============================================
    # 🗑️  ELIMINAR PRODUCTO
    # ============================================
    def eliminar_producto(self, id_producto):
        """Elimina un producto del diccionario por su ID"""
        if id_producto not in self.productos:
            return False, "❌ Producto no encontrado"

        del self.productos[id_producto]
        self.__ids_registrados.discard(id_producto)
        self.__guardar_en_archivo()
        return True, "✅ Producto eliminado exitosamente"