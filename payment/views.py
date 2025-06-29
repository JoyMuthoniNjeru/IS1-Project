from django.shortcuts import render, redirect, get_object_or_404
from .models import Payment
from .forms import PaymentForm
from booking.models import Booking

def payment_form(request):
    booking_id = request.GET.get('booking_id')
    if not booking_id:
        return render(request, 'payment/payment_form.html', {
            'error': 'No booking ID provided.'
        })
    
    booking = get_object_or_404(Booking, id=booking_id) if booking_id else None

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            if amount < 1050:
                return render(request, 'payment/payment_form.html', {
                    'form': form,
                    'error': 'Amount must be at least KES 1050.',
                    'booking_id': booking_id
                })

            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            return redirect('payment:payment_success')
    else:
        form = PaymentForm()

    return render(request, 'payment/payment_form.html', {
        'form': form,
        'booking_id': booking_id
    })

def payment_success(request):
    return render(request, 'payment/payment_success.html')