from django.conf.urls import url, include
from .views import bmi_form, bmi_result, macro_form, macro_result

urlpatterns = [
    url(r'^$', bmi_form, name='bmi_form'),
    url(r'^bmi_result/$', bmi_result, name='bmi_result'),
    url(r'^macro/$', macro_form, name='macro_form'),
    url(r'^macro_result/$', macro_result, name='macro_result'),
]