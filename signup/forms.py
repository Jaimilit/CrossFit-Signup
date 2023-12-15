from django import forms
from .models import WorkoutSession, Booking
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    """create form for user"""
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        labels = {
            'username': 'Username (cannot be changed)',
        }


class BookingForm(forms.ModelForm):
    """create form for booking for user"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['workout_session'].queryset = WorkoutSession.objects.all()

    class Meta:
        model = Booking
        fields = '__all__'
        labels = {
            'user': 'Username',
            'workout_session': 'Workout Session',
            'note': 'Note',  
        }
