from django.db import models
from django.http.response import HttpResponse
from .import models
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth.models import User
from knox.models import AuthToken
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView
# Create your views here.


from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer, itemSerializer

# Register API

# user register API


class APIregister(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # it returns user context and token if it got success
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Login API for user along permision,, it also return token of the user


class APIlogin(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(APIlogin, self).post(request, format=None)

# user edit Account API


class editAccount(APIView):
    def post(self, request):
        print("edit account request is posted")
        try:
            fname = request.data['fname']
            lname = request.data['lname']
            email = request.data['email']
            password = request.data['password']
            userid = request.data['user_id']

            data = User.objects.filter(id=userid)
            datam = User.objects.get(id=userid)
            datam.set_password(password)
            datam.first_name = fname
            datam.last_name = lname
            datam.email = email
            datam.save()

            print(fname, lname, email, password, userid)
            # user.set_password(password)  # replace with your real password

            return Response(
                {
                    'data': 'N/A',
                })
        except Exception as ex:
            print(str(ex))
            return Response({'message': str(ex)})

# API to insert in items


class APIinsert(APIView):

    def post(self, request):
        try:
            serializer = itemSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)

        except Exception as ex:
            print("exception  occured")
            return Response({'message': str(ex)})

# API which list the items details


class APIlist(APIView):

    def get(self, request):
        try:
            tasks = models.item.objects.all().order_by('-id')
            serializer = itemSerializer(tasks, many=True)
            return Response(serializer.data)
        except Exception as ex:

            print("exception  occured")
        message = {'message': "welcome to rest api"}

        return Response(message)

# API to update data of items


class APIupdate(APIView):

    def post(self, request):
        try:
            pk = request.data['pk']
            item = models.item.objects.get(id=pk)
            serializer = itemSerializer(instance=item, data=request.data)

            if serializer.is_valid():
                serializer.save()

            return Response(serializer.data)

        except Exception as ex:
            print("exception  occured")
            return Response({'message': str(ex)})


# API to delete an item using his primarykey
class APIdelete(APIView):

    def post(self, request):
        try:
            pk = request.data['pk']
            item = models.item.objects.get(id=pk)
            item.delete()

            return Response('Item succsesfully delete!')

        except Exception as ex:
            print("exception  occured")
            return Response({'message': str(ex)})

# API to search in items


class APIsearch(APIView):
    serializer_class = itemSerializer

    def post(self, request):
        try:
            queryset = models.item.objects.all()
            username = self.request.query_params.get('username')
            if username is not None:
                queryset = queryset.filter(purchaser__username=username)
            l = list(queryset)
            return HttpResponse(l)

        except Exception as ex:
            print("exception  occured")
            return Response({'message': str(ex)})
