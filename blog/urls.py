from blog.views import archive
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    url(r'^$', archive),
]