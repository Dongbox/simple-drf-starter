from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import UserRegisterView, UserRetrieveUpdateDestroyView

urlpatterns = [
    re_path(r"login$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    re_path(r"token/refresh$", TokenRefreshView.as_view(), name="token_refresh"),
    re_path(r"token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    re_path(r"$", UserRetrieveUpdateDestroyView.as_view(), name="user_management"),
    re_path(r"register$", UserRegisterView.as_view(), name="user_register"),
]


app_name = "users"
