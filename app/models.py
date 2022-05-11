from django.db import models
from django.utils.html import mark_safe
class Category(models.Model):
    name=models.CharField(max_length=200)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='img',null=True,)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    def imageDisplay(self):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(self.image.url))
    imageDisplay.short_description = 'image'
   

    def __str__(self):
        return self.title
