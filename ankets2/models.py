from django.db import models
from django.contrib.auth.models import User

class Anket(User):
    photo = models.ImageField(upload_to='ankets2/photos/', null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    gender = models.CharField(max_length=10)
    previous_experience = models.CharField(max_length=200)
    recommendation = models.CharField(max_length=200)
    reason_to_join = models.CharField(max_length=200)
    hours_per_week = models.IntegerField()
    satisfaction_level = models.IntegerField()
    views = models.PositiveBigIntegerField(default=0, null=True)

    def __str__(self):
        return self.username