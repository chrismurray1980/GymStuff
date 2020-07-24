from django.conf.urls import url, include
from .views import customer_reviews, review_detail, create_or_edit_review

urlpatterns = [
    url(r'^(?P<id>\d)/$', customer_reviews, name='customer_reviews'),
    url(r'^review_detail/(?P<id>\d+)/$', review_detail, name='review_detail'),
    url(r'^new/$', create_or_edit_review, name='new_review'),
   # url(r'^(?P<pk>\d+)/edit/$', create_or_edit_review, name='edit_review')
]