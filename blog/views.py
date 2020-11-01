from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

#add fake data to populate the app pages
posts = [
    {
        'author':'corey',
        'title':'first blog',
        'content':'le contents of di first blog.',
        'date_posted':'November 1, 2020'
    },
    {
        'author':'Mowaffak',
        'title':'Second blog',
        'content':'le contents of di Second blog :O .',
        'date_posted':'November 2, 2020'
    },
]
# Create your views here.
def home(request):
    #Context is passed to the templating engine, you can pass whatever you want there.
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', context={'title':'About Page'})