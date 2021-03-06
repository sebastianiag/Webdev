from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import link
from User.models import User
from User.permissions import IsAccountOwner
from User.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsAccountOwner(),)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
    
            User.objects.create_user(**serializer.validated_data)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'data' : request.data,
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
        }, status=status.HTTP_400_BAD_REQUEST)


    @link()
    def tutors(self, request):
        pass

    @link()
    def tutors_course(self, request):
        pass

    @link()
    def tutors_address(self, request):
        pass
