print('1. suma | 2. resta | 3. multiplicación | 4. división | 5. salir')

def suma(numero1, numero2):
    resultado = numero1 + numero2
    print('El resultado es: '+str(resultado))

def resta(numero1, numero2):
    resultado = numero1 - numero2
    print('El resultado es: '+str(resultado))

def multi(numero1, numero2):
    resultado = numero1 * numero2
    print('El resultado es: '+str(resultado))

def divi(numero1, numero2):
    resultado = numero1 / numero2
    print('El resultado es: '+str(resultado))

while True:
    elegir = int(input('Selecciona la opción: '))

    if elegir >= 1 and elegir <= 4:
        print('Escribe los números: ')

        num1 = int(input('Nº 1: '))
        num2 = int(input('Nº 2: '))

        if elegir == 1:
            suma(num1, num2)

        elif elegir == 2:
            resta(num1, num2)

        elif elegir == 3:
            multi(num1, num2)

        else:
            divi(num1, num2)
    
    elif elegir == 5:
        break

    else:
        print('No es una opción válida')

