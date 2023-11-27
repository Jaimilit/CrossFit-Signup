from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify  # Import slugify

# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))

DAYS_OF_WEEK = (
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
)


class WorkoutSession(models.Model):
    title = models.CharField(max_length=200)
    time = models.TimeField(default='00:00')
    instructor_name = models.CharField(max_length=200)
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, default='Monday')  # New field for the day

    slug = models.SlugField(max_length=200, unique=True, blank=True)

    @property
    def day_of_week(self):
        return self.date.strftime("%A")  # This assumes 'date' is a DateTimeField


    def __str__(self):
        return self.title

    def generate_slug(self):
        return slugify(self.title)

    def save(self, *args, **kwargs):
        # Generate the slug only if it's not provided
        if not self.slug:
            self.slug = self.generate_slug()
        super(WorkoutSession, self).save(*args, **kwargs)

        
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(WorkoutSession, on_delete=models.CASCADE)

"""
class WorkoutSession(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True,
                            default="default-slug")
    date = models.DateField()
    session_creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_sessions"
    )
    featured_image = models.ImageField(
        upload_to='workout_images/', default='placeholder.jpg')
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    attendees = models.ManyToManyField(
        User, related_name='signed_up_for', blank=True)

    def __str__(self):
        return self.title

    def generate_slug(self):
        return slugify(self.title)  # Use slugify to generate the slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super(WorkoutSession, self).save(*args, **kwargs)



class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="session_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
    User, related_name='blogpost_like', blank=True)
 



    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
"""
