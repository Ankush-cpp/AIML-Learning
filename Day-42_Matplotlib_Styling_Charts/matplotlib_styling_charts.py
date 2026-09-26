import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Styling a line plot
plt.plot(
    x,
    y,
    color="blue",
    linestyle="--",
    marker="o",
    linewidth=2,
    markersize=6
)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Styled Line Plot")
plt.grid(True)

# Save plot
plt.savefig("styled_line_plot.png", dpi=300, bbox_inches="tight")

plt.show()


# Bar Chart
categories = ["A", "B", "C", "D"]
values = [25, 40, 30, 50]

plt.bar(categories, values)
plt.xlabel("Category")
plt.ylabel("Value")
plt.title("Bar Chart")
plt.show()


# Scatter Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 12, 25, 20]

plt.scatter(x, y)
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot")
plt.show()


# Histogram
data = [10, 12, 15, 15, 18, 20, 20, 21, 22, 25, 25, 28, 30]

plt.hist(data, bins=5)
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()


# Pie Chart
labels = ["Python", "SQL", "Pandas", "NumPy"]
sizes = [40, 25, 20, 15]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Learning Distribution")
plt.show()