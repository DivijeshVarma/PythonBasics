import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, linestyle='--', label='All devs')
plt.plot(ages, py_salaries, label='python salaries')

overall_median = 57000

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries > dev_salaries),
                 interpolate=True, alpha=0.25, label='Above average')

plt.fill_between(ages, py_salaries, dev_salaries,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True, color='red', alpha=0.25, label='Below average')

plt.xlabel('Ages')
plt.ylabel('Salaries')
plt.title('Median Developer Salaries (USD)')
plt.legend()

plt.legend()
plt.tight_layout()

plt.show()