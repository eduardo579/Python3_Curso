class Empleados:
    cont = 0

    def __init__(self, nombre, email, edad):
        self.nombre = nombre
        self.email = email
        self.edad = edad
        Empleados.cont += 1
    
    def enseñaCont(self):
        print('El total de empleados es: '+str(Empleados.cont))

    def enseñaInfo(self):
        print('Nombre: '+self.nombre, '- E-mail: '+self.email, '- Edad: '+str(self.edad))

empleado1 = Empleados('Manolo', 'hola@manolo.com', 23)
empleado2 = Empleados('Laura', 'hola@laura.com', 24)

empleado1.enseñaInfo()
empleado1.enseñaCont()

empleado1.email = 'Cambiado@gmail.com'

empleado1.enseñaInfo()