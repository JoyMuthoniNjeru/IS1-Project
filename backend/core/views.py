from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile

def login_view(request):
    if request.method == 'POST':
        email_or_id = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email_or_id, password=password)
        if user is not None:
            login(request, user)
            role = user.userprofile.role

            if role == 'admin':
                return redirect('/admin-dashboard/')
            elif role == 'manager':
                return redirect('/manager-dashboard/')
            elif role == 'applicant':
                return redirect('/booking/')
            else:
                messages.error(request, 'Unknown user role.')
        else:
            messages.error(request, 'Invalid credentials.')

    return render(request, 'loginPage.html')