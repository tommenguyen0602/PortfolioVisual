import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Example data
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# Create a scatter plot
fig, ax = plt.subplots()
scatter = ax.scatter(x, y)

def update_plot(index):
    # Delete a data point at the given index
    del x[index]
    del y[index]
    scatter.set_offsets(list(zip(x, y)))

def on_button_click(event):
    # Call the update_plot function to delete a data point
    index = 2  # Specify the index of the row to delete
    update_plot(index)
    plt.draw()  # Redraw the plot after updating

# Create a button to trigger the deletion
ax_button = plt.axes([0.1, 0.05, 0.1, 0.075])
button = plt.Button(ax_button, 'Delete Row')
button.on_clicked(on_button_click)

# Show the plot
plt.show()

