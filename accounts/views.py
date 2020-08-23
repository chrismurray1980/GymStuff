# Import libraries and forms
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required


# Index view
def index(request):
    # Display the index page
    return render(request, "index.html")

# Logout functionality
def logout(request):
    # Log out user
    auth.logout(request)
    # Inform user of logout
    messages.success(request, 'You have successfully logged out')
    # Display the index page
    return redirect(reverse('index'))

# Login functionality
def login(request):
    # Login form functionality
    if request.method == 'POST':
        # Create user form
        user_form = UserLoginForm(request.POST)
        # Validate user form
        if user_form.is_valid():
            # Authenticate user
            user = auth.authenticate(request.POST['username_or_email'],
                                     password=request.POST['password'])
            # If user valid
            if user:
                # Login user
                auth.login(request, user)
                # Inform user that login successful
                messages.error(request, "You have successfully logged in")
                # Pass user to requested page
                if request.GET and request.GET['next'] !='':
                    next = request.GET['next']
                    return HttpResponseRedirect(next)
                # Pass user to index if no requested page
                else:
                    return redirect(reverse('index'))
            # Inform user that login details incorrect
            else:
                user_form.add_error(None, "Your username or password are incorrect")
    # Reload user login form
    else:
        user_form = UserLoginForm()
    args = {'user_form': user_form, 'next': request.GET.get('next', '')}
    # Render user login page
    return render(request, 'login.html', args)

# Register functionality
def register(request):
    # User registration
    if request.method == 'POST':
        # Create instance of registration form
        user_form = UserRegistrationForm(request.POST)
        # Validate form
        if user_form.is_valid():
            user_form.save()
            # Authenticate user
            user = auth.authenticate(request.POST.get('email'),
                                     password=request.POST.get('password1'))
            # Confirm registration successful
            if user:
                # Authorise user
                auth.login(request, user)
                # Inform user of succesful registration
                messages.success(request, "You have successfully registered")
                # Return user to index page
                return redirect(reverse('index'))
            # Inform user of unsuccessful registration
            else:
                messages.error(request, "unable to log you in at this time!")
    # Reload registration form
    else:
        user_form = UserRegistrationForm()
    args = {'user_form': user_form}
    # Render registration page
    return render(request, 'register.html', args)

