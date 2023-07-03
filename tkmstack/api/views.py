from rest_framework import generics
from .models import Stack,Tags,Answers
from .serializers import StackSerializer,TagSerializer,AnswerSerializer
from rest_framework import filters



class TagCreate(generics.CreateAPIView):
    queryset=Tags
    serializer_class=TagSerializer


class StackList(generics.ListCreateAPIView):
    queryset=Stack.objects.all()
    serializer_class=StackSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags__tag_name']

class AnswersCreate(generics.CreateAPIView):
    queryset=Answers.objects.all()
    serializer_class=AnswerSerializer

class StackDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Stack.objects.all()
    serializer_class=StackSerializer