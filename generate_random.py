import numpy as np
import matplotlib.pyplot as plt

def generate_random_numbers(size=150):
    """Generate a single column of random numbers."""
    return np.random.rand(size)

def plot_random_numbers(x, y):
    """Plot the dataset on x,y axis using matplotlib, highlighting points above index 80 in red."""
    plt.scatter(x, y, color='blue')  # Creates a scatter plot with default color blue
    plt.scatter(x[x > 80], y[x > 80], color='red')  # Highlights points above index 80 in red
    plt.title('Single Column Random Numbers Plot')
    plt.xlabel('Index')
    plt.ylabel('Random Number')
    plt.show()

# Main execution
y = generate_random_numbers(100)  # 100 random numbers
x = np.arange(len(y))  # Using the index of each number as the x-axis value
plot_random_numbers(x, y)
