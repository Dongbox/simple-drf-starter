from django.conf import settings
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

urlpatterns = [
    path("user/", include("apps.users.urls", namespace="users")),
]


app_name = "api"
# urlpatterns += router.urls
