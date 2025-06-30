from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TestSlotForm

def login_view(request):
    if request.method == 'POST':
        email_or_id = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        user = authenticate(request, username=email_or_id, password=password)
        if user is not None:
            login(request, user)
            try:
                role = user.userprofile.user_type

                if role == 'admin':
                    return redirect('/admin-dashboard/')
                elif role == 'manager':
                    return redirect('/testcentre/test-centres/')
                elif role == 'applicant':
                    return redirect('/booking/')
                else:
                    messages.error(request, 'Unknown user role.')
            except UserProfile.DoesNotExist:
                messages.error(request, 'User profile not found.')
            else:
                messages.error(request, 'Invalid login credentials.')

    return render(request, 'loginPage.html')

@login_required
def admin_dashboard(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.user_type == 'admin':
        return render(request, 'admindashboard.html')
    else:
        return HttpResponse("Unauthorized", status=401)
    
@login_required
def slot_configuration(request):
    if request.method == 'POST':
        form = TestSlotForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Test slot created successfully.')
            return redirect('admin_dashboard')
    else:
        form = TestSlotForm()
    return render(request, 'adminslotconfig.html', {'form': form})

def applicant_dashboard(request):
    return HttpResponse("Applicant Dashboard")

def manager_dashboard(request):
    return HttpResponse("Manager Dashboard")