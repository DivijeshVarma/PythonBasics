import csv
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('fivethirtyeight')

data = pd.read_csv('csvd.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))
    # Counter({'JavaScript': 59218, 'HTML/CSS': 55465, 'SQL': 47544, 'Python': 36442, 'Java': 35916,...

languages = []
popularity = []

for items in language_counter.most_common(10):
    languages.append(items[0])
    popularity.append(items[1])
    # ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript']
    # [59218, 55465, 47544, 36442, 35916, 31991, 27097, 23030, 20524, 18523]

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.xlabel('Popularity')
# plt.ylabel('Languages')
plt.title('Languages by popularity')

plt.tight_layout()

plt.show()
