from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=99)
    content = models.TextField(null=True, blank=True)
    rate = models.IntegerField(default=0, max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'этот пост о: {self.title}'

    objects = models.Manager()
