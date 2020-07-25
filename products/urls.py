from django.conf.urls import url, include
from .views import all_products, product

urlpatterns = [
    url(r'^$', all_products, name='all_products'),
    url(r'^(?P<id>\d)/$', product, name='product'),
    url(r'^category/$', product, name='product_category'),
]