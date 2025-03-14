import joblib
from train_model import model  # Importer le modèle après l'entraînement

# Sauvegarder le modèle
joblib.dump(model, 'intrusion_detection_model.pkl')

print("Modèle sauvegardé.")
