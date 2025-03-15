from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

# Le template HTML avec le formulaire et les résultats
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Résultats du scan</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f9;
        }
        h1 {
            color: #333;
        }
        .scan-button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }
        .scan-button:hover {
            background-color: #45a049;
        }
        .result {
            margin-top: 20px;
            padding: 10px;
            border-radius: 5px;
        }
        .vulnerable {
            background-color: #ffcccb;
            color: red;
        }
        .safe {
            background-color: #c8e6c9;
            color: green;
        }
    </style>
</head>
<body>
    <h1>Résultats du scan</h1>
    <form action="/" method="get">
        <input type="text" name="url" placeholder="http://example.com" required>
        <button class="scan-button" type="submit">Scanner</button>
    </form>

    {% if url %}
        <p>Scan du site : {{ url }}</p>
        {% if vuln_found %}
            <div class="result vulnerable">
                <p>⚠️ Vulnérabilité trouvée !</p>
            </div>
        {% else %}
            <div class="result safe">
                <p>✅ Aucun problème détecté.</p>
            </div>
        {% endif %}
    {% endif %}
</body>
</html>
"""

# Fonction de vérification de vulnérabilité
def is_vulnerable(url):
    try:
        response = requests.get(url + "'")
        return "error" in response.text.lower() or "sql" in response.text.lower()
    except:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    url = request.args.get("url")
    vuln_found = None

    if url:
        vuln_found = is_vulnerable(url)
    
    return render_template_string(HTML_TEMPLATE, url=url, vuln_found=vuln_found)

if __name__ == "__main__":
    app.run(debug=True)
