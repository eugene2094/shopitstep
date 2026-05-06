from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.index, name="home"),
    path('contacts/', views.contacts, name="contacts"),
    path('post/<slug:slug>', views.post_detail, name="post_detail"),
    path('category/<slug:slug>', views.category, name="category"),
    path('search/', views.search, name='search'),
    path('create-post/', views.create_post, name="create_post"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('post/<slug:slug>/delete/', views.delete_post, name="delete_post")
]
