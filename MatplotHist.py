import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('hist.csv')
ids = data['Responder_id']
ages = data['Age']

bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# plt.hist(ages, bins=bins, edgecolor='black')
plt.hist(ages, bins=bins, edgecolor='black', log=True)

median_age = 29
color = 'red'

plt.axvline(median_age, color=color, label='Age median', linewidth=2)

plt.xlabel('Ages')
plt.ylabel('Total respondents')
plt.title('Age of respondents')
plt.legend()

plt.legend()
plt.tight_layout()

plt.show()