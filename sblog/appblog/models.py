from django.db import models
from django.contrib.auth.models import User
from django.db.models import DateTimeField
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('appblog:index')

class usrpfp(models.Model):
    user = models.OneToOneField(User, null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile = models.ImageField(null=True,blank=True,upload_to='profile/')
    website_url = models.CharField(max_length=200,null=True,blank=True)
    github_url = models.CharField(max_length=200,null=True,blank=True)
    twitter_url = models.CharField(max_length=200,null=True,blank=True)   
    instagram_url = models.CharField(max_length=200,null=True,blank=True) 
    def __str__(self):
        return str(self.user)
    def get_absolute_url(self):
        return reverse('appblog:index')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to='header/')
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    text = RichTextField(blank=True,null=True)
    create_at = models.DateTimeField(auto_now_add=True) 
    category = models.CharField(max_length=200,default="yoo")
    likes = models.ManyToManyField(User,related_name='blog_posts')
    
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + " | " + str(self.author)
    
    def get_absolute_url(self):
        return reverse('appblog:index')
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'