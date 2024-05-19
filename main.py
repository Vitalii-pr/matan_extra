import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def eqs(x:list[int], time:list[int]):
    '''diff resolver'''

    x1 = x[0]
    x2 = x[1]

    # Parameters to define
    alfa = 0.15
    beta = 0.03
    gamma = 0.1
    delta = 0.01

    #Lotka-Volterra equation
    dxdt = [alfa * x1 - beta * x1 * x2,
            delta * x1 * x2 - gamma * x2]
    return dxdt


if __name__ == '__main__':

    # Set initial conditions
    y0 = [10, 2]

    # Set the time grid
    t = np.linspace(0, 360, 500)

    # Solve the ODE system
    sol = odeint(eqs, y0, t)

    # Extract the solution variables for plotting
    x1 = sol[:, 0]
    x2 = sol[:, 1] 

    # Plot the solution
    plt.plot(t, x1, label='Prey')
    plt.plot(t, x2, label='Predator')
    plt.xlabel('Time')
    plt.ylabel('Number')
    plt.legend(loc='upper right')
    # Set the maximum y-value on the plot
    plt.ylim(0, np.max(x1) + 10)
    plt.grid(True)
    plt.show()
