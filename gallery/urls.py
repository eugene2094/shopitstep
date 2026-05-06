from . import views
from django.urls import path

app_name = 'gallery'
urlpatterns = [
    path('', views.gallery_list, name="gallery"),
    path('upload/', views.upload, name="upload")
]
