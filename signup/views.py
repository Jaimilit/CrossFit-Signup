from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import WorkoutSession
from .forms import UserForm


class WorkoutSession(generic.ListView):
    model = WorkoutSession
    # queryset = WorkoutSession.objects.filter(status=1).order_by("-created_on")
    queryset = WorkoutSession.objects.order_by("date")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        workout_sessions = WorkoutSession.objects.filter(status=1)
        session = get_object_or_404(workout_sessions, slug=slug)
        instructor = session.session_creator
        signed_up_count = session.attendees.count()

        return render(
            request,
            "post_detail.html",
            {
                "session": session,
                "instructor": instructor,
                "signed_up_count": signed_up_count,
                "user_form": UserForm()
            },
        )


"""
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )
"""
