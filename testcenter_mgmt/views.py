from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import TestCenter
from .forms import TestCenterForm
from django.http import HttpResponse


# View dashboard with up to 3 test centres
@login_required
def test_center_dashboard(request):
    if request.user.userprofile.user_type == 'manager':
        centers = TestCenter.objects.filter(manager=request.user)
        return render(request, 'testcenter_mgmt/test_center_dashboard.html', {
            'centers': centers,
            'title': 'Your Test Centers'
        })
    return HttpResponse("Unauthorized", status=401)

# Add new test center
@login_required
def add_test_center(request):
    if request.user.userprofile.user_type != 'manager':
        return HttpResponse("Unauthorized", status=401)

    if request.method == 'POST':
        form = TestCenterForm(request.POST)
        if form.is_valid():
            center = form.save(commit=False)
            center.manager = request.user  
            center.save()
            return redirect('testcenter_mgmt:test_center_dashboard')
    else:
        form = TestCenterForm()
    
    return render(request, 'testcenter_mgmt/form.html', {
        'form': form,
        'title': 'Add Test Center'
    })

# Edit existing test center
def edit_test_center(request, pk):
    center = get_object_or_404(TestCenter, pk=pk)
    if request.method == 'POST':
        form = TestCenterForm(request.POST, instance=center)
        if form.is_valid():
            form.save()
            return redirect('testcenter_mgmt:test_center_dashboard')
    else:
        form = TestCenterForm(instance=center)
    return render(request, 'testcenter_mgmt/form.html', {'form': form, 'title': 'Edit Test Center'})

# Delete test center
def delete_test_center(request, pk):
    center = get_object_or_404(TestCenter, pk=pk)
    if request.method == 'POST':
        center.delete()
        return redirect('testcenter_mgmt:test_center_dashboard')
    return render(request, 'testcenter_mgmt/confirm_delete.html', {'center': center})
