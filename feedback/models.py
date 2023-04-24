from django.db import models


# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=1000)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.email} feedback => {self.message}"
