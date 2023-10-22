from . import views
from django.urls import path

urlpatterns = [
    path("", views.WorkoutLSession.as_view(), name="home"),
]

"""
from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]
"""
