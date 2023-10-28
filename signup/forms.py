# from .models import Comment
from django import forms
from .models import WorkoutSession
from django.contrib.auth.models import User


# User form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        labels = {
            'username': 'Username (cannot be changed)',
        }


"""
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
"""
