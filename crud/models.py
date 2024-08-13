from django.db import models
from ckeditor.fields import RichTextField

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # RichTextFieldに変更
    date_published = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


