from django.urls import path
from . import views
from .views import PostListView,PostCreateView,PostDetailView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(),name='blog-home'),
    path('post/new/', PostCreateView.as_view(),name='post-created'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(),name='post-delete'),
    path('post/<int:pk>/update', PostUpdateView.as_view(),name='post-update'),
    path('about/',views.about,name='blog-About')
]
