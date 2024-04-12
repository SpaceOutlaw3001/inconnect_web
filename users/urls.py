from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from . import api

app_name = 'users'
urlpatterns = [
    # path('login/', views.LoginUser.as_view(), name='login'),
    # path('logout/', views.logout_user, name='logout'),
    # path('register/', views.RegisterUser.as_view(), name='logout_user'),
    # path('test/', views.test_func, name='test'),
    path('register/', api.signup, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', api.me, name='me'),
]