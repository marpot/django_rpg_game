from django.urls import path, include
from rest_framework.routers import DefaultRouter
from accounts.characters.views import PlayerCharacterViewSet
from accounts.users.views import UserRegisterView, UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'characters', PlayerCharacterViewSet)
router.register(r'register', UserRegisterView, basename='user-register')

urlpatterns = [
	path('login/', UserLoginView.as_view(), name='login'),
	path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
	path('', include(router.urls)),
]