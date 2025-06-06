

#while True:
#    try:
#        num=int(input("ingrese un numero "))
#        break
#    except Exception:
#        print("Solo puede ingresar numeros enteros ")
#print("Su numero es", num)




while True:
    try:
        opcion=int(input(''' Carrito de compras
                         Selecione una opcion 
                         1.-comprar frutas
                         2.-comprar verduras
                         3.-pagar
                         4.-Salir
                         '''))
        match opcion:
            case 1:
                while True:
                    try:
                        opcion=int(input('''
                                        Selecione una opcion 
                                        1.-Frutillas $1500
                                        2.-Pera $1200
                                        3.-Manzana $1300
                                        4.-Volver al menu
                                        '''))
                        match opcion:
                            case 1:
                                print("Has selecciona las frutilas")
                                total+=1500
                                cantArt=+1
                            case 2:
                                print("Has selecciona las peras")
                                total+=1200
                                cantArt=+1
                            case 3:
                                 print("Has selecciona las manzanas")
                                 total+=1300
                                 cantArt=+1
                            case 4:
                                print("Saliendo...")
                                break
                            case _:
                                print("Opcion invalida")
                    except Exception:
                        print("Solo puede ingresar numeros enteros:")
            case 2:
                print("Has seleccionado la opcion 2")
            case 3:
                print("Has seleccionado la opcion 3")
            case 4:
                print("Saliendo...")
                break
            case _:
                print("Opcion invalida")
    except Exception:
        print("Solo puede ingresar numeros enteros:")



total=0
cantArt=0
