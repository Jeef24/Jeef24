# preprocess_data.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

# Charger les données (à adapter si tu as déjà chargé les données dans un autre fichier)
data = pd.read_csv('path_to_data.csv')

# Exemple de prétraitement : encoder les colonnes catégorielles (si applicable)
encoder = LabelEncoder()
data['protocol_type'] = encoder.fit_transform(data['protocol_type'])
data['service'] = encoder.fit_transform(data['service'])
data['flag'] = encoder.fit_transform(data['flag'])

# Normalisation des données
scaler = StandardScaler()
data[['duration', 'src_bytes', 'dst_bytes']] = scaler.fit_transform(data[['duration', 'src_bytes', 'dst_bytes']])

# Sauvegarder les données prétraitées
data.to_csv('preprocessed_data.csv', index=False)

print("Données prétraitées sauvegardées.")
data['flag'] = encoder.fit_transform(data['flag'])

# Normalisation des données
scaler = StandardScaler()
data[['duration', 'src_bytes', 'dst_bytes']] = scaler.fit_transform(data[['dura>

# Sauvegarder les données prétraitées
data.to_csv('preprocessed_data.csv', index=False)

print("Données prétraitées sauvegardées.")

