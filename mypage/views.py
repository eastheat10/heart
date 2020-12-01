from django.shortcuts import render, get_object_or_404
from contact.models import Post
from contact.forms import PostForm
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, pk):
    users = User.objects.get(username=pk)
    posts = Post.objects.filter(user=users).order_by('-id')
    return render(request, 'mypage.html', {"users": users, "posts": posts})

def speakers(request):
    return render(request, 'speakers.html')

def faq(request):
    return render(request, 'faq.html')

def supporters(request):
    return render(request, 'supporters.html')