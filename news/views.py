from django.shortcuts import render
from .models import News
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializers import NewsSerializer

class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = []
    authentication_classes = []

def news(request):
    news = News.objects.all().order_by('-date')
    return render(request, 'news.html', {'newss': news})