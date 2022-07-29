from django.urls import path
from .import views
app_name = "members"

urlpatterns = [
 
    path('', views.index,name='index'),
    path('home/', views.home,name='home'),
    path('blogpost/',views.blogpost, name='blogpost'),
    path('displayblogpost/',views.displayblogpost, name='displayblogpost'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('authordetail/',views.author, name='authordetail'),
]     