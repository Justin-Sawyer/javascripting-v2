from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Article, Category
from .forms import ArticleForm

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


def add_article(request):
    """ Add an article """
    articles = Article.objects.all()
    # article = get_object_or_404(Article, pk=article_id)
    # filteredArticle = Article.objects.get(pk=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Successfully added article!')
            return redirect(reverse('add_article'))
        else:
            # messages.error(request, 'Failed to add article. Please ensure the form is valid.')
            pass
    else:
        form = ArticleForm
    template = 'basics/add_article.html'
    context = {
        'form': form,
        # 'article': article,
        'articles': articles,
        'title': 'JavaScripting : The Basics.',
        'pagename': 'Add an Article',
        # 'filteredArticle': filteredArticle,
    }

    return render(request, template, context)
