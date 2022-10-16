from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
path('<int:job_opening_id>/', views.detail),
]