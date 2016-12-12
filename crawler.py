import argparse
import re
import requests

parser = argparse.ArgumentParser(description='Crawler to count word in site.')
parser.add_argument('url', help='url of the site')
parser.add_argument('word', help='word to count in the site')
args = parser.parse_args()

pat_is_http = re.compile(r'(https?:\/\/[^\s]+)')
dic = {}


def url_contain_http(url, pat_is_http):
    ''' Checks if url contains http '''
    if not pat_is_http.match(url):
        url = 'http://' + url
    return url


def crawler(url):
    try:
        url = url_contain_http(args.url, pat_is_http)
        return requests.get(url).text
    except Exception as e:
        print('Erro na conexão', e)
        return None


def quantity_word(word=''):
    ''' Count words in text returned '''
    res = crawler(args.url)
    dic[word] = res.count(word)
    return dic


if __name__ == '__main__':
    print(quantity_word(args.word))
