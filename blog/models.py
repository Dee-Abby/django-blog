from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    # id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=80)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('chat-detail', kwargs={'pk' : self.pk})