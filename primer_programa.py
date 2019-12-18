import random

def adivinaNum():
    global guess
    for i in range(1, 4):
        print('Deduce el número: ')

        guess = int(input('Escribe un nº del 1 al 20: '))

        if guess < numSecreto:
            print('El nº a adivinar es mayor...')

        elif guess > numSecreto:
            print('El nº a adivinar es menor...')

        else:
            break

def comprobar(guess, numSecreto):
    if guess == numSecreto:
        print('Has acertado!')

    else:
        print('Lo siento, el número era '+str(numSecreto))

numSecreto = random.randint(1, 20)
print('Pensando en el número...')

adivinaNum()

comprobar(guess, numSecreto)
