#Пример работы с пользовательскими исключениями
import requests
import sys

url = sys.argv[1]
try:
    response = requests.get(url,timeout=30)
    response.raise_for_status() #Если статус ответа не 200(т.е нет сайта итд)
except requests.Timeout:
    print("ошибка timeout url", url)
except requests.HTTPError as err:
    code = err.response.status_code # статус ответа
    print("Ошибка url: {0}, code {1}" .format(url, code))
except requests.RequestException:
    print("Ошибка скачивания url: ", url)
else:
    print(response.content)