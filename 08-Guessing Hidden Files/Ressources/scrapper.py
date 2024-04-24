import requests
from bs4 import BeautifulSoup
import re

def scrap_hidden_directory(url, base_url, counter):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for link in soup.find_all('a', href=True):
        if link['href'] == "../":
            continue

        next_url = base_url if link['href'].startswith("/") else url
        full_link = next_url + link['href']

        if "README" in full_link:
            counter[0] += 1
            print(f"README files checked: {counter[0]}", end="\r")
            readme_response = requests.get(full_link)
            if re.search(r'\b[a-f0-9]{64}\b', readme_response.text):
                print("\nFlag found!")
                return readme_response.text
        else:
            flag = scrap_hidden_directory(full_link, base_url, counter)
            if flag:
                return flag
    return None

start_url = "http://x.x.x.x/.hidden/"
counter = [0]
flag = scrap_hidden_directory(start_url, start_url, counter)
print("\n" + (flag if flag else "Flag not found"))
