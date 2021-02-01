import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('subdata.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
python_salaries = data['Python']
javaScript_salaries = data['JavaScript']

# fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

ax1.plot(ages, dev_salaries, color='#444444', linestyle='--', label='All devs')

ax2.plot(ages, python_salaries, label='Python devs')
ax2.plot(ages, javaScript_salaries, label='Javascript devs')

ax1.set_ylabel('Salaries')
ax1.set_title('Median Developer Salaries (USD)')
ax1.legend()

ax2.set_xlabel('Ages')
ax2.set_ylabel('Salaries')
ax2.legend()

plt.tight_layout()
# plt.grid(True)

plt.show()

# To save figures
# fig1.savefig('fig1.png')
# fig2.savefig('fig2.png')