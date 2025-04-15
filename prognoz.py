import requests
from bs4 import BeautifulSoup

def get_weather(city):
    try:
        url = f"https://rp5.ru/{city}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # segodnya = soup.find('span', {'class': 't_0'}).text
        segodnya2 = soup.find('div', {'class': 'round-5'}).text
        # print(segodnya2)
        # weather_data = get_weather(city)
        
        return segodnya2
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return 'None'
    



def get_weather_zavtra(city):
    try:
        url = f"https://rp5.ru/{city}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        zavtra = soup.find('span', {'class': 'second-part'}).text

        # weather_data = get_weather(city)
        
        return zavtra
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return 'None'


