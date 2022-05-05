import numpy as np
import matplotlib.pyplot as plt

VoltsPerNum = 3.3 / 255

volt  = np.loadtxt('data.txt')
volt *= VoltsPerNum

settings = np.loadtxt('settings.txt')

charge = settings[2]
finish = settings[3]

dt = settings[0]
dv = settings[1]

time   = np.linspace(0, finish, len(volt))

x_axes = np.linspace(0, finish,     10)
y_axes = np.linspace(0, volt.max(), 10)

plt.ylim([0, volt.max() * 1.1])
plt.xlim([0, finish])

plt.minorticks_on()

plt.grid(which = 'major', axis = 'y', color = 'purple', linewidth = 1)
plt.grid(which = 'minor', axis = 'y', color = 'blue',   linestyle = ':')

plt.plot(time, volt, c = 'red', linewidth = 2, label = 'Voltage(t)')
plt.axvline(charge, linestyle = ':', c = 'brown', linewidth = 2, label = "start discharging")

sp = "    "
plt.text(charge + 2.5, volt.max() - 0.5,  sp + "charge time:  {:.2f}s".format(charge), c = 'blue')
plt.text(charge + 2.5, volt.max() - 0.65,   "discharge time:  {:.2f}s".format(finish - charge), c = 'blue')

plt.xlabel(r'$Time$,  $s$', wrap = True)
plt.ylabel(r'Voltage, $V$', wrap = True)

plt.scatter(charge, volt.max(), c = "red")

print(volt)
print(len(volt))

plt.legend()

for i in range(0, len(volt), len(volt) // 20):
    plt.scatter(i * dt / 1.2, volt[i], c = 'blue')

plt.title('CHARGING & DISCHARGING', wrap = True)
plt.savefig('graph.svg')
plt.savefig('graph.png')
plt.show()
