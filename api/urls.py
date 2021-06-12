from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView
from . import views


urlpatterns = [
    path('login/', views.UserAPI.as_view()),
    path('logout/', views.LogoutAPI.as_view()),
    path('packs_date/active', views.PacksApi.as_view())
]
