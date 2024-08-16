
from django.shortcuts import render, redirect
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


def post_create_view(request):
    if request.method == "GET":
        return render(request=request, template_name="posts/post_create.html")
    if request.method == "POST":
        image = request.FILES.get("image")
        title = request.POST.get("title")
        content = request.POST.get("content")
        rate = request.POST.get("rate")
        Post.objects.create(image=image, title=title, content=content, rate=rate)
        return redirect("/posts/")

