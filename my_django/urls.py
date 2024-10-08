

"""
URL configuration for my_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from posts.views import post_list_view, home_view, post_detail_view, post_create_view
from user.views import register_view, login_view, logout_view, profile_view
from posts.views import post_update_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('posts/', post_list_view, name='post_list'),
    path('posts/<int:post_id>/', post_detail_view, name='post_detail'),
    path('posts/create/', post_create_view, name='post_create'),
    path('register/', register_view, name='user_register'),
    path('login/', login_view, name="user_login"),
    path('logout/', logout_view, name="user_logout"),
    path('profile/', profile_view, name="user_profile"),
    path('post/<int:post_id>/update', post_update_view, name="post_update")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




