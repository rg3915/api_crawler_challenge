import re
import requests

def contains_http(url):
    ''' Checks if url contains http or https. '''
    STARTS_WITH_HTTP_OR_HTTPS = re.compile(r'(https?:\/\/[^\s]+)')
    return 'http://' + url if not STARTS_WITH_HTTP_OR_HTTPS.match(url) else url

def get_text_content(url):
    """Retrieves the page text content given a URL."""
    try:
        url = contains_http(url)
        return requests.get(url).text
    except Exception as e:
        print('Erro na conexão', e)
        return None


def find_word_occurrences(url, word=''):
    """Find word occurrences based on the content retrieved."""
    occurrences = {}
    occurrences[word] = get_text_content(url).count(word)
    return occurrences


