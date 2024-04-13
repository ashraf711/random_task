import numpy as np
import matplotlib.pyplot as plt

def fourier_series_square_wave(x, n_terms):
    sum = np.zeros_like(x)
    for n in range(1, n_terms + 1):
        term = np.sin((2 * n - 1) * x) / (2 * n - 1)
        sum += term
    return (4 / np.pi) * sum

def plot_fourier_approximation():
    while True:
        # User inputs
        n_terms = int(input("Enter the number of terms in the Fourier series: "))
        x_min = float(input("Enter the minimum x value: "))
        x_max = float(input("Enter the maximum x value: "))

        # Creating the x values and calculating the Fourier series
        x_values = np.linspace(x_min, x_max, 1000)
        y_values = fourier_series_square_wave(x_values, n_terms)

        # Plotting the function
        plt.figure(figsize=(10, 6))
        plt.plot(x_values, y_values, label= 'Square Wave Approximation')
        plt.title(f'Fourier Series Approximation with {n_terms} terms')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend(loc = 'upper right')
        plt.grid(True)
        plt.show()

        # Ask the user if they want to continue
        continue_plotting = input("Do you want to plot a new graph? (y/n): ")
        if continue_plotting.lower() != 'y':
            break

if __name__ == "__main__":
    plot_fourier_approximation()
