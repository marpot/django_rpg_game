from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegisterSerializer

User = get_user_model()

class UserRegisterView(APIView):
	def post(self, request, *args, **kwargs):
		serializer = UserRegisterSerializer(data=request.data)

		if serializer.is_valid():
			user = serializer.save()

			return Response({
				"username": user.username,
				"email": user.email
				}, status=status.HTTP_201_CREATED)

		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)