#Ejercicio 21: Fusionar dos listas enlazadas ordenadas.
class Nodo:
    def __init__(self, valor):
        self.valor = valor    #valor del nodo
        self.siguiente = None #sig nodo

def crear_lista_enlazada(lista):
    if not lista:  #si la lista está vacía no se crea nada
        return None

    primer_nodo = Nodo(lista[0])  #se crea el primer nodo
    actual = primer_nodo          #empieza desde el primer nodo

    for numero in lista[1:]:      #recorre los demás num
        actual.siguiente = Nodo(numero)  #se crea el sig nodo
        actual = actual.siguiente        #se mueve al nuevo nodo

    return primer_nodo  #retorna el primer nodo de la lista enlazada

def fusionar_listas(nodo1, nodo2):
    #si alguna de las listas está vacía, devolvemos la otra
    if not nodo1:
        return nodo2
    if not nodo2:
        return nodo1
    if not nodo1 and not nodo2:
        return None


    if nodo1.valor < nodo2.valor:   #comparamos los valores de los nodos
        resultado = nodo1
        resultado.siguiente = fusionar_listas(nodo1.siguiente, nodo2)  #se va creando la lista fusionada
    else:
        resultado = nodo2
        resultado.siguiente = fusionar_listas(nodo1, nodo2.siguiente)

    return resultado

def mostrar_lista(nodo):
    resultado = []
    while nodo:
        resultado.append(nodo.valor)
        nodo = nodo.siguiente
    print(resultado)


#Caso de uso
lista1 = [1, 2, 4]
lista2 = [1, 3, 4]

#se crean listas enlazadas a partir de las listas comunes
nodo1 = crear_lista_enlazada(lista1)
nodo2 = crear_lista_enlazada(lista2)

#se fusionan las listas
lista_fusionada = fusionar_listas(nodo1, nodo2)

mostrar_lista(lista_fusionada)
