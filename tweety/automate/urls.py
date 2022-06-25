from django.urls import path
from .views import home, config, edit_conf, delete_tweet, edit_tweet, three_btns


urlpatterns = [
    path('', home, name='home'),
    path('config/', config, name='conf'),
    path('edit_conf/', edit_conf, name='edit_conf'),
    path('delete_tweet/<str:id>/', delete_tweet, name='delete_tweet'),
    path('edit_tweet/<str:id>/', edit_tweet, name='edit_tweet'),
    path('btns/', three_btns, name='three_btns'),
]

