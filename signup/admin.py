from django.contrib import admin
from .models import WorkoutSession
from django_summernote.admin import SummernoteModelAdmin


@admin.register(WorkoutSession)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
