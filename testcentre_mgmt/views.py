from django.shortcuts import render, redirect, get_object_or_404
from .models import TestCentre
from .forms import TestCentreForm

# View dashboard with up to 3 test centres
def test_centre_dashboard(request):
    centres = TestCentre.objects.all()[:3]
    return render(request, 'testcentre_mgmt/test_centre_dashboard.html', {'centres': centres})

# Add new test centre
def add_test_centre(request):
    if request.method == 'POST':
        form = TestCentreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testcentre_mgmt:test_centre_dashboard')
    else:
        form = TestCentreForm()
    return render(request, 'testcentre_mgmt/form.html', {'form': form, 'title': 'Add Test Centre'})

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
