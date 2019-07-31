"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path 
from blog.views import CreatePostView, PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', PostListView.as_view(), name='post-list'),
    url('^create/$', CreatePostView.as_view(), name='post-create'),
    url('^(?P<pk>\d+)/$', PostDetailView.as_view(), name='post-detail'),
    url('^update/(?P<pk>\d+)/$', PostUpdateView.as_view(), name='post-update'),
    url('^delete/(?P<pk>\d+)/$', PostDeleteView.as_view(), name='post-delete'),  
]
