from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from my_auth.views.cbv import UsersAPIView, ChangeAPIView, ForgotPasswordAPIView, ResetPasswordAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh-token/', TokenRefreshView.as_view()),
    path('register/', UsersAPIView.as_view()),
    path('change-password/', ChangeAPIView.as_view()),
    path('forgot-password/', ForgotPasswordAPIView.as_view()),
    path('reset-password/<slug:token>/', ResetPasswordAPIView.as_view())
]
