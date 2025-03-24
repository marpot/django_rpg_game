from django.contrib.auth import get_user_model
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
import logging
from .serializers import UserRegisterSerializer, UserLoginSerializer

User = get_user_model()
logger = logging.getLogger(__name__)

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
        logger.info(f"Otrzymane dane logowania: {request.data}")
        logger.info(f"Content-Type: {request.content_type}")
        logger.info(f"Metoda żądania: {request.method}")
        
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid():
            validated_data = serializer.validated_data
            logger.info(f"Logowanie udane dla użytkownika: {validated_data.get('username')}")
            return Response(validated_data, status=status.HTTP_200_OK)
        
        logger.error(f"Błąd walidacji logowania: {serializer.errors}")
        logger.error(f"Szczegóły błędu: {serializer.error_messages}")
        error_message = serializer.errors.get('non_field_errors', [''])[0]
        return Response({'detail': error_message}, status=status.HTTP_401_UNAUTHORIZED) 