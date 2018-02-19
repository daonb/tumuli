from biography.models import Biography, Period, Memoir, ContentAtom
from biography.serializers import UserSerializer, MemoirSerializer, BiographySerializer, ContentAtomSerializer, PeriodSerializer
from rest_framework import generics
from django.contrib.auth.models import User

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BiographyByUserList(generics.ListCreateAPIView):
    serializer_class = BiographySerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return Biography.objects.filter(user__username=username)

class PeriodByUserList(generics.ListCreateAPIView):
    serializer_class = PeriodSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return Biography.objects.filter(user__username=username)

class MemoirsByUserList(generics.ListCreateAPIView):
    serializer_class = MemoirSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return Memoir.objects.filter(author__username=username)

class ContentAtomByUserList(generics.ListCreateAPIView):
    serializer_class = ContentAtomSerializer
    
    def get_queryset(self):
        username = self.kwargs['username']
        return ContentAtom.objects.filter(owner__username=username)