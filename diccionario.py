examen_notas = {'Jake': 'A', 'Jack': 'D', 'Adam': 'F'}

print('Escribe el nombre de la persona a revisar: ')

persona = input('Nombre: ')

if persona == None:
    exit()

if persona in examen_notas:
    print('La marca de ' + persona + ' es ' + examen_notas[persona])

else:
    print('No está en la lista...')