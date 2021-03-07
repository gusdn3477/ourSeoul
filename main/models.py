from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length = 50)
    mainphoto = models.ImageField(upload_to = 'images/', default="images/None/no-image.jpg", blank=True, null=True)
    contents = models.TextField()

    def __str__(self):
        return self.postname