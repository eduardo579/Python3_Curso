class Estudiantes:
    cont = 0

    def __init__(self, nombre, apellido, asignatura, nota):
        self.nombre = nombre
        self.apellido = apellido
        self.asignatura = asignatura
        self.nota = nota
        Estudiantes.cont += 1

    def enseñaEstiduantes(self):
        print('El total de estudiantes del centro es %d' % (Estudiantes.cont))

    def enseñaInfo(self):
        print('Nombre: ' + self.nombre + '\n' + 'Apellido: ' + self.apellido + '\n' + 'Asignatura: ' + self.asignatura + '\n' + 'Nota: ' + self.nota)


print('Uso...\nq -- Cierra el programa\nañadir -- Añadir estudiante\nenseña -- Muestra la info del estudiante\nconteo -- Muestra el nº de estudiantes en total')
while True:
    opcion = input('Escribe la opción deseada: ')

    if opcion == 'q':
        break

    elif opcion == 'añadir':
        nombre_usu = input('Escribe el nombre del estudiante: ')
        apellido_usu = input('Escribe el apellido del estudiante: ')
        asignatura_usu = input('Escribe la asignatura del estudiante: ')
        nota_usu = input('Escribe la nota del estudiante: ')

        estudiante = Estudiantes(nombre_usu, apellido_usu, asignatura_usu, nota_usu)

    elif opcion == 'enseña':
        estudiante.enseñaInfo()
        
    elif opcion == 'conteo':
        print('El total de estudiantes es: %d' % (Estudiantes.cont))