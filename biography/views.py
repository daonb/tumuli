from .models import Biography, Period, Memoir, ContentAtom
from .serializers import (UserSerializer, MemoirSerializer, BiographySerializer,    
                                            ContentAtomSerializer, PeriodSerializer)
from rest_framework import generics
from django.contrib.auth.models import User


class GetUserPage(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        if 'uuid' in self.kwargs:
            uuid = self.kwargs['uuid']
            # return Memoir.objects.filter(author__uuid=uuid)
            return "Nice!`"



            # return 
        # if 'username' in self.kwargs:
        #     username = self.kwargs['username']
        #     return Biography.objects.filter(user__username=username)

class BiographyByUserList(generics.ListAPIView):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer
    
    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            # return Biography.objects.filter(user__username=username)
            return username


class PeriodByUserList(generics.ListCreateAPIView):
    serializer_class = PeriodSerializer
    
    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            return Biography.objects.filter(user__username=username)

class MemoirsByUserList(generics.ListCreateAPIView):
    serializer_class = MemoirSerializer
    
    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            return Memoir.objects.filter(author__username=username)

class ContentAtomByUserList(generics.ListCreateAPIView):
    serializer_class = ContentAtomSerializer
    
    def get_queryset(self):
        if 'username' in self.kwargs:
            username = self.kwargs['username']
            return ContentAtom.objects.filter(owner__username=username)
