from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('delete/<int:post_id>/', views.delete, name='delete'),
    path('like/<int:post_id>/', views.LikeView, ),
    path('edit/<int:post_id>/', views.edit, name='edit' ),

]