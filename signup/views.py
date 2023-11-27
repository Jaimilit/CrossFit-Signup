from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import WorkoutSession
from .forms import UserForm
from .forms import BookingForm
from django.views.generic.edit import FormView
from django.db.models.functions import ExtractDay, ExtractMonth
from django.db.models import IntegerField, Case, When, Value
from django.db.models import F
from django.db.models import CharField
from django.db.models import Value
from django.http import HttpResponse

class WorkoutSessionListView(generic.ListView):
    model = WorkoutSession
    queryset = WorkoutSession.objects.order_by("title")  # Change "title" to the field you want to order by
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        session = get_object_or_404(WorkoutSession, slug=slug)
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
        session = get_object_or_404(WorkoutSession, slug=slug)
        instructor = session.session_creator
        signed_up_count = session.attendees.count()

        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.email = request.user.email
            user.name = request.user.username
            user.session = session  # Associate the user with the session
            user.save()
            return redirect("post_detail", slug=slug)
        else:
            return render(
                request,
                "post_detail.html",
                {
                    "session": session,
                    "instructor": instructor,
                    "signed_up_count": signed_up_count,
                    "user_form": user_form,
                },
            )


def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            selected_session = form.cleaned_data["session"]
            booking = Booking(user=request.user, session=selected_session)
            booking.save()
            # You can add more booking logic here

    else:
        form = BookingForm()

    sessions = WorkoutSession.objects.all()
    context = {"form": form, "sessions": sessions}
    return render(request, "booking.html", context)


def home(request):
    # Modify the query to suit your needs
    workout_sessions = WorkoutSession.objects.all()
    return render(request, "index.html", {"workout_sessions": workout_sessions})


class BookingView(View):
    def get(self, request):
        # Fetch sessions grouped by day and sorted by time
        sessions = WorkoutSession.objects.annotate(
            day=ExtractDay('date', output_field=IntegerField()),
            month=ExtractMonth('date', output_field=IntegerField())
        ).annotate(
            day_name=Case(
                When(day=1, then=Value("Monday")),
                When(day=2, then=Value("Tuesday")),
                When(day=3, then=Value("Wednesday")),
                When(day=4, then=Value("Thursday")),
                When(day=5, then=Value("Friday")),
                When(day=6, then=Value("Saturday")),
                When(day=7, then=Value("Sunday")),
                default=Value("Unknown"),
                output_field=CharField()
            )
        ).order_by('day', 'time')

        # Group sessions by day
        sessions_by_day = {}
        for session in sessions:
            if session.day_name not in sessions_by_day:
                sessions_by_day[session.day_name] = []
            # Limit to 4 sessions per day
            if len(sessions_by_day[session.day_name]) < 4:
                sessions_by_day[session.day_name].append(session)

        context = {'sessions_by_day': sessions_by_day}
        return render(request, 'booking.html', context)


def book_session(request, session_id):
    # Placeholder logic, replace with your actual view logic
    return HttpResponse(f"Booking session {session_id}")

"""
def gym_session_booking(request):
    sessions = GymSession.objects.all()
    if request.method == "POST":
        form = GymSessionBookingForm(request.POST)
        if form.is_valid():
            # Process the form data and save the booking
            return redirect("home")  # Replace with your success page

    else:
        form = GymSessionBookingForm()

    return render(
        request, "booking_page.html", {"form": form, "sessions": sessions}
    )


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
