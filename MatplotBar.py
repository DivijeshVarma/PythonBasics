import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

# [ 0  1  2  3  4  5  6  7  8  9 10]
index_x = np.arange(len(dev_x))
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]
plt.bar(index_x - width, dev_y, width=width, color='r', label='All devs')

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
plt.bar(index_x, py_dev_y, width=width, color='#5a7d9a', label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(index_x + width, js_dev_y, width=width, color='#adad3b', label='Java Script')

plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.title('Median Developer Salaries (USD)')

# for label
plt.legend()
# change labels
plt.xticks(ticks=index_x, labels=dev_x)
# for correct padding
plt.tight_layout()
plt.grid(True)

plt.show()
