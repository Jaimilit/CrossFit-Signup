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


def post(self, request, slug, *args, **kwargs):

        workout_sessions = WorkoutSession.objects.filter(status=1)
        session = get_object_or_404(workout_sessions, slug=slug)
        instructor = session.session_creator
        signed_up_count = session.attendees.count()

        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_form.instance.email = request.user.email
            user_form.instance.name = request.user.username
            user.post = post
            user.save()
        else:
            user_form = UserForm()

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

def booking(request):
    # Your view logic here
    return render(request, 'booking.html')


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

def post(self, request, slug, *args, **kwargs):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
     comments = post.comments.filter(approved=True).order_by("-created_on")
      liked = False
       if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )
"""
