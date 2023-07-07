from django.urls import path, include, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.social.urls')),
    path('api/save-tag-preference/', views.save_user_tag_preference, name='save_tag_preference'),
    path('api/get-tag-preference/', views.get_user_tag_preference, name='get_tag_preference'),

]

