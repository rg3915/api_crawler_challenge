from django.conf.urls import url
from django.contrib import admin
from myproject.core.views import counter_word

urlpatterns = [
    url(r'^api/$', counter_word, name='counter_word'),
    url(r'^admin/', admin.site.urls),
]
