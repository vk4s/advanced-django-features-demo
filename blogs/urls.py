from django.urls import path, include

from blogs.views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_home'),
    path('<pk>/', BlogDetailView.as_view(), name='blog_detail_page'),
]
