from django.db import models
from User.models import User
# Create your models here.

class Posts(models.Model):
    author = models.ForeignKey(User)
    content = models.TextField()
    postTo = models.ForeignKey(User, related_name="post_to")
    #parent id
    replyTo = models.ForeignKey('self')
    created_at = models.DateTimeField(auto_now_add=True)

class Tags(models.Model):
    post = models.ForeignKey(Posts)
    tag = models.CharField(max_length=40)


    
