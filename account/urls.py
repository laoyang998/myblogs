from django.urls import path
from . import  views

app_name = 'account'
urlpatterns=[
    path('',views.user_login,name='login') , #由主程的映射引导进来，所以，这里为空就可以了
    path('logout/',views.user_logout,name='logout'),
    path('register/',views.register,name='register'),
    path('my-information',views.Myself,name='my-information'),
    path('myself_edit',views.Myself_edit,name='myself_edit'),
    path('myimage',views.my_image,name='myimage')

]