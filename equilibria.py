import nashpy as nash
import numpy as np

### 3x3 payoff matrix
A = np.array([[1, 1, -1], [2, -1, 0]])
B = np.array([[1/2, -1, -1/2], [-1, 3, 2]])
game = nash.Game(A, B)
game


### generate equilibria
eqs = game.support_enumeration()
type(eqs)

for eq in eqs:
        print(eq)