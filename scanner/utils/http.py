import requests
from bs4 import BeautifulSoup

def send_request(url, method='get', params=None, data=None):
    try:
        if method.lower() == 'post':
            return requests.post(url, data=data)
        return requests.get(url, params=params)
    except Exception as e:
        print(f"[HTTP Error] {e}")
        return None

def get_forms(url, session):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('form')