from django.db import models

# Create your models here.
class BioLink(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    owner = models.ForeignKey('users.CustomUser', related_name='bio_links', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}({self.link})'
