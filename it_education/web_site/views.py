from rest_framework import generics, viewsets, status
from .serializers import *
from .models import *
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth.models import update_last_login
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer

from rest_framework.exceptions import ValidationError

from it_education import *


class ChangePasswordView(generics.UpdateAPIView):
    """
    Изменение пароля текущего пользователя.
    """
    queryset = UserProfile.objects.all()
    serializer_class = ChangePasswordSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """
        Возвращает текущего пользователя.
        """
        return self.request.user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        # Проверка старого пароля
        if not user.check_password(serializer.validated_data.get('old_password')):
            raise ValidationError({'old_password': 'Incorrect old password.'})

        # Установка нового пароля
        user.set_password(serializer.validated_data.get('new_password'))
        user.save()

        # Обновление сессии
        update_session_auth_hash(request, user)

        return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)



class RegisterView(generics.GenericAPIView):
    """Регистрация нового пользователя с выдачей токенов"""
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        # Генерация токенов
        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "message": "User registered successfully.",
                "tokens": tokens,
            },
            status=status.HTTP_201_CREATED,
        )


class LoginView(generics.GenericAPIView):
    """Авторизация пользователя по email с выдачей токенов"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        user = authenticate(username=user.username, password=password)
        if user is None:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)
        tokens = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response(
            {
                "message": "Login successful.",
                "tokens": tokens,
            },
            status=status.HTTP_200_OK,
        )


class LogoutView(generics.GenericAPIView):
    """Логаут пользователя"""
    # permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {"message": "Logout successful."},
                status=status.HTTP_200_OK,
            )
        except Exception:
            return Response(
                {"error": "Invalid or expired token."},
                status=status.HTTP_400_BAD_REQUEST,
            )



class ResetPasswordRequestView(generics.CreateAPIView):
    serializer_class = ResetPasswordEmailSerializer
    def post(self, request):
        serializer = ResetPasswordEmailSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = UserProfile.objects.get(email=email)
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)

            reset_url = request.build_absolute_uri(f'/reset-password-confirm/{token}/')

            # Отправляем email
            send_mail(
                subject="Сброс пароля",
                message=f"Перейдите по следующей ссылке для сброса пароля: {reset_url}",
                from_email="e.osmonkulov@yandex.ru",
                recipient_list=[email],
                fail_silently=False,
            )

            return Response({"message": "Письмо для сброса пароля отправлено."}, status=200)
        return Response(serializer.errors, status=400)



class ResetPasswordConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer

    def post(self, request, token):
        try:
            access_token = AccessToken(token)
            user_id = access_token['user_id']
            user = UserProfile.objects.get(id=user_id)
        except Exception:
            return Response({"error": "Недействительный или истекший токен"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({"message": "Пароль успешно обновлен"}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)











class UserProfileDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class VisaCartListView(generics.ListCreateAPIView):
    queryset = VisaCart.objects.all()
    serializer_class = VisaCartSerializer

class TariffView(generics.ListCreateAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffListSerializer




class StatyaListView(generics.ListAPIView):
    queryset = Statya.objects.all()
    serializer_class = StatyaListSerializer


class StatyaPosleDetailView(generics.RetrieveAPIView):
    queryset = Statya.objects.all()
    serializer_class = StatyaPosleSerializer

class StatyDoaDetailView(generics.RetrieveAPIView):
    queryset = Statya.objects.all()
    serializer_class = StatyaDoSerializer

class CoursListView(generics.ListAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursListSerializer


class CoursDetailView(generics.RetrieveAPIView):
    queryset = Cours.objects.all()
    serializer_class = CoursDetailSerializer


class MasterClassListView(generics.ListAPIView):
    queryset = MasterClass.objects.all()
    serializer_class = MasterClassListSerializer


class MasterClassDetailView(generics.RetrieveAPIView):
    queryset = MasterClass.objects.all()
    serializer_class = MasterClassDetailSerializer


class FeedBackListView(generics.ListAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedBackSerializer




class CartItemViewSet(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class CartViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # def get_queryset(self):
    #     return Cart.objects.filter(user__id=self.request.user.id)


class PodpiskiUserView(generics.ListCreateAPIView):
    queryset = PodpiskiUser.objects.all()
    serializer_class = PodpiskiSerializer