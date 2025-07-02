from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import TestCentre
from .forms import TestCentreForm
from django.http import HttpResponse


# View dashboard with up to 3 test centres
@login_required
def test_centre_dashboard(request):
    if request.user.userprofile.user_type == 'manager':
        centers = TestCentre.objects.filter(manager=request.user)
        return render(request, 'testcentre_mgmt/test_centre_dashboard.html', {
            'centers': centers,
            'title': 'Your Test Centers'
        })
    return HttpResponse("Unauthorized", status=401)

# Add new test centre
@login_required
def add_test_center(request):
    if request.user.userprofile.user_type != 'manager':
        return HttpResponse("Unauthorized", status=401)

    if request.method == 'POST':
        form = TestCentreForm(request.POST)
        if form.is_valid():
            center = form.save(commit=False)
            center.manager = request.user  
            center.save()
            return redirect('testcentre_mgmt:test_centre_dashboard')
    else:
        form = TestCentreForm()
    
    return render(request, 'testcentre_mgmt/form.html', {
        'form': form,
        'title': 'Add Test Center'
    })

# Edit existing test centre
def edit_test_centre(request, pk):
    centre = get_object_or_404(TestCentre, pk=pk)
    if request.method == 'POST':
        form = TestCentreForm(request.POST, instance=centre)
        if form.is_valid():
            form.save()
            return redirect('testcentre_mgmt:test_centre_dashboard')
    else:
        form = TestCentreForm(instance=centre)
    return render(request, 'testcentre_mgmt/form.html', {'form': form, 'title': 'Edit Test Centre'})

# Delete test centre
def delete_test_centre(request, pk):
    centre = get_object_or_404(TestCentre, pk=pk)
    if request.method == 'POST':
        centre.delete()
        return redirect('testcentre_mgmt:test_centre_dashboard')
    return render(request, 'testcentre_mgmt/confirm_delete.html', {'centre': centre})
