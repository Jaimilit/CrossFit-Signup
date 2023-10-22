from django.shortcuts import render
from django.views import generic
from .models import WorkoutSession


class WorkoutSession(generic.ListView):
    model = WorkoutSession
    # queryset = WorkoutSession.objects.filter(status=1).order_by("-created_on")
    queryset = WorkoutSession.objects.order_by("date")
    template_name = "index.html"
    paginate_by = 6


"""
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6
"""
