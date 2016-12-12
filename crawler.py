import argparse
import requests


parser = argparse.ArgumentParser(description='Crawler to count word in site.')
parser.add_argument('site', help='url of the site')
parser.add_argument('word', help='word to count in the site')
args = parser.parse_args()

dic = {}


def crawler(site):
    try:
        return requests.get(site)
    except Exception as e:
        print('Erro na conexão', e)
        return None


def _counter(word=''):
    res = crawler(args.site)
    dic[word] = res.text.count(word)
    return dic


print(_counter(args.word))
