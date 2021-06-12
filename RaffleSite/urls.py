from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView

from RaffleSite import views


urlpatterns = [
    url(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.png'), name='favicon'),
    path('', views.index),
    path('purchase/', views.purchase)
]
