import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('site')
parser.add_argument('word')
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
