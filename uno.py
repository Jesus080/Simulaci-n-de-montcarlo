import random
import matplotlib.pyplot as plt

def estimate_pi(num_samples):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate, x_inside, y_inside, x_outside, y_outside

# Número de muestras para la simulación
num_samples = 10000

# Estimar el valor de pi
pi_estimate, x_inside, y_inside, x_outside, y_outside = estimate_pi(num_samples)

# Mostrar el resultado
print(f"Estimación de pi: {pi_estimate}")

# Visualización de la simulación
plt.figure(figsize=(6,6))
plt.scatter(x_inside, y_inside, color="blue", marker=".")
plt.scatter(x_outside, y_outside, color="red", marker=".")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Estimación de Pi usando Monte Carlo con {num_samples} muestras\nEstimación: {pi_estimate}")
plt.show()
