from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include


from diary.apps import DiaryConfig
from diary.views import DiaryListView
from users.views import UserCreateView, email_verification, UserResetPasswordView, ProfileView, UserUpdateView

app_name = DiaryConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', UserCreateView.as_view(), name="register"),
    path('email-confirm/<str:token>/', email_verification, name="email-confirm"),
    path('reset-password/', UserResetPasswordView.as_view(), name="reset_password"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path("update/", UserUpdateView.as_view(), name="update"),
]
