def validar_codigo(codigo):
    if len(codigo) < 6:
        return False
    if not any(c.isupper() for c in codigo):
        return False
    if not any(c.isdigit() for c in codigo):
        return False
    if ' ' in codigo:
        return False
    return True

def comprar_entrada(compradores):
    nombre = input("Ingrese nombre de comprador: ").strip()
    if nombre in compradores:
        print("El comprador ya está registrado.")
        return
    tipo = input("Ingrese tipo de entrada (G/V): ").strip().upper()
    if tipo not in ['G', 'V']:
        print("Tipo de entrada no válido. Solo se acepta G o V.")
        return
    while True:
        codigo = input("Ingrese código de confirmación: ").strip()
        if validar_codigo(codigo):
            print("Código validado. ¡Entrada registrada con éxito!")
            compradores[nombre] = (tipo, codigo)
            break
        else:
            print("Código no válido. Intente otra vez.")

def consultar_comprador(compradores):
    nombre = input("Ingrese nombre de comprador a buscar: ").strip()
    if nombre in compradores:
        tipo, codigo = compradores[nombre]
        print(f"Tipo de entrada: {tipo}, Código: {codigo}")
    else:
        print("El comprador no se encuentra.")

def cancelar_compra(compradores):
    nombre = input("Ingrese nombre de comprador a cancelar: ").strip()
    if nombre in compradores:
        del compradores[nombre]
        print("¡Compra cancelada!")
    else:
        print("No se pudo cancelar la compra.")

def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1.- Comprar entrada.")
    print("2.- Consultar comprador.")
    print("3.- Cancelar compra.")
    print("4.- Salir.")

def main():
    compradores = {}
    while True:
        mostrar_menu()
        opcion = input("Ingrese opción: ").strip()
        if opcion == "1":
            comprar_entrada(compradores)
        elif opcion == "2":
            consultar_comprador(compradores)
        elif opcion == "3":
            cancelar_compra(compradores)
        elif opcion == "4":
            print("Programa terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

# Ejecutar el programa
main()
