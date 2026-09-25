import matplotlib.pyplot as plt

# Single dataset
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(x, y)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Basic Line Plot")

plt.show()


# Multiple datasets
x = [1, 2, 3, 4, 5]

y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

plt.plot(x, y1, "r-o", label="Dataset 1")
plt.plot(x, y2, "b--s", label="Dataset 2")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Multiple Datasets")

plt.legend()
plt.show()