from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import joblib

# Exemple de jeu de données (remplace-le par ton propre dataset)
X, y = make_classification(n_samples=1000, n_features=20, random_state=42)

# Diviser en données d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Sauvegarder le modèle
joblib.dump(model, 'intrusion_detection_model.pkl')

