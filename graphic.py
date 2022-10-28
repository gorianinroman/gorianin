import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
with open("settings1.txt", "r") as settings:
    tmp = np.array([float(i) for i in settings.read().split("\n")])

data_values = np.loadtxt("data1.txt", dtype=int)
data_values = 3.3 * data_values / 256

fig, ax = plt.subplots(figsize=(18,10), dpi = 200)

x = np.arange(1,899,1)
x = x*tmp[0]

ax.plot(x,  data_values, label = r"V = V(t)",color = "green")

ax.plot(x,  data_values, 'ro', markersize = 0.3, color = "black")
plt.minorticks_on()


plt.title(r"Зависимость напряжения от времени в RC-цепи")
plt.text(8.05,2.3,r"Время заряда = 5.2 c", color = "blue", fontsize = 8)
plt.text(8.05,1.8,r"Время разряда = 6.8 c", color = "blue", fontsize = 8)
plt.xlabel("Время, с", fontsize = 16)
plt.ylabel("Напряжение, В", fontsize = 16)
plt.grid(which="major", linestyle="-")
plt.grid(which="minor", linestyle="-")
ax.legend(loc = "best", fontsize = 12)
ax.grid(color = "black", linewidth = 1)
fig.savefig("graphic.svg")
ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))

plt.xlim([0, 12.5])
plt.ylim([0, 3.5])
plt.show()

