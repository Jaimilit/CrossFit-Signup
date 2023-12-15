from django.contrib import admin
from .models import WorkoutSession, Booking


@admin.register(WorkoutSession)
# Create workout sessions in admin panel
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'time',
        'instructor_name',
        'day',
        'available_spots',
        'booked_spots'
    )


@admin.register(Booking)
# Create booking opporunities based on the workout sessions in admin panel
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout_session', 'note')
    list_filter = ('user', 'workout_session')
