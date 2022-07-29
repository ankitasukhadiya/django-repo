from django.forms import ModelForm
#from django.db import models
from .models import Blog, User

class Blogpostform(ModelForm):
    class Meta:
        model = Blog
        fields = ["Blogpost_name","User"]

class signupform(ModelForm):
    class Meta:
        model = User
        fields = ["User_name","User_mail","User_pwd","User_pno"] 

                 