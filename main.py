import requests


def geo_logs_func(geo_logs):
    index = 0
    ru_list = []
    for visit in geo_logs:
        for country in visit.values():
            if country[1] == 'Россия':
                ru_list.append(geo_logs[index])
            index += 1
    geo_logs = ru_list
    return geo_logs


def geo_id_func(ids):
    z = set()
    for users in ids:
        set_user = set(ids[users])
        z = set_user | z
    return z


def stats_func(stats):
    max_value = 0
    source = ''
    for key, value in stats.items():
        if value > max_value:
            max_value = value
            source = key
    return source


token = ""  # Необходимо указать токен


def create_folder(path):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(f'{URL}?path={path}', headers=headers)
    return response
