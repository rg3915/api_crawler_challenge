from django.http import HttpResponse, JsonResponse
from .crawler import find_word_occurrences


def counter_word(request):
    '''
    url is the parameter to url.
    w is the parameter to word.
    Type: localhost:8000/api/?url=python.org&w=Python
    '''
    url = request.GET['url']
    word = request.GET['w']
    if url is not None and word is not None:
        res = find_word_occurrences(url, word)
    return HttpResponse(JsonResponse(res))
