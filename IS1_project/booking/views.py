from django.shortcuts import render, redirect
from .forms import ApplicantForm, BookingForm, PaymentForm

def booking_view(request):
    if request.method == 'POST':
        applicant_form = ApplicantForm(request.POST)
        booking_form = BookingForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if applicant_form.is_valid() and booking_form.is_valid() and payment_form.is_valid():
            applicant = applicant_form.save()
            booking = booking_form.save(commit=False)
            booking.applicant = applicant
            booking.save()

            payment = payment_form.save(commit=False)
            payment.applicant = applicant
            payment.save()

            return redirect('booking_success')  # you'll create this page later
    else:
        applicant_form = ApplicantForm()
        booking_form = BookingForm()
        payment_form = PaymentForm()

    return render(request, 'booking/booking_form.html', {
        'applicant_form': applicant_form,
        'booking_form': booking_form,
        'payment_form': payment_form
    })

