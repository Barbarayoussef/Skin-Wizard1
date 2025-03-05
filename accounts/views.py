from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password
from .models import Patient, Doctor
from .serializers import PatientSerializer, DoctorSerializer

# Patient Signup View
class PatientSignupView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Doctor Signup View
class DoctorSignupView(ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# Login View
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = Patient.objects.filter(email=email).first() or Doctor.objects.filter(email=email).first()

        if user and check_password(password, user.password):
            return Response({"message": "Login successful", "user_id": user.id}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Patient Detail View
class PatientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# Doctor Detail View
class DoctorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
