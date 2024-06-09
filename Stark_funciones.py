from FUNCIONES_DEF import *
from data_stark import *
from time import sleep


#B  
def mostar_superheroes(lista_personajes:list)->None:
    lista_nombres = mapear_campo(lista_personajes,'nombre')
    for el in lista_nombres:
        print(el)

# mostar_superheroes(lista_personajes)
# enter()
#C

def mostar_superheroes_altura(lista_personajes:list)->None:
    for elm in lista_personajes:
        print(f"{elm['nombre']}, {float(elm['altura'])} cm")

# mostar_superheroes_altura(lista_personajes)

#D 
def altura(lista_personajes:list)->list:
    alturas = convertir_a_float(mapear_campo(lista_personajes,'altura'))
    return alturas

alturas = altura(lista_personajes)
# enter()

def superheroe_ALTO(alturas:list)->float:
    mayor = str(calcular_mayor_in_lista(alturas))
    nombre_mayor = ""
    for el in lista_personajes:
        if el['altura'] == mayor:
            nombre_mayor = el['nombre']
    return f"El Superhéroe más alto midiendo {mayor} cm es {nombre_mayor}"



#E
def superheroe_BAJO(alturas:list)->float:
    menor = str(calcular_menor_in_lista(alturas))
    nombre_menor = ""
    for el in lista_personajes:
        if el['altura'] == menor:
            nombre_menor = el['nombre']
    return f"El SuperHeroe mas bajo midiendo {menor} cm es {nombre_menor}"
# print(f"El Superheroe mas bajo de la lista mide {superheroe_BAJO(alturas)}")

#F
# enter()

#G
# enter()

#H

def pesos(lista_personajes:list)->list:
    pesos = convertir_a_float(mapear_campo(lista_personajes,'peso'))
    return pesos

pesos = pesos(lista_personajes)

# enter()

def superheroe_pesasdo(pesos:list):
    pesado = str(calcular_mayor_in_lista(pesos))
    nombre_pesado = ""
    for el in lista_personajes:
        if el['peso'] == pesado:
            nombre_pesado = el['nombre']
    return f"El Superhéroe más pesado {pesado} kg es {nombre_pesado}"

def superheroe_liviano(pesos:list):
    liviano = str(calcular_menor_in_lista(pesos))
    nombre_liviano = ""
    for el in lista_personajes:
        if el['peso'] == liviano:
            nombre_liviano = el['nombre']
    return f"El más liviano {liviano} kg es {nombre_liviano}"

#menu_superheroes
#     print("           Bienvenido")
#     num_1 = print("1. SuperHeroes")
#     num_2 = print("2. SuperHeroes y alturas")
#     num_3 = print("3. SuperHeroe mas alto")
#     num_4 = print("4. SuperHeroe mas bajo")
#     num_5 = print("5. Promedio de alturas")
#     num_6 = print("6. SuperHeroe mas pesado")
#     num_7 = print("6. SuperHeroe menos pesado")


def mostar_superheroes_genero(lista_personajes:list, genero:str):
    generos = genero
    filtradora = lambda a: a['genero'] == generos
    return filtrar_lista(filtradora, lista_personajes)


# nombres =mostar_superheroes_genero(lista_personajes,"F")
# for el in nombres:
#     print(el['nombre'])


def lista_genero(genero:str,lista_personajes:list):
    aux = []
    for el in lista_personajes:
        if el['genero'] == genero:
            aux.append(el)
    return aux

F = lista_genero("F",lista_personajes)
M = lista_genero("M",lista_personajes)

F = altura(F)
M = altura(M)

# print(superheroe_ALTO(F))
# enter()
# print(superheroe_ALTO(M))
# enter()
# print(superheroe_BAJO(F))
# enter()
# print(superheroe_BAJO(M))
# enter()

# print(f"El promedio de altura de los SuperHeroes de genero Femenino es {calcular_promedio(F)} cm")
# enter()
# print(f"El promedio de altura de los SuperHeroes de genero Masculino es {calcular_promedio(M)} cm")

# enter()


def no_elementos_repetidos(lista:list):
    elementos_sin_repetir = []
    for i in range(len(lista)):
        elemento = lista[i]
        repetido = False
        for j in range(i):
            if lista[j] == elemento:
                repetido = True
                break
        if not repetido:
             elementos_sin_repetir.append(elemento)
    return  elementos_sin_repetir



def contador_elementos(lista: list, posicion: int):
    elemento_buscar = lista[posicion]  
    contador = 0
    for el in lista:
        if el == elemento_buscar:
            contador += 1
    return contador

def mostrar_elemento(lista:list,campo:str):
    contador = 0
    for el in lista:
        if el == "":
            print(f"{contador}. No tiene. Cantidad: {contador_elementos(campo,contador)}")
            contador += 1
        else:
            print(f"{contador}. {el}. Cantidad: {contador_elementos(campo,contador)}")
            contador += 1

def contador_elementos(lista: list, posicion: int):
    unicos = no_elementos_repetidos(lista)
    elemento_buscar = unicos[posicion]  
    contador = 0
    for el in lista:
        if el == elemento_buscar:
            contador += 1
    return contador

colores_ojos = mapear_campo(lista_personajes,'color_ojos')
# print(colores_ojos)

colores_unicos = no_elementos_repetidos(colores_ojos)

# mostrar_elemento(colores_unicos,colores_ojos)

# enter()

colores_pelo = mapear_campo(lista_personajes,'color_pelo')
# print(colores_pelo)

colores_pelo_unicos = no_elementos_repetidos(colores_pelo)

# mostrar_elemento(colores_pelo_unicos,colores_pelo)

# enter()

inteligencia = mapear_campo(lista_personajes,'inteligencia')
# print(inteligencia)
inteligencia_unica = no_elementos_repetidos(inteligencia)

# mostrar_elemento(inteligencia_unica,inteligencia)

elemento = 'color_ojos'
def agrupar_por_elementos(lista_elementos: list, elemento: str) -> list:
    valores_unicos = no_elementos_repetidos(mapear_campo(lista_elementos, elemento))
    resultado = []
    for valor_unico in valores_unicos:
        elementos_con_nombre = []
        for diccionario in lista_elementos:
            if diccionario.get(elemento) == valor_unico:
                elementos_con_nombre.append(diccionario['nombre'])
        resultado.append({elemento: valor_unico, 'nombre': elementos_con_nombre})
    return resultado
    
# aux = (agrupar_por_elementos(lista_personajes,elemento))

# for el in aux:
#     print(el)




# aux = (agrupar_por_elementos(lista_personajes,'inteligencia'))
# for el in aux:
#     None

# print(el.keys())


def mostrar_tipo(tipo:str):
    aux = (agrupar_por_elementos(lista_personajes,tipo))
    for el in aux:
        if el[tipo] == "":
            print(f"no tiene , {el['nombre']}")
        else:
            print(f"{el[tipo]} , {el['nombre']}")

def validar_entrada(rango_min, rango_max):
    while True:
        aux = input("Opcion: ")
        if aux == "":
            enter()
            print("ERROR: No se ha ingresado ninguna opción")
            enter()
        elif aux.isalpha():
            enter()
            print("ERROR: Se esperaba un entero")
            enter()
        elif not aux.isdigit() or int(aux) < rango_min or int(aux) > rango_max:
            enter()
            print(f"ERROR: Seleccione una de las opciones ({rango_min}-{rango_max})")
            enter()
        else:
            return int(aux)