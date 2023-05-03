from django.shortcuts import render, redirect
from .forms import ArticleForm

def ajouter_article(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('login') # Rediriger les utilisateurs non authentifiés ou non-administrateurs vers la page de connexion

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'backoffice/ajouter_article.html', {'form': form})

