from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [

    path('register/', SignUpView.as_view(), name='customer_register'),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api-authentication/', include('rest_framework.urls')),



]