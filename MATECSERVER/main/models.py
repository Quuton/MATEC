from django.db import models
from django.contrib.auth.models import User

class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone = models.CharField(max_length = 11)
    preferences_notify_form_approval = models.BooleanField(default = True)

class Form(models.Model):
    class Approval_Status(models.TextChoices):
        PENDING = "pending"
        APPROVED = "approved"
        DENIED = "denied"

    user = models.ForeignKey(User, on_delete = models.CASCADE)
    type = models.CharField(max_length = 50)
    file = models.FileField(upload_to="documents/forms")
    approval_status = models.CharField(max_length = 10, choices = Approval_Status.choices, default = Approval_Status.PENDING)
    date_posted = models.DateTimeField(auto_now = True)

class Announcement(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True)
    thumbnail = models.ImageField(upload_to='images/announcement_thumbnails', blank = True)
    date_posted = models.DateTimeField(auto_now = True)

class Project(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(blank = True)    
    thumbnail = models.ImageField(upload_to='images/project_thumbnails', blank = True)
    date_posted = models.DateTimeField(auto_now = True)