from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Form)
admin.site.register(models.Announcement)
admin.site.register(models.Project)