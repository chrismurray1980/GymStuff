# Import libraries and views
from django.conf.urls import url, include
from .views import customer_reviews

# URLs for customer reviews
urlpatterns = [
    url(r'^(?P<id>\d+)/$', customer_reviews, name='customer_reviews'),
]