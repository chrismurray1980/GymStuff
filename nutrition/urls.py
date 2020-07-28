from django.conf.urls import url, include
from .views import bmi_form, bmi_result

urlpatterns = [
    url(r'^$', bmi_form, name='bmi_form'),
    url(r'^bmi_result/$', bmi_result, name='bmi_result'),
]