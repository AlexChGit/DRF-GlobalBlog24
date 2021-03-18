from django.db import models
from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from globalblog24 import settings

# Create your models here.
class Post(models.Model):
    """ A class to represent an user post """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=9)
    title = models.CharField(max_length=120)
    body = models.TextField()
    description = models.TextField(default='Description', blank=True)
    keywords = models.CharField(max_length=120, default='Key words', blank=True)
    creation_date = CreationDateTimeField(auto_now_add=True)
    change_date = ModificationDateTimeField(auto_now=True)
    visible = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-title", "-creation_date"]


class Comment(models.Model):
    """ A class to represent a comment for a post """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=120)
    body = models.TextField()
    creation_date = CreationDateTimeField(auto_now_add=True)
    change_date = ModificationDateTimeField(auto_now=True)
    visible = models.BooleanField(default=False)

    class Meta:
        ordering = ("-name", "-creation_date",)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.creation_date)
