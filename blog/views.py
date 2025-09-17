from django.shortcuts import render
from .models import Article
from django.views import generic


class ArticlesList(generic.ListView):
    queryset = Article.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class ArticleDetails(generic.DetailView):
    model = Article
    template_name = 'article_details.html'
