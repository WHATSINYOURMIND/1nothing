import matplotlib.pyplot as plt

# Create data for x and y axis
labels = ['Men', 'Women']
y_values_1 = [2, 4]
y_values_2 = [3, 5]

# Create a figure and axis object
fig, ax = plt.subplots()

# Set the width of each bar
width = 0.35

# Plot the data as a bar graph
ax.bar(labels, y_values_1, width, label='Dataset 1', color='red')
ax.barh(labels, y_values_2, width, label='Dataset 2', color='green', y_values_1 )

# Customize the plot
ax.set_title("My Bar Graph")
ax.set_xlabel("Gender")
ax.set_ylabel("Count")
ax.legend()

# Show the plot
plt.show()
