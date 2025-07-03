import numpy as plt
import matplotlib.pyplot as plt


def objective(x):
    return x[0]**2

r_min, r_max = -5.0, 5.0

inputs = np.arrange(r_min, r_max, 0.1)

results = [objective([x]) for x in inputs]

plt.plot(inputs, results, label='f(x) = x^2')
plt.axvline(x=0.0, linestyle='--', color='red', label='optimum at x=0')
plt.title("Objective Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()