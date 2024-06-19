import matplotlib.pyplot as plt

def logistic_map(r, x, n):
    """
    Generates a sequence using the logistic map.
    
    Parameters:
    r : float - The parameter that controls the behavior of the map.
    x : float - The initial value (between 0 and 1).
    n : int - The number of iterations.
    
    Returns:
    list of floats - The generated sequence.
    """
    sequence = []
    for _ in range(n):
        x = r * x * (1 - x)
        sequence.append(x)
    return sequence

# Parameters
r = 3.9  # Parameter that leads to chaotic behavior
x0 = 0.4  # Initial value
iterations = 100  # Number of iterations

# Generate the sequence
sequence = logistic_map(r, x0, iterations)

# Plot the sequence
plt.plot(sequence)
plt.title('Logistic Map Sequence')
plt.xlabel('Iteration')
plt.ylabel('Value')
plt.show()

