from dataclasses import field
from django.db import models
from django.utils import timezone


class User(models.Model): 
    User_name = models.CharField(max_length=50)
    User_mail = models.CharField(max_length=50)
    User_pwd = models.CharField(max_length=50)
    User_pno = models.BigIntegerField()
   

    def __str__(self):
        return self.User_name   

class Blog(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Blogpost_name = models.CharField(max_length=50)
    Post_date = models.DateTimeField("date created",default=timezone.now())
    Content = models.CharField(max_length=100)
 
    def __str__(self):
        return self.Blogpost_name


    

# class Comment(models.Model):

#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     Blogpost_name = models.CharField(max_length=50)
#     Content = models.CharField(max_length=50)
    
#     def __str__(self) -> str:
#         return self.Author_id



     