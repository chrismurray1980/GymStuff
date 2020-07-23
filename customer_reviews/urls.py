from django.conf.urls import url, include
from .views import customer_reviews, review_detail

urlpatterns = [
    url(r'^(?P<id>\d)/$', customer_reviews, name='customer_reviews'),
    url(r'^review_detail/(?P<id>\d)/$', review_detail, name='review_detail'),
]