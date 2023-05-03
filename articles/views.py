from django.shortcuts import render
from .models import Article

def liste_articles(request):
    articles = Article.objects.all()
    return render(request, 'articles/liste_articles.html', {'articles': articles})

def home(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'home.html', context)