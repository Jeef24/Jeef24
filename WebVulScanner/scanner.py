import requests
from bs4 import BeautifulSoup
import sys

def check_sql_injection(url):
    # Exemple simple : rechercher des paramètres URL susceptibles d'être vulnérables
    if "'" in url:
        print(f"Potentiel risque d'injection SQL dans l'URL : {url}")
    else:
        print(f"L'URL semble sans risque pour l'injection SQL : {url}")

def check_admin_page(url):
    # Vérifier si l'URL contient des chemins courants d'administration
    admin_pages = ['/admin', '/login', '/admin.php', '/wp-admin']
    for page in admin_pages:
        full_url = url + page
        response = requests.get(full_url)
        if response.status_code == 200:
            print(f"Page d'administration trouvée : {full_url}")

def scan_site(url):
    print(f"Scan du site : {url}")
    
    # Vérification de l'injection SQL
    check_sql_injection(url)
    
    # Vérification de pages d'administration
    check_admin_page(url)

def main():
    if len(sys.argv) < 2:
        print("Usage : python scanner.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    scan_site(url)

if __name__ == "__main__":
    main()
