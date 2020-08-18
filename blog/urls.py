from django.urls import path
#copied from original urls.py
from . import views
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView,
	PostUpdateView,
	PostDeleteView,
    UserPostListView)
# because we want to use home function here
urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('user/<username>', UserPostListView.as_view(), name="user-post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('about/',views.about, name="Blog-about")

]
# step 3: Open urls.py main file because edits need to be made there because that file decides which URLS will be available to blog app 
