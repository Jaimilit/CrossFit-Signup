from django.db import models
from django.contrib.auth.models import User

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
    """this model provides the info of the workout sessions to be able to book"""
    title = models.CharField(max_length=200)
    time = models.TimeField(default='00:00')
    instructor_name = models.CharField(max_length=200)
    day = models.CharField(max_length=20, choices=DAYS_OF_WEEK, default='Monday')   

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(WorkoutSession, self).save(*args, **kwargs)


class Booking(models.Model):
    """this model provides the booking info for the user to book workout sessions"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_session = models.ForeignKey('WorkoutSession', on_delete=models.CASCADE)
  

    def __str__(self):
        return f"{self.user.username} booked {self.workout_session.title} on {self.workout_session.day} at {self.workout_session.time}"
    
    def save(self, *args, **kwargs):
        super(Booking, self).save(*args, **kwargs)
