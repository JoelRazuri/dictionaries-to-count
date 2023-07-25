"""
    Diccionarios usados para contar.
        a) Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad
        de apariciones de cada palabra en la cadena. Por ejemplo, si recibe ”Qué lindo día que
        hace hoy” debe devolver: { 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1}.
        b) Escribir una función que cuente la cantidad de apariciones de cada caracter en una cadena de texto, y los devuelva en un diccionario.
        c) Escribir una función que reciba una cantidad de iteraciones de una tirada de 2 dados a realizar y devuelva la cantidad de veces que 
        se observa cada valor de la suma de los dos dados.
        Nota: utilizar el módulo random para obtener tiradas aleatorias.
"""


def palabras_repetidas(cadena):

    diccionario = {}
    a,b = 'áéíóúü','aeiouu'
    cambio = str.maketrans(a,b)
    lista_palabras = ((cadena.translate(cambio)).lower()).split()
    

    for palabra in lista_palabras:

        if not diccionario:
            contador = 1
    
        if palabra in diccionario:
            contador = diccionario[palabra] + 1
        else:
            contador = 1

        diccionario[palabra] = contador

    return diccionario

# print(palabras_repetidas("Qué lindo día que hace hoy"))



def letras_repetidas(cadena):

    diccionario = {}
    a,b = 'áéíóúü','aeiouu'
    cambio = str.maketrans(a,b)
    cadena = (cadena.translate(cambio)).lower()
    

    for letra in cadena:

        if not diccionario:
            contador = 1

        if letra in diccionario:
            contador = diccionario[letra] + 1
        else:
            contador = 1

        diccionario[letra] = contador

    return diccionario


print(letras_repetidas("Qué lindo día que hace hoy"))