from django.shortcuts import render, redirect
from .models import Booking

def booking_view(request):
    if request.method == 'POST':
        id_number = request.POST.get('id_number')
        name = request.POST.get('name')
        pdl_number = request.POST.get('pdl_number')
        phone_number = request.POST.get('phone_number')
        country = request.POST.get('country')

        # Save to database
        Booking.objects.create(
            id_number=id_number,
            name=name,
            pdl_number=pdl_number,
            phone_number=phone_number,
            country=country
        )

        return redirect('booking_page')  # or redirect to success/payment

    return render(request, 'booking/booking_form.html', {'success': True})
