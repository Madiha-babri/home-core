from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Consultant, Booking
from django.utils import timezone

@login_required
def create_booking(request, consultant_id):
    consultant = Consultant.objects.get(id=consultant_id)
    
    if request.method == 'POST':
        consultation_date = request.POST['consultation_date']
        notes = request.POST.get('notes', '')
        
        booking = Booking.objects.create(
            user=request.user,
            consultant=consultant,
            consultation_date=consultation_date,
            notes=notes,
            status='PENDING'
        )
        return redirect('booking_detail', booking_id=booking.id)

    return render(request, 'create_booking.html', {'consultant': consultant})

