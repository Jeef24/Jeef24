from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Charger le modèle
model = joblib.load('intrusion_detection_model.pkl')

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    labels = [f"Feature {i}" for i in range(1, 21)]
    values = []
    colors = []

    if request.method == "POST":
        try:
            # Récupérer les valeurs des features
            values = [float(request.form.get(f"feature{i}", 0)) for i in range(1, 21)]
            data = np.array(values).reshape(1, -1)

            # Prédiction du modèle
            prediction = model.predict(data)[0]

            # Définir les couleurs pour le graphique
            colors = ["red" if prediction == 1 else "green"] * 20
        except Exception as e:
            print(f"Erreur : {e}")

    return render_template("index.html", prediction=prediction, labels=labels, values=values, colors=colors)

if __name__ == "__main__":
    app.run(debug=True)

