from django.urls import path
from auth_app.views import UserCreateView,UserLoginView,UserLogoutView,UserProfileView,buy_now,UserUpdateView,UserPasswordChangeView
urlpatterns = [
    path('user_register/', UserCreateView.as_view(), name = 'user_register'),
    path('user_login/', UserLoginView.as_view(), name = 'user_login'),
    path('user_logout/', UserLogoutView.as_view(), name = 'user_logout'),
    path('profile/', UserProfileView.as_view(), name = 'profile'),
    path('profile/purchase/<int:id>/', buy_now, name = 'buy_now'),
    path('profile/edit_profile/<int:id>/', UserUpdateView.as_view(), name = 'edit_profile'),
    path('profile/change_password/', UserPasswordChangeView.as_view(), name = 'change_password'),
]
