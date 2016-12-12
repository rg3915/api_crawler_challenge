import argparse
import requests


parser = argparse.ArgumentParser(description='Crawler to count word in site.')
parser.add_argument('site', help='url of the site')
parser.add_argument('word', help='word to count in the site')
args = parser.parse_args()

dic = {}


def crawler(site, word=''):
    try:
        req = requests.get(site)
        dic[word] = req.text.count(word)
        return dic
    except Exception as e:
        print('Erro na conexão', e)
        return None


print(crawler(args.site, args.word))
