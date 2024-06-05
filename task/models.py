from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    is_private = models.BooleanField(default=True)
    description = models.TextField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name