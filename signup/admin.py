from django.contrib import admin
from .models import WorkoutSession, Booking


@admin.register(WorkoutSession)
# create workout sessions in admin panel
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'instructor_name', 'day')  # Add 'day' to display


@admin.register(Booking)
# create booking opporunities based on the workout sessions in admin panel
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout_session')
    list_filter = ('user', 'workout_session')
