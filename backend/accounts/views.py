from django.contrib.auth import get_user_model, authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.tokens import RefreshToken
import logging
from rest_framework import viewsets
from .models import PlayerCharacter
from .serializers import PlayerCharacterSerializer

User = get_user_model()
logger = logging.getLogger(__name__)

class PlayerCharacterViewSet(viewsets.ModelViewSet):
	queryset = PlayerCharacter.objects.all()
	serializer_class = PlayerCharacterSerializer

	def get_queryset(self):
		return PlayerCharacter.objects.filter(user=self.request.user)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)

class UserRegisterView(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserRegisterSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		refresh = RefreshToken.for_user(user)
		return Response({
			'refresh': str(refresh),
			'access': str(refresh.access_token),
			'userId': user.id,
		}, status=status.HTTP_201_CREATED)

class UserLoginView(APIView):
	def post(self, request, *args, **kwargs):
		serializer = UserLoginSerializer(data=request.data)

		if serializer.is_valid():
			user = User.objects.get(username=serializer.validated_data['username'])
			logger.info(f"Znaleziony użytkownik: {user.username}, userId: {user.id}")
			print(f"Znaleziony użytkownik: {user.username}, userId: {user.id}")
			refresh = RefreshToken.for_user(user)
			logger.info(f"Generowanie tokenów: refresh: {refresh}, access: {refresh.access_token}")
			return Response({
				'access': str(refresh.access_token),
				'refresh': str(refresh),
				'userId': user.id,
			}, status=status.HTTP_200_OK)
		
		logger.error(f"Błąd walidacji logowania: {serializer.errors}")
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

