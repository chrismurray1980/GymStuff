# Import libraries and views
from django.conf.urls import url, include
from . import urls_reset
from .views import index, register, logout, login

# URL patterns for account app
urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(urls_reset)),
]
