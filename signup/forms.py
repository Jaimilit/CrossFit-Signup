# from .models import Comment
from django import forms
from .models import WorkoutSession
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.forms.widgets import RadioSelect  # Add this import

# from .models import GymSession


# User form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
        labels = {
            'username': 'Username (cannot be changed)',
        }

# Add custom fields to the allauth signup form

class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=50, label='First Name')
    last_name = forms.CharField(max_length=50, label='Last Name')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()

        return user


class BookingForm(forms.Form):
    session = forms.ModelChoiceField(
        queryset=WorkoutSession.objects.all(),
        empty_label=None,  # Remove the "Select a session" option
        widget=RadioSelect,  # Use RadioSelect widget
    )



"""
class GymSessionBookingForm(forms.Form):
    session_choices = forms.ModelChoiceField(
        queryset=GymSession.objects.all(),
        empty_label="Select a session",
        widget=forms.RadioSelect,
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
"""
