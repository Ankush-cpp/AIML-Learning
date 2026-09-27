import matplotlib.pyplot as plt

data1 = [12, 15, 14, 18, 20, 22, 19, 25]
data2 = [10, 13, 15, 17, 18, 21, 23, 28]
data3 = [8, 12, 14, 16, 20, 24, 26, 35]

plt.boxplot(
    [data1, data2, data3],
    labels=["Dataset 1", "Dataset 2", "Dataset 3"]
)

plt.title("Multiple Box Plots")
plt.ylabel("Values")

plt.show()