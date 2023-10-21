from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

STATUS = ((0, "Draft"). (1, "Publoshed"))

"""
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
 """


class WorkoutSession(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()  # Add a field to represent the date of the workout session
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

    # You can also add a method to generate a slug based on the title
    def generate_slug(self):
        return self.title.lower().replace(" ", "-")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_slug()
        super(WorkoutSession, self).save(*args, **kwargs)
"""
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