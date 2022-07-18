"""
Изучение основного уровня MathLab, возможности библиотеки,
функционал.
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Стиль графиков
# Заголовок
plt.title(r'$\frac{3}{4} \binom{3}{4} \genfrac{}{}{0}{}{3}{4}$')
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2 * np.pi * t)
line = plt.plot(t, s, lw = 2)
plt.ylim(-2, 2)

plt.show()