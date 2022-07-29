from multiprocessing import context
from re import template
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from django.core.paginator import Paginator
from .models import Blog
from .forms import Blogpostform
from .forms import signupform
from members.models import Blog,User

def index(request):
    template = loader.get_template("index.html")
    return render(request,"index.html")

def home(request):
    template = loader.get_template('home.html')
    return render(request,"home.html") 

def blogpost(request):
    
    form = Blogpostform 
    print(form,"-")
    print(request.method)
    if 'save' in request.POST:
      
        data = Blogpostform(request.POST,request.FILES)
        print(data)
        if data.is_valid():
            data.save()
            return redirect('/members/displayblogpost')
    return render(request,'blogpost.html',{'form':form})  

def displayblogpost(request):
   mymembers = Blog.objects.all().order_by('-Post_date')
   
   paginator = Paginator(mymembers, 5) # Show 5 contacts per page.
   page_number = request.GET.get('page')
   mymembers = paginator.get_page(page_number)

   context = {
       'mymembers' : mymembers,
   } 
   return render(request,"displayblogpost.html",context)   
    

def signup(request):
    form = signupform
    if 'save' in request.POST:
        data = signupform(request.POST,request.FILES)
        if data.is_valid():
            data.save()
            return redirect('/members/')
    return render(request,'signup.html',{'form':form})    

def login(request):
    message =''
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:
        User_name = request.POST['User_name']
        User_pwd = request.POST['User_pwd']
        data = User.objects.all().filter(User_name=User_name,User_pwd=User_pwd)
        print(User_name,"-----------------------")
        print(User_pwd)
        for x in data:
            if x.User_name == User_name and x.User_pwd == User_pwd:
                print(User_name)
                print(User_pwd)
                print("Successfully inserted.............")
                return render(request, "index.html")
            # else:
            #     return render(request, "login.html")
            #     message = "Invalid login!"
            # #     return render(request, "login.html",context={'message':message})
       
def author(request):
    mymembers = User.objects.all()
    context = {
        'mymembers' : mymembers,
    }
    
    return render(request,"authordetail.html",context)     
      


