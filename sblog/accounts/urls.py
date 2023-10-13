from .views import *
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('login', login_form, name="login"),
    path('register', register_form, name="register"),
    path('activate/<uidb64>/<token>',activate,name="activate"),
    path('logout',logout_form,name="logout"),
    path('password/', PasswordsChangeView.as_view(template_name = 'accounts/change-password.html') ,name="password"),
    path('password_success/', password_sucess ,name="password_sucess"),
]
