from django.urls import path
from . import views

urlpatterns=[
    path('create-teacher-parent/',views.CreateTeacherParentView.as_view()),
   
]