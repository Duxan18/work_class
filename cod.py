from math import sqrt
import math

print("\t\tPráctica 1: Ubicar un punto en el plano cartesiano\n")

x = float(input("Por favor ingrese el valor de X\n"))

y = float(input("Por favor ingrese el valor de Y\n"))

if x > 0 and y > 0:
      print("El punto se encuentra en el primer cuadrante del plano cartesiano")
if x < 0 and y > 0:
      print("El punto se encuentra en el segundo cuadrante del plano cartesiano")
if x < 0 and y < 0:
      print("El punto se encuentra en el tercer cuadrante del plano cartesiano")
if x > 0 and y < 0:
      print("El punto se encuentra en el cuarto cuadrante del plano cartesiano")
if x == 0 and y == 0:
      print("El punto se encuentra en el origen del plano cartesiano")
if x == 0:
      print("El punto se encuentra en el eje Y del plano cartesiano")
if y == 0:
      print("El punto se encuentra en el eje X del plano cartesiano")

if x == y:
      print("El punto se encuentra en la línea X = Y")
if x > y:
      print("El punto se encuentra por debajo de la línea X = Y")
else:
      print("El punto se encuentra por encima de la línea X = Y")

if x == -y:
      print("El punto se encuentra en la línea X = -Y")
if x > -y:
      print("El punto se encuentra por debajo de la línea X = -Y")
else:
      print("El punto se encuentra por encima de la línea X = -Y")

v_x = int(x**2)
v_y = int(y**2)

resultado = v_x + v_y

r_sqrt = round(sqrt(resultado), 1)

cir = round((r_sqrt * math.pi), 1)

print("El resultado de la circunferencia es ", cir, " y su distancia es ", r_sqrt)