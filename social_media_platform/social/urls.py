from django.urls import path
from .views import user_list, user_detail, post_list, post_detail
from .auth_views import signup, login

urlpatterns = [
    path('users/', user_list),
    path('users/<int:pk>/', user_detail),
    path('posts/', post_list),
    path('posts/<int:pk>/', post_detail),
    path('auth/signup/', signup),
    path('auth/login/', login),
]
