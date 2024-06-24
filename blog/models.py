from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                .filter(status=Post.Status.PUBLISHED)




class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')   # on_delete will del all posts when user obj is deleted and 
                                                                                            # related_name is name with which we can access posts from User model
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)   #  the date will be saved automatically when creating an object
    updated = models.DateTimeField(auto_now=True)       #  the date will be updated automatically when saving an object 

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)


    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']     # will order data in reverse order by publish date, i.e new first
        indexes = [
            models.Index(fields=['-publish']),
        ]                           # use to index in database

    def __str__(self):
        return self.title

