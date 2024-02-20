from cod import x1, x2, y1, y2
import matplotlib.pyplot as plt
import numpy as np

# Definir los puntos y el radio de la circunferencia
puntos = [(x1, y1), (-x2, y2)]
centro_circunferencia = (1, 1)
radio_circunferencia = 3

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Graficar los puntos en el plano cartesiano
for punto in puntos:
    ax.plot(punto[0], punto[1], 'ro')  # 'ro' para puntos rojos

# Dibujar la circunferencia
theta = np.linspace(0, 2*np.pi, 100)
x_circunferencia = centro_circunferencia[0] + radio_circunferencia * np.cos(theta)
y_circunferencia = centro_circunferencia[1] + radio_circunferencia * np.sin(theta)
ax.plot(x_circunferencia, y_circunferencia, 'b-')  # 'b-' para línea azul

# Ajustar los límites de los ejes para que se vea mejor
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Mostrar la cuadrícula y los ejes
ax.grid(True)
ax.axhline(0, color='black',linewidth=0.5)
ax.axvline(0, color='black',linewidth=0.5)

# Etiquetar los ejes
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')

# Dar título al gráfico
ax.set_title('Puntos y circunferencia en el plano cartesiano')

# Mostrar el gráfico
plt.show()
