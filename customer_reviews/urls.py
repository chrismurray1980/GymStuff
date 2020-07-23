from django.conf.urls import url, include
from .views import customer_reviews, review_detail

urlpatterns = [
    url(r'^(?P<id>\d)/$', customer_reviews, name='customer_reviews'),
    url(r'^(?P<customer_review_id>[0-9]+)/$', review_detail, name='review_detail'),
]