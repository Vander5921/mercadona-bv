from django.shortcuts import render, get_object_or_404, redirect
from .models import Promotion
from articles.models import Article
from .forms import PromotionForm

def add_promotion(request, article_id, promotion_id=None):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = PromotionForm(request.POST)
        if form.is_valid():
            promotion = form.save(commit=False)
            promotion.article = article
            promotion.save()
            article.prix -= article.prix * promotion.pourcentage / 100
            article.save()
            return redirect('liste_articles')
    else:
        form = PromotionForm()
    return render(request, 'promotion/add_promotion.html', {'form': form, 'article': article})
