import requests
import json

client_id = 'da6b6f093293576c0964'
client_secret = 'a1ed58a15dcf615a2569fd4ac61fc334'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}
# инициируем запрос с заголовком

with open('dataset_24476_4.txt', encoding='utf-8') as inf, open('artsy_res', 'w', encoding='utf-8') as ouf:
    artist_dict = dict()
    for artist in inf.readlines():
        r = requests.get(f"https://api.artsy.net/api/artists/{artist.strip()}", headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        # print(j['sortable_name'], j['birthday'])

        if int(j['birthday']) in artist_dict.keys():
            artist_dict[int(j['birthday'])].append(j['sortable_name'])
        else:
            artist_dict[int(j['birthday'])] = [j['sortable_name']]

    for key in sorted(list(artist_dict.keys())):
        if len(artist_dict[key]) > 1:
            for name in sorted(artist_dict[key]):
                print(name, file=ouf)
        else:
            print(*artist_dict[key], file=ouf)

