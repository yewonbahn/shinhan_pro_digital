from rest_framework import mixins, generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
from .models import Member
from .serializers import (MemberSerializer)

class MemberRegisterView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    serializer_class = MemberSerializer
    # permission_classes =[IsAuthenticated]
    def get_queryset(self):
    
        members = Member.objects.all()
        return members.order_by('id')

    def get(self,request,*args,**kwargs):
        print(request.user)
        return self.list(request,args,kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,args,kwargs)
        
# class MemberRegisterView(APIView):
#     def post(self,request,*args,**kwargs):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         tel = request.data.get("tel")
#         if Member.objects.filter(username=username).exists():
#             return Response({
#                 'datail':'Alreay used',
#             },status=status.HTTP_400_BAD_REQUEST)
#         member = Member(
#             username=username,
#             password=make_password(password),
#             tel=tel

#         ) 
#         member.save()

#         return Response(status=status.HTTP_201_CREATED)
