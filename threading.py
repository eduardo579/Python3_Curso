import _thread
import time

def imprimirTiempo(nombreHilo, delay):
    cont = 0

    while cont < 5:
        time.sleep(delay)
        cont += 1
        print("%s: %s" % (nombreHilo, time.ctime(time.time())))


try:
    _thread.start_new_thread(imprimirTiempo, ("Hilo_1", 2, ))
    _thread.start_new_thread(imprimirTiempo, ("Hilo_2", 4, ))

except:
    print("Error al empezar")

while True:
    pass