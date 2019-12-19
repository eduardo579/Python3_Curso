def mirar_grande(num1, num2, num3):
    global masLargo
    masLargo = num1

    if masLargo < num2:
        if num2 > num3:
            masLargo = num2
        
        else:
            masLargo = num3
    
    elif masLargo < num3:
        if num3 > num2:
            masLargo = num3

        else:
            masLargo = num2
    
    else:
        masLargo = num1

cont = 1

print('Escribe tres números (x para salir): ')

num1 = input('Primer nº: ')

if num1 == 'x':
    exit()

else:
    num1 = int(num1)
    num2 = int(input('Segundo nº: '))
    num3 = int(input('Tercer nº: '))

    mirar_grande(num1, num2, num3)

    if num1 == num2 and num1 == num3:
        cont = 0
    
    if cont == 0:
        print('Los tres números son iguales')
    
    else:
        print('El más grande de los nºs es: '+str(masLargo))