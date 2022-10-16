from django.urls import path

from . import views

app_name = 'preonboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:job_opening_id>/', views.detail, name='detail'),
    path('applies/create/<int:job_opening_id>/', views.apply_create, name='answer_create'),
    path('job_opening/create/', views.job_opening_create, name='job_opening_create'),
    path('job_opening/modify/<int:job_opening_id>/', views.job_opening_modify, name='job_opening_modify'),
    path('job_opening/delete/<int:job_opening_id>/', views.job_opening_delete, name='job_opening_delete'),
    path('job_opening/apply/<int:job_opening_id>/', views.apply_create, name='apply_create')
]