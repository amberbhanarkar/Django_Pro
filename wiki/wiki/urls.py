"""wiki URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from .views import add_article, edit_article, article_history, ArticleList, ArticleDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',ArticleList.as_view(), name = 'wiki_article_index'),
    path('article/<str:slug>',ArticleDetail.as_view(), name = 'wiki_article_detail'),
    path('history/<str:slug>',article_history, name = 'wiki_article_history'),
    path('add/article', add_article, name = 'wiki_article_add'),
    path('edit/article/<str:slug>', edit_article, name = 'wiki_article_edit'),
]
