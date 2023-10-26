import matplotlib.pyplot as plt
import numpy as np
import random

# Definición de parámetros
Vc = 0.002  # Volumen del cilindro en metros cúbicos
RC = 10.0   # Relación de compresión
theta = np.linspace(0, 720, 360)  # Ángulo del cigüeñal en grados

# Simulación de la distribución de Poisson para eventos de combustión
lambda_ = 10  # Tasa de ocurrencia de eventos
combustion_events = np.random.poisson(lambda_, len(theta))

# Volumen del cilindro en función del ángulo del cigüeñal
V = Vc / (1 + (1 / (RC - 1)) * (1 - np.cos(np.radians(theta))))

# Gráfica del ciclo de 4 tiempos con eventos de combustión
plt.figure(figsize=(8, 6))
plt.plot(theta, V, label="Volumen del cilindro")
plt.scatter(theta, V, c='red', s=combustion_events, label="Eventos de combustión")
plt.xlabel("Ángulo del cigüeñal (grados)")
plt.ylabel("Volumen del cilindro (m^3)")
plt.title("Ciclo de 4 tiempos de un motor con eventos de combustión")
plt.grid(True)
plt.legend()
plt.show()
