import requests


def crawler(site, palavra=''):
    try:
        req = requests.get(site)
        return req.text.count(palavra)
    except Exception as e:
        print('Erro na conexão', e)
        return None


print(crawler('https://www.python.org/', 'Python'))
