from django.urls import path
app_name = 'blogs'
from .views import (
    BlogDeleteView,
    BlogCreateView,
    BlogDetailView,
    BlogsListView,
    BlogUpdateView
)
urlpatterns = [
    path('',BlogsListView.as_view() ,name='blogs_view'),
    path('<int:pk>',BlogDetailView.as_view() ,name='blogs_view'),
    path('create', BlogCreateView.as_view(), name='blogs_create'),
    path('<int:pk>/update', BlogUpdateView.as_view(), name='blogs_update'),
    path('<int:pk>/delete', BlogDeleteView.as_view(), name='blogs_delete'),
]