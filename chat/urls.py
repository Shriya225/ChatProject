from django.urls import path
from .views import RegisterUserView,logout
from rest_framework_simplejwt.views import(TokenObtainPairView,TokenRefreshView)

urlpatterns = [
 path("api/register/",RegisterUserView.as_view(),name="RegisterView"),
 path("api/login/",TokenObtainPairView.as_view()),
 path("api/refresh/",TokenRefreshView.as_view()),
 path("api/logout/",logout)
]
