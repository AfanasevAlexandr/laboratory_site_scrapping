import json
import csv
import requests
import os
from datetime import datetime


def collect_data():
    t_date = datetime.now().strftime('%d_%m_%Y')

    response = requests.get(url='https://lifetime.plus/api/analysis2')

    with open(f'info_{t_date}.json', 'w') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)

    categories = response.json()['categories']
    result = []
    for c in categories:
        c_name = c.get('name').strip()
        c_items = c.get('items')

        for item in c_items:
            item_name = item.get('name').strip()
            item_price = item.get('price')
            item_desc = item.get('description').strip().replace('α', 'a').replace('γ', 'Y').replace('β', 'B')
            item_wait_time = item.get('days')
            item_bio = item.get('biomaterial')

            result.append(
                [c_name, item_name, item_bio, item_desc, item_price, item_wait_time]
            )
    with open(f'result_{t_date}.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow(
            (
                'Категория',
                'Анализ',
                'Биоматериал',
                'Описание',
                'Стоимость',
                'Готовность, дней'
            )
        )

        writer.writerows(
            result
    )


if __name__ == '__main__':
    collect_data()
