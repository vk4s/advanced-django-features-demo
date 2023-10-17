from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=256)
    description = models.TextField()
    author = models.ForeignKey('users.CustomUser', related_name='blogs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title