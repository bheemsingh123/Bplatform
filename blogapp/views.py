from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import authenticate, login


def home(request):
    # posts = Post.objects.all()[:6]
    posts = Post.objects.all()
    print(posts)
    cats = Category.objects.all()
    data = {
        'posts':posts,
        'cats':cats
    }
    return render(request,'index.html',data)


def post(request,url):
    # Post.objects.filter(url=url)
    post = Post.objects.get(url=url)
    print(post)
    cats = Category.objects.all()
    data = {
        'posts':post,
        'cats':cats
    }
    return render(request,'post.html',data)

def category(request,url):
    cat = Category.objects.get(url=url)
    post = Post.objects.filter(cat=cat)
    print(post)
    return render(request,"category.html",{'cat':cat, 'posts':post})



def aboutus(request):
    return render(request,'aboutus.html')

def login(request):
    if request.method =='post':
        username = request.POST["username"]
        password = request.POST["password"]
        print(username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
           login(request, user)
    else:
        return render(request,'login.html')

def logout(request):
    logout(request)
    return redirect('/')

def register(request):
    # if request.method =='post':
    return render(request,'register.html')

def contactus(request):
    return render(request,'contactus.html')