from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer,ProfileSerializer
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.


class RegisterUserView(APIView):
    def post(self,request):
        try:
            serializer=RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data,"msg":"succesfully created user."})
            return Response({"errors":serializer.errors,"msg":"cannot create user."})
        except Exception as e:
            raise serializers.ValidationError({"msg":str(e)})

@api_view(["POST"])
def logout(request):
    try:
        refresh_token=request.data.get("refresh")
        if not refresh_token:
            return Response({"msg":"could not get token"})
        token=RefreshToken(refresh_token)
        token.blacklist()
        return Response({"msg":"succesfully logged out."})
    except Exception as e:
        return Response({"msg":str(e)})
    

class ProfileView(APIView):
    permission_classes=[IsAuthenticated]
    authentication_classes=[JWTAuthentication]

    def get(self,request):
        print(request.user,type(request.user))
        try:
            user=request.user
            print(user,type(user))
            serializer=ProfileSerializer(user)
            return Response(serializer.data)
        except Exception as e:
            return Response({"msg":str(e)})
    


