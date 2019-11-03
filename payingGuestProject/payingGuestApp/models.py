
from django.db import models
from django.contrib.auth.models import User


class Location(models.Model):
    city=models.TextField()
    state=models.TextField()

class PayingGuestDetails(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)
    nearestLandmark=models.TextField()
    no_of_beds=models.IntegerField()
    price=models.IntegerField()
    gst=models.IntegerField()
    wifi_no_wifi=models.CharField(max_length=100);
    ac_no_ac=models.CharField(max_length=100);
    male_or_female=models.CharField(max_length=100);
    publishedDate=models.DateField()


class NotificationBooth(models.Model):
    payingGuestDetails=models.ForeignKey(PayingGuestDetails, on_delete=models.CASCADE)
    name=models.TextField();
    email = models.EmailField()
    comments=models.TextField()
    notification_date = models.DateField()
