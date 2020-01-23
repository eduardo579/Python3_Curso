""" calcularemos cuanto gasta un coche, 
si el mismo cada 100km consume 5,5 litros. 
Resulta que mi trabajo de mi casa se encuentra a 15 kilómetros. 
¿Cuanto gastare en gasolina durante 20 días si el precio es 1,02€/l?"""

kilomsRecorridos = 20 * 15

print("Los kms que recorres son: "+str(kilomsRecorridos))

gastoGasolina = float((kilomsRecorridos * 5.5) / 100)

print("El gasto en gasolina es de: "+str(gastoGasolina)+" litros")

precioFinal = float(gastoGasolina * 1.02)

print("El coste de los trayectos es de: "+str(precioFinal)+" €")
