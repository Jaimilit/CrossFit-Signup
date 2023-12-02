from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import WorkoutSession, Booking
from .forms import UserForm, BookingForm
from django.contrib.auth.decorators import login_required

class WorkoutSessionListView(generic.ListView):
    """This view renders the index.html page and extends the base.html page"""
    model = WorkoutSession
    queryset = WorkoutSession.objects.order_by("title")
    template_name = "index.html"

"""ensure authenticated users can access this view of booking options"""
@login_required
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    context = {
        'user_bookings': user_bookings,
    }
    return render(request, 'my_bookings.html', context)


"""retreives workout sessions from the database, it associates the booking with the current authenticated user"""
@login_required
def booking(request):
    sessions = WorkoutSession.objects.all()  
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()

            messages.success(request, 'Booking is confirmed')
            return redirect('booking_success')
    else:
        form = BookingForm()

    context = {
        'form': form,
        'sessions': sessions  
    }
    return render(request, 'booking.html', context)


def book_session(request, session_id):
    """this allows the user to book a session and tells the user if they have already booked that session or if they have booked successfully"""
    if request.user.is_authenticated:
        session_to_be_booked = get_object_or_404(WorkoutSession, pk=session_id)
        user = request.user

        # Check if the user has already booked this session
        existing_booking = Booking.objects.filter(user=user, workout_session=session_to_be_booked).first()
        if existing_booking:
            context = {'booked_session': session_to_be_booked}
            return render(request, 'already_booked.html', context)

        # Check if there are available spots before booking
        else:
            booking = Booking(user=user, workout_session=session_to_be_booked)
            booking.save()
            context = {
                'booked_session': session_to_be_booked,
            }
            return render(request, 'booking_success.html', context)
    else:
        return redirect('../accounts/signup')


def delete_booking(request, session_id):
    """ this allows the user to delete a booking, send them to the delete booking page to check if they want to delete
    a session or go back to the my bookings page"""
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=session_id)

        if booking.user == request.user:
            if request.method == "POST":
                booking.delete()
                
                return redirect('my_bookings')  

            context = {'record': booking}
            return render(request, 'delete_booking.html', context)
        else:
            return redirect('my_bookings')
    else:
        return redirect('../accounts/signup')


def home(request):
    """ creates index of workout sessions """
    workout_sessions = WorkoutSession.objects.all()
    return render(request, "index.html", {"workout_sessions": workout_sessions})
