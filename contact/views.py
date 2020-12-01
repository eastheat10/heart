from django.shortcuts import render, redirect, get_object_or_404

from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def create(request):
    if not request.user.is_active:
        return HttpResponse("로그인 해주세요.")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            if post.post_type == 'Donor':
                return redirect('views_donor')
            elif post.post_type == 'recipient':
                return redirect('views_recipient')
            else:
                return redirect('create')
    else:
        form = PostForm()
        posts = Post.objects.all().order_by('-pub_date')
        return render(request, 'create.html', {'form': form, 'posts': posts})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    name = post.user
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = name
            post.save()
            if post.post_type == 'Donor':
                return redirect('views_donor')
            elif post.post_type == 'recipient':
                return redirect('views_recipient')
            else:
                return redirect('create')
    else:
        form = PostForm(instance=post)
        return render(request, 'create.html', {'form': form})

def detail(request, pk):
    form = get_object_or_404(Post, pk=pk)
    return render(request, 'detail.html', {'form': form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    if post.post_type == 'Donor':
        return redirect('views_donor')
    elif post.post_type == 'recipient':
        return redirect('views_recipient')
    else:
        return redirect('create')

def views_donor(request):
    post = Post.objects.filter(post_type='Donor').order_by('-pub_date')
    return render(request, 'views_donor.html', {'post': post})

def views_recipient(request):
    post = Post.objects.filter(post_type='recipient').order_by('-pub_date')
    return render(request, 'views_recipient.html', {'post': post})

