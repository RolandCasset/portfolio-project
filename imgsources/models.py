from django.db import models

class Imgsources(models.Model):
    image = models.ImageField(upload_to="images/")
    body = models.TextField()

    def __str__(self):
        return self.body
