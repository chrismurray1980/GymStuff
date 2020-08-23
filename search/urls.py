from django.conf.urls import url
from .views import do_search, weight_search, supplement_search, bench_search, accessory_search, vitamin_search

# URLs for search
urlpatterns = [
    url(r'^$', do_search, name='search'),
    url(r'^weights/$', weight_search, name='weight_search'),
    url(r'^supplements/$', supplement_search, name='supplement_search'),
    url(r'^benches/$', bench_search, name='bench_search'),
    url(r'^accessories/$', accessory_search, name='accessory_search'),
    url(r'^vitamins/$', vitamin_search, name='vitamin_search'),
]