import threading
import queue
import time

banderaSalida = 0

class miHilo(threading.Thread):
    def __init__(self, hiloID, nombre, q):
        threading.Thread.__init__(self)
        self.hiloID = hiloID
        self.nombre = nombre
        self.q = q
    
    def run(self):
        print("Empezando " + self.nombre)
        process_data(self.nombre, self.q)
        print("Saliendo " + self.nombre)

def process_data(hiloNombre, q):
    while not banderaSalida:
        queueLock.acquire()

        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print("%s procesando %s" % (hiloNombre, data))
        
        else:
            queueLock.release()
            time.sleep(1)


hiloLista = ["Hilo_1", "Hilo_2", "Hilo_3"]
nombreLista = ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]

queueLock = threading.Lock()
workQueue = queue.Queue(10)

hilos = []

hiloID = 1

for tNombre in hiloLista:
    hilo = miHilo(hiloID, tNombre, workQueue)
    hilo.start()
    hilos.append(hilo)
    hiloID += 1

queueLock.acquire()

for palabra in nombreLista:
    workQueue.put(palabra)

queueLock.release()

while not workQueue.empty():
    pass

banderaSalida = 1

for t in hilos:
    t.join()

print("Saliendo del loop principal")