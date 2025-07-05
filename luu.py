t = 0
pol = 5
pant = 5
cha = 5
while True:
    try:
        print("1. Comprar")
        print("2. Total a pagar")
        print("3. Salir del programa")
        opc = int("Ingrese una opcion: ")
        if opc == 1:
            while True:
                try:
                    print("------Productos Disponibles------")
                    print(f"1. {pol} Polera, precio por unidad $4000")
                    print(f"2. {pant} Pantalon, precio por unidad $12000")
                    print(f"3. {cha} Chaqueta, precio por unidad $15000")
                    print("4. Salir")
                    prod = int(input("Ingrese numero del producto a comprar: "))
                    if prod == 1 and pol > 0:
                        t += 4000
                        pol -= 1
                    elif prod == 2 and pant > 0:
                        t += 12000
                        pant -=1
                    elif prod == 3 and cha > 0:
                        t += 15000
                        cha -=1
                    elif prod == 4:
                        break
                    elif prod == 1 and cha == 0:
                        print("No quedan stocks de Poleras")
                    elif prod == 2 and cha == 0:
                        print("No quedan stocks de Pantalones")
                    elif prod == 3 and cha == 0:
                        print("No quedan stocks de Chaquetas")
                    else:
                        print("Opcion no valida")
                except ValueError:
                    print("Ingrese un valor numerico")
        elif opc == 2:
            print("")
        elif opc == 3 and t == 0:
            print("a")
        else:
            print("Opcion no valida")

    except ValueError:
        print("Ingrese valor numerico")