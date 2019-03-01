from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth.views import login
from .views import view_post, add_post, PostMonthArchive, PostWeekArchiveView

urlpatterns = [
	path('accounts/login/', login),
	path('admin/', admin.site.urls),
	path('blog/', include('blog.urls'),
	path('post/<str:slug>', view_post, name='blog_post_detail'),
    	path('add/post', add_post, name='blog_add_post'),
    	path('archive/<int:year>/month/<int:month>', PostMonthArchiveView.as_view(month_format='%m'), name='blog_archive_month',),
    path('archive/<int:year>/week/<int:week>', PostWeekArchiveView.as_view(), name='blog_archive_week'),
	]
	
