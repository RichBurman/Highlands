from django.urls import path
from . import views
from allauth.account.views import SignupView, LoginView, LogoutView

app_name = 'user'

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.MyPasswordChangeView.as_view(),
         name='change_password'),
]
