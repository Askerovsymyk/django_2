
from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
from posts.forms import SearchForm
from django.db.models import Q
from posts.forms import PostUpdateForm

def home_view(request):
    return render(request, "posts/main.html")

@login_required(login_url="user_login")
def post_list_view(request):
    if request.method == "GET":
        search = request.GET.get('search', None)
        tags = request.GET.get('tags', None)
        orderings = request.GET.get('orderings')
        search_form = SearchForm(request.GET)
        page = int(request.GET.get('page', 1))
        posts = Post.objects.all()
        # деление страниц
        page = int(request.GET.get('page', 1))
        limit = 3
        max_pages = posts.count() / limit

        if search:
            # Q для filter
            # posts = posts.filter(Q(title_icontains=search) | Q(content__icontains=search))
            # можно использовать проста filter без Q
            posts = posts.filter(title__icontains=search) | posts.filter(content_icontains=search)
        if tags:
            posts = posts.filter(tag__in__in=tags)
        if orderings:
            posts = posts.order_by(orderings)

        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1

        else:
            max_pages = round(max_pages)

        start = (page - 1) * limit
        end = page + limit
        posts = posts[start:end]


        context = {'posts': posts, 'search_form': search_form, "max_pages": range(1, max_pages + 1)}
        return render(request, "posts/post_list.html", context=context)

@login_required(login_url="user_login")
def post_detail_view(request, post_id,):
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        return render(request, "posts/post_detail.html", context={"post": post})

@login_required(login_url="user_login")
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
@login_required(login_url="user_login")
def post_update_view(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "GET":
        form = PostUpdateForm(instance=post)
        return render(request=request, template_name="posts/post_update.html", context={"form": form, "post": post})
    if request.method == "POST":
        form = PostUpdateForm(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request=request, template_name="posts/post_update.html", context={"form": form, "post": post})
        form.save()
        return redirect("/profile/")