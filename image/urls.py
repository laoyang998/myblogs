from django.urls import path
from . import views

app_name = 'image'
urlpatterns = [
    path('image_list', views.list_image, name='image_list'),
    path('upload_image', views.upload_image, name='upload_image'),
    path('del_image', views.del_image, name='del_image'),
    path('falls_images', views.falls_images, name='falls_images'),
]
