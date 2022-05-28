import requests


def interisting_or_boring_number():
    with open('dataset_24476_3.txt') as inf:
        for i in inf:
            url = f'http://numbersapi.com/{i.strip()}/math?json=true'
            res = requests.get(url)
            if res.json()['found']:
                print('Interesting')
            else:
                print('Boring')


interisting_or_boring_number()
