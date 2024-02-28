from math import sqrt, pi

print("\t\tPráctica 1: Ubicar un punto en el plano cartesiano\n")

print("Como instrucciones, primero ingrese el radio de la circunferencia. Luego, ingrese las coordenadas del centro de la circunferencia. En el último paso, ingrese las coordenadas del punto que desea ubicar en la circunferencia.\n")

# Variables
radio = float(input("Por favor ingrese el radio de la circunferencia: "))

x1 = 0
y1 = 0

x2 = float(input("Por favor ingrese el valor para la coordenada X del punto: "))
y2 = float(input("Por favor ingrese el valor para la coordenada Y del punto: "))

options = ["1. Plano Cartesiano", "2. Triángulo", "3. Cancelar"]

print("\nSeleccione una opción:\n")
for opcion in options:
    print(opcion)

option_el = input("\nIngrese el número de la opción que desea: ")

if option_el == "1":
    print("\nEjecutando código para la Opción 1...")

    # Funcionamiento para indicar área del punto dado
    if x2 > 0 and y2 > 0:
        print("El punto se encuentra en el primer cuadrante del plano cartesiano.")
    elif x2 < 0 and y2 > 0:
        print("El punto se encuentra en el segundo cuadrante del plano cartesiano.")
    elif x2 < 0 and y2 < 0:
        print("El punto se encuentra en el tercer cuadrante del plano cartesiano.")
    elif x2 > 0 and y2 < 0:
        print("El punto se encuentra en el cuarto cuadrante del plano cartesiano.")
    elif x2 == 0 and y2 == 0:
        print("El punto se encuentra en el origen del plano cartesiano.")
    elif x2 == 0:
        print("El punto se encuentra en el eje Y del plano cartesiano.")
    elif y2 == 0:
        print("El punto se encuentra en el eje X del plano cartesiano.")

    if x2 == y2:
        print("El punto se encuentra en la línea X = Y.")
    elif x2 > y2:
        print("El punto se encuentra por debajo de la línea X = Y.")
    else:
        print("El punto se encuentra por encima de la línea X = Y.")

    distancia = sqrt((x2 - x1)**2 + (y2 - y1)**2)

    # Calcular distancia del punto hasta el centro
    if distancia < radio:
        print("El punto está dentro de la circunferencia.")
    elif distancia == radio:
        print("El punto está en la circunferencia.")
    else:
        print("El punto está fuera de la circunferencia.")

    circunferencia = round((radio * 2 * pi), 1)
    print("\nEl resultado de la circunferencia es:", circunferencia, "y su radio es:", radio)

elif option_el == "2":
    print("\nEjecutando código para la Opción 2...")

    # Función para ubicar punto en triángulo
    def punto_dentro_triangulo(x2, y2):
        # Coordenadas de los vértices del triángulo (A, B, C)
        a = (0, 0)
        b = (20, 0)
        c = (10, 17.32)  # Altura de un triángulo equilátero de lado 20

        # Coordenadas baricéntricas del punto (x2, y2) con respecto al triángulo ABC
        alpha = ((b[1] - c[1]) * (x2 - c[0]) + (c[0] - b[0]) * (y2 - c[1])) / \
                ((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1]))
        beta = ((c[1] - a[1]) * (x2 - c[0]) + (a[0] - c[0]) * (y2 - c[1])) / \
               ((b[1] - c[1]) * (a[0] - c[0]) + (c[0] - b[0]) * (a[1] - c[1]))
        gamma = 1 - alpha - beta

        # Si las coordenadas baricéntricas son positivas, el punto está dentro del triángulo
        return alpha > 0 and beta > 0 and gamma > 0

    if punto_dentro_triangulo(x2, y2):
        print("El punto está dentro del triángulo.")
    else:
        print("El punto está fuera del triángulo.")

elif option_el == "3":
    print("\nCancelado.")
