import numpy as np

# 1. Créer un ndarray x comprenant 25 valeurs séquentielles commençant par 10 et finissant par 260.
x = np.arange(10, 261, 10)

# 2. Créer un ndarray y comprenant 10 valeurs aléatoires allant de 0 à 9.
y = np.random.randint(0, 10, 10)

# 3. Créer un ndarray z résultant de la concaténation de x et y.
z = np.concatenate((x, y))

# 4. Calculer et afficher la moyenne des valeurs du ndarray z.
mean_z = np.mean(z)
print("Moyenne de z:", mean_z)

# 5. Afficher le tuple correspondant aux dimensions de matrix.
matrix = np.array([[15, 12, 8007], [121, 5, 171], [5123, 444, 68]])
dimensions_matrix = matrix.shape
print("Dimensions de matrix:", dimensions_matrix)

# 6. Changer la valeur 444 de matrix en 12688 puis l'afficher.
matrix[2, 1] = 12688
print("Matrix avec la modification:", matrix)

# 7. Quel est le type de données le plus adapté aux valeurs comprises dans matrix ?
# Le type de données le plus adapté semble être int64.

# 8. Afficher le niveau de profondeur (nombre de dimensions) de matrix.
depth_matrix = matrix.ndim
print("Niveau de profondeur de matrix:", depth_matrix)

# 9. Expliquer l'intérêt d'une librairie comme NumPy dans l'analyse et la manipulation de grande quantité de données.

#NumPy est une bibliothèque Python spécialisée dans la manipulation de tableaux multidimensionnels et offre des
#fonctions mathématiques avancées pour travailler efficacement avec ces tableaux. Son intérêt réside dans sa
#capacité à effectuer des opérations vectorisées, ce qui signifie qu'elle peut effectuer des opérations sur
#l'ensemble du tableau sans avoir besoin de boucles explicites. Cela améliore la performance, la lisibilité du
#code et la productivité dans le domaine de l'analyse de données et du calcul scientifique, surtout lorsque l'on
#travaille avec de grandes quantités de données.

