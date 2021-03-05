from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=20, verbose_name='유저메일')
    contents = models.CharField(max_length = 100, verbose_name="내용")

    def __str__(self):
        return self.email