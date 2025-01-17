from rest_framework import generics, viewsets
from .serializers import *
from .models import *



class StatyaListView(generics.ListAPIView):
    queryset = Statya.objects.all()
    serializer_class = StatyaListSerializer

class StatyaDetailView(generics.RetrieveAPIView):
    queryset = Statya.objects.all()
    serializer_class = StatyaDetailSerializer

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
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

class FeedBackDetailView(generics.RetrieveAPIView):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer