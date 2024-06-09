from Stark_funciones import *

salir = True
  

while salir:
    print("           Bienvenido")
    print("1. SuperHeroes")
    print("2. SuperHeroes y alturas")
    print("3. SuperHeroe mas alto")
    print("4. SuperHeroe mas bajo")
    print("5. Promedio de alturas")
    print("6. SuperHeroe mas pesado")
    print("7. SuperHeroe menos pesado")
    print("8. Salir")
    print("9. Mas opciones")
    enter()
    salir2 = True
    opciones = validar_entrada(1,9)
    enter()

    match opciones:
        case 1:
            mostar_superheroes(lista_personajes)
            enter()
            continuar()
            limpiar_terminal()
        
        case 2:
            mostar_superheroes_altura(lista_personajes)
            enter()
            continuar()
            limpiar_terminal()

        case 3:
            print(superheroe_ALTO(alturas))
            enter()
            continuar()
            limpiar_terminal()
        
        case 4:
            print(superheroe_BAJO(alturas))
            enter()
            continuar()
            limpiar_terminal()

        case 5:
            print(f"El promedio de alturas es {calcular_promedio(alturas)}")
            enter()
            continuar()
            limpiar_terminal()

        case 6:
            print(f"{superheroe_pesasdo(pesos)}")
            enter()
            continuar()
            limpiar_terminal()

        case 7:
            print(f"{superheroe_liviano(pesos)}")
            enter()
            continuar()
            limpiar_terminal()
        case 8:
            abandonar = True
            while abandonar:
                salir= input("Desea abandonar? y/n: ")
                salir = salir.lower()
                if salir != "y" and salir != "n":
                    enter()
                    print("ERROR: No se ha seleccionado una opción válida (y/n)")
                    enter()
                elif salir.lower() == "n":
                    print("¡Gracias por quedarse!")
                    enter()
                    continuar()
                    limpiar_terminal()
                    abandonar = False
                else:
                    print("Cerrando")
                    for _ in range(3):
                        print(".")
                        sleep(1)
                    abandonar = False
                    salir = False


        case 9:
            while salir2:
                limpiar_terminal()
                print("1. SuperHeroes F")
                print("2. SuperHeroes M")
                print("3. Color de ojos")
                print("4. Color de peolo")
                print("5. Tipo de inteligencia")
                print("6. Agrupor SuperHeroes por tipo")
                print("7. Volver")
                enter()
                salir3 = True
                salir4 = True
                salir5 = True
                opciones = validar_entrada(1,7)
                enter()

                match opciones:
                    case 1:
                        while salir3:
                            limpiar_terminal()
                            print("1. Mostrar SuperHeroes F")
                            print("2. SuperHeroes F mas alta")
                            print("3. SuperHeroes F mas baja")
                            print("4. Promedio de altura")
                            print("5. Volver")
                            enter()
                            opciones = validar_entrada(1,5)
                            enter()
                            match opciones:
                                case 1:
                                    limpiar_terminal()
                                    nombres =mostar_superheroes_genero(lista_personajes,"F")
                                    for el in nombres:
                                        print(el['nombre'])
                                    enter()
                                    continuar()
                                case 2:
                                    limpiar_terminal()
                                    print(superheroe_ALTO(F))
                                    enter()
                                    continuar()
                                case 3:
                                    limpiar_terminal()
                                    print(superheroe_BAJO(F))
                                    enter()
                                    continuar()
                                case 4:
                                    limpiar_terminal()
                                    print(f"El promedio de altura de los SuperHeroes de genero Femenino es {calcular_promedio(F)} cm")
                                    enter()
                                    continuar()
                                case 5:
                                    salir3 = False
                                    limpiar_terminal()

                    case 2:
                        while salir4:
                            limpiar_terminal()
                            print("1. Mostrar SuperHeroes M")
                            print("2. SuperHeroes M mas alta")
                            print("3. SuperHeroes M mas baja")
                            print("4. Promedio de altura")
                            print("5. Volver")
                            enter()
                            opciones = validar_entrada(1,5)
                            enter()

                            match opciones:
                                case 1:
                                    limpiar_terminal()
                                    nombres =mostar_superheroes_genero(lista_personajes,"M")
                                    for el in nombres:
                                        print(el['nombre'])
                                    enter()
                                    continuar()
                                case 2:
                                    limpiar_terminal()
                                    print(superheroe_ALTO(M))
                                    enter()
                                    continuar()
                                case 3:
                                    limpiar_terminal()
                                    print(superheroe_BAJO(M))
                                    enter()
                                    continuar()
                                case 4:
                                    limpiar_terminal()
                                    print(f"El promedio de altura de los SuperHeroes de genero Femenino es {calcular_promedio(M)} cm")
                                    enter()
                                    continuar()
                                case 5:
                                    salir4 = False
                                    limpiar_terminal()
                    
                    case 3:
                        limpiar_terminal()
                        mostrar_elemento(colores_unicos,colores_ojos)
                        continuar()
                        enter()
                    case 4:
                        limpiar_terminal()
                        mostrar_elemento(colores_pelo_unicos,colores_pelo)
                        continuar()
                        enter()
                    case 5:
                        limpiar_terminal()
                        mostrar_elemento(inteligencia_unica,inteligencia)
                        continuar()
                        enter()
                    case 7:
                        salir2 = False
                        limpiar_terminal()
                    case 6:
                        while salir5:
                            limpiar_terminal()
                            print("1. color de ojos")
                            print("2. color de pelo")
                            print("3. tipo de inteligencia")
                            print("4. volver")
                            enter()
                            opciones = validar_entrada(1,4)
                            enter()

                            match opciones:
                                case 1:
                                    limpiar_terminal()
                                    mostrar_tipo('color_ojos')
                                    continuar()
                                    enter()
                                case 2:
                                    limpiar_terminal()
                                    mostrar_tipo('color_pelo')
                                    continuar()
                                    enter()
                                case 3:
                                    limpiar_terminal()
                                    mostrar_tipo('inteligencia')
                                    continuar()
                                    enter()
                                case 4:
                                    salir5 = False
                                    limpiar_terminal()
                    
