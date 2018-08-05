from django.db import models

class Posts(models.Model):
    title = models.CharField("title",max_length=120)
    text = models.CharField(max_length=10000)
    date = models.DateTimeField()
    autor = models.CharField(max_length=120)

    def __str__ (self):
        return self.title
