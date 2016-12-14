import re
import requests


pat_is_http = re.compile(r'(https?:\/\/[^\s]+)')
dic = {}

url = 'python.org'


def url_contain_http(url, pat_is_http):
    ''' Checks if url contains http '''
    if not pat_is_http.match(url):
        url = 'http://' + url
    return url


def crawler(url):
    try:
        url = url_contain_http(url, pat_is_http)
        return requests.get(url).text
    except Exception as e:
        print('Erro na conexão', e)
        return None


def quantity_word(word=''):
    ''' Count words in text returned '''
    res = crawler(url)
    dic[word] = res.count(word)
    return dic
