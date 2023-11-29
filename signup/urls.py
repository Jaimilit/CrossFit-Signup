from . import views
from django.urls import path
from . import views
from signup import views
from .views import book_session


urlpatterns = [
    path("", views.home, name="home"),
    path('booking/', views.booking, name='booking'),
    path('book_session/<int:session_id>/', views.book_session, name='book_session'),
    path('change_booking/<int:session_id>/', views.change_booking, name='change_booking'),
    path('delete_booking/<int:session_id>/', views.delete_booking, name='delete_booking'),
 
]

#path("", views.WorkoutSessionListView.as_view(), name="home"),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
