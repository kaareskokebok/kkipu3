import matplotlib.pyplot as plt
import numpy as np

x_grader = np.arange(0, 360, 0.1)
# Konverterer gradene til radianer
x_radianer = np.deg2rad(x_grader)

# Regner ut sinus og cosinus til alle vinklene
sin_verdier = np.sin(x_radianer)
cos_verdier = np.cos(x_radianer)

plt.plot(x_grader, sin_verdier, label=r"$f(x)=\sin x$")
plt.plot(x_grader, cos_verdier, label=r"$g(x)=\cos x$")

plt.xlabel(r"Vinkel ($\degree$)")
plt.ylabel("Funksjonsverdi")
plt.grid()
plt.title("Sinus og cosinus til de første 360 gradene")
plt.legend()
plt.show()