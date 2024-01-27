from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField()
    sbject = models.CharField(max_length = 255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add = True)
    updated_time = models.DateTimeField(auto_now = True)