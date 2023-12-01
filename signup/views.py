from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import WorkoutSession, Booking
from .forms import UserForm, BookingForm
from django.views.generic.edit import FormView
from django.db.models import IntegerField, Case, When, Value, F, CharField, Count
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.http import HttpResponse
from django.contrib import messages


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
        # Retrieve the booked session based on the session_id
        session_to_be_booked = get_object_or_404(WorkoutSession, pk=session_id) # Get get session based on ID
        booking = Booking(user=request.user, workout_session=session_to_be_booked)  # create a booking from the user and the session
        booking.save()  # save the booking in the database
        context = {
            'booked_session': session_to_be_booked,  # Pass the booked session to the template       # Send data to next page using context
        }
        return render(request, 'booking_success.html', context)
    else:
        return redirect('../accounts/signup')

def change_booking(request, session_id):
    booking = get_object_or_404(Booking, id=session_id)
    session = booking.workout_session
    user_bookings = Booking.objects.filter(user=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'You successfully updated your booking.')
            return redirect('my_bookings')  # Redirect to the my_bookings page
    else:
        form = BookingForm(instance=booking)

    context = {
        'form': form,
        'booked_session': session,
        'user_bookings': user_bookings,
    }
    return render(request, 'my_bookings.html', context)


def delete_booking(request, session_id):
    """
    Function enables user to delete a booking record
    """
    booking = get_object_or_404(Booking, id=session_id)
    session = booking.workout_session
    user_bookings = Booking.objects.filter(user=request.user)
    record = get_object_or_404(Booking, id=session_id)
    
    if request.method == "POST":
        form = BookingForm(request.POST, instance=record)
        if record.delete():
            messages.success(request, 'Your booking has been deleted.')
            return redirect('my_bookings')

    form = BookingForm(instance=record)
    context = {
        'form': form, 'record': record}
    return render(request, 'delete_booking.html', context)

"""
def delete_booking(request, session_id):
    booking = get_object_or_404(Booking, id=session_id)
    session = booking.workout_session
    user_bookings = Booking.objects.filter(user=request.user)
    
    if request.method == "POST":
        session_id = request.POST.get('session_id')
        record = get_object_or_404(Booking, id=session_id)
        record.delete()
        messages.success(request, 'Your booking has been deleted.')
        return redirect('my_bookings')  # Redirect to the bookings list

        context = {
        'form': form,
        'booked_session': session,
        'user_bookings': user_bookings,
        'record': record,
    }

    return render(request, 'delete_booking.html', context, {'record': record})

"""

def home(request):
    workout_sessions = WorkoutSession.objects.all()
    return render(request, "index.html", {"workout_sessions": workout_sessions})


"""
def change_booking(request, session_id):
    
    booking = get_object_or_404(Booking, id=session_id)
    session = booking.workout_session
    user_bookings = Booking.objects.filter(user=request.user)
    context = {
            'booked_session': session,  # Pass the booked session to the template       # Send data to next page using context
            'user_bookings': user_bookings, # All bookings related to the user
        }
    return render(request, 'my_bookings.html', context)
"""



    



