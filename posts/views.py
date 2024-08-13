from django.shortcuts import render
from posts.models import Post
# Create your views here.




def home_view(request):
    return render(request, "posts/main.html")

def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", context={"posts": posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "posts/post_detail.html", context={"post": post})



