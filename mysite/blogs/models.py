from django.db import models
from users.models import CustomUser

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField(max_length=500, null=True, blank=True)
    media = models.ImageField(upload_to='blog_media/', null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="blogs")

    def __str__(self):
        return f"{self.id}, {self.name}"