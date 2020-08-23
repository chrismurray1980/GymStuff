# Import libraries, models and forms
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from physical.forms import bmi, macro
from .models import Physical, Macro
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
import datetime
import json

# Bmi form view
@login_required
def bmi_form(request):
    # Create instance of form
    form = bmi(request.POST)
    # Validate form 
    if form.is_valid():
        # Get data from form
        height = form.cleaned_data['height']
        weight = form.cleaned_data['weight']
        unit_type = form.cleaned_data['unit_type']
        # Create instance of model 
        physical = Physical()
        # Assign values to model instance
        physical.height= height
        physical.weight= weight
        physical.unit_type = unit_type
        physical.date_now = datetime.datetime.now()
        form_save= form.save(commit=False)
        form_save.user= request.user
        # Save created instance
        form_save.save()
        # Search database for model instance
        details = Physical.objects.filter(user=request.user).order_by('-date_now')[:1]
        # Render result with model instance
        return render(request, 'bmi_result.html', {'details':details})
        # Render bmi form
    return render(request, 'bmi_form.html', {'form': form})

# Create BMI results view
def bmi_result(request):
    return render(request, 'bmi_result.html')

# Macro form   
@login_required
def macro_form(request):
    # Create form instance
    form = macro(request.POST)
    # Validate form
    if form.is_valid():
        # Get form data
        height = form.cleaned_data['height']
        weight = form.cleaned_data['weight']
        age = form.cleaned_data['age']
        activity_level = form.cleaned_data['activity_level']
        aim = form.cleaned_data['aim']
        # Create model instance
        macro_calc = Macro()
        # Assign data to model instance
        macro_calc.height= height
        macro_calc.weight= weight
        macro_calc.age = age
        macro_calc.activity_level = activity_level
        macro_calc.aim = aim
        form_save= form.save(commit=False)
        form_save.user= request.user
        # Save model instance
        form_save.save()
        # Search database for model instance 
        details = Macro.objects.filter(user=request.user).order_by('-date')[:1]
        # Extract weight and percentage data from macro database search
        for item in details:
            carb_weight = item.carb_weight
            protein_weight = item.protein_weight
            fat_weight = item.fat_weight
            carb_percent = 100*item.carb_percent
            protein_percent = 100*item.protein_percent
            fat_percent = 100*item.fat_percent
        # Create macro array
        macros = [carb_weight, protein_weight, fat_weight, carb_percent, protein_percent, fat_percent]
        # Convert array to JSON
        macros_json = json.dumps(macros)
        # Render macro results page passing details and macro_json as arguments
        return render(request, 'macro_result.html', {'details': details, 'macros': macros_json})
    # Render macro form
    return render(request, 'macro_form.html', {'form': form})    

# Create macro results view   
def macro_result(request):
    return render(request, 'macro_result.html')
