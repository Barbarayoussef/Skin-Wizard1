from django.urls import path
from .views import (
    PatientSignupView,
    DoctorSignupView,
    LoginView,
    PatientDetailView,
    DoctorDetailView,
)

urlpatterns = [
    path('signup/patient/', PatientSignupView.as_view(), name='patient_signup'),
    path('signup/doctor/', DoctorSignupView.as_view(), name='doctor_signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
]
