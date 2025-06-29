from django.shortcuts import render, redirect
from .models import Booking


def booking_view(request):
    if request.method == 'POST':
        
        print("POST DATA:", request.POST)  
        print("FILES:", request.FILES) 
        print("FORM DATA:", request.POST)
        
    

        id_number = request.POST.get('id_number')
        print("ID NUMBER:", id_number)     


        booking = Booking.objects.create(
            id_number=request.POST.get('id_number'),
            name=request.POST.get('name'),
            pdl_number=request.POST.get('pdl_number'),
            gender=request.POST.get('gender'),
            date_of_birth=request.POST.get('date_of_birth'),
            nationality=request.POST.get('nationality'),
            country=request.POST.get('country'),
            mobile=request.POST.get('mobile'),
            email=request.POST.get('email'),
            license_type=request.POST.get('license_type'),
            test_date=request.POST.get('test_date'),
            time_slot=request.POST.get('time_slot'),
            document=request.FILES.get('document')
        )

        return redirect(f'/payment/?booking_id={booking.id}')

    return render(request, 'booking/booking_form.html')
