import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['SimHei']

x = np.linspace(0, 1, 100)
y = 0.7 * x + 1

plt.figure(dpi = 400)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#ax.spines['bottom'].set_position(('data', 0))
#ax.spines['left'].set_position(('axes', 0.5))
#plt.title('a sin curve')

xmin, xmax = x.min(), x.max()
ymin, ymax = y.min(), y.max()
dx = (xmax - xmin) * 0.2
dy = (ymax - ymin) * 0.2

plt.xlabel('数量', fontsize = 12)
plt.ylabel('价格', fontsize = 12)
plt.xticks([])
plt.yticks([])
plt.ylim(ymin - dy, ymax + dy)
plt.xlim(xmin - dx, xmax + dx)
plt.plot(x, y)
plt.show()
