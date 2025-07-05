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

def entrada(base_datos):
    nom = input("Ingrese nombre de comprador: ").strip()
    if nom in base_datos:
        print("Ese nombre ya está registrado.")
        return
    tipo_ent = input("Ingrese tipo de entrada(G/V): ").strip().upper()
    if tipo_ent not in ["G", "V"]:
        print("Tipo de entrada no válido.")
        return

    while True:
        codigo = input("Ingrese código de confirmación: ").strip()
        if validar_codigo(codigo):
            print("Código validado. ¡Entrada registrada con éxito!")
            base_datos[nom] = (tipo_ent, codigo)
            break
        else:
            print("Código no válido. Intente otra vez.")

def comprador(base_datos):
    nom = input("Ingrese nombre de comprador a buscar: ").strip()
    if nom in base_datos:
        tipo_ent, codigo = base_datos[nom]
        print(f"Tipo de entrada: {tipo_ent}, Código: {codigo}")
    else:
        print("El comprador no se encuentra.")

def cancelar(base_datos):
    nom = input("Ingrese nombre del comprador: ").strip()
    if nom in base_datos:
        del base_datos[nom]
        print("¡Compra cancelada!")
    else:
        print("No se pudo cancelar la compra.")

def main():
    base_datos = {}  # Diccionario global que se pasa a las funciones
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Comprar entrada.")
        print("2.- Consultar comprador.")
        print("3.- Cancelar compra.")
        print("4.- Salir")
        try:
            opc = int(input("Ingrese opción: "))
            if opc == 1:
                entrada(base_datos)
            elif opc == 2:
                comprador(base_datos)
            elif opc == 3:
                cancelar(base_datos)
            elif opc == 4:
                print("Programa terminado...")
                break
            else:
                print("Debe ingresar una opción válida!!")
        except ValueError:
            print("Debe ingresar un número válido.")

main()
