import matplotlib.pyplot as plt
# # pip3 install PyQt5
# # style = ['Solarize_Light2', '_classic_test_patch', 'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight',
# #'ggplot', 'grayscale', 'seaborn', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark', 'seaborn-dark-palette',
# #'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper', 'seaborn-pastel',
# #'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'tableau-colorblind10']
#
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# # ax.plot(input_values, squares, linewidth=3)
# ax.scatter(input_values, squares, s=100)
#
# # set chart title and label axis
# ax.set_title("square numbers", fontsize=24)
# ax.set_xlabel("value", fontsize=14)
# ax.set_ylabel("square of value", fontsize=14)
#
# # set size of tick labels
# ax.tick_params(axis='both', labelsize=14)
#
# plt.show()

# Calculating Data Automatically

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
ax.scatter(x_values, y_values, s=5)

# set chart title and label axis
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)


# ax.tick_params(axis='both', labelsize=14)
# set range for each axis
ax.axis([0, 1100, 0, 1100000])

plt.tight_layout()
plt.show()


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# set chart title and label axis
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("square of value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# snippets

# Median Developer Salaries by Age
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


# Median Python Developer Salaries by Age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]


# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]


# Ages 18 to 55
ages_x = [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
          36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55]

py_dev_y = [20046, 17100, 20000, 24744, 30500, 37732, 41247, 45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666,
            84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870, 120000]

js_dev_y = [16446, 16791, 18942, 21780, 25704, 29000, 34372, 37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000,
            78508, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000, 104000]

dev_y = [17784, 16500, 18012, 20628, 25206, 30252, 34368, 38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232,
         78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000, 103117]