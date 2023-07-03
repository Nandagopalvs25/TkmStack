from django.conf import settings
from django.db import models

# Create your models here.




class Tags(models.Model):
    tag_name = models.CharField(max_length=100)


    def __str__(self):
        return self.tag_name

class Stack(models.Model):
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags, blank=True)

    def __str__(self):
        return self.title

    


class Answers(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    stack = models.ForeignKey(Stack,related_name='answers',  on_delete = models.CASCADE)
    body = models.TextField()
 

    def __str__(self):
        return self.body














    