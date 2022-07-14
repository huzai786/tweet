from django.urls import path
from .views import home, delete_tweet, edit_tweet


urlpatterns = [
    path('', home, name='home'),
    path('delete_tweet/<str:id>/', delete_tweet, name='delete_tweet'),
    path('edit_tweet/<str:id>/', edit_tweet, name='edit_tweet'),
]

