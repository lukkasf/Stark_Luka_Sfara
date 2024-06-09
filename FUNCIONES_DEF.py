import os
from decimal import Decimal
#                VALIDADORAS

def validar_lista(lista:list)->bool:
    if not isinstance(lista,list):
        raise TypeError("ERROR:Se esperaba una lista")
    return True

def validar_entero(entero:int)->bool:
    if not isinstance(entero,int):
        raise(TypeError("ERROR:Se esperaba un entero"))
    return True
    
def validar_lista_no_vacia(lista:list)->bool:
    if not len(lista) == 0:
        raise(ValueError("ERROR:La lista NO esta vacia"))
    return True

def validar_lista_vacia(lista:list)->bool:
    if not len(lista) > 0:
        raise(ValueError("ERROR:La lista esta vacia"))
    return True

def validar_bool(valor:bool)->bool:
    if not isinstance(valor,bool):
        raise(TypeError("ERROR:Se esperaba un Bool"))
    
#--------------------------------------------------------------------------
#                         LISTAS
def mostrar_lista(lista:list)->None:
    for el in lista:
        print(el,end=" ")
    print()

def filtrar_lista(filtradora, lista:list)-> list:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            aux = []
            for ele in lista:
                if filtradora(ele):
                    aux.append(ele)
            return aux

def swapeadora_de_listas(parametro, lista:list)->None:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            tam = len(lista)
            for i in range (tam-1):
                for j in range (i+1, tam):
                    if parametro(lista[i], lista[j]):
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

def cargar_lista_enteros_random(lista:list, cantidad:int, desde:int, hasta:int)-> None:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            if validar_entero(cantidad, desde, hasta):
                from random import randint
                for _ in range(cantidad):
                    lista.append(randint(desde,hasta))

def crear_lista_enteros_random(cant:int, desde:int, hasta:int)-> list:
    validar_entero(cant, desde, hasta)
    lista = []
    cargar_lista_enteros_random(lista,cant,desde,hasta)
    return lista

def mapear_lista(procesadora, lista:list) -> list:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            lista_retorno = []
            for el in lista:
                lista_retorno.append(procesadora(el))
            return lista_retorno
    
def totalizar_lista(lista:list)-> int:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            total = 0
            for elem in lista:
                total += elem
            return total

def calcular_promedio(lista:list)->int:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            promedio = totalizar_lista(lista) / len(lista)
            return promedio

def calcular_mayor_in_lista(lista:list)->float:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            elemento_mayor = lista[0]
            for elm in lista:
                if elm > elemento_mayor:
                    elemento_mayor = elm
            return elemento_mayor
    
def calcular_menor_in_lista(lista:list)->float:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            elemento_menor = lista[0]
            for elm in lista:
                if elm < elemento_menor:
                    elemento_menor = elm
            return elemento_menor


def entero_in_lista(lista:list, target:int)->bool:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
            if validar_entero(target):
                for elem in lista:
                    if elem == target:
                        return True
                return False
        

   

def buscar_in_lista(lista:int, target:int)->int:
    if validar_lista(lista):
        if validar_lista_vacia(lista):
                    esta = -1
                    for i in range(len(lista)):
                        if lista[i] == target:
                            esta = i
                            break
                    return esta

def contar_in_lista(lista:list, target:int)->int:
    if validar_lista(lista):
        if validar_entero(target):
            if validar_lista_no_vacia(lista):
                contador = 0
                for elem in lista:
                    if elem == target:
                        contador += 1
                return contador
    
def sorteador(lista:list)->None:
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            from random import randint
            i = randint(0, len(lista))
            return i
            
def ordenar_lista_ascendente(lista:list)->None:
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            tam = len(lista)
            for i in range (tam-1):
                for j in range (i+1, tam):
                    if lista[i] > lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

def ordenar_lista_descendente(lista:list)->None:
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            tam = len(lista)
            for i in range (tam-1):
                for j in range (i+1, tam):
                    if lista[i] < lista[j]:
                        aux = lista[i]
                        lista[i] = lista[j]
                        lista[j] = aux

def ordenar_lista(lista:list,tipo:bool)->None:
    if validar_lista(lista):
        if validar_lista_no_vacia(lista):
            if validar_bool(tipo):
                if tipo == True:
                    ordenar_lista_ascendente(lista)
                else:
                    ordenar_lista_descendente(lista)

def promediar_listas(lista_a:list, lista_b:list, lista_promedios:list)-> None:
    if validar_lista(lista_a) and validar_lista(lista_b) and validar_lista(lista_promedios): 
        if validar_lista_no_vacia(lista_a) and validar_lista_no_vacia(lista_b):
            if validar_lista_vacia(lista_promedios) :
                for i in range(len(lista_a)):
                    num_1 = lista_a[i]
                    num_2 = lista_b[i]
                    prom =calcular_promedio(num_1,num_2)
                    lista_promedios.append(prom)

def for_each_lista(funcion,lista)->None:
    nueva_lista = []
    if validar_lista(lista):
        for el in lista:
            nueva_lista.append(funcion(el))
        lista[:] = nueva_lista
            
def reduce_lista(funcion, lista):
    None

def ordenar_lista(criterio, lista:list)-> None:
    pass


def busqueda_binaria(target, lista):
    inf = 0
    sup = len(lista - 1 )
    contador = 1
    while inf <= sup:
        medio = (inf + sup) // 2 
        if lista[medio] == target:
            print(contador)
            return(medio)
        elif target > lista[medio]:
            inf = medio + 1
        else:
            sup = medio - 1

def buscar_binario2(legajo,lista):
    indice = 0
    while indice > len(lista) and lista[indice]['legajo'] != legajo:
        indice += 1 
    if indice ==len(lista):
        return None
    else:
        return indice

def filtrar_lista(filtradora, lista:list)-> list:
    aux = []
    for ele in lista:
        if filtradora(ele):
            aux.append(ele)
    return aux

def mapear_lista(procesadora, lista:list) -> list:
    lista_retorno = []
    for elm in lista:
        lista_retorno.append(procesadora(elm))
    return lista_retorno
        
def mapear_campo(lista:list, campo)->list:
    lista_retorno = []
    for el in lista:
        lista_retorno.append(el[campo])
    return lista_retorno

def continuar():
    input("Presione una tecla para continuar...")

def enter():
    print()

def limpiar_terminal():
    if os.name == 'nt':
        os.system('cls')

def convertir_a_float(lista: list) -> list:
    lista_convertida = []
    for elemento in lista:
        lista_convertida.append(Decimal(elemento))
    return lista_convertida



# lista = [2,4,6,8,32,44,53,128,35]
# for_each_lista(lambda a : a * 2,lista)
# print(lista)

#----------------------------------------------------------------

# numeros = [5,7,8,9,7,5,43]

# # try:
# #     swapeadora_de_listas(lambda a , b : a > b ,lista)
# # except TypeError as e:
# #     print(e)

# # print(lista)

# numeros = [5,7,8,9,7,5,43]

# lista = mapear_lista(lambda impares : impares * 2, filtrar_lista(lambda n : n % 2 != 0, numeros))

# print(lista)
