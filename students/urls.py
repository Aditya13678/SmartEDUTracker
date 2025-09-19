from django.urls import path
from .views import StudentRegistrationView,LinkParentToStudentView

urlpatterns=[
    path('register/',StudentRegistrationView.as_view()),
    path('Link-parent-to-student/',LinkParentToStudentView.as_view())
]