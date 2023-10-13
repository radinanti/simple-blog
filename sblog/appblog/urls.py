from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

app_name = 'appblog'

urlpatterns = [
    path('', Index.as_view(), name="index"),
    path('contact/', contact_us, name='contact_us'),
    path('article/<int:pk>/<str:name>/', ArticleView.as_view(), name='article-detail'),
    path('post/', AddPost.as_view(), name="apost"),
    path('article/edit/<int:pk>', Edit.as_view(), name="edit_post" ),
    path('category_create/',CategoryView.as_view(),name="add_category"),
    path('article/<int:pk>/delete' , Delete.as_view(), name="delete_post"),
    path('category/<str:list>/',CategoryList,name="category"),
    path('category-list/',CategoryListViw,name="category-list"),
    path('like/<int:pk>/<str:name>/', LikePost, name='lk_post'),
    path('edit_user', ProfileEdit.as_view() ,name="edit_profile"),
    path('<str:username>/profile/', ProfilePage.as_view(), name="profile"),
    path('<int:pk>/<str:username>/edit_profile/',EditProfilePage.as_view(),name="edit_profile_page" ),
    path('<str:username>/create_profile/',CreateProfilePage.as_view(),name="create_profile_page" ),
    path('delete-comment/<int:comment_id>/', DeleteCommentView.as_view(), name='delete-comment'),
]