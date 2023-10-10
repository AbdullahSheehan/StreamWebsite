from django.shortcuts import render
from random import shuffle
from .models import Category, Video, Comment
from .forms import CommentForm
# Create your views here.
def index(req):
    videos = Video.objects.all()
    categories = Category.objects.all()
    if(req.method == 'GET'):
        search = req.GET.get('search', '')
        result = Video.objects.filter(title__icontains=search)
    return render(req, 'AppStream/home.html', context={'videos':videos, 'categories':categories, 'search':search, 'results':result})

def categories(req, pk):
    videocats = Category.objects.get(pk=pk)
    return render(req, 'AppStream/category.html', context={'category':videocats.name, 'videocats':videocats})

def videoview(req, pk):
    video = Video.objects.get(pk=pk)
    comments = Comment.objects.filter(video=video)
    form = CommentForm()
    #allcomments = Comment.objects.filter(video=video)
    if(req.method == 'POST'):
        form = CommentForm(req.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.user = req.user
            obj.video = video
            obj.save()
    return render(req, 'AppStream/details.html', context={'video':video, 'form':form, 'comments':comments})