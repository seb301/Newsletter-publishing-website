"""
URL configuration for web_project project.

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
from django.urls import path,include
from news_app import views
from django.conf.urls.static import static
from django.conf import settings
import news_app


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.PostListView.as_view(),name='home'),
    path('posts/',views.PostListView.as_view(),name='home'),
    path('posts/<int:cat>/',views.PostListView.as_view(),name='post_list'),
     path('posts/archive/<int:dt>/',views.PostListView.as_view(),name='post_archive'),
    path('posts/detail/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),  #int,slug,str=path converters
    path('submission/',views.post_form,name="post_form"),
    path('pdf/',views.pdf_generate,name='pdf_generate')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# cseadmin
# u: cseAdmin
# p: admin@123

# admin
# u: admin
# p: superadmin@123
