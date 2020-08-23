#Import libraries and views
from django.conf.urls import url
from .views import checkout

# URL patterns for checkout
urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]