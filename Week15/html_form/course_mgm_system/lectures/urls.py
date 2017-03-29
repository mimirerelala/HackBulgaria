from django.conf.urls import url, patterns
from lectures.views import new

urlpatterns = [
    url(r'^lectures/new/', new),
]
