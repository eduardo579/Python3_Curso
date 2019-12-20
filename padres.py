class Padre:
    atributo = 100

    def __init__(self):
        print('Llamando al constructor Padre')

    def PadreMethod(self):
        print('Llamando al método Padre')

    def setAttrib(self, attr):
        Padre.atributo = attr

    def getAttrib(self):
        print('Atributo del Padre: ' + str(Padre.atributo))

class Hijo(Padre):
    def __init__(self):
        print('Llamando al constructor Hijo')
    
    def HijoMethod(self):
        print('Llamando al método Hijo')

c = Hijo()
c.HijoMethod()
c.PadreMethod()
c.setAttrib(300)
c.getAttrib()