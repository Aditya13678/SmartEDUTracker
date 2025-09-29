from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
    path('create-teacher-parent/',views.CreateTeacherParentView.as_view()),
    path('session-login/',csrf_exempt(views.SessionLoginView.as_view())),
    path('logout/',views.SessionLogoutView.as_view()),

    path('password-reset-request/',views.PasswordResetRequestView.as_view()),
    path('password-reset-confirm/',views.PasswordResetConfirmView.as_view()),



    path('api/data/', views.get_data),

   
]