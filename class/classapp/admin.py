from django.contrib import admin

from . import models

admin.site.register(models.UserProfile)
admin.site.register(models.ClassRoom)
admin.site.register(models.Exam)
admin.site.register(models.Question)
admin.site.register(models.Answer)
