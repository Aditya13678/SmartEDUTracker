from django.urls import path
from .views import StudentRegistrationView,LinkParentToStudentView,StandardCreateView,SectionCreateView,AttendanceMarkView,ClassAttendanceView,StudentAttendanceView,AttendanceReportPrincipalView

urlpatterns=[
    path('register/',StudentRegistrationView.as_view()),
    path('Link-parent-to-student/',LinkParentToStudentView.as_view()),
    path('standards/',StandardCreateView.as_view()),
    path('sections/',SectionCreateView.as_view()),

    path("attendace/mark/",AttendanceMarkView.as_view()),

    path("attendance/student/<int:student_id>/",StudentAttendanceView.as_view()),
    path("attendance/class/<int:section_id>/",ClassAttendanceView.as_view()),

    path("attendance-report/principal/",AttendanceReportPrincipalView.as_view()),
]