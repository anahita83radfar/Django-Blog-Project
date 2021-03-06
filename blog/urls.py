from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    path('new/', views.PostCreate.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/update/', views.PostUpdate.as_view(),
         name='post_update'),
    path('<slug:slug>/delete/', views.PostDelete.as_view(),
         name='post_delete'),
]
