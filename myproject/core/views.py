from django.http import HttpResponse, JsonResponse
from .crawler import quantity_word


def counter_word(request):
    word = request.GET['word']
    if word is not None:
        res = quantity_word(word)
    return HttpResponse(JsonResponse(res))
