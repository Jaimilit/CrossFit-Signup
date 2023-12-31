from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import WorkoutSession, Booking
from .forms import UserForm, BookingForm, BookingNoteForm
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Concat
from django.db.models import Case, When, Value, IntegerField
from django.contrib import messages


class WorkoutSessionListView(generic.ListView):
    """This view renders the index.html page and extends the base.html page"""
    model = WorkoutSession
    queryset = WorkoutSession.objects.order_by("title")
    template_name = "index.html"


@login_required
def my_bookings(request):
    """Ensure authenticated users can access this view of booking options.
        Also orders the list of bookings first by day and then by time"""
    day_mapping = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7
    }

    day_conditions = [
        When(workout_session__day=day, then=Value(num))
        for day, num in day_mapping.items()
    ]

    user_bookings = Booking.objects.filter(user=request.user).annotate(
        day_numeric=Case(
            *day_conditions,
            output_field=IntegerField()
        )
    ).order_by('day_numeric', 'workout_session__time')

    context = {
        'user_bookings': user_bookings,
    }

    return render(request, 'my_bookings.html', context)


@login_required
def booking(request):
    """Retreives workout sessions from the database, it associates
    the booking with the current authenticated user"""
    sessions = WorkoutSession.objects.order_by('time')

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
    """This allows the user to book a session and tells the user
    if they have already booked that session or if they have booked
    successfully. Also calculates spaces available for booking"""
    if request.user.is_authenticated:
        session_to_be_booked = get_object_or_404(WorkoutSession, pk=session_id)
        user = request.user

        # Check if the user has already booked this session
        existing_booking = Booking.objects.filter(
            user=user, workout_session=session_to_be_booked
        ).first()
        if existing_booking:
            context = {'booked_session': session_to_be_booked}
            return render(request, 'already_booked.html', context)

        # Check if are available spots before booking
        if (
            session_to_be_booked.available_spots >
            session_to_be_booked.booked_spots
        ):
            session_to_be_booked.booked_spots += 1
            session_to_be_booked.save()
            booking = Booking(user=user, workout_session=session_to_be_booked)
            booking.save()
            context = {
                'booked_session': session_to_be_booked,
            }
            return render(request, 'booking_success.html', context)
        else:
            context = {
                'message': 'Error',
                'next_page': 'booking.html'
            }
            return render(request, 'error.html', context)
    else:
        return redirect('../accounts/signup')


def edit_booking(request, booking_id):
    """ User can edit booking with a note"""
    if request.user.is_authenticated:
        booking_to_edit = get_object_or_404(
            Booking,
            id=booking_id,
            user=request.user
        )

        if booking_to_edit.user == request.user:
            if request.method == 'POST':
                form = BookingNoteForm(request.POST, instance=booking_to_edit)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Note has been updated')
                    return redirect('my_bookings')
            else:
                form = BookingNoteForm(instance=booking_to_edit)

            context = {
                'form': form,
                'booking_to_edit': booking_to_edit,
            }
            return render(request, 'edit_booking.html', context)
        else:
            return redirect('my_bookings')
    else:
        return redirect('../accounts/signup')


def delete_booking(request, session_id):
    """ this allows the user to delete a booking, send them to the
    delete booking page to check if they want to delete
    a session or go back to the my bookings page.
    Also recalculates spots available"""
    if request.user.is_authenticated:
        booking = get_object_or_404(Booking, id=session_id)

        if booking.user == request.user:
            if request.method == "POST":
                booking.workout_session.booked_spots -= 1
                booking.workout_session.save()
                booking.delete()
                return redirect('my_bookings')

            context = {'record': booking}
            return render(request, 'delete_booking.html', context)
        else:
            return redirect('my_bookings')
    else:
        return redirect('../accounts/signup')


def home(request):
    """ Creates index of workout sessions """
    workout_sessions = WorkoutSession.objects.all()
    return render(request, "index.html", {
        "workout_sessions": workout_sessions
        })
