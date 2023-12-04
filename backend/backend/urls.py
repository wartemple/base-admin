
from django.urls import include, path
from common.auth.views import LoginView, UserInfoView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/login', LoginView.as_view(), name='login'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/userinfo', UserInfoView.as_view(), name='token_refresh'),
    path("api/experiment/", include('experiment.urls'))
]
