from django.db import models
from django.contrib.auth.models import User

class Diagnosis(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="diagnoses")
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_diagnoses", null=True, blank=True)
    image = models.ImageField(upload_to='diagnosis_images/')
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
