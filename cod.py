from math import sqrt
import math

print("\t\tPráctica 1: Ubicar un punto en el plano cartesiano\n")

print("Como instruciones debe ingresar primero el radio de la circunferencia, luego de esto ingrese las coordenadas del centro de circunferencia para que asi en el ultimo paso ingrese el punto que desea ubicar en la circunferencia.\n")

#Variables

radio = float(input("Por favor ingrese el radio de la circunferencia\n"))

x1 = float(input("Por favor ingrese el valor del punto centro en el eje X\n"))

y1 = float(input("Por favor ingrese el valor del punto centro en el eje Y\n"))

x2 = float(input("Por favor ingrese el valor para el punto de X\n"))

y2 = float(input("Por favor ingrese el valor para el punto de Y\n"))


#Funcionamiento para indicar area del punto dado

if x2 > 0 and y2 > 0:
      print("El punto se encuentra en el primer cuadrante del plano cartesiano")
if x2 < 0 and y2 > 0:
      print("El punto se encuentra en el segundo cuadrante del plano cartesiano")
if x2 < 0 and y2 < 0:
      print("El punto se encuentra en el tercer cuadrante del plano cartesiano")
if x2 > 0 and y2 < 0:
      print("El punto se encuentra en el cuarto cuadrante del plano cartesiano")
if x2 == 0 and y2 == 0:
      print("El punto se encuentra en el origen del plano cartesiano")
if x2 == 0:
      print("El punto se encuentra en el eje Y del plano cartesiano")
if y2 == 0:
      print("El punto se encuentra en el eje X del plano cartesiano")

if x2 == y2:
      print("El punto se encuentra en la línea X = Y")
if x2 > y2:
      print("El punto se encuentra por debajo de la línea X = Y")
else:
      print("El punto se encuentra por encima de la línea X = Y")


distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)


#Calcular distancia del punto hasta el centro
if distancia < radio:
    print("El punto está dentro de la circunferencia")
elif distancia == radio:
    print("El punto está en la circunferencia")
else:
    print("El punto está fuera de la circunferencia")



circunf = round((radio * 2 * math.pi), 1)

print("El resultado de la circunferencia es ", circunf, " y su distancia es ", radio)