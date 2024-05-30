import numpy as np
import matplotlib.pyplot as plt

def montecarlo_pi_approximation(num_samples):
    """Approximate Pi using the Monte Carlo method.
    
    This function uses the Monte Carlo method to approximate the value of Pi. 
    It generates a specified number of random points in a square and then determines
    the proportion of points that lie within a circle inscribed in the square. 
    The approximate value of Pi is then calculated as four times this proportion.
    The function also plots a scatter plot of the generated points, with points 
    inside the circle colored in blue and points outside the circle colored in red.
    """
    
    # Generate random points
    x = np.random.rand(num_samples) * 2 - 1  # Scale to [-1, 1]
    y = np.random.rand(num_samples) * 2 - 1  # Scale to [-1, 1]
    inside_circle = x**2 + y**2 <= 1  # Check if points are inside the unit circle
    
    # Approximate Pi
    pi_approx = 4 * np.sum(inside_circle) / num_samples
    
    # Plotting
    plt.figure(figsize=(8,8))
    plt.scatter(x[inside_circle], y[inside_circle], color='blue', s=1)
    plt.scatter(x[~inside_circle], y[~inside_circle], color='red', s=1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Monte Carlo Pi Approximation\nSamples: {num_samples}, Pi ≈ {pi_approx}')
    plt.axis('equal')
    plt.show()
    
    return pi_approx

# Example usage
num_samples = 10000
montecarlo_pi_approximation(num_samples)
