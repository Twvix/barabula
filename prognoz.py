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
        
        segodnya = soup.find('span', {'class': 't_0'}).text

        # weather_data = get_weather(city)
        
        return 'Сегодня ' + segodnya
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return 'None'
    



def get_weather_zavtra(city):
    try:
        # Пример для сайта Яндекс.Погода (может потребоваться обновление селекторов)
        url = f"https://rp5.ru/{city}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Эти селекторы могут устареть - нужно проверять актуальность
        zavtra = soup.find('span', {'class': 'second-part'}).text

        # weather_data = get_weather(city)
        
        return zavtra
        
    except Exception as e:
        print(f"Ошибка при парсинге: {e}")
        return 'None'
