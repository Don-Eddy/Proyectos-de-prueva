def menu_salida():
    """El menu se utiliza para preguntar al usuario si desea abandonar 
    algun menu en el que esté o si desea salir del programa
    retona la palabra False si se dice que si saldra 
    retorna la paalbra True si dice que no saldra 
    de lo contrario se tomará como un error y se volvera pedir que ingrese 
    la informacion"""

    contador= True
    while contador == True:
        opcion =input("Desea salir (si, no): ")
        opcion = opcion.upper()
        if opcion == "SI":
            print("saliendo")
            return False
        elif opcion == "NO":
            print("Cancelando")
            return True
        else:
            print("La opcion ingresada es incorrecta, intente de nuevo\n")


def menu_de_venta(combustible, presio):
    """Funcion de venta, solicita el nombre de comprador, asi como el numero de NIt, además
    del total a pagar a asi como el total de galones vendidos"""
    contador = True
    while contador ==True:
        try:
            print("")
            nombre =input("Ingrese el nombre del Comprador: ")
            nit=input("Ingrese el numero de NIT o DPI: ")
            galones_vendidos = float(input("Ingrese la cantidad de galones que desea adquier: "))
            
            total_pagar = galones_vendidos*presio

            print("\n==Venta realizada exitosamente==\n")

            print(f"Comprador: {nombre}")
            print(f"NIT o DPI: {nit}")
            print(f"Total de galones vendidos: {galones_vendidos}")
            print(f"El valor del producto sin IVA es: {total_pagar/1.12}")
            print(f"IVA: {(total_pagar/1.12)*0.12}")
            print(f"El total a pagar es: {total_pagar}")

            combustible = combustible-galones_vendidos
        except:
            print("\nups, ubo un error")
            print("hubo un error en la ejecucion del menu")
            print("Vuelve a intentar enviar la información\n")
            contador = True
        else:
            print("Regresando al menu de venta")
            return combustible


def run():
    diesel= 1000
    super=1000
    regular=1000
    presio_diesel = 21.5
    presio_regular= 26.5
    presio_super = 26.5
    """Programa que servira para vender tres tipos de combustible (super, regural y diesel)
    para eso debe de pedir: nombre del comprador, numero de NIT o numero de DPI
    al final debe de mostrar los datos ingresados y además debe mostrar en pantalla el total a pagar,
    cantidad vendida, IVA al credito fiscal,
    
    para el operador del programa debe de ingresar su contraseña y usuario para poder vender."""
    # variable que validará si el usurario ingresa su contraseña correctamente
    contador=0
    while contador <5:
        print("---Bienvenido a  su Gasolinera---\n")
        # para este ejemplo el nombre de usuario será ADMIN123
        usuario= input("Ingrese su nombre de usuario: ")
        # para esde ejemplo la contraseña será 01230321
        contrasena = input("Ingrese su contraseña: ")

        #si el usuario ingresa su usuario y contraseña correctamente ingresa al sistema
        if usuario == "ADMIN123" and contrasena == "01230321":

            print(f"\nBienvenido {usuario}\n")
            #creación de la variable que servira para el ciclo que funciona en el menu principal
            #al cual regresara todos los submenus de cada opcion

            menu_principal=True
            while menu_principal ==True:
                
                #se mestra el  menu, y las opciones que puede realizar dentro del programa
                print("--MENU DE PRINCIPAL--\n")
                print("+-----+-------------+")
                print("| NO  | OPCION      |")
                print("+-----+-------------+")
                print("|  1  |  VENDER     |")
                print("|  2  |  VER SALDOS |")  
                print("+-----+-------------+")
                print("|  3  |  SALIR      |")
                print("+-----+-------------+\n")
                
                # Se le pide al usuario que ingrese el numero de la opcion que desea ejecutar
                opcion = input("¿Qué deseas hacer el día de hoy? NO:")

                #si la opcion ingresada es 1, ingresara al menu de venta 
                if opcion == "1":
                    
                    #se crean variable para el ciclo que funcionará al acbar de ejecutar cada opcion 
                    menu_combustible = True
                    while menu_combustible == True:
                        print("\n--MENU DE VENTA--")
                        print("+-----+-----------------+")
                        print("| NO  | OPCION          |")
                        print("+-----+-----------------+")
                        print("|  1  |  DIESEL         |")
                        print("|  2  |  SUPER          |")  
                        print("|  3  |  REGULAR        |")
                        print("+-----+-----------------+")
                        print("|  4  |  SALIR DEL MENU |")
                        print("+-----+-----------------+\n")
                        
                        #Solicito al usuario que ingrese el numero de la opcion que desea realizar
                        venta=input("¿Que tipo de combustible deseas vender? NO:")

                        # Al ingresar el numero 1, se venderá diesel
                        if venta == "1":
                            #llamando la funcion del menu de venta con los argumentos: diesel, presio de diesel
                            diesel= menu_de_venta(diesel,presio_diesel)

                        #al ingresar el numero 2, se vendrá super
                        elif venta == "2":
                            # llamando a la funcion del menu de ve venta con los argumentos: super y presio de super
                            super= menu_de_venta(super,presio_super) 

                        # Al ingresar el numero 3, se venderá  regular                                                                                                                                   
                        elif venta =="3":
                           #llamando a la funcion del menuu de ventas con los argumentos: regular y presio de regular
                            regular= menu_de_venta(regular, presio_regular)

                        # Al ingresar el numero 4, se mostrara el menu de salida
                        elif venta == "4":
                            #llamando a la funcion de menu de salir
                            menu_combustible = menu_salida()
                        #si ingresa alguan opcion incorrecta se pide que intente de nuevo
                        else:
                            print("No ha escojido una opcion valida, por favor vuelve a intentar\n")
                        

                # Si el usuario ingresa el numero 2, se mostraran los saldos de que se tienen de gasolina
                elif opcion =="2":
                    #muestra en pantalla los saldos
                    print("\nLos Saldos son:\n")
                    print(f"Super: {super} GALONES ")
                    print(f"Regular: {regular} GALONES ")
                    print(f"Diesel: {diesel} GALONES\n")

                # Si el usuario ingresa el numero, se mostrará el menu salida 
                elif opcion == "3":
                   #En el menu se pregunta si el usuario desea salir o se arrepintio, de salirse
                   #el valor devuelto se almacenará en la variable menu_principal
                   menu_principal= menu_salida()
                else:
                    #si el usuario se equivocó o no colocó lo que se esperaba se regresara al menu principal
                    print("Opción incorrecta, por favor intente de nuevo")
                    continue

            # Al finalizar se asigna el valor de 6 a la variable contador, asi ya no se ejecuta el while de
            # incio de sesión
            contador = 6
        else:
            #si el usuario ingresa un usuario o contraseña incorrecto, se le indica el error
            # y se le pide que vuelva intentar
            print("Nombre o contraseña incorrecto por favor vuelve a intenar.")

            #se le suma 1 al valor de l contador
            contador +=1
            #se muestran en pantalla los intentos que le hacen falta
            print(f"Te quedan {5-contador} intentos\n")

    #se muestra en pantalla el final de programa
    print("FIN DEL PROGRAMA")   


if __name__=='__main__':
    #se llama a la funcioón principal
    run()   