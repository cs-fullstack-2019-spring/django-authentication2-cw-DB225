from django.db import models

# Create your models here.
class Blog(models.Model):
    username = models.CharField(max_length=200)
    blog_title = models.CharField(max_length=200)
    blog_entry = models.CharField(max_length=200)

    def __str__(self):
        return self.username