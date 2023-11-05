from django.contrib import admin
from .models import WorkoutSession
from django_summernote.admin import SummernoteModelAdmin


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(SummernoteModelAdmin):
    list_display = ('title', 'date', 'time', 'instructor_name')
    search_fields = ['title', 'content']
    list_filter = ('date', 'session_creator')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


"""
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
