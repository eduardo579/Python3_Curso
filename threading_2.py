import threading
import time

banderaSalida = 0

class miHilo(threading.Thread):
    def __init__(self, hiloID, nombre, cont):
        threading.Thread.__init__(self)
        self.hiloID = hiloID
        self.nombre = nombre
        self.cont = cont
    
    def run(self):
        print("Empezando " + self.nombre)
        threadLock.acquire()
        imprimir_tiempo(self.nombre, self.cont, 3)
        threadLock.release()

def imprimir_tiempo(hiloNombre, delay, cont):
    while cont:
        time.sleep(delay)
        print("%s: %s" % (hiloNombre, time.ctime(time.time())))
        cont -= 1

threadLock = threading.Lock()
hilos = []

hilo1 = miHilo(1, "Hilo-1", 1)
hilo2 = miHilo(2, "Hilo-2", 2)

hilo1.start()
hilo2.start()

hilos.append(hilo1)
hilos.append(hilo2)

for t in hilos:
    t.join()

print("Saliendo del loop principal")