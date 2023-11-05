from . import views
from django.urls import path
from . import views
from signup import views

#urlpatterns = [
 #   path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
  #  path('booking/', views.booking, name='booking'),
#]

urlpatterns = [
    # Assuming you have a function-based view called "home"
    path("", views.home, name="home"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('booking/', views.booking, name='booking'),
    path("", views.WorkoutSessionListView.as_view(), name="home"),

]

"""
from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
]
   # path('booking/', views.booking, name='booking'),

"""
