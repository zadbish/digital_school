from django.shortcuts import render
from .models import Post


# 
# Create your views here.

# posts = [
#     {
#         'author' : 'zahid',
#         'title' : 'Blog post1',
#         'content' : 'First post content',
#         'date_posted' : 'May 30, 2019'
#     },
#     {
#         'author' : 'nadia',
#         'title' : 'Blog post2',
#         'content' : 'Second post content',
#         'date_posted' : 'May 26, 2019'
#     },
#     {
#         'author' : 'Nabeeha',
#         'title' : 'Blog post3',
#         'content' : 'Third post content',
#         'date_posted' : 'May 27, 2019'
#     },
#     {
#         'author' : 'Hadia',
#         'title' : 'Blog post4',
#         'content' : 'Fourth post content',
#         'date_posted' : 'May 28, 2019'
#     }
# ]

def home(request):
    context= {
        'posts' : Post.objects.all()
        # 'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title' : 'About' })
