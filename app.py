import requests as req
import os
from time import sleep


def clear():
    if 'nt' in os.name:
        os.system('cls')
    else:
        os.system('clear')


while True:
    ask = input('Do you want to do a zip code inquiry? (Y/n) ')

    if ask[0].upper() == 'Y':
        cep = int(input('Enter the zip code: '))

        try:
            data = req.get(f'https://viacep.com.br/ws/{cep}/json/')

            dic = dict(data.json()).items()

            for items in dic:
                print(f'{items[0]}: {items[1]}')
        except Exception:
            message = 'Zip Code Not Found'

            response = {
                'response status': data.status_code,
                'message': message,
            }

            print(response)
            continue

    elif ask[0].upper() == 'N':
        clear()
        break

    sleep(5)
    clear()
