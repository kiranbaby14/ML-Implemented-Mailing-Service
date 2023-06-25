from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('api/user/details', views.user_details, name='user_details'),
    path('api/user/interests', views.user_interests, name='user_interests'),
    path('api/fetch', views.api_view, name='fetch_data'),
]