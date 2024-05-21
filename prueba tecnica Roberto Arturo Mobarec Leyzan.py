def funcion1():
    texto1 = "Hola"
    texto2 = "Mundo"
    
    conteoTexto1 = 0
    conteoTexto2 = 0
    conteoTexto1y2 = 0
    conteoNumero = 0
    numerosEnPantalla = []

    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(texto1 + texto2)
            conteoTexto1y2 += 1
        elif i % 3 == 0:
            print(texto1)
            conteoTexto1 += 1
        elif i % 5 == 0:
            print(texto2)
            conteoTexto2 += 1
        else:
            print(i)
            conteoNumero += 1
            numerosEnPantalla.append(i)

    print(f"{texto1} se mostro en pantalla {conteoTexto1} veces")
    print(f"{texto2} se mostro en pantalla {conteoTexto2} veces")
    print(f"{texto1} {texto2} se mostro en pantalla {conteoTexto1y2} veces")
    
    return numerosEnPantalla

def InversionLetras(texto1, texto2, numerosEnPantalla):
    vector1 = list(texto1)
    vector2 = list(texto2)

    vector1.reverse()
    vector2.reverse()

    for numero in numerosEnPantalla:
        if numero <= len(vector1):
            print(f"Letra de la palabra {texto1} ocupa {numero} lugar en el vector: {vector1[numero - 1]}")
        if numero <= len(vector2):
            print(f"Letra de la palabra {texto2} ocupa {numero} lugar en el vector: {vector2[numero - 1]}")

numeros = funcion1()
InversionLetras("Hola", "Mundo", numeros)