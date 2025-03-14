# load_data.py

import pandas as pd

# Charger le dataset KDDCup99 (en téléchargeant le fichier CSV depuis un lien)
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/0028/kddcup99.zip"
data = pd.read_csv(url, header=None)

# Afficher les premières lignes pour vérifier que le chargement a bien fonctionné
print(data.head())
