import numpy as np
num_states = 10

transition_matrix = np.array([
    [0.0, 0.7, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0, 0.0],
    [0.0, 0.0, 0.55, 0.0, 0.0, 0.0, 0.0, 0.0, 0.45, 0.0],
    [0.0, 0.5, 0.0, 0.0, 0.0, 0.0, 0.0, 0.5, 0.0, 0.0],
    [0.3, 0.0, 0.0, 0.0, 0.2, 0.0, 0.5, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    [0.1, 0.0, 0.0, 0.0, 0.3, 0.0, 0.6, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0],
    [0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
])

densities = np.array([17.03, 32.90, 18.09, 35.73, 52.20, 90.25, 79.67, 21.41, 18.50, 4.81])

initial_probabilities = densities / np.sum(densities)

num_iterations = 100

probabilities = initial_probabilities
for _ in range(num_iterations):
    probabilities = np.dot(probabilities, transition_matrix)

print("Probabilities after updating:\n")
print(probabilities)
input('\n please enter to exit...')