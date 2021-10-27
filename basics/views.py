from django.shortcuts import render, get_object_or_404
from .models import Article, Category

# This view is not really needed, but is being kept for if users type
# /basics into the url bar
def all_basics(request):
    """ A view to return the basic-cat page """
    articles = Article.objects.all()
    article = get_object_or_404(Article, pk=1)
    filteredArticle = Article.objects.get(pk=1)

    context = {
        'article': article,
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'pagename': article.name,
        'filteredArticle': filteredArticle,
    }
    return render(request, 'basics/articles.html', context)


def article(request, article_id):
    """ A view to show the individual article """
    articles = Article.objects.all()
    article = get_object_or_404(Article, pk=article_id)
    filteredArticle = Article.objects.get(pk=article_id)
    
    context = {
        'article': article,
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'pagename': article.name,
        'filteredArticle': filteredArticle,
    }
    return render(request, 'basics/article.html', context)
