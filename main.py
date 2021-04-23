import nashpy as nash
import numpy as np

### construct payoff matrix of zero sum matching pennies game
A = [[1,-1], [-1, 1]]
matching_pennies = nash.Game(A)

### create probability arrays r for rows c for columns
sigma_r = np.array([0.8, 0.2])
sigma_c = np.array([0.6, 0.4])
matching_pennies[sigma_r, sigma_c]

### print the expected payoffs for each player
print(f'{matching_pennies[sigma_r, sigma_c]}')

