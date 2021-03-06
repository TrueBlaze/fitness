"""urls pattern for users"""

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'

urlpatterns = [
    # login page
    path('login/',
         auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),

    # logout page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # signup page
    path('signup/', views.signup, name='signup'),
]