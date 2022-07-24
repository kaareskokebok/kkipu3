import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 200, 0.1)

# Regner ut y-verdiene til hver av funksjonene
inntekt = 120*x - 0.3*x**2
kostnad = 0.15*x**2 + 40*x + 1700

# Tegner grafene til funksjonene
plt.plot(x, inntekt, label="Inntekt")
plt.plot(x, kostnad, label=r"$K(x)=0.15x^2+40x+1700$")

# Legger til titler, rutenett og forklaringer
plt.xlabel("Antall enheter")
plt.ylabel("Kr")
plt.grid()
plt.title("Inntekt og kostnad")
plt.legend()
plt.show()