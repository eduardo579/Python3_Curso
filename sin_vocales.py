def remover_vocales(stringInicial, frase):
    vocales = ('a', 'e', 'i', 'o', 'u')

    for i in frase.lower():
        if i in vocales:
            stringInicial = stringInicial.replace(i, '')
    return stringInicial

stringVocales = input('Escribe una frase cualquiera (x para salir): ')

if stringVocales == 'x':
    exit()

else:
    nuevoString = stringVocales
    print('Removiendo las vocales...')

    nuevoString = remover_vocales(nuevoString, stringVocales)

    print('La nueva frase es: '+nuevoString)
