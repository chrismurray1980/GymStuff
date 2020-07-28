from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from nutrition.forms import bmi
from .models import Physical
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
import datetime

@login_required
def bmi_form(request):
    form = bmi(request.POST)
    if form.is_valid():
        height = form.cleaned_data['height']
        weight = form.cleaned_data['weight']
        physical = Physical()
        physical.height= height
        physical.weight= weight
        bmi_calc=weight/height**2
        physical.bmi_calc=bmi_calc
        form_save= form.save(commit=False)
        form_save.user= request.user
        form_save.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'bmi_result.html', {'bmi_calc':bmi_calc})

    return render(request, 'bmi_form.html', {'form': form})

def bmi_result(request):
    #physical=Physical.objects.order_by('user')[0]
    #bmi_calc=physical.weight/(physical.weight**2)
    return render(request, 'bmi_result.html')
