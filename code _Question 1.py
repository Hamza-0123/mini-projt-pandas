# Question 1
import numpy as np
donnes = np.random.rand(100, 3)
cov_matrice = np.cov(donnes, rowvar=False)
print("Tableau de données :")
print(donnes)
print("\nMatrice de covariance :")
print(cov_matrice)
