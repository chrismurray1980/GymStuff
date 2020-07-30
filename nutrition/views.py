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
        bmi_calc=round(weight/height**2, 2)   
        if (bmi_calc < 18.5):
            bmi_category='Underweight'
        elif (bmi_calc >= 18.5) and (bmi_calc < 25):
            bmi_category='Healthy'
        elif (bmi_calc >= 25) and (bmi_calc < 30):
            bmi_category='Overweight'
        elif (bmi_calc >= 30) and (bmi_calc < 35):
            bmi_category='Obese'   
        elif (bmi_calc >= 35) and (bmi_calc < 40):
            bmi_category='Severely obese'    
        elif (bmi_calc >= 40) and (bmi_calc < 50):
            bmi_category='Morbidly obese'
        elif (bmi_calc >= 50):
            bmi_category='Super obese'
        else:
            bmi_category='No data available'
        form_save= form.save(commit=False)
        form_save.user= request.user
        form_save.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'bmi_result.html', {'bmi_calc':bmi_calc, 'bmi_category':bmi_category})
    return render(request, 'bmi_form.html', {'form': form})

def bmi_result(request):
    return render(request, 'bmi_result.html')
    
    
