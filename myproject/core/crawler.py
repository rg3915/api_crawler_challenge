import re
import requests

def contains_http(url):
    ''' Checks if url contains http '''
    STARTS_WITH_HTTP_OR_HTTPS = re.compile(r'(https?:\/\/[^\s]+)')
    return 'http://' + url if not STARTS_WITH_HTTP_OR_HTTPS.match(url) else url

def crawler(url):
    """Retrieves the page content given a URL."""
    try:
        url = contains_http(url)
        return requests.get(url).text
    except Exception as e:
        print('Erro na conexão', e)
        return None


def quantity_word(url, word=''):
    """Count words in text returned"""
    occurrences = {}
    res = crawler(url)
    occurrences[word] = res.count(word)
    return occurrences
