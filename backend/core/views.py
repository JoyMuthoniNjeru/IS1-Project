from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TestSlotForm
from .forms import TestCenterForm
from .models import TestCenter
from django.contrib.auth.decorators import login_required
from .models import Booking

@login_required
def add_test_center(request):
    if request.method == 'POST':
        form = TestCenterForm(request.POST)
        if form.is_valid():
            test_centre = form.save(commit=False)
            test_centre.manager = request.user  # 👈 auto-assign logged-in manager
            test_centre.save()
            return redirect('testcentre_mgmt:test_centre_dashboard')
    else:
        form = TestCenterForm()
    return render(request, 'testcentre_mgmt/form.html', {'form': form, 'title': 'Add Test Centre'})

from django.contrib.auth.models import User
from .models import UserProfile

from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        email_or_id = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        # Try to authenticate existing user
        user = authenticate(request, username=email_or_id, password=password)

        if user is None:
            # Create new user if not found (for demo purposes)
            if not User.objects.filter(username=email_or_id).exists():
                user = User.objects.create_user(username=email_or_id, password=password)
                user.save()

                # Create profile and assign role
                UserProfile.objects.create(user=user, user_type=user_type)
            else:
                # User exists but wrong password → show error
                messages.error(request, "Incorrect password for existing user.")
                return redirect('/login/')
        else:
            # Ensure the user has a UserProfile
            profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                profile.user_type = user_type
                profile.save()

        # Log in the user
        login(request, user)

        # Redirect based on role
        role = user.userprofile.user_type
        if role == 'admin':
            return redirect('/admin-dashboard/')
        elif role == 'manager':
            return redirect('/testcentre/test-centres/')
        elif role == 'applicant':
            return redirect('/booking/')
        else:
            messages.error(request, 'Unknown user role.')
            return redirect('/login/')

    return render(request, 'loginPage.html')

@login_required
def admin_dashboard(request):
    if hasattr(request.user, 'userprofile') and request.user.userprofile.user_type == 'admin':
        bookings = Booking.objects.all().select_related('user', 'slot', 'slot__center')  # Get all confirmed bookings
        return render(request, 'admindashboard.html', {'bookings': bookings})
    else:
        return HttpResponse("Unauthorized", status=401)

@login_required
def slot_configuration(request):

    manager_centers = TestCenter.objects.filter(manager__userprofile__user_type='manager')
    
    if request.method == 'POST':
        form = TestSlotForm(request.POST, manager_centers=manager_centers)
        if form.is_valid():
            form.save()
            messages.success(request, 'Test slot created successfully.')
            return redirect('slot_configuration')
    else:
        form = TestSlotForm(manager_centers=manager_centers)

    return render(request, 'adminslotconfig.html', {'form': form})

@login_required
def add_slot(request):
    manager_centers = TestCenter.objects.filter(manager__userprofile__user_type='manager')

    if request.method == 'POST':
        form = TestSlotForm(request.POST, manager_centers=manager_centers)
        if form.is_valid():
            form.save()
            messages.success(request, 'Slot added successfully.')
            return redirect('slot_configuration')
    else:
        form = TestSlotForm(manager_centers=manager_centers)

    return render(request, 'adminslotform.html', {'form': form, 'title': 'Add Test Slot'})

def applicant_dashboard(request):
    return HttpResponse("Applicant Dashboard")

def manager_dashboard(request):
    return HttpResponse("Manager Dashboard")