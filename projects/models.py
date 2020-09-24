from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to="images/")


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
