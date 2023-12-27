from rest_framework import viewsets, views, status
from .models import Student, Teacher, User
from .serializers import StudentSerializer, TeacherSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from datetime import timedelta

# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CustomRefreshToken(RefreshToken):
    @classmethod
    def for_user(cls, user):
        token = cls()
        token['username'] = user.username

        return token

class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = None
        try:
            user = Student.objects.get(username=username)
        except Student.DoesNotExist:
            try:
                user = Teacher.objects.get(username=username)
            except Teacher.DoesNotExist:
              return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        if check_password(password, user.password):
            refresh = CustomRefreshToken.for_user(user)

            response = Response()
            response.set_cookie(
                key='refresh_token', 
                value=str(refresh), 
                httponly=True, 
                secure=True,
                samesite='None'
            )
            response.data = {
                'access_token': str(refresh.access_token),
            }

            return response

        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
    
class RefreshTokenView(views.APIView):
    def get(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        if not refresh_token:
            return Response({'error': 'Refresh token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            token = RefreshToken(refresh_token)
            username = token['username']

            user = None
            if Student.objects.filter(username=username).exists():
                user = Student.objects.get(username=username)
            elif Teacher.objects.filter(username=username).exists():
                user = Teacher.objects.get(username=username)

            if user:
                new_access_token = str(CustomRefreshToken.for_user(user).access_token)
                return Response({'access_token': new_access_token})
            else:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            print(e)
            return Response({'error': 'Invalid or expired token'}, status=status.HTTP_401_UNAUTHORIZED)
        
class LogoutView(views.APIView):
    def get(self, request):
        response = Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
        response.set_cookie(
            key='refresh_token',
            expires=timezone.now() - timedelta(days=1),
            httponly=True, 
            secure=True, 
            samesite='None'
        )
        return response
