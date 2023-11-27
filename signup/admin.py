from django.contrib import admin
from django.db.models import Case, When, Value, CharField  # Import CharField
from .models import WorkoutSession
from datetime import datetime


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'time', 'instructor_name', 'day')  # Add 'day' to display

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        current_day = datetime.now().strftime('%A')  # Get the current day as a string (e.g., 'Monday', 'Tuesday', etc.)
        return qs.filter(day=current_day)

"""
    def day_of_week(self, obj):
        # Map the day of the week
        return (
            Case(
                When(date__week_day=1, then=Value("Monday")),
                When(date__week_day=2, then=Value("Tuesday")),
                When(date__week_day=3, then=Value("Wednesday")),
                When(date__week_day=4, then=Value("Thursday")),
                When(date__week_day=5, then=Value("Friday")),
                When(date__week_day=6, then=Value("Saturday")),
                When(date__week_day=7, then=Value("Sunday")),
                output_field=CharField(),
            )
        )

    day_of_week.short_description = 'Day of the Week'


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
"""
