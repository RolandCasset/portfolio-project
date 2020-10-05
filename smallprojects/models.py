from django.db import models

class SmallProjects(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
    body = models.CharField(max_length=200)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
