from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

days = [1, 2, 3, 4, 5, 6, 7, 8, 9]

dev1 = [8, 6, 5, 5, 4, 2, 1, 1, 0]
dev2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
dev3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels = ['dev1', 'dev2', 'dev3']
colors = ['#008fd5', '#e5ae37', '#6d904f']

plt.stackplot(days, dev1, dev2, dev3, colors=colors, labels=labels)

plt.xlabel('Days')
plt.ylabel('Hours')

plt.title('Pie chart')
plt.tight_layout()
plt.legend(loc=(0.07, 0.05))

plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f