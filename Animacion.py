import numpy as np
from numpy import pi, sin, cos, sqrt
import matplotlib.pyplot as plt
import matplotlib.animation as animation

r = 1.0
l = 4.0
d = 0.5  # Distancia de desplazamiento
rot_num = 6  # Número de rotaciones de la manivela
increment = 0.1  # Incremento del ángulo
head_width = 0.2  # Ancho de la cabeza del pistón
head_height = 0.4  # Altura de la cabeza del pistón

angle_minus_last = np.arange(0, rot_num * 2 * pi, increment)
angles = np.append(angle_minus_last, rot_num * 2 * pi)

X1 = np.zeros(len(angles))  # Posiciones X de la manivela
Y1 = np.zeros(len(angles))  # Posiciones Y de la manivela
X2 = np.zeros(len(angles))  # Posiciones X de la biela
Y2 = np.zeros(len(angles))  # Posiciones Y de la biela

fig, ax = plt.subplots()
ax.set_aspect('equal')  # Configura el aspecto en 'equal'

# Inicializa la cabeza del pistón
head = plt.Rectangle((d - head_width / 2, r + l), head_width, head_height, color='gray', alpha=0.8)
ax.add_patch(head)

# Inicializa la línea del pistón
line, = ax.plot([], [], 'o-', lw=5, color='#de2d26')

def init():
    line.set_data([], [])
    return line, head

def on_scroll(event):
    # Maneja el zoom con la rueda del mouse
    current_xlimits = ax.get_xlim()
    current_ylimits = ax.get_ylim()
    xdata = event.xdata  # Coordenada x donde ocurrió el evento de scroll
    ydata = event.ydata  # Coordenada y donde ocurrió el evento de scroll
    zoom_factor = 1.2 if event.step > 0 else 1 / 1.2  # Factor de zoom
    new_xlimits = [(current_xlimits[0] - xdata) * zoom_factor + xdata, (current_xlimits[1] - xdata) * zoom_factor + xdata]
    new_ylimits = [(current_ylimits[0] - ydata) * zoom_factor + ydata, (current_ylimits[1] - ydata) * zoom_factor + ydata]
    ax.set_xlim(new_xlimits)
    ax.set_ylim(new_ylimits)
    plt.draw()

fig.canvas.mpl_connect('scroll_event', on_scroll)

def animate(i):
    x1 = r * cos(angles[i])
    y1 = r * sin(angles[i])
    x2 = d
    y2 = r * sin(angles[i]) + sqrt(l**2 - (r * cos(angles[i]))**2)
    x_points = [0, x1, x2]
    y_points = [0, y1, y2]
    line.set_data(x_points, y_points)
    head.set_xy((x2 - head_width / 2, y2))
    return line, head

ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(angles), interval=40, blit=True, repeat=True)

plt.show()
