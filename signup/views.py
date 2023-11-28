from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import WorkoutSession, Booking
from .forms import UserForm, BookingForm
from django.views.generic.edit import FormView
from django.db.models import IntegerField, Case, When, Value, F, CharField, Count
from datetime import datetime


class WorkoutSessionListView(generic.ListView):
    model = WorkoutSession
    queryset = WorkoutSession.objects.order_by("title")  # Change "title" to the field you want to order by
    template_name = "index.html"
    # paginate_by = 6


"""
class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        session = get_object_or_404(WorkoutSession, slug=slug)
        instructor = session.session_creator
       # signed_up_count = session.attendees.count()
        return render(
            request,
            "post_detail.html",
            {
                "title": title,
                "instructor": instructor,
                "day":day,
                "time":time,
              #  "signed_up_count": signed_up_count,
               # "user_form": UserForm(),
                "booking_form":BookingForm,
            },
        )

    def post(self, request, slug, *args, **kwargs):
        session = get_object_or_404(WorkoutSession, slug=slug)
        instructor = session.session_creator
       # signed_up_count = session.attendees.count()

        bookingform = BookingForm(data=request.POST)

        if bookingform.is_valid():
            bookingform.instance.email = request.user.email
            bookingform.instance.name = request.user.username
            booking = bookingform.save
            booking.save()

        else:
            bookingform = BookingForm()

            return render(
                request,
                "post_detail.html",
                {
                    "title": title,
                    "instructor": instructor,
                    "day":day,
                    "time":time,
              #  "signed_up_count": signed_up_count,
               # "user_form": UserForm(),
                    "booking_form":BookingForm,
                },
            )
"""
def booking(request):
    sessions = WorkoutSession.objects.all()  # Fetch all available workout sessions
    context = {'sessions': sessions}
    return render(request, 'booking.html', context)

"""
def booking(request):

    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.session_title = session.title
            booking_form.session_time = session.time
            booking_form.session_day = session.day
            booking_form.session_instructor = session.instructor_name
            booking_form.save()
            messages.success(request, 'Your Workout is Booked')
            return redirect('booking.html')
    else:
        initial_data = {
            'session_title': session.title,
            'session_time': session.time,
            'session_day': session.day,
            'session_instructor': session.instructor_name
        }
        form = BookingForm(initial=initial_data)
    
    context = {'form': form}
    return render(request, 'booking.html', context)



def booking(request):
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking_form = form.save(commit=False)
            booking_form.user = request.user
            booking_form.save()
            messages.success(request, 'Your Workout is Booked')
            return redirect('booking.html')
    else:
        form = BookingForm()
    
    context = {
        'form': form
    }
    return render(request, 'booking.html', context)

"""


def home(request):
# Modify the query to suit your needs
    workout_sessions = WorkoutSession.objects.all()
    return render(request, "index.html", {"workout_sessions": workout_sessions})


"""
class BookingView(View):
    def get(self, request):
        current_day = datetime.now().strftime('%A')  # Get the current day of the week
        sessions = WorkoutSession.objects.filter(day=current_day)
        context = {'sessions': sessions, 'current_day': current_day}
        return render(request, 'booking.html', context)


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


class BookingView(View):
    def get(self, request):
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        sessions_by_day = {}
        for day in days_of_week:
            # Retrieve sessions for each day
            sessions = WorkoutSession.objects.filter(day=day)
            sessions_by_day[day] = sessions

        context = {'sessions_by_day': sessions_by_day}
        return render(request, 'booking.html', context)

"""
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
