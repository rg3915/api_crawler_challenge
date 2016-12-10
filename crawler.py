import requests


dic = {}


def crawler(site, word=''):
    try:
        req = requests.get(site)
        dic[word] = req.text.count(word)
        return dic
    except Exception as e:
        print('Erro na conexão', e)
        return None


print(crawler('https://www.python.org/', 'Python'))
