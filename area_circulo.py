def calcularRadio(rad):
    radius = float(rad)
    area = 3.14 * radius * radius
    print('El area del círculo es: '+str(area))

while True:
    rad = input('Escribe radios de círculos: (x para cerrar el programa)')

    if rad == 'x':
        break
    
    calcularRadio(rad)