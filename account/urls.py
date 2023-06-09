from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from django.urls import path

from .views import ChangePasswordView,ForgotPasswordView,ForgotPasswordCompleteView, RegisterView, ActivationView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('forgot_password_complete/', ForgotPasswordCompleteView.as_view(), name='forgot_password_complete'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
]
