from django.urls import path
from . import views

urlpatterns =[
    path('', views.registerpage),
    path('userlog/',views.userloginpage),
    path('adminlog/', views.adminlogin),
    path('adminhome/',views.adminhome),
    path('pending/',views.pending),
    path('approve/<int:id>/',views.approve),
    path('approved/',views.approved),
    path('operations/',views.operations),
    path('edit/<int:id>/',views.edit),
    path('delete/<int:id>/',views.delete)
]