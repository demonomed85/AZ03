import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

url = "https://www.divan.ru/category/divany"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    prices = []

    for price_tag in soup.find_all(class_='ui-LD-ZU'):
        price = price_tag.get_text(strip=True)
        price_numeric = int(price.replace('руб.', '').replace(' ', '').replace('\xa0',
                                                                                 ''))
        prices.append(price_numeric)


    df = pd.DataFrame(prices, columns=['Price'])
    df.to_csv('prices_numeric.csv', index=False, encoding='utf-8-sig')
    print("Цены успешно сохранены в файл prices_numeric.csv")
    print(f'Средняя цена: {df.mean()}')

    plt.hist(df['Price'])
    plt.show()

else:
    print(f"Ошибка при получении страницы. Код статуса: {response.status_code}")