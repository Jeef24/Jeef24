from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Résultats du scan</title>
</head>
<body>
    <h1>Résultats du scan</h1>
    <p>Scan du site : {{ url }}</p>
    {% if vuln_found %}
        <p style="color:red;">⚠️ Vulnérabilité trouvée !</p>
    {% else %}
        <p style="color:green;">✅ Aucun problème détecté.</p>
    {% endif %}
    <a href="/">Retour</a>
</body>
</html>
"""

def is_vulnerable(url):
    try:
        response = requests.get(url + "'")
        return "error" in response.text.lower() or "sql" in response.text.lower()
    except:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        url = request.form.get("url")
        vuln_found = is_vulnerable(url)
        return render_template_string(HTML_TEMPLATE, url=url, vuln_found=vuln_found)
    return '''
    <form action="WebVulScanner/app.py" method="get">
        <input type="text" name="url" placeholder="http://example.com" required>
        <button type="submit">Scanner</button>
    </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
