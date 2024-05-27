import numpy as np

P = np.array([[0, 0.7, 0, 0, 0, 0, 0, 0.3, 0, 0],
              [0, 0, 0.55, 0, 0, 0, 0, 0, 0.45, 0],
              [0, 0.5, 0, 0, 0, 0, 0, 0.5, 0, 0],
              [0.3, 0, 0, 0, 0.2, 0, 0.5, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
              [0.1, 0, 0, 0, 0.3, 0, 0.6, 0, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])

eigenvalues, eigenvectors = np.linalg.eig(P.T)

stationary_vector = np.real(eigenvectors[:, np.isclose(eigenvalues, 1)])

stationary_vector /= np.sum(stationary_vector)

st  = stationary_vector.flatten()
print( f'your stationary probabilty is \n\n {st}\n' )
input("\nPress Enter to exit...")