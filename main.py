from servicios.inventario_servicio import InventarioServicio

def mostrar_menu():
    print("""
====================================
📦 SISTEMA DE GESTIÓN DE INVENTARIO
====================================
1. ➕ Añadir producto
2. 📋 Listar inventario
3. 🔍 Buscar producto por nombre
4. ✏️  Actualizar producto
5. 🗑️  Eliminar producto
6. 🔎 Buscar producto por ID
0. 🚪 Salir
====================================
""")

def main():
    inventario = InventarioServicio()

    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Seleccione opción: "))

            if opcion == 1:  # Añadir
                id_p = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: ").replace(",", "."))
                exito, msg = inventario.agregar_producto(id_p, nombre, cantidad, precio)
                print(msg)

            elif opcion == 2:  # Listar
                inventario.listar_productos()

            elif opcion == 3:  # Buscar
                texto = input("Busqueda por nombre:")
                resultados = inventario.buscar_por_nombre(texto)
                if resultados:
                    print(f"\n Resultados ({len(resultados)}):")
                    for p in resultados:
                        print(p)
                else:
                    print(" No se encontraron coincidencias")

            elif opcion == 4:  # Actualizar
                id_p = int(input("ID del producto: "))
                print("Deje en blanco para no modificar")
                cant = input("Nueva cantidad: ")
                prec = input("Nuevo precio: ")
                
                nueva_cant = int(cant) if cant.strip() else None
                nuevo_prec = float(prec.replace(",", ".")) if prec.strip() else None
                
                exito, msg = inventario.actualizar_producto(id_p, nueva_cant, nuevo_prec)
                print(msg)

            elif opcion == 5:  # Eliminar
                id_p = int(input("ID a eliminar: "))
                exito, msg = inventario.eliminar_producto(id_p)
                print(msg)

            elif opcion == 0:  # Salir
                print(" Sistema cerrado")
                break

            else:
                print(" Opción inválida")

        except ValueError:
            print(" Error: Ingrese datos válidos")
        except KeyboardInterrupt:
            print("\n Sistema cerrado por el usuario")
            break

if __name__ == "__main__":
    main()