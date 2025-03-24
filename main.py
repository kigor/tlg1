import requests
import time


"""
API_URL = 'https://api.telegram.org/bot'
BOT_TOKEN = '7351163387:AAEXCihHtqh1DFyRy081K22qBkSsVb0op-I'
TEXT = 'Ура! Классный апдейт!'
MAX_COUNTER = 100
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('


offset = -2
counter = 0
chat_id: int
cat_response: requests.Response
cat_link: str


while counter < MAX_COUNTER:

    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            cat_response = requests.get(API_CATS_URL)
            if cat_response.status_code == 200:
                cat_link = cat_response.json()[0]['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')
    time.sleep(1)
    counter += 1

"""

from c9_conf_2 import load_config

config = load_config('config_dir/.env')

print('BOT_TOKEN:', config.tg_bot.token)
print('ADMIN_IDS:', config.tg_bot.admin_ids)
print()
print('DATABASE:', config.db.database)
print('DB_HOST:', config.db.db_host)
print('DB_USER:', config.db.db_user)
print('DB_PASSWORD:', config.db.db_password)