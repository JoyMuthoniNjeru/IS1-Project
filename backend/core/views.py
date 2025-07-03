from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import UserProfile
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import TestSlotForm
from .forms import TestSlot
from .forms import TestCenterForm
from .models import TestCenter
from django.contrib.auth.decorators import login_required
from .models import Booking
from core.models import TestCenter, TestSlot
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
            return redirect('/testcenter/test-centers/')
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
    manager_centers = TestCenter.objects.exclude(manager__isnull=True).filter(manager__userprofile__user_type='manager')

    centers = TestCenter.objects.filter(manager__userprofile__user_type='manager')
    slots = TestSlot.objects.all()
    
    if request.method == 'POST':
        form = TestSlotForm(request.POST, manager_centers=manager_centers)
        if form.is_valid():
            form.save()
            messages.success(request, 'Test slot created successfully.')
            return redirect('slot_configuration')
    else:
        form = TestSlotForm(manager_centers=manager_centers)

    slots = TestSlot.objects.all()
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

@login_required
def edit_slot(request, pk):
    slot = get_object_or_404(TestSlot, pk=pk)
    if request.method == 'POST':
        form = TestSlotForm(request.POST, instance=slot)
        if form.is_valid():
            form.save()
            return redirect('slot_configuration')
    else:
        form = TestSlotForm(instance=slot)
    return render(request, 'adminslotform.html', {'form': form, 'title': 'Edit Test Slot'})

@login_required
def delete_slot(request, pk):
    slot = get_object_or_404(TestSlot, pk=pk)
    if request.method == 'POST':
        slot.delete()
        return redirect('slot_configuration')
    return render(request, 'confirm_delete.html', {'slot': slot})

def applicant_dashboard(request):
    return HttpResponse("Applicant Dashboard")

def manager_dashboard(request):
    return HttpResponse("Manager Dashboard")