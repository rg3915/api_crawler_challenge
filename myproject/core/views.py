from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .crawler import quantity_word


class JSONResponse(HttpResponse):
    '''
    An HttpResponse that renders its content into JSON.
    '''

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def counter_word(request):
    word = request.query_params.get('word', None)
    if word is not None:
        res = quantity_word(word)
    return JSONResponse(res)
