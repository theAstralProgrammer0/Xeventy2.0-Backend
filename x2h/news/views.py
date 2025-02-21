from django.shortcuts import render
from .models import NewsArticle, VideoNews
from .serializers import NewsArticleSerializer, VideoNewsSerializer

# Create your views here.

class LatestNewsArticleList(generics.ListAPIView):
    serializer_class = NewsArticleSerializer
    # return only latest 8 articles
    def get_queryset(self):
        return NewsArticle.objects.all()[:8]


class LatestVideoNews(generics.RetrieveAPIView):
    serializer_class = VideoNewsSerializer
    def get_object(self):
        # return latest video news obj
        return VideoNews.objects.first()
