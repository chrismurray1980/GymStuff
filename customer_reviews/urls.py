from django.conf.urls import url, include
from .views import customer_reviews

urlpatterns = [
    url(r'^(?P<id>\d+)/$', customer_reviews, name='customer_reviews'),
]