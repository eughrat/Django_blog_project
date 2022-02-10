from django.urls import path, include
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(),name='post_list'),
    path('about/', views.AboutView.as_view(),name='about'),
    path('post/(<pk>\d+', views.PostDetailView.as_view(),name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(),name='post_new'),
    path('post/(<pk>\d+/edit', views.PostUpdateView.as_view(),name='post_edit'),
    path('post/(<pk>\d+/remove', views.PostDeleteView.as_view(),name='post_delete'),
    path('drafts/', views.DraftListView.as_view(),name='post_draft_list'),
    ]