from common import views as common_views
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)
from common.auth.views import LoginView, UserInfoView
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('api/login', LoginView.as_view(), name='login'),
    # path('api/login', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/userinfo', UserInfoView.as_view(), name='token_refresh'),
    # path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # # Optional UI:
    # path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # path(r'api/file/upload/', common_views.UploadFileView.as_view()),
]
