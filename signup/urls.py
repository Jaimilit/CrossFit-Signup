from . import views
from django.urls import path

urlpatterns = [
    path("", views.WorkoutSession.as_view(), name="home"),
]

"""
from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]
"""
