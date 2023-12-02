from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import WorkoutSession, Booking
from .forms import UserForm, BookingForm
# from django.views.generic.edit import FormView
# from django.db.models import IntegerField, Case, When, Value, F, CharField, Count
from django.contrib.auth.decorators import login_required
# from datetime import datetime
# from django.http import HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.template import RequestContext



class WorkoutSessionListView(generic.ListView):
    model = WorkoutSession
    queryset = WorkoutSession.objects.order_by("title")
    template_name = "index.html"

@login_required
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    context = {
        'user_bookings': user_bookings,
    }
    return render(request, 'my_bookings.html', context)

@login_required
def booking(request):
    print("booked_session")
    sessions = WorkoutSession.objects.all()  # Retrieve all workout sessions
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
        'sessions': sessions  # Include sessions in the context
    }
    return render(request, 'booking.html', context)


def book_session(request, session_id):
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
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=session_id)

        # Check if the user deleting the booking is the one who made the booking
        if booking.user == request.user:
            if request.method == "POST":
                booking.delete()
                # Redirect to my_bookings after deletion
                return redirect('my_bookings')  # Ensure 'my_bookings' is the correct URL name

            context = {'record': booking}
            return render(request, 'delete_booking.html', context)
        else:
            # Redirect if the user doesn't have permission to delete this booking
            return redirect('my_bookings')
    else:
        # Redirect if the user is not authenticated
        return redirect('../accounts/signup')


def home(request):
    workout_sessions = WorkoutSession.objects.all()
    return render(request, "index.html", {"workout_sessions": workout_sessions})






    



