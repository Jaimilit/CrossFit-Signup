from django.contrib import admin
from .models import WorkoutSession, Booking


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'instructor_name', 'day')  # Add 'day' to display


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'workout_session')
    list_filter = ('user', 'workout_session')
