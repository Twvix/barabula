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
        
        arr = segodnya2.split('.')
        return arr[0] + arr[4] + '\n' + arr[5] + arr[9]
        
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
        
        # segodnya = soup.find('span', {'class': 't_0'}).text
        zavtra = soup.find('div', {'class': 'round-5'}).text
        # print(segodnya2)
        # weather_data = get_weather(city)
        
        arr2 = zavtra.split('.')

        return arr2[5] + arr2[9]
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return 'None'
    

