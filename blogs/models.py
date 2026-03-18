from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=255)

    def __str__(self):
        return f"'{self.title}' | {self.date}"