from django.shortcuts import render, redirect
from .models import Payment
from .forms import PaymentForm
from booking.models import Booking

def payment_form(request):
    booking = Booking.objects.last()  # Replace with real booking logic

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking

            if payment.amount < 1050:
                form.add_error('amount', 'Amount must be at least KES 1050')
            else:
                payment.save()
                return redirect('payment:payment_success')
    else:
        form = PaymentForm()

    return render(request, 'payment/payment_form.html', {'form': form})

def payment_success(request):
    return render(request, 'payment/payment_success.html')