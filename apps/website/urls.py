# Librerias Django
from django.contrib.auth import views as auth_views
from django.urls import path

# Librerias en carpetas locales
from .subviews.post import (
    DeletePost, PostCreateView, PostDetailView, PostListView, PostUpdateView)
from .subviews.website_config import UpdateWebsiteConfigView

urlpatterns = [
    path('post', PostListView.as_view(), name='post'),
    path('post/add/', PostCreateView.as_view(), name='post-add'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', DeletePost, name='post-delete'),

    path('config/<int:pk>', UpdateWebsiteConfigView.as_view(), name='website-config'),
]
