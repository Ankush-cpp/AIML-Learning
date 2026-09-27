import matplotlib.pyplot as plt

data = [12, 15, 14, 18, 20, 22, 19, 25, 30, 45]

plt.boxplot(data)

plt.title("Box Plot")
plt.ylabel("Values")

plt.show()