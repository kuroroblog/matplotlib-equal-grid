from matplotlib import pyplot as plt
from datetime import datetime, timedelta

xvalues = range(0, 21)
yvalues = xvalues

fig, ax = plt.subplots()
plt.plot(xvalues, yvalues)

# 参考 : https://www.yutaka-note.com/entry/matplotlib_axis
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
plt.yticks([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5])

plt.grid(True)
ax.set_aspect('equal')

plt.show()
