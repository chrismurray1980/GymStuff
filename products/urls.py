from django.conf.urls import url, include
from .views import all_products, product, create_or_edit_review

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^(?P<id>\d)/$', product, name='product'),
    url(r'^category/$', product, name='product_category'),
    url(r'^(?P<product_id>[0-9]+)/new_review/$', create_or_edit_review, name='new_review'),
]