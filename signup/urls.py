from . import views
from django.urls import path

urlpatterns = [
    path("", views.WorkoutSession.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]

"""
from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]
"""
