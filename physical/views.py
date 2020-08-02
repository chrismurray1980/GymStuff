from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from physical.forms import bmi, macro
from .models import Physical, Macro
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
        physical.date_now = datetime.datetime.now()
        form_save= form.save(commit=False)
        form_save.user= request.user
        form_save.save()
        details = Physical.objects.filter(user=request.user).order_by('-date_now')[:1]
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'bmi_result.html', {'details':details})
    return render(request, 'bmi_form.html', {'form': form})

def bmi_result(request):
    physical= Physical.object.get(user=request.user)[:1]
    return render(request, 'bmi_result.html',{'physical':physical.id})
    
@login_required
def macro_form(request):
    form = macro(request.POST)
    if form.is_valid():
        height = form.cleaned_data['height']
        weight = form.cleaned_data['weight']
        age = form.cleaned_data['age']
        activity_level = form.cleaned_data['activity_level']
        aim = form.cleaned_data['aim']
        macro_calc = Macro()
        macro_calc.height= height
        macro_calc.weight= weight
        macro_calc.age = age
        macro_calc.activity_level = activity_level
        macro_calc.aim = aim
        form_save= form.save(commit=False)
        form_save.user= request.user
        form_save.save()
        details = Macro.objects.filter(user=request.user).order_by('-date')[:1]
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return render(request, 'macro_result.html', {'details': details})
    return render(request, 'macro_form.html', {'form': form})    
    
def macro_result(request):
    return render(request, 'macro_result.html')
