from django.db import models



class UrlParser(models.Model):
    url = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    result = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url
