from django.shortcuts import render
from .models import Article, Category


def all_basics(request):
    """ A view to return the basic-cat page """
    articles = Article.objects.all()

    context = {
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'pagename': 'Main.',
    }
    return render(request, 'basics/articles.html', context)
