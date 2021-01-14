import re

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse





class Note(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default="")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    # Na jaką stronę przenieść po dodaniu notatki
    def get_absolute_url(self):
        return reverse('note_view', args=(str(self.id)))
        # return reverse('home')

    def get_introduction(self):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', self.body)
        return cleantext[:200]