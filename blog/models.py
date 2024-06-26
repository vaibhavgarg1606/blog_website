from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()\
                .filter(status=Post.Status.PUBLISHED)




class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')                      # makes it unique for publish date, i.e there can be no 2 post with same slug and publish date
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
    

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                        args=[
                            self.publish.year,
                            self.publish.month,
                            self.publish.day,
                            self.slug
                        ])  # replace in html file with harcoded(sorta) urls




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    
    def __str__(self):
        return f"Comment by {self.name} on {self.post}"

