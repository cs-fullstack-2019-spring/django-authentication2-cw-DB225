from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Blog

# Create your views here.
@login_required
def index(request):
    myBlog = Blog.objects.all()
    return render(request, 'myApp/index.html', {'myBlog': myBlog})


@login_required
def entries(request):
    return render(request, 'myApp/index.html')